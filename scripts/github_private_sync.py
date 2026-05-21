#!/usr/bin/env python3
"""Sync a local git workspace to a private GitHub repository.

This script is intentionally provider-agnostic at the credential layer:
it relies on the local git client, remote URLs already configured in git,
or an optional config file that stores repository metadata only.

Typical use cases:
- commit staged changes with a standard message;
- push the current branch to a private GitHub remote;
- run as a git-hook friendly post-commit / post-merge / post-rebase helper.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_CONFIG: dict[str, Any] = {
    "remote_name": "origin",
    "branch": None,
    "push_tags": False,
    "auto_commit": False,
    "commit_message": "chore(sync): update private mirror",
    "allowed_paths": [],
}


@dataclass(frozen=True)
class GitSyncResult:
    branch: str
    remote_name: str
    remote_url: str | None
    committed: bool
    pushed: bool
    status: str


def run_git(args: list[str], cwd: Path, capture_output: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=False,
        text=True,
        capture_output=capture_output,
    )


def load_config(path: str | None) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if path:
        p = Path(path).expanduser()
        data = json.loads(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("config must be a JSON object")
        cfg.update(data)
    return cfg


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync a local git repo to a private GitHub remote.")
    parser.add_argument("--repo-root", default=".", help="Local git repository root.")
    parser.add_argument("--config", default=None, help="Optional JSON config path.")
    parser.add_argument("--remote-name", default=None, help="Override remote name, e.g. origin or github-private.")
    parser.add_argument("--remote-url", default=None, help="Override remote URL for this run.")
    parser.add_argument("--branch", default=None, help="Override branch to push.")
    parser.add_argument("--commit-message", default=None, help="Override commit message for auto-commit.")
    parser.add_argument("--auto-commit", action="store_true", help="Commit staged changes before pushing.")
    parser.add_argument("--push-tags", action="store_true", help="Also push tags.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned actions without pushing.")
    return parser.parse_args()


def ensure_git_repo(root: Path) -> None:
    proc = run_git(["rev-parse", "--is-inside-work-tree"], root)
    if proc.returncode != 0 or proc.stdout.strip() != "true":
        raise RuntimeError(f"not a git repository: {root}")


def git_output(args: list[str], cwd: Path) -> str:
    proc = run_git(args, cwd)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


def current_branch(root: Path) -> str:
    branch = git_output(["rev-parse", "--abbrev-ref", "HEAD"], root)
    if branch == "HEAD":
        raise RuntimeError("detached HEAD state; specify --branch explicitly")
    return branch


def remote_url(root: Path, remote_name: str) -> str | None:
    proc = run_git(["remote", "get-url", remote_name], root)
    if proc.returncode != 0:
        return None
    return proc.stdout.strip() or None


def working_tree_dirty(root: Path) -> bool:
    status = git_output(["status", "--porcelain"], root)
    return bool(status)


def stage_all(root: Path) -> None:
    proc = run_git(["add", "-A"], root, capture_output=False)
    if proc.returncode != 0:
        raise RuntimeError("git add -A failed")


def create_commit(root: Path, message: str) -> bool:
    proc = run_git(["commit", "-m", message], root)
    if proc.returncode == 0:
        return True
    stderr = (proc.stderr or "").lower()
    if "nothing to commit" in stderr:
        return False
    raise RuntimeError(proc.stderr.strip() or "git commit failed")


def push(root: Path, remote_name: str, branch: str, push_tags: bool) -> None:
    proc = run_git(["push", remote_name, branch], root)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git push {remote_name} {branch} failed")
    if push_tags:
        tag_proc = run_git(["push", remote_name, "--tags"], root)
        if tag_proc.returncode != 0:
            raise RuntimeError(tag_proc.stderr.strip() or f"git push {remote_name} --tags failed")


def push_to_url(root: Path, remote_url: str, branch: str, push_tags: bool) -> None:
    proc = run_git(["push", remote_url, branch], root)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git push {remote_url} {branch} failed")
    if push_tags:
        tag_proc = run_git(["push", remote_url, "--tags"], root)
        if tag_proc.returncode != 0:
            raise RuntimeError(proc.stderr.strip() or f"git push {remote_url} --tags failed")


def sync_repo(root: Path, cfg: dict[str, Any], args: argparse.Namespace) -> GitSyncResult:
    ensure_git_repo(root)

    remote_name = args.remote_name or cfg.get("remote_name") or "origin"
    branch = args.branch or cfg.get("branch") or current_branch(root)
    commit_message = args.commit_message or cfg.get("commit_message") or "chore(sync): update private mirror"
    push_tags = bool(args.push_tags or cfg.get("push_tags", False))
    auto_commit = bool(args.auto_commit or cfg.get("auto_commit", False))
    remote_url_value = args.remote_url or cfg.get("remote_url") or remote_url(root, remote_name)

    if auto_commit and working_tree_dirty(root):
        stage_all(root)
        committed = create_commit(root, commit_message)
    else:
        committed = False

    if args.dry_run:
        return GitSyncResult(
            branch=branch,
            remote_name=remote_name,
            remote_url=remote_url_value,
            committed=committed,
            pushed=False,
            status="dry-run",
        )

    if remote_url_value is None:
        raise RuntimeError(f"remote '{remote_name}' is not configured and --remote-url was not provided")

    if args.remote_url:
        push_to_url(root, remote_url_value, branch, push_tags)
    else:
        push(root, remote_name, branch, push_tags)

    return GitSyncResult(
        branch=branch,
        remote_name=remote_name,
        remote_url=remote_url_value,
        committed=committed,
        pushed=True,
        status="synced",
    )


def main() -> int:
    args = parse_args()
    root = Path(args.repo_root).expanduser().resolve()

    try:
        cfg = load_config(args.config)
        result = sync_repo(root, cfg, args)
    except Exception as exc:  # intentionally surfaced as CLI failure with a clear message
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"OK: {result.status}")
    print(f"- branch: {result.branch}")
    print(f"- remote: {result.remote_name}")
    if result.remote_url:
        print(f"- remote_url: {result.remote_url}")
    print(f"- committed: {'yes' if result.committed else 'no'}")
    print(f"- pushed: {'yes' if result.pushed else 'no'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())