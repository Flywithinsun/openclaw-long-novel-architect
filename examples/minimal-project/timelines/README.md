# Timelines / 时间线

This directory demonstrates the P1 dual-axis historical timeline system.

本目录展示 P1 双轴历史时间线系统。

## Files / 文件

- `real-history.md` — researched or known historical events.
- `alt-history.md` — fictional divergences and chapter-linked consequences.

## Event schema / 事件格式

Each event uses Markdown metadata:

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

## Validation / 验证

From a project root that contains `novel-architect.config.json`, run:

```bash
python3 scripts/timeline_lint.py --project-root . --config novel-architect.config.json --write-report
```

The report is written to:

```text
reports/timeline-lint-report.md
```