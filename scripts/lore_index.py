#!/usr/bin/env python3
"""Index lore cards and metadata tags for historical long-novel projects."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "lore_dir": "lore",
    "reports_dir": "reports",
    "metadata_tags": {
        "characters": "@char",
        "places": "@place",
        "lore": "@lore",
        "events": "@event",
        "sources": "@source",
        "chapters": "@chapter",
    },
}

FIELD_RE = re.compile(r"^-\s*([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")
TAG_RE = re.compile(r"(?P<tag>@[A-Za-z][A-Za-z0-9_-]*)\s*:\s*(?P<value>[^\n#;，。]+)")
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")
PLACEHOLDERS = {"", "TODO", "TBD", "[]"}
SCAN_SUFFIXES = {".md", ".txt"}


@dataclass
class LoreCard:
    path: Path
    fields: dict[str, str]

    @property
    def lore_id(self) -> str:
        return self.fields.get("id", "").strip()


@dataclass
class TagHit:
    path: Path
    line: int
    tag: str
    value: str


def merge_config(data: dict[str, Any]) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    cfg.update(data)
    tags = dict(DEFAULT_CONFIG["metadata_tags"])
    value = data.get("metadata_tags")
    if isinstance(value, dict):
        tags.update(value)
    cfg["metadata_tags"] = tags
    return cfg


def load_config(path: str | None) -> dict[str, Any]:
    if not path:
        return dict(DEFAULT_CONFIG)
    p = Path(path).expanduser()
    if not p.exists():
        raise FileNotFoundError(f"config not found: {p}")
    return merge_config(json.loads(p.read_text(encoding="utf-8")))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Index lore cards and metadata tags.")
    p.add_argument("--project-root", default=".")
    p.add_argument("--config", default=None)
    p.add_argument("--lore-dir", default=None)
    p.add_argument("--report", default=None, help="Default: reports/lore-index-report.md")
    p.add_argument("--write-report", action="store_true")
    p.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    return p.parse_args()


def is_placeholder(value: str) -> bool:
    return value.strip() in PLACEHOLDERS


def parse_lore_card(path: Path) -> LoreCard | None:
    fields: dict[str, str] = {}
    in_fenced_code = False
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.lstrip().startswith("```"):
            in_fenced_code = not in_fenced_code
            continue
        if in_fenced_code:
            continue
        match = FIELD_RE.match(line.strip())
        if match:
            key, value = match.groups()
            fields[key.strip()] = value.strip()
    if "id" not in fields:
        return None
    return LoreCard(path=path, fields=fields)


def collect_lore_cards(lore_dir: Path) -> list[LoreCard]:
    cards: list[LoreCard] = []
    for path in sorted(lore_dir.rglob("*.md")):
        if path.name.lower() in {"readme.md", "index.md"}:
            continue
        if "sources" in path.relative_to(lore_dir).parts:
            continue
        card = parse_lore_card(path)
        if card:
            cards.append(card)
    return cards


def collect_tags(root: Path, configured_tags: set[str]) -> list[TagHit]:
    hits: list[TagHit] = []
    skip_parts = {".git", "external-data", "reports", "__pycache__"}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SCAN_SUFFIXES:
            continue
        if any(part in skip_parts for part in path.relative_to(root).parts):
            continue
        in_fenced_code = False
        for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fenced_code = not in_fenced_code
                continue
            if in_fenced_code:
                continue
            for match in TAG_RE.finditer(line):
                tag = match.group("tag")
                if tag not in configured_tags:
                    continue
                value = match.group("value").strip().strip("`'\"[]() ,，。")
                hits.append(TagHit(path=path, line=lineno, tag=tag, value=value))
    return hits


def validate(root: Path, lore_dir: Path, cfg: dict[str, Any]) -> tuple[list[LoreCard], list[TagHit], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not lore_dir.exists():
        return [], [], [f"lore dir not found: {lore_dir}"], []

    if not (lore_dir / "index.md").exists():
        warnings.append("missing lore/index.md")

    cards = collect_lore_cards(lore_dir)
    seen: dict[str, Path] = {}
    required = ["id", "category", "period", "confidence", "sources"]
    for card in cards:
        rel = card.path.relative_to(root).as_posix()
        for field in required:
            if field not in card.fields:
                errors.append(f"{rel}: missing required field: {field}")
            elif field != "sources" and is_placeholder(card.fields[field]):
                errors.append(f"{rel}: empty or placeholder field: {field}")
        if not ID_RE.match(card.lore_id):
            errors.append(f"{rel}: invalid lore id: {card.lore_id}")
        if card.lore_id in seen:
            errors.append(f"{rel}: duplicate lore id {card.lore_id}; first seen at {seen[card.lore_id].relative_to(root).as_posix()}")
        else:
            seen[card.lore_id] = card.path

    tags_cfg = cfg.get("metadata_tags", DEFAULT_CONFIG["metadata_tags"])
    lore_tag = tags_cfg.get("lore", "@lore")
    configured_tags = set(tags_cfg.values())
    hits = collect_tags(root, configured_tags)
    known_lore = set(seen)
    for hit in hits:
        if hit.tag == lore_tag and hit.value not in known_lore:
            warnings.append(
                f"{hit.path.relative_to(root).as_posix()}:{hit.line}: @lore points to missing card: {hit.value}"
            )

    if not cards:
        warnings.append("no lore cards found")
    return cards, hits, errors, warnings


def build_report(root: Path, lore_dir: Path, cards: list[LoreCard], hits: list[TagHit], errors: list[str], warnings: list[str]) -> str:
    lines = [
        "# Lore Index Report",
        "",
        f"- Project root: `{root}`",
        f"- Lore dir: `{lore_dir.relative_to(root).as_posix() if lore_dir.is_relative_to(root) else lore_dir}`",
        f"- Lore cards: {len(cards)}",
        f"- Metadata tag hits: {len(hits)}",
        f"- Errors: {len(errors)}",
        f"- Warnings: {len(warnings)}",
        "",
        "## Errors",
        "",
    ]
    lines.extend([f"- {e}" for e in errors] or ["- None"])
    lines.extend(["", "## Warnings", ""])
    lines.extend([f"- {w}" for w in warnings] or ["- None"])
    lines.extend(["", "## Lore cards", ""])
    for card in cards:
        rel = card.path.relative_to(root).as_posix()
        lines.append(f"- `{card.lore_id}` — `{rel}`")
    lines.extend(["", "## Metadata tags", ""])
    for hit in hits:
        rel = hit.path.relative_to(root).as_posix()
        lines.append(f"- `{hit.tag}: {hit.value}` at `{rel}:{hit.line}`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    cfg = load_config(args.config)
    lore_rel = args.lore_dir or cfg.get("lore_dir", "lore")
    lore_dir = (root / lore_rel).resolve()
    report_rel = args.report or str(Path(cfg.get("reports_dir", "reports")) / "lore-index-report.md")
    report_path = (root / report_rel).resolve()

    if not root.exists():
        print(f"ERROR: project root not found: {root}", file=sys.stderr)
        return 2

    cards, hits, errors, warnings = validate(root, lore_dir, cfg)
    report = build_report(root, lore_dir, cards, hits, errors, warnings)
    if args.write_report:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")

    print(f"Lore dir: {lore_dir}")
    print(f"Lore cards: {len(cards)}")
    print(f"Metadata tag hits: {len(hits)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    if args.write_report:
        print(f"Report: {report_path}")
    if errors:
        print("\nERRORS:")
        for item in errors:
            print(f"- {item}")
        return 1
    if warnings:
        print("\nWARNINGS:")
        for item in warnings:
            print(f"- {item}")
    if args.strict and warnings:
        print("\nSTRICT mode: warnings treated as failure.")
        return 1
    print("\nOK: lore index looks usable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())