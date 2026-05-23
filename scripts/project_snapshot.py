#!/usr/bin/env python3
"""Write a Git/project-state snapshot report for OpenClaw novel projects."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "project_name": "Long Novel Project",
    "chapter_prefix": "ch",
    "draft_dir": "drafts",
    "readable_dir": "readable",
    "summary_dir": "summaries",
    "audit_dir": "audits",
    "reports_dir": "reports",
    "github_sync_config": "github-sync.config.json",
}


def load_config(path: str | None) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if path:
        p = Path(path).expanduser()
        data = json.loads(p.read_text(encoding="utf-8"))
        cfg.update(data)
    return cfg


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Create a project snapshot report.")
    p.add_argument("--project-root", default=".")
    p.add_argument("--config", default=None, help="JSON config path.")
    p.add_argument("--write-report", action="store_true", help="Write reports/project-snapshot-YYYYMMDD-HHMMSS.md.")
    return p.parse_args()


def run_git(root: Path, args: list[str]) -> tuple[bool, str]:
    try:
        cp = subprocess.run(["git", *args], cwd=root, text=True, capture_output=True, timeout=8)
    except FileNotFoundError:
        return False, "git executable not found"
    except Exception as exc:  # pragma: no cover - defensive for user environments
        return False, str(exc)
    output = (cp.stdout or cp.stderr or "").strip()
    return cp.returncode == 0, output


def latest_file(directory: Path, prefix: str | None = None) -> str:
    if not directory.exists():
        return "missing directory"
    files = [p for p in directory.glob("*.md") if p.is_file()]
    if prefix:
        pat = re.compile(rf"^{re.escape(prefix)}(\d+)(?:[-_].*)?\.md$")
        numbered = [(int(m.group(1)), p) for p in files if (m := pat.match(p.name))]
        if numbered:
            return max(numbered, key=lambda item: item[0])[1].relative_to(directory.parent).as_posix()
    if not files:
        return "none"
    return max(files, key=lambda p: p.stat().st_mtime).relative_to(directory.parent).as_posix()


def project_state_fields(root: Path) -> dict[str, str]:
    p = root / "PROJECT_STATE.md"
    fields = {"completed_chapter": "unknown", "stop_point": "unknown"}
    if not p.exists():
        return fields
    for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        lower = line.lower()
        if "current completed chapter" in lower and ":" in line:
            fields["completed_chapter"] = line.split(":", 1)[1].strip()
        if "current stop point" in lower and ":" in line:
            fields["stop_point"] = line.split(":", 1)[1].strip()
    return fields


def build_report(root: Path, cfg: dict[str, Any]) -> str:
    stamp = dt.datetime.now().isoformat(timespec="seconds")
    prefix = cfg.get("chapter_prefix", "ch")
    state = project_state_fields(root)

    branch_ok, branch = run_git(root, ["branch", "--show-current"])
    commits_ok, commits = run_git(root, ["log", "--oneline", "-5"])
    status_ok, status = run_git(root, ["status", "--short"])

    github_cfg = root / cfg.get("github_sync_config", "github-sync.config.json")
    lines = [
        "# Project Snapshot",
        "",
        f"- created: {stamp}",
        f"- project_name: {cfg.get('project_name')}",
        f"- project_root: {root}",
        f"- git_branch: {branch if branch_ok and branch else 'unavailable'}",
        f"- current_completed_chapter: {state['completed_chapter']}",
        f"- current_stop_point: {state['stop_point']}",
        f"- latest_draft: {latest_file(root / cfg.get('draft_dir', 'drafts'), prefix)}",
        f"- latest_readable: {latest_file(root / cfg.get('readable_dir', 'readable'), prefix)}",
        f"- latest_summary: {latest_file(root / cfg.get('summary_dir', 'summaries'), prefix)}",
        f"- latest_audit: {latest_file(root / cfg.get('audit_dir', 'audits'))}",
        f"- github_sync_config: {'present' if github_cfg.exists() else 'not configured'}",
        "",
        "## Recent commits",
        "",
        commits if commits_ok and commits else "Git commits unavailable or repository has no commits.",
        "",
        "## Uncommitted files",
        "",
        status if status_ok and status else "none / unavailable",
        "",
        "## Git limitations",
        "",
    ]
    if branch_ok and commits_ok and status_ok:
        lines.append("none")
    else:
        lines.extend([
            f"- branch check: {'ok' if branch_ok else branch}",
            f"- recent commits check: {'ok' if commits_ok else commits}",
            f"- status check: {'ok' if status_ok else status}",
        ])
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    cfg = load_config(args.config)
    report = build_report(root, cfg)
    print(report)
    if args.write_report:
        reports_dir = root / cfg.get("reports_dir", "reports")
        reports_dir.mkdir(parents=True, exist_ok=True)
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        path = reports_dir / f"project-snapshot-{stamp}.md"
        path.write_text(report, encoding="utf-8")
        print(f"OK: wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
