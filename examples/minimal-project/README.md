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

## Historical-mode examples / 历史模式示例

This minimal project includes example directories for timeline, geography/logistics, lore metadata, external-data placeholders, style standards, context packs, logic audits, branch simulations, reports, and exports. They are safe starter examples, not real historical research.

本最小项目包含时间线、地理/后勤、lore 元数据、external-data 占位目录、风格标准、上下文包、逻辑审计、分支模拟、报告和导出目录示例。这些只是安全起步样例，不是真实历史研究资料。

If you need a navigable Org-mode project outline, copy `scripts/` into the project and run:

```bash
python scripts/export_org_outline.py --project-root . --config novel-architect.config.json
```

The default output is `exports/org/project-outline.org`; it is a generated navigation aid, not canon approval.

如果需要可导航的 Org-mode 项目大纲，请先把 `scripts/` 复制进项目，再运行上面的命令。默认输出为 `exports/org/project-outline.org`；它只是生成的导航辅助，不是 canon 审批。

Keep external historical datasets outside public packages. `external-data/`, SQLite databases, and unreviewed local CSV / JSON research dumps should remain private unless license-reviewed.

外部历史数据集不要默认进入公开包。`external-data/`、SQLite 数据库，以及未审查的本地 CSV / JSON 研究数据应保持私有，除非已完成许可证审查。
