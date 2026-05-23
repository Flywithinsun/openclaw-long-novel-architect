# AI Next Steps / 下一步 AI 交接说明

This file is the shortest handoff entry for any AI assistant continuing this repository in another chat.

本文件是给其他对话里的 AI 用的最短交接入口。

---

## Read first / 先读这些

```text
README.md
skill/SKILL.md
docs/HISTORICAL_NOVEL_ENHANCEMENT_PLAN.md
```

The full plan is here:

```text
docs/HISTORICAL_NOVEL_ENHANCEMENT_PLAN.md
```

---

## Current objective / 当前目标

Upgrade `openclaw-long-novel-architect` from a general long-novel OpenClaw workflow template into a rigorous historical / alternate-history / time-travel long-novel engineering workflow.

把 `openclaw-long-novel-architect` 从通用长篇小说 OpenClaw 工作流模板，升级成适合严谨历史 / 架空历史 / 穿越长篇的工程化写作系统。

---

## Start with this phase / 从这一阶段开始

P1, P2, P3, P4, P5, P6, P7, P8, P9, and P10 final release verification have first usable implementations. No feature phase is pending; continue with release/tag preparation or user-requested repairs.

**P1、P2、P3、P4、P5、P6、P7、P8、P9、P10 final 发布前总验收**已有可用实现。当前没有待推进功能阶段；下一步只做 release/tag 准备或用户指定修补。

P0 licensing / safety / scope boundary is complete, and P1/P3/P4 basics are implemented. Do not start with AutoGen, CBDB, Electron, Obsidian, Emacs, or model-provider integrations.

P0 许可 / 安全 / 范围边界已经完成，P1/P3/P4 基础也已实现。不要一上来就集成 AutoGen、CBDB、Electron、Obsidian、Emacs 或任何模型 provider。

---

## First command / 第一条命令

```bash
git status --short --branch
```

---

## P0 completion record / P0 完成记录

Status: **complete**.

状态：**已完成**。

Completed P0 scope:

- documented third-party inspiration and license boundaries;
- stated that GPL projects are concept-only unless clean-room reimplemented;
- stated that CBDB and other historical datasets are user-provided external data and must not be packaged by default;
- added `external-data` to default excluded dirs;
- added `*.db`, `*.sqlite`, and `*.sqlite3` to default excluded patterns;
- added a visible historical-mode roadmap pointer in README;
- kept old non-historical projects working;
- verified the minimal project assets.

已完成的 P0 范围：

- 记录第三方灵感来源与许可证边界；
- 明确 GPL 项目只能作为概念参考，除非干净重写；
- 明确 CBDB 和其他历史数据集属于用户自备外部数据，默认不得打包；
- 默认排除目录加入 `external-data`；
- 默认排除模式加入 `*.db`、`*.sqlite`、`*.sqlite3`；
- README 已加入历史模式路线图入口；
- 旧的非历史项目仍可工作；
- 已验证 minimal project 资产可用。

---

## P1 completion record / P1 完成记录

Status: **first usable version complete**.

状态：**首个可用版本已完成**。

Completed P1 scope:

- added `skill/references/timeline-workflow.md`;
- added timeline event and audit templates;
- added minimal project timeline examples for `real_history` and `alt_history`;
- added `scripts/timeline_lint.py` with no external dependencies;
- validates event id, date, calendar, track, confidence, source, related chapters, required fields, and duplicate ids;
- can write `reports/timeline-lint-report.md`;
- updated chapter workflow, audit workflow, README, roadmap, and changelog;
- kept old non-historical projects working.

已完成的 P1 范围：

- 新增 `skill/references/timeline-workflow.md`；
- 新增时间线事件模板与审计模板；
- 新增 minimal project 的 `real_history` 与 `alt_history` 示例时间线；
- 新增无外部依赖的 `scripts/timeline_lint.py`；
- 可检查事件 id、日期、历法、轨道、可信度、来源、关联章节、必填字段与重复 id；
- 可写出 `reports/timeline-lint-report.md`；
- 已更新章节工作流、审计工作流、README、路线图与 changelog；
- 旧的非历史项目仍可工作。

---

## Previous P1 implementation checklist / 既往 P1 实施清单

Create:

```text
skill/references/timeline-workflow.md
skill/templates/timeline-event-template.md
skill/templates/timeline-audit-template.md
examples/minimal-project/timelines/README.md
examples/minimal-project/timelines/real-history.md
examples/minimal-project/timelines/alt-history.md
scripts/timeline_lint.py
```

Minimum required changes:

- define the Markdown timeline event schema;
- support real-history and alternate-history tracks;
- require sources for real-history events when configured;
- require chapter links for alternate-history events when configured;
- validate event id, date, calendar, track, confidence, source, and related chapters;
- write or support a report path such as `reports/timeline-lint-report.md`;
- update README / roadmap / verification notes if behavior changes;
- keep old non-historical projects working.

---

## P3 completion record / P3 完成记录

Status: **first usable version complete**.

状态：**首个可用版本已完成**。

Completed P3 scope:

- added `skill/references/lore-metadata-workflow.md`;
- added lore card and source note templates;
- added minimal project lore index, sample lore card, source note, and category folders;
- added `scripts/lore_index.py` with no external dependencies;
- validates lore ids, required fields, duplicate ids, metadata tags, and missing lore references where possible;
- can write `reports/lore-index-report.md`;
- updated chapter workflow, audit workflow, README, roadmap, and changelog;
- kept old non-historical projects working.

已完成的 P3 范围：

- 新增 `skill/references/lore-metadata-workflow.md`；
- 新增 lore 卡片模板与来源笔记模板；
- 新增 minimal project 的 lore 索引、示例 lore 卡、来源笔记与分类目录；
- 新增无外部依赖的 `scripts/lore_index.py`；
- 可检查 lore id、必填字段、重复 id、元数据标签和可判断的缺失 lore 引用；
- 可写出 `reports/lore-index-report.md`；
- 已更新章节工作流、审计工作流、README、路线图与 changelog；
- 旧的非历史项目仍可工作。

---

## P4 completion record / P4 完成记录

Status: **first usable version complete**.

状态：**首个可用版本已完成**。

Completed P4 scope:

- added `skill/references/context-layer-workflow.md`;
- added context pack and style standard templates;
- added minimal project standards for prose style, historical dialogue, forbidden modernisms, de-AI style rules, and chapter rhythm;
- added minimal project context-pack templates for chapter, audit, and de-AI work;
- updated `skill/SKILL.md`, chapter workflow, and de-AI workflow to load standards/context packs when present;
- kept old non-historical projects working.

已完成的 P4 范围：

- 新增 `skill/references/context-layer-workflow.md`；
- 新增 context pack 模板与 style standard 模板；
- 新增 minimal project 的叙事风格、时代对白、禁用现代词、去 AI 味规则与章节节奏标准；
- 新增 minimal project 的章节、审计、去 AI 上下文包模板；
- 已更新 `skill/SKILL.md`、章节工作流与 de-AI 工作流，使其在存在 standards/context-packs 时读取相关文件；
- 旧的非历史项目仍可工作。

---

## P7 completion record / P7 完成记录

Status: **first usable version complete**.

状态：**首个可用版本已完成**。

Completed P7 scope:

- added `skill/references/historical-data-workflow.md`;
- added historical data source and generated lore card templates;
- added `examples/minimal-project/external-data/README.md` as a public-safe placeholder;
- added `scripts/historical_data_query.py` with standard-library SQLite / CSV / JSON / Markdown-table querying;
- added `scripts/generate_lore_from_data.py` to create clearly marked generated lore draft cards;
- missing, disabled, or unconfigured data sources produce warnings instead of crashes;
- generated lore cards mark source, query, confidence, license boundary, and `final_canon` review requirement;
- external datasets remain user-provided and excluded from packages by default.

已完成的 P7 范围：

- 新增 `skill/references/historical-data-workflow.md`；
- 新增历史数据源模板与生成 lore 卡片模板；
- 新增 `examples/minimal-project/external-data/README.md`，作为公开安全占位目录说明；
- 新增 `scripts/historical_data_query.py`，使用标准库查询 SQLite / CSV / JSON / Markdown 表格；
- 新增 `scripts/generate_lore_from_data.py`，生成明确标记的 lore 草稿卡；
- 数据源缺失、禁用或未配置时输出 warning 而不是崩溃；
- 生成 lore 卡明确标记来源、查询词、置信度、许可证边界和 `final_canon` 审核要求；
- 外部数据集仍由用户自备，默认不进入打包。

---

## P8 completion record / P8 完成记录

Status: **first usable version complete**.

状态：**首个可用版本已完成**。

Completed P8 scope:

- added `skill/references/org-export-workflow.md`;
- added `scripts/export_org_outline.py` with Python standard library only;
- exports `PROJECT_STATE.md`, `WORK_QUEUE.md`, `outlines/`, `characters/`, `lore/`, `timelines/`, and `branches/` into `exports/org/project-outline.org`;
- Emacs is not required;
- generated Org output stays under `exports/` by default;
- no GPL code is copied.

已完成的 P8 范围：

- 新增 `skill/references/org-export-workflow.md`；
- 新增仅使用 Python 标准库的 `scripts/export_org_outline.py`；
- 可把 `PROJECT_STATE.md`、`WORK_QUEUE.md`、`outlines/`、`characters/`、`lore/`、`timelines/` 和 `branches/` 导出到 `exports/org/project-outline.org`；
- 生成过程不需要 Emacs；
- 生成的 Org 输出默认留在 `exports/` 下；
- 不复制 GPL 代码。

---

## P10 final completion record / P10 final 完成记录

Status: **final release verification complete**.

状态：**发布前总验收已完成**。

Completed P10 final scope:

- all scripts pass Python syntax checks and `--help` smoke tests;
- minimal project passes asset, timeline, lore, geo, and branch validation;
- P7 local CSV query/generation smoke test passes on a temporary project;
- P8 Org outline export smoke test passes and generated `.org` output is not kept in the public template;
- P9 snapshot/manuscript export smoke test passes on a temporary project;
- portable package smoke test confirms `external-data/`, local database files, and generated Org output are excluded by default;
- stale handoff prompts pointing to P8 were removed;
- `git diff --check` passes.

已完成的 P10 final 范围：

- 全部脚本通过 Python 语法检查与 `--help` 冒烟检查；
- minimal project 通过资产、时间线、lore、地理和分支验证；
- P7 本地 CSV 查询 / 生成在临时项目中通过冒烟测试；
- P8 Org 大纲导出通过冒烟测试，生成 `.org` 文件不会保留在公开模板中；
- P9 快照 / 手稿导出在临时项目中通过冒烟测试；
- 便携包冒烟测试确认默认排除 `external-data/`、本地数据库文件和生成的 Org 输出；
- 已移除指向 P8 的陈旧交接提示；
- `git diff --check` 通过。

---

## Previous P0 implementation checklist / 既往 P0 实施清单

Create:

```text
docs/third-party-inspiration.md
docs/historical-mode-roadmap.md
```

Update:

```text
README.md
docs/github-release-checklist.md
docs/sanitization-report.md
examples/project-config.example.json
examples/minimal-project/novel-architect.config.json
scripts/package_portable_assets.py
scripts/verify_portable_assets.py
```

Minimum required changes:

- document third-party inspiration and license boundaries;
- state that GPL projects are concept-only unless clean-room reimplemented;
- state that CBDB and other historical datasets are user-provided external data and must not be packaged by default;
- add `external-data` to default excluded dirs;
- add `*.db`, `*.sqlite`, and `*.sqlite3` to default excluded patterns;
- add a visible historical-mode roadmap pointer in README;
- keep old non-historical projects working.

---

## Safety rules / 安全规则

1. Do not copy GPL code into this MIT repository.
2. Do not commit private novel drafts.
3. Do not commit API keys, tokens, provider credentials, personal paths, or account identifiers.
4. Do not bundle CBDB or other third-party historical databases.
5. Do not bind the public template to a specific AI provider or model.
6. Do not let side-model output enter canon without `final_canon` review.
7. Do not continue to the next chapter or next phase automatically after a completion report.

---

## Implementation order after P0 / P0 之后的顺序

Follow the full plan, but the recommended order is:

```text
P0  Licensing, safety, scope boundary
P1  Dual-axis historical timeline
P3  Lore metadata and cross-reference system
P4  Context layers and period-language controls
P10 Closeout sync for verification/package/README/docs/examples
P5  Historical logic audit committee
P6  Butterfly-effect branch simulation
P9  Git snapshot and manuscript export
P2  Geography and logistics
P7  Historical data adapter
P8  Org mode export
P10 Final release verification and changelog sync
```

---

## MVP scope / 最小可交付范围

If the user asks for the smallest useful implementation, build:

```text
docs/third-party-inspiration.md
docs/historical-mode-roadmap.md

skill/references/timeline-workflow.md
skill/templates/timeline-event-template.md
examples/minimal-project/timelines/README.md
examples/minimal-project/timelines/real-history.md
examples/minimal-project/timelines/alt-history.md
scripts/timeline_lint.py

skill/references/lore-metadata-workflow.md
skill/templates/lore-card-template.md
examples/minimal-project/lore/README.md
examples/minimal-project/lore/index.md
scripts/lore_index.py

examples/minimal-project/standards/prose-style.md
examples/minimal-project/standards/historical-dialogue.md
examples/minimal-project/standards/forbidden-modernisms.md

README.md updates
verify_portable_assets.py updates
package_portable_assets.py external-data/database exclusions
historical_data_query.py / generate_lore_from_data.py optional local data adapters
```

---

## Required completion behavior / 完成时必须做

Before reporting any phase complete:

```text
- [ ] docs/templates/examples updated
- [ ] config updated
- [ ] verification/package scripts updated if needed
- [ ] README updated
- [ ] CHANGELOG updated
- [ ] verification command run
- [ ] git status reviewed
- [ ] commit created
- [ ] push completed if requested
- [ ] stop point reported
```

Do not auto-start the next phase unless the user explicitly asks.
