#!/usr/bin/env python3
"""Generate clearly marked draft lore cards from optional local historical data."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any

import historical_data_query as hdq


DEFAULT_CONFIG: dict[str, Any] = {
    "lore_dir": "lore",
    "historical_data_sources": [],
}


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
    p = argparse.ArgumentParser(description="Generate a draft lore card from local historical data.")
    p.add_argument("--project-root", default=".")
    p.add_argument("--config", default=None)
    p.add_argument("--source", required=True)
    p.add_argument("--person", default=None, help="Generate under lore/generated/persons/.")
    p.add_argument("--query", default=None, help="Generic query term; used when --person is not provided.")
    p.add_argument("--category", default=None, help="Default: generated-person or generated-topic.")
    p.add_argument("--output", default=None, help="Override output path relative to project root or absolute.")
    p.add_argument("--limit", type=int, default=5)
    p.add_argument("--allow-empty", action="store_true", help="Write a marked placeholder even when no rows are returned.")
    p.add_argument("--force", action="store_true", help="Overwrite existing generated card.")
    return p.parse_args()


def slugify(value: str) -> str:
    value = value.strip().lower()
    out = []
    for ch in value:
        if ch.isascii() and ch.isalnum():
            out.append(ch)
        elif ch in {" ", "-", "_", "."}:
            out.append("-")
        elif not ch.isascii():
            out.append(f"-u{ord(ch):x}-")
    slug = re.sub(r"-+", "-", "".join(out)).strip("-")
    return slug or "item"


def source_note_id(source_name: str) -> str:
    return f"source-historical-data-{slugify(source_name)}"


def lore_id(category: str, query: str, source_name: str) -> str:
    return f"lore-{slugify(category)}-{slugify(query)}-{slugify(source_name)}"


def resolve_output(root: Path, cfg: dict[str, Any], args: argparse.Namespace, query: str) -> Path:
    if args.output:
        out = Path(args.output).expanduser()
        return out if out.is_absolute() else root / out
    lore_dir = root / cfg.get("lore_dir", "lore")
    if args.person:
        return lore_dir / "generated" / "persons" / f"{slugify(query)}.md"
    return lore_dir / "generated" / "topics" / f"{slugify(query)}.md"


def format_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def build_card(query: str, category: str, source: dict[str, Any], result: hdq.QueryResult) -> str:
    now = dt.datetime.now().isoformat(timespec="seconds")
    source_name = str(source.get("name", "unknown-source"))
    title = query
    lid = lore_id(category, query, source_name)
    sid = source_note_id(source_name)
    license_note = source.get("license_note", "not provided")
    lines = [
        f"# {title}",
        "",
        f"- id: {lid}",
        f"- category: {category}",
        "- period: unknown",
        "- confidence: data-derived-unreviewed",
        "- sources:",
        f"  - {sid}",
        f"- data_source: {source_name}",
        f"- query: {query}",
        f"- generated_at: {now}",
        "- related_places:",
        "  - TODO",
        "- related_characters:",
        "  - TODO",
        "- related_chapters:",
        "  - TODO",
        "",
        "## Generated summary / 生成摘要",
        "",
        f"This draft lore card was generated from `{source_name}` with query `{query}`. Treat it as research material until reviewed by `final_canon`.",
        "",
        "本卡片由本地历史数据源自动生成，在 `final_canon` 审核前仅作为研究材料。",
        "",
        "## Extracted data / 抽取数据",
        "",
    ]
    if result.rows:
        for idx, row in enumerate(result.rows, 1):
            lines.append(f"### Match {idx}")
            lines.append("")
            for key, value in row.items():
                lines.append(f"- {key}: {format_value(value)}")
            lines.append("")
    else:
        lines.append("- No matching rows were returned. Keep this card as a placeholder only if the source warning is acceptable.")
        lines.append("")
    lines.extend([
        "## Source and license boundary / 来源与许可证边界",
        "",
        f"- Dataset: {source_name}",
        f"- Source path: {source.get('path', 'not provided')}",
        f"- License note: {license_note}",
        "- Do not copy restricted source text into public templates.",
        "- Do not bundle the underlying dataset by default.",
        "",
        "## Query warnings / 查询警告",
        "",
    ])
    lines.extend([f"- {w}" for w in result.warnings] or ["- None"])
    lines.extend([
        "",
        "## Canon review required / Canon 审核要求",
        "",
        "- This generated card is research material only.",
        "- `final_canon` must review it before any prose or continuity decision uses it.",
        "- If it changes institutions, war, economy, logistics, geography, technology, or social order, run a logic audit or record an explicit user override.",
        "",
        "## Open questions",
        "",
        "- TODO",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    cfg = load_config(args.config)
    query = args.person or args.query
    if not query:
        print("ERROR: provide --person or --query", file=sys.stderr)
        return 2
    category = args.category or ("generated-person" if args.person else "generated-topic")
    source = hdq.find_source(cfg, args.source)
    if not source:
        print(f"WARN: source not configured: {args.source}")
        return 0
    result = hdq.run_query(root, cfg, args.source, query, args.limit)
    if not result.rows and not args.allow_empty:
        print("WARN: no matching rows returned; no lore card written. Use --allow-empty to write a placeholder.")
        for warning in result.warnings:
            print(f"- {warning}")
        return 0
    out = resolve_output(root, cfg, args, query).resolve()
    if out.exists() and not args.force:
        print(f"ERROR: output exists; use --force to overwrite: {out}", file=sys.stderr)
        return 3
    out.parent.mkdir(parents=True, exist_ok=True)
    card = build_card(query, category, source, result)
    out.write_text(card, encoding="utf-8")
    print(f"OK: wrote {out}")
    print(f"Rows: {len(result.rows)}")
    print(f"Warnings: {len(result.warnings)}")
    for warning in result.warnings:
        print(f"- {warning}")
    print("Stop point: generated lore requires final_canon review before canon use.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())