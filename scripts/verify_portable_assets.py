#!/usr/bin/env python3
"""Verify a long-novel project asset layout for OpenClaw handoff."""
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import os
from pathlib import Path
import sys
from typing import Any

DEFAULT_CONFIG: dict[str, Any] = {
    "project_name": "Long Novel Project",
    "chapter_prefix": "ch",
    "required_paths": [
        "PROJECT_STATE.md",
        "WORK_QUEUE.md",
        "PROJECT_INDEX.md",
        "workflow",
        "drafts",
        "readable",
        "summaries",
        "audits",
        "ledgers",
        "outlines",
        "characters",
        "skill",
        "scripts",
    ],
    "recommended_paths": ["canon", "bible", "writing-requests", "exports", "standards", "context-packs", "branches"],
    "draft_dir": "drafts",
    "readable_dir": "readable",
    "summary_dir": "summaries",
    "audit_dir": "audits",
    "ledger_dir": "ledgers",
    "timeline_dir": "timelines",
    "map_dir": "maps",
    "lore_dir": "lore",
    "standards_dir": "standards",
    "context_pack_dir": "context-packs",
    "branch_dir": "branches",
    "reports_dir": "reports",
    "external_data_dir": "external-data",
    "exports_dir": "exports",
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
    "metadata_tags": {
        "characters": "@char",
        "places": "@place",
        "lore": "@lore",
        "events": "@event",
        "sources": "@source",
        "chapters": "@chapter",
    },
    "historical_data_sources": [],
    "exclude_dirs": [
        ".git",
        ".secrets",
        "scratch",
        "inbox",
        "outbox",
        "archive",
        "backups",
        "external-data",
        "node_modules",
        "__pycache__",
    ],
    "exclude_patterns": [
        "*.db",
        "*.pyc",
        "*.pyo",
        "*.sqlite",
        "*.sqlite3",
        "*.zip",
        "*.tar",
        "*.tar.gz",
        "*.tgz",
        "*.7z",
        "*.rar",
        "*.log",
        ".env",
        ".env.*",
    ],
}

REQUIRED_SKILL_TEXT = [
    "Side material is not canon",
    "Stop after completion",
    "final_canon",
    "verify_portable_assets.py",
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"(?i)(api[_-]?key|token|secret|credential|authorization|bearer|password)\s*[:=]\s*['\"]?[^\s'\"]{8,}"),
]

DATABASE_PATTERNS = ("*.db", "*.sqlite", "*.sqlite3")


def merge_config(data: dict[str, Any]) -> dict[str, Any]:
    """Merge user config with safety-preserving defaults."""
    cfg = dict(DEFAULT_CONFIG)
    cfg.update(data)

    for key in ("historical_mode", "timeline_rules", "metadata_tags"):
        merged = dict(DEFAULT_CONFIG.get(key, {}))
        value = data.get(key)
        if isinstance(value, dict):
            merged.update(value)
        cfg[key] = merged

    for key in ("exclude_dirs", "exclude_patterns"):
        merged = list(DEFAULT_CONFIG.get(key, []))
        for item in data.get(key, []):
            if item not in merged:
                merged.append(item)
        cfg[key] = merged

    return cfg


def load_config(path: str | None) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if path:
        p = Path(path).expanduser()
        data = json.loads(p.read_text(encoding="utf-8"))
        cfg = merge_config(data)
    return cfg


def config_enabled(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Verify long-novel OpenClaw assets.")
    p.add_argument("--project-root", default=".")
    p.add_argument("--config", default=None, help="JSON config path.")
    p.add_argument("--strict", action="store_true")
    p.add_argument("--scan-secrets", action="store_true", help="Lightweight text secret scan for included docs/configs.")
    return p.parse_args()


def latest_num(directory: Path, prefix: str) -> int | None:
    if not directory.exists():
        return None
    pat = re.compile(rf"^{re.escape(prefix)}(\d+)(?:[-_].*)?\.md$")
    nums = []
    for p in directory.glob(f"{prefix}*.md"):
        m = pat.match(p.name)
        if m:
            nums.append(int(m.group(1)))
    return max(nums) if nums else None


def scan_file_for_secrets(p: Path) -> list[str]:
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if any(rx.search(line) for rx in SECRET_PATTERNS):
            hits.append(f"{p}:{i}")
    return hits


def is_under_excluded_dir(rel: str, cfg: dict[str, Any]) -> bool:
    excluded = set(cfg.get("exclude_dirs", []))
    return any(part in excluded for part in Path(rel).parts)


def matches_any_pattern(name: str, patterns: tuple[str, ...] | list[str]) -> bool:
    return any(fnmatch.fnmatch(name, pat) for pat in patterns)


def package_roots(root: Path, cfg: dict[str, Any]) -> list[str]:
    required = list(cfg.get("required_paths", []))
    recommended = [p for p in cfg.get("recommended_paths", []) if (root / p).exists()]
    roots: list[str] = []
    for rel in required + recommended:
        if rel not in roots:
            roots.append(rel)
    return roots


def scan_package_roots_for_databases(root: Path, cfg: dict[str, Any]) -> list[str]:
    """Warn about lightweight/local DB files in paths that packaging would consider."""
    hits: list[str] = []
    seen: set[str] = set()
    for rel_root in package_roots(root, cfg):
        base = root / rel_root
        if not base.exists():
            continue
        if base.is_file():
            rel = base.relative_to(root).as_posix()
            if rel not in seen and not is_under_excluded_dir(rel, cfg) and matches_any_pattern(base.name, DATABASE_PATTERNS):
                seen.add(rel)
                hits.append(rel)
            continue
        for cur, dirs, files in os.walk(base):
            curp = Path(cur)
            dirs[:] = [
                d
                for d in dirs
                if not is_under_excluded_dir((curp / d).relative_to(root).as_posix(), cfg)
            ]
            for name in files:
                if not matches_any_pattern(name, DATABASE_PATTERNS):
                    continue
                full = curp / name
                rel = full.relative_to(root).as_posix()
                if rel not in seen and not is_under_excluded_dir(rel, cfg):
                    seen.add(rel)
                    hits.append(rel)
    return hits


def add_historical_mode_warnings(root: Path, cfg: dict[str, Any], warnings: list[str]) -> None:
    historical = cfg.get("historical_mode", {})
    if not isinstance(historical, dict) or not config_enabled(historical.get("enabled", False)):
        return

    for key in ("timeline_dir", "lore_dir", "standards_dir", "context_pack_dir"):
        rel = cfg.get(key)
        if rel and not (root / rel).exists():
            warnings.append(f"historical mode enabled but missing recommended path: {rel}")

    lore_dir = cfg.get("lore_dir", "lore")
    if lore_dir and (root / lore_dir).exists() and not (root / lore_dir / "index.md").exists():
        warnings.append(f"historical mode enabled but missing lore index: {lore_dir}/index.md")

    external_data_dir = cfg.get("external_data_dir", "external-data")
    if external_data_dir not in cfg.get("exclude_dirs", []):
        warnings.append(f"historical external data dir is not excluded by default: {external_data_dir}")

    for pattern in DATABASE_PATTERNS:
        if pattern not in cfg.get("exclude_patterns", []):
            warnings.append(f"database files are not excluded by default: {pattern}")

    for source in cfg.get("historical_data_sources", []):
        if not isinstance(source, dict):
            continue
        name = source.get("name", "unnamed")
        if source.get("package") is True:
            warnings.append(f"historical data source requests packaging; review license before sharing: {name}")
        source_path = source.get("path")
        if source_path and external_data_dir not in Path(source_path).parts:
            warnings.append(f"historical data source is outside external data dir: {name} -> {source_path}")


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    cfg = load_config(args.config)
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        print(f"ERROR: project root not found: {root}", file=sys.stderr)
        return 2

    for rel in cfg.get("required_paths", []):
        if not (root / rel).exists():
            errors.append(f"missing REQUIRED: {rel}")
    for rel in cfg.get("recommended_paths", []):
        if not (root / rel).exists():
            warnings.append(f"missing recommended: {rel}")

    skill_path = root / "skill" / "SKILL.md"
    if skill_path.exists():
        text = skill_path.read_text(encoding="utf-8", errors="ignore")
        for needle in REQUIRED_SKILL_TEXT:
            if needle not in text:
                warnings.append(f"skill text may be incomplete: missing {needle!r}")

    prefix = cfg.get("chapter_prefix", "ch")
    draft_latest = latest_num(root / cfg.get("draft_dir", "drafts"), prefix)
    readable_latest = latest_num(root / cfg.get("readable_dir", "readable"), prefix)
    summary_latest = latest_num(root / cfg.get("summary_dir", "summaries"), prefix)

    if draft_latest is None:
        warnings.append("no draft chapter files detected")
    if readable_latest is None:
        warnings.append("no readable chapter files detected")
    if draft_latest and readable_latest and draft_latest != readable_latest:
        warnings.append(f"latest draft {draft_latest} != latest readable {readable_latest}")
    if draft_latest and summary_latest and summary_latest < draft_latest:
        warnings.append(f"latest summary {summary_latest} behind latest draft {draft_latest}")

    add_historical_mode_warnings(root, cfg, warnings)
    for rel in scan_package_roots_for_databases(root, cfg):
        warnings.append(
            "database file found under package roots; keep it lightweight, external, "
            f"and license-reviewed before sharing: {rel}"
        )

    if args.scan_secrets:
        for rel in ["."]:
            for p in (root / rel).rglob("*"):
                if p.is_file() and p.suffix.lower() in {".md", ".json", ".txt", ".yaml", ".yml", ".py"}:
                    for hit in scan_file_for_secrets(p):
                        warnings.append(f"possible secret: {hit}")

    print(f"Project: {cfg.get('project_name')}")
    print(f"Root: {root}")
    print(f"Latest draft: {draft_latest if draft_latest is not None else 'none'}")
    print(f"Latest readable: {readable_latest if readable_latest is not None else 'none'}")
    print(f"Latest summary: {summary_latest if summary_latest is not None else 'none'}")

    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"- {w}")
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"- {e}")
        return 1
    if args.strict and warnings:
        print("\nSTRICT mode: warnings treated as failure.")
        return 1
    print("\nOK: assets look usable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
