#!/usr/bin/env python3
"""Report branch-simulation state for an OpenClaw novel project."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Report branch-simulation state.")
    p.add_argument("--project-root", default=".")
    p.add_argument("--branch-dir", default="branches")
    return p.parse_args()


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")


def find_first_line(text: str, needle: str) -> str | None:
    for line in text.splitlines():
        if needle in line:
            return line.strip()
    return None


def branch_summary(branch_path: Path) -> dict[str, str]:
    state: dict[str, str] = {
        "branch_id": branch_path.name,
        "status": "unknown",
        "source_chapter": "unknown",
        "decision": "unknown",
    }
    for name, key in (
        ("BRANCH_STATE.md", "status"),
        ("divergence-point.md", "source_chapter"),
        ("merge-decision.md", "decision"),
    ):
        p = branch_path / name
        if not p.exists():
            continue
        text = read_text(p)
        line = find_first_line(text, f"- {key}:")
        if line:
            state[key] = line.split(":", 1)[1].strip()
    return state


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    branch_dir = root / args.branch_dir

    if not root.exists():
        print(f"ERROR: project root not found: {root}", file=sys.stderr)
        return 2

    print(f"Project root: {root}")
    print(f"Branch dir: {branch_dir}")

    if not branch_dir.exists():
        print("Branches: none")
        print("OK: no branch simulation directory yet.")
        return 0

    branches = [p for p in sorted(branch_dir.iterdir()) if p.is_dir()]
    print(f"Branches: {len(branches)}")
    for branch in branches:
        info = branch_summary(branch)
        print(
            "- {branch_id} | status={status} | source_chapter={source_chapter} | decision={decision}".format(
                **info
            )
        )
    print("OK: branch state report complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
