#!/usr/bin/env python3
"""Validate simple place and route metadata for OpenClaw historical projects."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "project_name": "Long Novel Project",
    "map_dir": "maps",
    "reports_dir": "reports",
}

REQUIRED_PLACE_FIELDS = ("id", "names", "modern_name", "period", "type")
REQUIRED_ROUTE_FIELDS = (
    "id",
    "from",
    "to",
    "distance_km",
    "terrain",
    "normal_travel_days",
    "military_travel_days",
)


def load_config(path: str | None) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if path:
        data = json.loads(Path(path).expanduser().read_text(encoding="utf-8"))
        cfg.update(data)
    return cfg


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate maps/places/routes metadata.")
    p.add_argument("--project-root", default=".")
    p.add_argument("--config", default=None, help="JSON config path.")
    p.add_argument("--write-report", action="store_true")
    return p.parse_args()


def parse_sections(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    sections: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    last_key: str | None = None
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            current = {"title": line[3:].strip(), "_file": path.name}
            sections.append(current)
            last_key = None
            continue
        if current is None:
            continue
        m = re.match(r"^- ([A-Za-z0-9_]+):\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            current[key] = value
            last_key = key
            continue
        m_item = re.match(r"^\s+-\s+(.+)$", line)
        if m_item and last_key:
            existing = current.get(last_key)
            if not isinstance(existing, list):
                current[last_key] = [] if existing in ("", None) else [existing]
            current[last_key].append(m_item.group(1).strip())
    return sections


def number(value: Any) -> float | None:
    try:
        return float(str(value).strip())
    except Exception:
        return None


def validate(root: Path, cfg: dict[str, Any]) -> tuple[list[str], list[str], dict[str, int]]:
    map_dir = root / cfg.get("map_dir", "maps")
    errors: list[str] = []
    warnings: list[str] = []

    if not map_dir.exists():
        errors.append(f"missing map dir: {cfg.get('map_dir', 'maps')}")
        return errors, warnings, {"places": 0, "routes": 0}

    places = parse_sections(map_dir / "places.md")
    routes = parse_sections(map_dir / "routes.md")
    place_ids: set[str] = set()
    route_ids: set[str] = set()

    for place in places:
        title = place.get("title", "unknown")
        for field in REQUIRED_PLACE_FIELDS:
            if not place.get(field):
                errors.append(f"place {title}: missing {field}")
        pid = str(place.get("id", "")).strip()
        if pid:
            if pid in place_ids:
                errors.append(f"duplicate place id: {pid}")
            place_ids.add(pid)
        for coord in ("lat", "lon"):
            value = place.get(coord)
            if value and value != "TODO" and number(value) is None:
                errors.append(f"place {title}: invalid {coord}: {value}")

    for route in routes:
        title = route.get("title", "unknown")
        for field in REQUIRED_ROUTE_FIELDS:
            if not route.get(field):
                errors.append(f"route {title}: missing {field}")
        rid = str(route.get("id", "")).strip()
        if rid:
            if rid in route_ids:
                errors.append(f"duplicate route id: {rid}")
            route_ids.add(rid)
        for endpoint in ("from", "to"):
            value = str(route.get(endpoint, "")).strip()
            if value and value not in place_ids:
                warnings.append(f"route {rid or title}: {endpoint} does not match a known place id: {value}")
        distance = number(route.get("distance_km"))
        normal_days = number(route.get("normal_travel_days"))
        military_days = number(route.get("military_travel_days"))
        if distance is None or distance <= 0:
            errors.append(f"route {rid or title}: distance_km must be positive")
        if normal_days is None or normal_days <= 0:
            errors.append(f"route {rid or title}: normal_travel_days must be positive")
        if military_days is None or military_days <= 0:
            errors.append(f"route {rid or title}: military_travel_days must be positive")
        if distance and normal_days and distance / normal_days > 80:
            warnings.append(f"route {rid or title}: normal travel speed exceeds 80 km/day")
        if distance and military_days and distance / military_days > 60:
            warnings.append(f"route {rid or title}: military travel speed exceeds 60 km/day")

    geo_events = map_dir / "geo-events.json"
    if geo_events.exists():
        try:
            data = json.loads(geo_events.read_text(encoding="utf-8"))
            if not isinstance(data, list):
                errors.append("geo-events.json must contain a list")
        except Exception as exc:
            errors.append(f"geo-events.json is invalid JSON: {exc}")

    return errors, warnings, {"places": len(places), "routes": len(routes)}


def report_text(cfg: dict[str, Any], errors: list[str], warnings: list[str], stats: dict[str, int]) -> str:
    lines = [
        "# Geo Lint Report",
        "",
        f"- project_name: {cfg.get('project_name')}",
        f"- places: {stats.get('places', 0)}",
        f"- routes: {stats.get('routes', 0)}",
        f"- errors: {len(errors)}",
        f"- warnings: {len(warnings)}",
        "",
        "## Errors",
    ]
    lines.extend(f"- {e}" for e in errors)
    if not errors:
        lines.append("none")
    lines.extend(["", "## Warnings"])
    lines.extend(f"- {w}" for w in warnings)
    if not warnings:
        lines.append("none")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    cfg = load_config(args.config)
    errors, warnings, stats = validate(root, cfg)
    text = report_text(cfg, errors, warnings, stats)
    print(text)
    if args.write_report:
        reports_dir = root / cfg.get("reports_dir", "reports")
        reports_dir.mkdir(parents=True, exist_ok=True)
        report_path = reports_dir / "geo-lint-report.md"
        report_path.write_text(text, encoding="utf-8")
        print(f"OK: wrote {report_path}")
    if errors:
        return 1
    print("OK: geo metadata looks usable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
