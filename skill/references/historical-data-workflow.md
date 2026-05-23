# Historical Data Workflow / 历史数据适配器工作流

Use this workflow when a project wants to consult optional local historical datasets such as SQLite, CSV, JSON, or Markdown tables for lore generation and fact checking.

本工作流用于在项目需要时查询本地自备的 SQLite、CSV、JSON 或 Markdown 表格等历史数据，用于辅助 lore 生成与事实检查。

## Core boundary / 核心边界

1. External datasets are **user-provided local research aids**, not public template assets.
2. Do not bundle CBDB, third-party databases, or unreviewed local research dumps by default.
3. Generated lore is mining material until reviewed by `final_canon`.
4. Missing data sources should produce clear warnings, not crashes.
5. The scripts use Python standard library only.

1. 外部数据集是**用户本地自备研究材料**，不是公开模板资产。
2. 默认不得打包 CBDB、第三方数据库或未经审查的本地研究数据。
3. 生成的 lore 在 `final_canon` 审核前只是矿料，不是 canon。
4. 数据源缺失时应给出清晰警告，而不是崩溃。
5. 脚本只使用 Python 标准库。

## Config pattern / 配置模式

Add data sources to `novel-architect.config.json` only when the user has prepared the local data and checked the license boundary:

```json
{
  "external_data_dir": "external-data",
  "historical_data_sources": [
    {
      "name": "cbdb-local",
      "type": "sqlite",
      "path": "external-data/cbdb/latest.db",
      "enabled": false,
      "package": false,
      "license_note": "User must download and comply with CBDB terms."
    }
  ]
}
```

Supported first-version source types:

- `sqlite`
- `csv`
- `json`
- `markdown-table`

## Query workflow / 查询流程

Run from a project root after copying `scripts/` into the project:

```bash
python3 scripts/historical_data_query.py \
  --project-root . \
  --config novel-architect.config.json \
  --source cbdb-local \
  --query-person "李自成" \
  --write-report
```

Default report path:

```text
reports/historical-data-report.md
```

If a source is disabled, missing, or unavailable, the script reports a warning and stops safely.

## Generated lore workflow / 生成 lore 流程

Use generated lore only as a draft research card:

```bash
python3 scripts/generate_lore_from_data.py \
  --project-root . \
  --config novel-architect.config.json \
  --source cbdb-local \
  --person "某人"
```

Default output path:

```text
lore/generated/persons/某人.md
```

Every generated card must clearly state source name, query term, generated timestamp, confidence level, license note / usage boundary, and `final_canon` review requirement.

If no matching rows are returned, `generate_lore_from_data.py` reports a warning and writes nothing by default. Use `--allow-empty` only when you intentionally want a marked placeholder.

## Canon rules / Canon 规则

- Query results are evidence candidates, not canon.
- Generated lore cards must be reviewed before chapter use.
- If generated lore changes institutions, war, economy, logistics, geography, technology, or social order, run a logic audit or record an explicit user override.
- If a source license does not permit redistribution, keep extracts short and do not package the source data.

## Packaging rules / 打包规则

- Keep `external-data/` in `exclude_dirs`.
- Keep `*.db`, `*.sqlite`, and `*.sqlite3` in `exclude_patterns`.
- Review CSV / JSON research dumps before sharing.
- Inspect the portable package manifest before release.

## Stop rule / 停止规则

After querying or generating lore, report the data source used, warnings, files written, verification result, and stop point. Do not continue into chapter drafting unless explicitly instructed.