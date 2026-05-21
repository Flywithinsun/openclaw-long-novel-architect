# Minimal OpenClaw Novel Project / 最小 OpenClaw 小说项目

This is a minimal project skeleton for testing or starting a new OpenClaw long-form fiction project.

这是一个最小项目骨架，用于测试或初始化新的 OpenClaw 长篇小说项目。

## Quick use / 快速使用

```bash
cp -R examples/minimal-project /path/to/my-novel-project
cd /path/to/my-novel-project
cp -R /path/to/openclaw-long-novel-architect/skill ./skill
cp -R /path/to/openclaw-long-novel-architect/scripts ./scripts
python scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
```

Fresh projects may warn that no draft/readable/summary chapter files exist yet. That is expected.

新项目可能会提示还没有 draft/readable/summary 章节文件，这是正常的。

This skeleton keeps `skill/` and `scripts/` as recommended paths so it can be copied without duplicating the full toolkit. For real use, copy them into the project root before asking OpenClaw to work.

这个骨架把 `skill/` 和 `scripts/` 设为推荐路径，避免示例项目重复包含整套工具。正式使用前，请把它们复制到项目根目录。
