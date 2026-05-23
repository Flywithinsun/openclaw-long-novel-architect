# Timeline Workflow / 时间线工作流

Use this workflow when a project enables historical, alternate-history, or time-travel mode.

当项目启用历史、架空历史或穿越题材模式时，使用本工作流。

## Purpose / 目标

The timeline system keeps two axes visible at the same time:

1. `real_history` — known or researched historical events.
2. `alt_history` — fictional divergences, character interventions, and consequences.

时间线系统同时维护两条轴：

1. `real_history`：真实历史或研究确认的事件。
2. `alt_history`：虚构分歧、角色干预与后果。

## Required files / 必需文件

For a historical project, read these before drafting or auditing a chapter:

```text
timelines/real-history.md
timelines/alt-history.md
timelines/character-events.md, if present
timelines/military-events.md, if present
timelines/policy-events.md, if present
```

## Event schema / 事件格式

Each event is a Markdown section headed by `# Timeline Event` or `## Timeline Event`, followed by bullet metadata:

```markdown
# Timeline Event

- id: event-1644-03-19-li-zicheng-beijing
- date: 1644-03-19
- calendar: CE
- track: real_history
- title: 李自成进入北京
- place: 北京
- source: TODO
- confidence: confirmed
- related_chapters: []
- related_characters: []
- consequence: 明朝中央统治崩溃
- notes: TODO
```

Required fields:

- `id`
- `date`
- `calendar`
- `track`
- `title`
- `place`
- `source`
- `confidence`
- `related_chapters`
- `related_characters`
- `consequence`
- `notes`

## Date and calendar rules / 日期与历法规则

- Use ISO-like dates when possible: `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`.
- BCE years may be written as negative years, such as `-0200-01-01`, if `historical_mode.allow_bce` is enabled.
- `calendar` should normally be `CE` or `BCE` unless a project config explicitly allows more calendars.
- If a project uses lunar dates, reign eras, or local calendars, record the normalized sortable date in `date` and the original expression in `notes`.

## Source and canon rules / 来源与 canon 规则

- `real_history` events need a non-empty `source` when `require_source_for_real_history` is enabled.
- `alt_history` events need at least one `related_chapters` entry when `require_chapter_link_for_alt_events` is enabled.
- Side-model outputs may propose events, but proposed events are not canon until `final_canon` accepts them.
- Fictional events must not silently overwrite researched historical events; use `consequence` and `notes` to explain divergence.

## Before writing a chapter / 写章节前

1. Read project state, work queue, chapter request, and model routing.
2. Read the timeline files listed above.
3. Identify timeline events that constrain the target chapter.
4. Put relevant event ids in the chapter request.
5. If the chapter changes history, mark the expected `alt_history` event and risk.

## After completing a chapter / 完成章节后

Either update timeline files directly or write a proposed update file:

```text
ledgers/chNNN-timeline-updates.md
```

The update should include:

- new event ids;
- changed event ids;
- affected real-history assumptions;
- affected alt-history consequences;
- whether final canon approved the change.

## Linting / 检查

Run:

```bash
python3 scripts/timeline_lint.py --project-root . --config novel-architect.config.json --write-report
```

The linter validates event ids, dates, calendars, tracks, confidence values, source requirements, chapter links, and duplicate ids. It can write:

```text
reports/timeline-lint-report.md
```

## Stop rule / 停止规则

Do not continue to the next chapter or next phase just because timeline lint passed. Report the stop point and wait for explicit instruction.