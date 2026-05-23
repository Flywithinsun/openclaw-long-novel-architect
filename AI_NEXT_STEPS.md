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

Start with **P0 — Licensing, safety, and scope boundary**.

先做 **P0：许可、安全与范围边界**。

Do not start with coding timeline parsers, AutoGen, CBDB, Electron, Obsidian, Emacs, or model-provider integrations.

不要一上来就写时间线解析器、集成 AutoGen、CBDB、Electron、Obsidian、Emacs 或任何模型 provider。

---

## First command / 第一条命令

```bash
git status --short --branch
```

---

## P0 implementation checklist / P0 实施清单

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
