#!/usr/bin/env python3
"""Export project planning files into an optional Emacs Org-mode outline."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "project_name": "Long Novel Project",
    "outline_dir": "outlines",
    "character_dir": "characters",
    "lore_dir": "lore",
    "timeline_dir": "timelines",
    "branch_dir": "branches",
    "exports_dir": "exports",
    "org_export_path": "exports/org/project-outline.org",
    "org_export_include_body": True,
}

FIELD_RE = re.compile(r"^-\s*([A-Za-z_][A-Za-z0-9_ /-]*):\s*(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
PLACEHOLDERS = {"", "TODO", "TBD", "[]"}


def load_config(path: str | None) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if path:
        p = Path(path).expanduser()
        data = json.loads(p.read_text(encoding="utf-8"))
        cfg.update(data)
    return cfg


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export project files into an optional Org-mode outline.")
    p.add_argument("--project-root", default=".")
    p.add_argument("--config", default=None, help="JSON config path.")
    p.add_argument("--output", default=None, help="Default: exports/org/project-outline.org")
    p.add_argument("--include-body", action="store_true", help="Include Markdown body text from source files.")
    p.add_argument("--no-body", action="store_true", help="Only export headings and metadata summaries.")
    return p.parse_args()


def rel_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def clean_title(value: str) -> str:
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", value)
    value = re.sub(r"\s+", " ", value).strip(" #\t")
    return value or "Untitled"


def org_heading(level: int, title: str) -> str:
    return f"{'*' * max(level, 1)} {clean_title(title)}"


def org_property_key(key: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]", "_", key).strip("_").upper()
    return cleaned or "VALUE"


def emit_properties(lines: list[str], props: dict[str, Any]) -> None:
    clean_props = {
        org_property_key(str(k)): str(v).replace("\n", " ").strip()
        for k, v in props.items()
        if v is not None and str(v).strip() and str(v).strip() not in PLACEHOLDERS
    }
    if not clean_props:
        return
    lines.append(":PROPERTIES:")
    for key, value in clean_props.items():
        lines.append(f":{key}: {value}")
    lines.append(":END:")
    lines.append("")


def first_markdown_heading(path: Path) -> str | None:
    for line in read_text(path).splitlines():
        match = HEADING_RE.match(line.strip())
        if match:
            return clean_title(match.group(2))
    return None


def parse_fields(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    in_fenced_code = False
    for line in read_text(path).splitlines():
        if line.lstrip().startswith("```"):
            in_fenced_code = not in_fenced_code
            continue
        if in_fenced_code:
            continue
        match = FIELD_RE.match(line.strip())
        if match:
            key, value = match.groups()
            fields[key.strip()] = value.strip()
    return fields


def append_markdown_as_org(lines: list[str], path: Path, base_level: int, skip_first_heading: bool) -> None:
    first_heading_skipped = False
    in_fenced_code = False
    for raw in read_text(path).splitlines():
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fenced_code = not in_fenced_code
            lines.append(raw)
            continue
        if not in_fenced_code:
            match = HEADING_RE.match(stripped)
            if match:
                if skip_first_heading and not first_heading_skipped:
                    first_heading_skipped = True
                    continue
                md_level = len(match.group(1))
                level = base_level + max(1, md_level - 1)
                lines.append(org_heading(level, match.group(2)))
                continue
        lines.append(raw)
    lines.append("")


def markdown_files(directory: Path, include_readme: bool = True) -> list[Path]:
    if not directory.exists():
        return []
    files = [p for p in sorted(directory.rglob("*.md")) if p.is_file()]
    if not include_readme:
        files = [p for p in files if p.name.lower() != "readme.md"]
    return files


def emit_named_file_section(lines: list[str], root: Path, title: str, path: Path, include_body: bool) -> None:
    lines.append(org_heading(1, title))
    if not path.exists():
        lines.append(f"- Missing source file: `{rel_path(path, root)}`")
        lines.append("")
        return
    emit_properties(lines, {"source_file": rel_path(path, root)})
    if include_body:
        append_markdown_as_org(lines, path, base_level=1, skip_first_heading=True)
    else:
        fields = parse_fields(path)
        for key, value in fields.items():
            lines.append(f"- {key}: {value}")
        lines.append("")


def emit_directory_section(lines: list[str], root: Path, title: str, directory: Path, include_body: bool) -> int:
    lines.append(org_heading(1, title))
    if not directory.exists():
        lines.append(f"- Missing directory: `{rel_path(directory, root)}`")
        lines.append("")
        return 0

    files = markdown_files(directory)
    if not files:
        lines.append("- No Markdown files found.")
        lines.append("")
        return 0

    for path in files:
        rel = rel_path(path, root)
        title_text = first_markdown_heading(path) or path.stem.replace("-", " ").title()
        lines.append(org_heading(2, f"{title_text} ({rel})"))
        emit_properties(lines, {"source_file": rel})
        if include_body:
            append_markdown_as_org(lines, path, base_level=2, skip_first_heading=True)
        else:
            fields = parse_fields(path)
            for key, value in fields.items():
                lines.append(f"- {key}: {value}")
            lines.append("")
    return len(files)


def parse_timeline_events(path: Path, root: Path) -> list[dict[str, str]]:
    events: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in read_text(path).splitlines():
        if line.strip() == "# Timeline Event":
            if current:
                events.append(current)
            current = {"source_file": rel_path(path, root)}
            continue
        if current is None:
            continue
        match = FIELD_RE.match(line.strip())
        if match:
            key, value = match.groups()
            current[key.strip()] = value.strip()
    if current:
        events.append(current)
    return events


def emit_timeline_section(lines: list[str], root: Path, timeline_dir: Path) -> int:
    lines.append(org_heading(1, "Timeline"))
    events: list[dict[str, str]] = []
    for path in markdown_files(timeline_dir, include_readme=False):
        events.extend(parse_timeline_events(path, root))
    events.sort(key=lambda item: (item.get("date", ""), item.get("title", ""), item.get("id", "")))

    if not events:
        lines.append("- No timeline events found.")
        lines.append("")
        return 0

    for event in events:
        title = event.get("title") or event.get("id") or "Timeline Event"
        date = event.get("date", "undated")
        lines.append(org_heading(2, f"{date} {title}"))
        emit_properties(
            lines,
            {
                "id": event.get("id"),
                "date": event.get("date"),
                "calendar": event.get("calendar"),
                "track": event.get("track"),
                "source_file": event.get("source_file"),
            },
        )
        for key in ("place", "source", "confidence", "related_chapters", "related_characters", "consequence", "notes"):
            if event.get(key):
                lines.append(f"- {key}: {event[key]}")
        lines.append("")
    return len(events)


def extract_summary(path: Path, max_lines: int = 4) -> list[str]:
    collected: list[str] = []
    in_summary = False
    for line in read_text(path).splitlines():
        match = HEADING_RE.match(line.strip())
        if match:
            title = clean_title(match.group(2)).lower()
            if title in {"summary", "overview", "摘要"}:
                in_summary = True
                continue
            if in_summary:
                break
        elif in_summary and line.strip():
            collected.append(line.strip())
            if len(collected) >= max_lines:
                break
    return collected


def emit_lore_section(lines: list[str], root: Path, lore_dir: Path) -> int:
    lines.append(org_heading(1, "Lore"))
    if not lore_dir.exists():
        lines.append(f"- Missing directory: `{rel_path(lore_dir, root)}`")
        lines.append("")
        return 0

    cards: list[tuple[Path, dict[str, str]]] = []
    for path in markdown_files(lore_dir, include_readme=False):
        rel_parts = path.relative_to(lore_dir).parts
        if path.name.lower() == "index.md" or "sources" in rel_parts:
            continue
        fields = parse_fields(path)
        if fields.get("id"):
            cards.append((path, fields))

    if not cards:
        lines.append("- No lore cards found.")
        lines.append("")
        return 0

    cards.sort(key=lambda item: (item[1].get("category", ""), item[1].get("id", "")))
    for path, fields in cards:
        title = first_markdown_heading(path) or fields.get("id", path.stem)
        lines.append(org_heading(2, title))
        emit_properties(
            lines,
            {
                "id": fields.get("id"),
                "category": fields.get("category"),
                "period": fields.get("period"),
                "confidence": fields.get("confidence"),
                "source_file": rel_path(path, root),
            },
        )
        for line in extract_summary(path):
            lines.append(f"- {line}")
        if fields.get("sources"):
            lines.append(f"- sources: {fields['sources']}")
        lines.append("")
    return len(cards)


def emit_branches_section(lines: list[str], root: Path, branch_dir: Path) -> int:
    lines.append(org_heading(1, "Branches"))
    if not branch_dir.exists():
        lines.append(f"- Missing directory: `{rel_path(branch_dir, root)}`")
        lines.append("")
        return 0

    branch_paths = [p for p in sorted(branch_dir.iterdir()) if p.is_dir()]
    if not branch_paths:
        lines.append("- No branch simulations found.")
        lines.append("")
        return 0

    for branch in branch_paths:
        state_path = branch / "BRANCH_STATE.md"
        fields = parse_fields(state_path) if state_path.exists() else {}
        branch_id = fields.get("branch_id", branch.name)
        branch_name = fields.get("branch_name", "")
        heading = f"{branch_id} — {branch_name}" if branch_name else branch_id
        lines.append(org_heading(2, heading))
        emit_properties(
            lines,
            {
                "status": fields.get("status"),
                "source_chapter": fields.get("source_chapter"),
                "created_from_event": fields.get("created_from_event"),
                "source_file": rel_path(state_path, root) if state_path.exists() else rel_path(branch, root),
            },
        )
        for path in markdown_files(branch):
            lines.append(f"- {rel_path(path, root)}")
        lines.append("")
    return len(branch_paths)


def build_org_outline(root: Path, cfg: dict[str, Any], include_body: bool) -> tuple[str, dict[str, int]]:
    lines: list[str] = [
        f"#+TITLE: {cfg.get('project_name', 'Long Novel Project')} Org Outline",
        f"#+DATE: {dt.datetime.now().isoformat(timespec='seconds')}",
        "#+OPTIONS: toc:2",
        "#+PROPERTY: generated_by scripts/export_org_outline.py",
        "",
        "# This file is generated from local project Markdown files. It is an optional navigation export, not canon approval.",
        "",
    ]
    stats: dict[str, int] = {}

    emit_named_file_section(lines, root, "Project State", root / "PROJECT_STATE.md", include_body)
    emit_named_file_section(lines, root, "Work Queue", root / "WORK_QUEUE.md", include_body)
    stats["outline_files"] = emit_directory_section(lines, root, "Outlines", root / cfg.get("outline_dir", "outlines"), include_body)
    stats["timeline_events"] = emit_timeline_section(lines, root, root / cfg.get("timeline_dir", "timelines"))
    stats["character_files"] = emit_directory_section(lines, root, "Characters", root / cfg.get("character_dir", "characters"), include_body)
    stats["lore_cards"] = emit_lore_section(lines, root, root / cfg.get("lore_dir", "lore"))
    stats["branches"] = emit_branches_section(lines, root, root / cfg.get("branch_dir", "branches"))

    return "\n".join(lines).rstrip() + "\n", stats


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    cfg = load_config(args.config)
    include_body = bool(cfg.get("org_export_include_body", True))
    if args.include_body:
        include_body = True
    if args.no_body:
        include_body = False

    output_value = args.output or cfg.get("org_export_path") or str(Path(cfg.get("exports_dir", "exports")) / "org" / "project-outline.org")
    output_path = Path(output_value).expanduser()
    if not output_path.is_absolute():
        output_path = root / output_path

    org_text, stats = build_org_outline(root, cfg, include_body)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(org_text, encoding="utf-8")

    print(f"Project root: {root}")
    print(f"Output: {output_path}")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")
    print("OK: wrote Org outline export")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())