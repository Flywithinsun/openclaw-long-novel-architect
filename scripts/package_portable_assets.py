#!/usr/bin/env python3
"""Create a sanitized portable asset package for a long-novel OpenClaw project."""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import os
from pathlib import Path
import sys
import zipfile
from typing import Any

DEFAULT_CONFIG: dict[str, Any] = {
    "project_name": "Long Novel Project",
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


def load_config(path: str | None) -> dict[str, Any]:
    cfg = dict(DEFAULT_CONFIG)
    if path:
        p = Path(path).expanduser()
        data = json.loads(p.read_text(encoding="utf-8"))
        cfg.update(data)
        for key in ("exclude_dirs", "exclude_patterns"):
            merged = list(DEFAULT_CONFIG.get(key, []))
            for item in data.get(key, []):
                if item not in merged:
                    merged.append(item)
            cfg[key] = merged
    return cfg


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Package sanitized long-novel assets.")
    p.add_argument("--project-root", default=".")
    p.add_argument("--config", default=None, help="JSON config path.")
    p.add_argument("--output-dir", default="portable-output")
    p.add_argument("--name", default=None)
    p.add_argument("--allow-missing-required", action="store_true")
    return p.parse_args()


def should_exclude(rel: str, is_dir: bool, cfg: dict[str, Any]) -> bool:
    parts = Path(rel).parts
    if any(part in set(cfg.get("exclude_dirs", [])) for part in parts):
        return True
    if not is_dir:
        name = Path(rel).name
        if any(fnmatch.fnmatch(name, pat) for pat in cfg.get("exclude_patterns", [])):
            return True
    return False


def iter_files(root: Path, rel_root: str, cfg: dict[str, Any]):
    base = root / rel_root
    if not base.exists():
        return
    if base.is_file():
        if not should_exclude(rel_root, False, cfg):
            yield base, rel_root
        return
    for cur, dirs, files in os.walk(base):
        curp = Path(cur)
        dirs[:] = [d for d in dirs if not should_exclude((curp / d).relative_to(root).as_posix(), True, cfg)]
        for f in files:
            full = curp / f
            rel = full.relative_to(root).as_posix()
            if not should_exclude(rel, False, cfg):
                yield full, rel


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    cfg = load_config(args.config)
    if not root.exists():
        print(f"ERROR: project root not found: {root}", file=sys.stderr)
        return 2

    required = cfg.get("required_paths", [])
    recommended = cfg.get("recommended_paths", [])
    missing_required = [p for p in required if not (root / p).exists()]
    missing_recommended = [p for p in recommended if not (root / p).exists()]
    if missing_required and not args.allow_missing_required:
        print("ERROR: missing required paths:", file=sys.stderr)
        for p in missing_required:
            print(f"- {p}", file=sys.stderr)
        return 3

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_project = "".join(c.lower() if c.isalnum() else "-" for c in cfg.get("project_name", "novel")).strip("-") or "novel"
    base_name = args.name or f"{safe_project}-portable-{stamp}"
    out_dir = Path(args.output_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"{base_name}.zip"
    manifest_path = out_dir / f"{base_name}-MANIFEST.txt"

    roots = list(required) + [p for p in recommended if (root / p).exists()]
    # Include config if it lives inside project root.
    if args.config:
        cp = Path(args.config).expanduser().resolve()
        try:
            rel_config = cp.relative_to(root).as_posix()
            if rel_config not in roots:
                roots.append(rel_config)
        except ValueError:
            pass

    written: list[str] = []
    seen: set[str] = set()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for rel_root in roots:
            for full, rel in iter_files(root, rel_root, cfg):
                if rel in seen:
                    continue
                seen.add(rel)
                zf.write(full, rel)
                written.append(rel)

    manifest = [
        "# Portable Long Novel Asset Manifest",
        f"created: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"project_name: {cfg.get('project_name')}",
        f"source_root: {root}",
        f"zip: {zip_path.name}",
        "",
        "## Missing required",
        *(f"- {p}" for p in missing_required),
        "none" if not missing_required else "",
        "",
        "## Missing recommended",
        *(f"- {p}" for p in missing_recommended),
        "none" if not missing_recommended else "",
        "",
        "## Excluded dirs",
        *(f"- {p}" for p in cfg.get("exclude_dirs", [])),
        "",
        "## Excluded patterns",
        *(f"- {p}" for p in cfg.get("exclude_patterns", [])),
        "",
        f"## Files written ({len(written)})",
        *written,
    ]
    manifest_path.write_text("\n".join(manifest), encoding="utf-8")

    print(f"OK: wrote {zip_path} ({zip_path.stat().st_size / 1024 / 1024:.2f} MB)")
    print(f"OK: wrote {manifest_path}")
    if missing_recommended:
        print("WARN: missing recommended: " + ", ".join(missing_recommended))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
