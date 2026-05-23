#!/usr/bin/env python3
"""Lint Markdown timeline events for historical / alternate-history projects."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "timeline_dir": "timelines",
    "reports_dir": "reports",
    "historical_mode": {
        "enabled": False,
        "primary_calendar": "CE",
        "allow_bce": True,
        "date_precision": ["year", "month", "day"],
        "require_source_for_real_history": True,
        "require_chapter_link_for_alt_events": True,
    },
    "timeline_rules": {
        "event_id_required": True,
        "allowed_tracks": [
            "real_history",
            "alt_history",
            "character",
            "military",
            "policy",
            "economy",
            "technology",
            "local",
        ],
        "allowed_confidence": ["confirmed", "probable", "fictional", "unknown"],
    },
}

REQUIRED_FIELDS = [
    "id",
    "date",
    "calendar",
    "track",
    "title",
    "place",
    "source",
    "confidence",
    "related_chapters",
    "related_characters",
    "consequence",
    "notes",
]

DATE_RE = re.compile(r"^(?P<sign>-?)(?P<year>\d{1,6})(?:-(?P<month>\d{2})(?:-(?P<day>\d{2}))?)?$")
FIELD_RE = re.compile(r"^-\s*([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")
EVENT_HEADING_RE = re.compile(r"^#{1,3}\s+Timeline Event\s*$", re.IGNORECASE)
EVENT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]*$")
PLACEHOLDER_VALUES = {"", "TODO", "TBD", "[]"}


@dataclass
class TimelineEvent:
    path: Path
    line: int
    fields: dict[str, str]

    @property
    def event_id(self) -> str:
        return self.fields.get("id", "").strip()

    def location(self, root: Path) -> str:
        return f"{self.path.relative_to(root).as_posix()}:{self.line}"


def merge_config(data: dict[str, Any]) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    cfg.update(data)
    for key in ("historical_mode", "timeline_rules"):
        merged = dict(DEFAULT_CONFIG.get(key, {}))
        value = data.get(key)
        if isinstance(value, dict):
            merged.update(value)
        cfg[key] = merged
    return cfg


def load_config(path: str | None) -> dict[str, Any]:
    if not path:
        return dict(DEFAULT_CONFIG)
    p = Path(path).expanduser()
    if not p.exists():
        raise FileNotFoundError(f"config not found: {p}")
    return merge_config(json.loads(p.read_text(encoding="utf-8")))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Lint Markdown timeline events.")
    p.add_argument("--project-root", default=".", help="Project root containing timeline files.")
    p.add_argument("--config", default=None, help="JSON config path.")
    p.add_argument("--timeline-dir", default=None, help="Override timeline directory.")
    p.add_argument("--report", default=None, help="Report path, default reports/timeline-lint-report.md.")
    p.add_argument("--write-report", action="store_true", help="Write a Markdown lint report.")
    p.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    return p.parse_args()


def parse_events(path: Path) -> list[TimelineEvent]:
    events: list[TimelineEvent] = []
    current_line: int | None = None
    current_fields: dict[str, str] = {}
    in_fenced_code = False

    def flush() -> None:
        nonlocal current_line, current_fields
        if current_line is not None:
            events.append(TimelineEvent(path=path, line=current_line, fields=current_fields))
        current_line = None
        current_fields = {}

    for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fenced_code = not in_fenced_code
            continue
        if in_fenced_code:
            continue
        if EVENT_HEADING_RE.match(line.strip()):
            flush()
            current_line = lineno
            current_fields = {}
            continue
        if current_line is None:
            continue
        match = FIELD_RE.match(line.strip())
        if match:
            key, value = match.groups()
            current_fields[key.strip()] = value.strip()
    flush()
    return events


def list_value(raw: str) -> list[str]:
    value = raw.strip()
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip("'\"") for item in inner.split(",") if item.strip()]
    return [value] if value else []


def validate_date(value: str, allow_bce: bool) -> str | None:
    match = DATE_RE.match(value.strip())
    if not match:
        return "invalid date format; expected YYYY, YYYY-MM, YYYY-MM-DD, or negative BCE year"
    year = int(match.group("year"))
    is_negative = bool(match.group("sign"))
    if is_negative and not allow_bce:
        return "BCE / negative year is disabled by config"
    if year == 0:
        return "year 0 is not valid for CE/BCE timeline use"
    month_raw = match.group("month")
    day_raw = match.group("day")
    if month_raw is None:
        return None
    month = int(month_raw)
    day = int(day_raw or "01")
    if is_negative:
        if not 1 <= month <= 12:
            return "invalid BCE month"
        if not 1 <= day <= 31:
            return "invalid BCE day"
        return None
    try:
        date(year, month, day)
    except ValueError as exc:
        return f"invalid date: {exc}"
    return None


def is_placeholder(value: str) -> bool:
    return value.strip() in PLACEHOLDER_VALUES


def validate_events(events: list[TimelineEvent], root: Path, cfg: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    seen_ids: dict[str, TimelineEvent] = {}
    historical = cfg.get("historical_mode", {}) if isinstance(cfg.get("historical_mode"), dict) else {}
    rules = cfg.get("timeline_rules", {}) if isinstance(cfg.get("timeline_rules"), dict) else {}
    allow_bce = bool(historical.get("allow_bce", True))
    require_source = bool(historical.get("require_source_for_real_history", True))
    require_chapter = bool(historical.get("require_chapter_link_for_alt_events", True))
    allowed_tracks = set(rules.get("allowed_tracks", DEFAULT_CONFIG["timeline_rules"]["allowed_tracks"]))
    allowed_confidence = set(rules.get("allowed_confidence", DEFAULT_CONFIG["timeline_rules"]["allowed_confidence"]))

    for event in events:
        loc = event.location(root)
        for field in REQUIRED_FIELDS:
            if field not in event.fields:
                errors.append(f"{loc}: missing required field: {field}")
            elif field not in {"related_chapters", "related_characters"} and is_placeholder(event.fields[field]):
                errors.append(f"{loc}: empty or placeholder field: {field}")

        event_id = event.event_id
        if event_id:
            if not EVENT_ID_RE.match(event_id):
                errors.append(f"{loc}: invalid event id: {event_id}")
            if event_id in seen_ids:
                errors.append(f"{loc}: duplicate event id {event_id}; first seen at {seen_ids[event_id].location(root)}")
            else:
                seen_ids[event_id] = event

        date_value = event.fields.get("date", "").strip()
        if date_value and not is_placeholder(date_value):
            date_error = validate_date(date_value, allow_bce=allow_bce)
            if date_error:
                errors.append(f"{loc}: {date_error}: {date_value}")

        calendar = event.fields.get("calendar", "").strip()
        if calendar and calendar not in {"CE", "BCE"}:
            warnings.append(f"{loc}: non-standard calendar {calendar!r}; document conversion in notes")

        track = event.fields.get("track", "").strip()
        if track and track not in allowed_tracks:
            errors.append(f"{loc}: track not allowed by config: {track}")

        confidence = event.fields.get("confidence", "").strip()
        if confidence and confidence not in allowed_confidence:
            errors.append(f"{loc}: confidence not allowed by config: {confidence}")

        source = event.fields.get("source", "").strip()
        if track == "real_history" and require_source and is_placeholder(source):
            errors.append(f"{loc}: real_history event requires a non-placeholder source")

        related_chapters = list_value(event.fields.get("related_chapters", ""))
        if track == "alt_history" and require_chapter and not related_chapters:
            errors.append(f"{loc}: alt_history event requires at least one related chapter")
        for chapter in related_chapters:
            if not re.match(r"^[A-Za-z]+\d+[A-Za-z0-9_-]*$", chapter):
                warnings.append(f"{loc}: related chapter has unusual format: {chapter}")

    if not events:
        warnings.append("no timeline events found")
    return errors, warnings


def build_report(root: Path, timeline_dir: Path, events: list[TimelineEvent], errors: list[str], warnings: list[str]) -> str:
    lines = [
        "# Timeline Lint Report",
        "",
        f"- Project root: `{root}`",
        f"- Timeline dir: `{timeline_dir.relative_to(root).as_posix() if timeline_dir.is_relative_to(root) else timeline_dir}`",
        f"- Events checked: {len(events)}",
        f"- Errors: {len(errors)}",
        f"- Warnings: {len(warnings)}",
        "",
        "## Errors",
        "",
    ]
    lines.extend([f"- {item}" for item in errors] or ["- None"])
    lines.extend(["", "## Warnings", ""])
    lines.extend([f"- {item}" for item in warnings] or ["- None"])
    lines.extend(["", "## Events", ""])
    for event in events:
        lines.append(f"- `{event.event_id or '<missing id>'}` at `{event.location(root)}`")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    cfg = load_config(args.config)
    timeline_rel = args.timeline_dir or cfg.get("timeline_dir", "timelines")
    timeline_dir = (root / timeline_rel).resolve()
    report_rel = args.report or str(Path(cfg.get("reports_dir", "reports")) / "timeline-lint-report.md")
    report_path = (root / report_rel).resolve()

    if not root.exists():
        print(f"ERROR: project root not found: {root}", file=sys.stderr)
        return 2
    if not timeline_dir.exists():
        print(f"ERROR: timeline dir not found: {timeline_dir}", file=sys.stderr)
        return 1

    events: list[TimelineEvent] = []
    for path in sorted(timeline_dir.rglob("*.md")):
        events.extend(parse_events(path))

    errors, warnings = validate_events(events, root, cfg)
    report = build_report(root, timeline_dir, events, errors, warnings)

    if args.write_report:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")

    print(f"Timeline dir: {timeline_dir}")
    print(f"Events checked: {len(events)}")
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
    print("\nOK: timeline events look usable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())