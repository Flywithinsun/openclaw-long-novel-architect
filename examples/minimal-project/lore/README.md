# Lore / 设定与史料卡片

This directory stores structured historical and worldbuilding notes.

本目录保存结构化历史资料与世界设定卡片。

## Files / 文件

- `index.md` — lore id index and category map.
- category folders such as `官制/`, `军制/`, `物价/`, `风俗/`.
- `generated/` — optional generated cards, clearly marked and reviewed before canon use.

## Metadata tags / 元数据标签

Use these tags in drafts, outlines, summaries, audits, ledgers, and notes:

```text
@lore: lore-ming-salary-system
@source: source-example-ming-institution
@event: event-1644-03-19-li-zicheng-beijing
@chapter: ch001
```

## Validation / 验证

From the project root:

```bash
python3 scripts/lore_index.py --project-root . --config novel-architect.config.json --write-report
```