# Lore Metadata Workflow / Lore 元数据工作流

Use this workflow for historical facts, institutions, prices, customs, technology, language, geography notes, and source-backed research that may affect prose or continuity.

本工作流用于管理会影响正文或连续性的历史事实、制度、物价、风俗、技术、语言、地理笔记与来源研究。

## Purpose / 目标

Lore cards make research explicit and referenceable. They prevent historical details from living only in chat memory.

Lore 卡片让研究资料显式化、可引用，避免历史细节只存在于聊天记忆里。

## Required files / 必需文件

When historical mode or lore tracking is enabled, read:

```text
lore/README.md
lore/index.md
relevant lore cards under lore/
```

## Lore card schema / Lore 卡片格式

```markdown
# 明代俸禄制度

- id: lore-ming-salary-system
- category: 官制
- period: 明代
- confidence: researched
- sources:
  - source-mingshi-example
- related_places:
  - place-beijing
- related_characters:
  - TODO
- related_chapters:
  - ch012

## Summary

TODO

## Hard rules

- TODO

## Common mistakes to avoid

- TODO

## Open questions

- TODO
```

Required metadata:

- `id`
- `category`
- `period`
- `confidence`
- `sources`

Recommended metadata:

- `related_places`
- `related_characters`
- `related_chapters`

## Metadata tags / 元数据标签

Use tags in prose, outlines, summaries, ledgers, audits, and notes:

```text
@char: 李自成
@place: place-beijing
@lore: lore-ming-salary-system
@event: event-1644-03-19-li-zicheng-beijing
@source: source-mingshi-example
@chapter: ch012
```

## Canon rules / Canon 规则

- A lore card is research material until `final_canon` accepts it into project canon.
- Generated or imported lore must clearly state source and confidence.
- External datasets remain user-provided and must not be bundled by default.
- If a chapter depends on a lore card, include the lore id in the chapter request.

## Indexing / 索引

Run:

```bash
python3 scripts/lore_index.py --project-root . --config novel-architect.config.json --write-report
```

The script can write:

```text
reports/lore-index-report.md
```

It checks duplicate lore ids, malformed metadata tags, missing `lore/index.md`, and references to missing lore cards where possible.

## Stop rule / 停止规则

Do not continue to the next chapter just because lore indexing passes. Report the files changed, validation result, and stop point.