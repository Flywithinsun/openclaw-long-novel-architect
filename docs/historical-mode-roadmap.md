# Historical Novel Roadmap / 历史小说路线图

This roadmap explains how `openclaw-long-novel-architect` evolves from a general long-novel workflow template into a historical / alternate-history / time-travel writing system.

本路线图说明 `openclaw-long-novel-architect` 如何从通用长篇小说工作流模板，演进为适合历史 / 架空历史 / 穿越题材的写作系统。

## Purpose / 目标

Historical mode is for projects that need:

- strict timeline discipline;
- historical geography and logistics constraints;
- lore notes for institutions, prices, customs, technology, and language;
- cross-references between prose, research, and source notes;
- multi-role plausibility audits;
- alternate-history branch simulation;
- optional local historical data adapters;
- Git-friendly handoff and export workflows.

历史模式适用于需要以下能力的项目：

- 严格时间线纪律；
- 历史地理与后勤约束；
- 制度、物价、风俗、技术、语言等 lore 记录；
- 正文、研究与来源之间的交叉引用；
- 多角色历史逻辑审计；
- 架空历史分支模拟；
- 可选的本地历史数据适配器；
- 适合 Git 交接与导出的工作流。

## New directory families / 新目录族群

| Family | Example paths | Purpose |
|---|---|---|
| Timelines | `timelines/real-history.md`, `timelines/alt-history.md` | Real history and fictional divergence tracking |
| Maps | `maps/places.md`, `maps/routes.md` | Geography, movement, and travel constraints |
| Lore | `lore/`, `lore/index.md` | Structured research notes and fact cards |
| Standards | `standards/prose-style.md`, `standards/historical-dialogue.md` | Period voice and anti-modernism rules |
| Context packs | `context-packs/chapter-context-template.md` | Chapter-level reading bundle |
| Branches | `branches/branch-history-A/` | Alternate-history simulation and merge decisions |
| Reports | `reports/timeline-lint-report.md`, `reports/lore-index-report.md` | Verification output and audit traces |
| External data | `external-data/` | User-provided historical datasets that stay out of public packages |
| Exports | `exports/manuscript.md`, `exports/org/` | Manuscript and optional outline exports |

## Implementation phases / 实施阶段

| Phase | Goal | What gets added |
|---|---|---|
| P0 | Licensing, safety, and scope boundary | Completed: third-party inspiration doc, roadmap, safe packaging exclusions |
| P1 | Dual-axis historical timeline | Completed first version: real-history and alt-history timelines, event templates, timeline linter |
| P2 | Geography and logistics | Place cards, routes, movement checks |
| P3 | Lore metadata and cross-reference system | Completed first version: lore cards, source notes, index script, metadata tags |
| P4 | Context layers and period-language controls | Completed first version: standards files, context packs, workflow references |
| P5 | Historical logic audit committee | Completed first version: logic audit workflow, request/report templates, and minimal-project example |
| P6 | Butterfly-effect branch simulation | Completed first version: branch simulation workflow, branch templates, minimal-project example branch, and branch status script |
| P7 | Historical data adapter | Optional local data sources such as SQLite / CSV / JSON |
| P8 | Org mode outline export | Optional outline export for large projects |
| P9 | Git writing, revision, snapshot, and export workflow | Snapshot/export scripts and release handling |
| P10 | Verification, packaging, README, and example sync | Partial in progress: P1/P3/P4 verification, packaging roots, README sync |

## First MVP scope / 最小可交付范围

The first useful historical-mode slice should include:

1. `docs/third-party-inspiration.md`
2. `docs/historical-mode-roadmap.md`
3. `skill/references/timeline-workflow.md`
4. `skill/templates/timeline-event-template.md`
5. `examples/minimal-project/timelines/real-history.md`
6. `examples/minimal-project/timelines/alt-history.md`
7. `scripts/timeline_lint.py`
8. `skill/references/lore-metadata-workflow.md`
9. `skill/templates/lore-card-template.md`
10. `examples/minimal-project/lore/index.md`
11. `scripts/lore_index.py`
12. `examples/minimal-project/standards/*`
13. README, verification, and packaging updates that keep the old workflow working

That MVP should be enough to manage a historical project without requiring a GUI, provider lock-in, or bundled datasets.

## Non-goals / 非目标

Do not turn this repository into:

- a GUI writing application;
- an Obsidian plugin;
- an Electron app;
- an Emacs package;
- a provider-specific AI client;
- an API-key manager;
- a public historical database mirror;
- a direct clone of novelWriter, timelines, StoryCraftr, AutoGen, or org-novelist.

## AI handoff instructions / AI 交接说明

If another AI takes over this repository:

1. Read `README.md`.
2. Read `AI_NEXT_STEPS.md`.
3. Read this roadmap.
4. P1, P3, P4, P5, and P6 first versions are complete; continue with P9 Git snapshot/export work unless the user asks for repairs.
5. Keep historical datasets external unless the user explicitly requests otherwise.
6. Keep GPL projects concept-only.
7. Do not start with provider integration or GUI work.

## Current stop point / 当前停点

The repository has completed P0, P1, P3, P4, P5, P6, and P10 partial. The next recommended phase is P9 Git snapshot and manuscript export workflow.

当前仓库已完成 P0、P1、P3、P4、P5、P6，以及 P10 partial。下一推荐阶段是 P9：Git 快照与手稿导出工作流。