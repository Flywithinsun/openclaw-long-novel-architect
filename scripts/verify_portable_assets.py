#!/usr/bin/env python3
"""Verify a long-novel project asset layout for OpenClaw handoff."""
from __future__ import annotations

import argparse
import json
import re
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
    "recommended_paths": ["canon", "bible", "writing-requests", "exports"],
    "draft_dir": "drafts",
    "readable_dir": "readable",
    "summary_dir": "summaries",
    "audit_dir": "audits",
    "ledger_dir": "ledgers",
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


def load_config(path: str | None) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if path:
        p = Path(path).expanduser()
        data = json.loads(p.read_text(encoding="utf-8"))
        cfg.update(data)
    return cfg


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
