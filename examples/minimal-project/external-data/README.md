# External Data / 外部历史数据

This directory is a placeholder for **user-provided local historical datasets**. It is excluded from portable packages by default.

本目录是**用户本地自备历史数据集**的占位目录，默认不进入可移植公开包。

## Intended contents / 可放置内容

- SQLite databases downloaded by the user after reviewing license terms.
- Local CSV / JSON research tables created by the project owner.
- Markdown tables copied from project-owned notes.

- 用户自行下载并审查许可证后的 SQLite 数据库。
- 项目所有者自建的 CSV / JSON 研究表。
- 来自项目自有笔记的 Markdown 表格。

## Safety rules / 安全规则

1. Do not commit third-party historical databases by default.
2. Do not package CBDB or other licensed datasets in public releases.
3. Keep `package: false` in `historical_data_sources` unless making a private, license-reviewed package.
4. Generated lore must cite source, confidence, and review status.

## Example config / 示例配置

```json
{
  "name": "example-local-csv",
  "type": "csv",
  "path": "external-data/example/persons.csv",
  "enabled": false,
  "package": false,
  "license_note": "Project-owned local CSV. Review before sharing."
}
```