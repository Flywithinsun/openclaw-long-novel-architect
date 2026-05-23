# Historical Data Source Template / 历史数据源模板

Copy this block into `historical_data_sources` in `novel-architect.config.json` after you have prepared the local dataset and reviewed its license.

在你准备好本地数据集并审查许可证后，可把此块复制到 `novel-architect.config.json` 的 `historical_data_sources` 中。

```json
{
  "name": "local-source-name",
  "type": "sqlite",
  "path": "external-data/source-name/data.sqlite",
  "enabled": false,
  "package": false,
  "license_note": "User-provided local data. Review license before use or sharing.",
  "description": "Short note about scope, period, region, and provenance.",
  "default_table": "optional_table_name_for_sqlite"
}
```

## Supported `type` values

- `sqlite`
- `csv`
- `json`
- `markdown-table`

## Required safety fields

- `enabled`: keep `false` until the path exists and the user approves local use.
- `package`: keep `false` for public templates and public packages.
- `license_note`: state who provided the dataset and what license boundary applies.

## Usage boundary

- Do not commit the dataset itself unless it is small, project-owned, and license-reviewed.
- Do not package third-party databases by default.
- Generated lore must cite this source and remain non-canon until reviewed.