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

Start with **P1 — Dual-axis historical timeline system**.

先做 **P1：双轴历史时间线系统**。

P0 licensing / safety / scope boundary is complete. Do not start with AutoGen, CBDB, Electron, Obsidian, Emacs, or model-provider integrations.

P0 许可 / 安全 / 范围边界已经完成。不要一上来就集成 AutoGen、CBDB、Electron、Obsidian、Emacs 或任何模型 provider。

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

## P1 implementation checklist / P1 实施清单

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
P10 Partial verification/package/README sync
P5  Historical logic audit committee
P6  Butterfly-effect branch simulation
P9  Git snapshot and manuscript export
P2  Geography and logistics
P7  Historical data adapter
P8  Org mode export
P10 Final docs/examples/verification/changelog sync
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
