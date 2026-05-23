# Export Workflow / 手稿导出工作流

Use this workflow when preparing a readable manuscript, volume export, or release bundle from project files.

本工作流用于从 `readable/` 等项目目录生成可交接、可阅读、可发布前审查的手稿文件。

## Default source / 默认来源

```text
readable/ch001.md
readable/ch002.md
...
```

If a project uses a different readable directory, read `novel-architect.config.json` first.

## Default outputs / 默认输出

```text
exports/manuscript.md
exports/manuscript.txt
exports/release/volume-01.md
```

## Export command / 导出命令

```bash
python3 scripts/export_manuscript.py --project-root . --config novel-architect.config.json --write-release
```

## Rules / 规则

- Export from readable/de-AI files unless the user explicitly requests drafts.
- Preserve chapter order by chapter number in filenames such as `ch001.md`.
- Keep generated files under `exports/`.
- Do not include private raw model logs, credentials, external datasets, or scratch material.
- Treat export as a product of current files, not as canon approval by itself.

## Before release / 发布前

Before sharing exported files, run verification and secret/database checks where appropriate:

```bash
python3 scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json --scan-secrets
python3 scripts/project_snapshot.py --project-root . --config novel-architect.config.json --write-report
```
