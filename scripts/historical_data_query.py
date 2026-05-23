#!/usr/bin/env python3
"""Query optional local historical datasets without bundling them."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "reports_dir": "reports",
    "external_data_dir": "external-data",
    "historical_data_sources": [],
}

SUPPORTED_TYPES = {"sqlite", "csv", "json", "markdown-table"}


@dataclass
class QueryResult:
    source: dict[str, Any]
    source_path: Path
    query: str
    rows: list[dict[str, Any]]
    warnings: list[str]


def merge_config(data: dict[str, Any]) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    cfg.update(data)
    if not isinstance(cfg.get("historical_data_sources"), list):
        cfg["historical_data_sources"] = []
    return cfg


def load_config(path: str | None) -> dict[str, Any]:
    if not path:
        return dict(DEFAULT_CONFIG)
    p = Path(path).expanduser()
    return merge_config(json.loads(p.read_text(encoding="utf-8")))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Query local historical data sources.")
    p.add_argument("--project-root", default=".")
    p.add_argument("--config", default=None)
    p.add_argument("--source", default=None, help="Name in historical_data_sources.")
    p.add_argument("--query-person", default=None, help="Convenience alias for --query.")
    p.add_argument("--query", default=None, help="Case-insensitive text query across supported columns/fields.")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--report", default=None, help="Default: reports/historical-data-report.md")
    p.add_argument("--write-report", action="store_true")
    p.add_argument("--list-sources", action="store_true")
    return p.parse_args()


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


def configured_sources(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    return [s for s in cfg.get("historical_data_sources", []) if isinstance(s, dict)]


def find_source(cfg: dict[str, Any], name: str) -> dict[str, Any] | None:
    for source in configured_sources(cfg):
        if source.get("name") == name:
            return source
    return None


def resolve_source_path(root: Path, source: dict[str, Any]) -> Path:
    raw = str(source.get("path", "")).strip()
    p = Path(raw).expanduser()
    if not p.is_absolute():
        p = root / p
    return p.resolve()


def row_matches(row: dict[str, Any], query: str) -> bool:
    needle = query.casefold()
    return any(needle in str(value).casefold() for value in row.values())


def trim_rows(rows: list[dict[str, Any]], query: str, limit: int) -> list[dict[str, Any]]:
    matched = [row for row in rows if row_matches(row, query)]
    return matched[: max(limit, 0)]


def query_csv(path: Path, query: str, limit: int) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return trim_rows([dict(row) for row in reader], query, limit)


def flatten_json_records(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        for key in ("records", "items", "data", "persons", "people"):
            if isinstance(data.get(key), list):
                items = data[key]
                break
        else:
            items = [data]
    else:
        items = []
    rows: list[dict[str, Any]] = []
    for item in items:
        if isinstance(item, dict):
            rows.append({str(k): v for k, v in item.items()})
        else:
            rows.append({"value": item})
    return rows


def query_json(path: Path, query: str, limit: int) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return trim_rows(flatten_json_records(data), query, limit)


def parse_markdown_tables(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines) - 1:
        header = lines[i].strip()
        separator = lines[i + 1].strip()
        if header.startswith("|") and separator.startswith("|") and re.match(r"^\|?\s*:?-{3,}:?", separator):
            headers = [cell.strip() for cell in header.strip("|").split("|")]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [cell.strip() for cell in lines[i].strip().strip("|").split("|")]
                rows.append({headers[idx] if idx < len(headers) else f"col{idx + 1}": cell for idx, cell in enumerate(cells)})
                i += 1
            continue
        i += 1
    return rows


def query_markdown_table(path: Path, query: str, limit: int) -> list[dict[str, Any]]:
    rows = parse_markdown_tables(path.read_text(encoding="utf-8", errors="ignore"))
    return trim_rows(rows, query, limit)


def sqlite_tables(conn: sqlite3.Connection) -> list[str]:
    cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
    return [str(row[0]) for row in cur.fetchall()]


def quote_identifier(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def query_sqlite(path: Path, source: dict[str, Any], query: str, limit: int, warnings: list[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with sqlite3.connect(path) as conn:
        conn.row_factory = sqlite3.Row
        tables = sqlite_tables(conn)
        default_table = source.get("default_table")
        if default_table:
            if default_table in tables:
                tables = [str(default_table)]
            else:
                warnings.append(f"default_table not found, scanning all tables instead: {default_table}")
        for table in tables:
            if len(rows) >= limit:
                break
            try:
                cur = conn.execute(f"SELECT * FROM {quote_identifier(table)} LIMIT 500")
            except sqlite3.Error as exc:
                warnings.append(f"sqlite table skipped: {table}: {exc}")
                continue
            for record in cur.fetchall():
                row = {str(key): record[key] for key in record.keys()}
                row["_table"] = table
                if row_matches(row, query):
                    rows.append(row)
                    if len(rows) >= limit:
                        break
    return rows


def run_query(root: Path, cfg: dict[str, Any], source_name: str, query: str, limit: int) -> QueryResult:
    warnings: list[str] = []
    source = find_source(cfg, source_name)
    if not source:
        return QueryResult({}, root, query, [], [f"source not configured: {source_name}"])
    source_type = str(source.get("type", "")).strip().lower()
    source_path = resolve_source_path(root, source)
    if source_type not in SUPPORTED_TYPES:
        warnings.append(f"unsupported source type: {source_type or 'missing'}")
        return QueryResult(source, source_path, query, [], warnings)
    if not truthy(source.get("enabled", False)):
        warnings.append(f"source is disabled: {source_name}")
        return QueryResult(source, source_path, query, [], warnings)
    if not source_path.exists():
        warnings.append(f"source path not found: {source_path}")
        return QueryResult(source, source_path, query, [], warnings)
    try:
        if source_type == "sqlite":
            rows = query_sqlite(source_path, source, query, limit, warnings)
        elif source_type == "csv":
            rows = query_csv(source_path, query, limit)
        elif source_type == "json":
            rows = query_json(source_path, query, limit)
        else:
            rows = query_markdown_table(source_path, query, limit)
    except Exception as exc:
        warnings.append(f"query failed: {exc}")
        rows = []
    return QueryResult(source, source_path, query, rows, warnings)


def build_report(root: Path, result: QueryResult) -> str:
    source_name = result.source.get("name", "<missing>") if result.source else "<missing>"
    source_type = result.source.get("type", "<missing>") if result.source else "<missing>"
    license_note = result.source.get("license_note", "") if result.source else ""
    lines = [
        "# Historical Data Query Report",
        "",
        f"- Project root: `{root}`",
        f"- Source: `{source_name}`",
        f"- Type: `{source_type}`",
        f"- Path: `{result.source_path}`",
        f"- Query: `{result.query}`",
        f"- Results: {len(result.rows)}",
        f"- Warnings: {len(result.warnings)}",
        f"- License note: {license_note or 'not provided'}",
        "",
        "## Warnings",
        "",
    ]
    lines.extend([f"- {w}" for w in result.warnings] or ["- None"])
    lines.extend(["", "## Results", ""])
    if not result.rows:
        lines.append("- None")
    else:
        for idx, row in enumerate(result.rows, 1):
            lines.append(f"### Result {idx}")
            lines.append("")
            for key, value in row.items():
                lines.append(f"- {key}: {value}")
            lines.append("")
    lines.extend([
        "## Usage boundary",
        "",
        "- Query results are research material, not canon.",
        "- Do not package external datasets by default.",
        "- Generated lore requires `final_canon` review before chapter use.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    cfg = load_config(args.config)
    if args.list_sources:
        for source in configured_sources(cfg):
            print(f"{source.get('name')}\t{source.get('type')}\t enabled={truthy(source.get('enabled', False))}\t{source.get('path')}")
        return 0
    if not args.source:
        print("ERROR: provide --source or use --list-sources", file=sys.stderr)
        return 2
    query = args.query_person or args.query
    if not query:
        print("ERROR: provide --query-person or --query", file=sys.stderr)
        return 2
    result = run_query(root, cfg, args.source, query, args.limit)
    report = build_report(root, result)
    print(report)
    if args.write_report:
        report_rel = args.report or str(Path(cfg.get("reports_dir", "reports")) / "historical-data-report.md")
        report_path = (root / report_rel).resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")
        print(f"OK: wrote {report_path}")
    if result.warnings and not result.rows:
        print("WARN: no usable rows returned; see warnings above.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())