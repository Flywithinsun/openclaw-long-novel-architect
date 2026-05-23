# Changelog

## Unreleased - Historical Mode P1/P2/P3/P4/P5/P6/P9 Timeline, Geography, Lore, Context, Logic Audit, Branch Simulation, Snapshot, and Export

### 中文

- 新增历史模式 P0 基础文档：第三方灵感与许可证边界、历史模式路线图。
- 扩展配置安全边界：默认排除 `external-data/` 与数据库文件（`*.db`、`*.sqlite`、`*.sqlite3`），避免打包 CBDB 等外部历史数据。
- 增强验证脚本：在历史模式启用时提示时间线 / lore / 标准目录缺失，并警告包内路径下的本地数据库文件。
- 同步 README、发布检查清单与脱敏报告，强调历史数据适配器应保持轻量、可选、用户本地自备。
- 补齐 P0 完成记录与 P1 下一步交接说明，README、`AI_NEXT_STEPS.md` 和路线图不再提示从 P0 开始。
- 新增 P1 双轴历史时间线系统：`timeline-workflow.md`、时间线事件模板、时间线审计模板、minimal project 示例时间线。
- 新增 `scripts/timeline_lint.py`，无外部依赖检查事件 id、日期、历法、轨道、可信度、真实历史来源、架空历史章节关联和重复 id，并可写出 `reports/timeline-lint-report.md`。
- 新增 P2 地理 / 地图 / 后勤约束首版：`geo-logistics-workflow.md`、地点/路线/后勤模板、minimal project `maps/` 示例和 `scripts/geo_lint.py`。
- 更新章节请求模板、章节工作流和审计工作流，要求历史模式下读取相关时间线并记录分歧后果。
- 新增 P3 lore 元数据系统：`lore-metadata-workflow.md`、lore 卡片模板、来源笔记模板、minimal project 示例 lore 卡和分类目录。
- 新增 `scripts/lore_index.py`，无外部依赖检查 lore id、必填字段、重复 id、元数据标签和可判断的缺失 lore 引用，并可写出 `reports/lore-index-report.md`。
- 新增 P4 上下文层与时代语言控制首版：context-layer 工作流、context/style 模板、minimal project standards 与 context-packs 示例。
- 开始 P10 partial 收口：standards / context-packs 已纳入推荐资产、验证脚本与打包脚本默认配置。
- 补充 minimal project 的 `exports/` 占位目录，并为 `reports/` 增加忽略规则，避免验证演练产物污染模板工作区。
- 新增 P5 历史逻辑审计委员会首版：逻辑审计工作流、请求/报告模板、minimal project 示例审计文件，以及章节工作流的高影响变化接入说明。
- 新增 P6 蝴蝶效应分支模拟首版：branch simulation 工作流、分支状态/分歧点/合并决策模板、minimal project 示例分支、`scripts/branch_status.py`，并把 `branches/` 纳入推荐资产与打包/验证规则。
- 新增 P9 Git 快照与手稿导出首版：versioning/export 工作流、修订分支模板、发布说明模板、`scripts/project_snapshot.py` 和 `scripts/export_manuscript.py`。

### English

- Added historical-mode P0 groundwork docs: third-party inspiration/license boundaries and the historical-mode roadmap.
- Expanded config safety boundaries: exclude `external-data/` and database files (`*.db`, `*.sqlite`, `*.sqlite3`) by default to avoid packaging CBDB or other external historical data.
- Enhanced verification: warn when historical mode is enabled but timeline / lore / standards paths are missing, and warn about local database files under package roots.
- Synced README, release checklist, and sanitization guidance to keep historical data adapters lightweight, optional, and user-provided.
- Added the P0 completion record and P1 next-step handoff so README, `AI_NEXT_STEPS.md`, and the roadmap no longer tell new sessions to start from P0.
- Added the P1 dual-axis historical timeline system: `timeline-workflow.md`, timeline event template, timeline audit template, and minimal project timeline examples.
- Added `scripts/timeline_lint.py` with no external dependencies to validate event ids, dates, calendars, tracks, confidence values, real-history sources, alternate-history chapter links, and duplicate ids, with optional `reports/timeline-lint-report.md` output.
- Added the first P2 geography/map/logistics constraints slice: `geo-logistics-workflow.md`, place/route/logistics templates, minimal-project `maps/` examples, and `scripts/geo_lint.py`.
- Updated the chapter request template, chapter workflow, and audit workflow to load relevant timelines and record divergence consequences in historical mode.
- Added the P3 lore metadata system: `lore-metadata-workflow.md`, lore card template, source note template, minimal project sample lore card, and category folders.
- Added `scripts/lore_index.py` with no external dependencies to validate lore ids, required fields, duplicate ids, metadata tags, and detectable missing lore references, with optional `reports/lore-index-report.md` output.
- Added the first P4 context-layer and period-language controls: context-layer workflow, context/style templates, minimal project standards, and context-pack examples.
- Started P10 partial polish: standards / context-packs are now part of recommended assets and default verification/packaging configuration.
- Added a minimal-project `exports/` placeholder and a `reports/` ignore rule so verification runs do not pollute the template workspace.
- Added the first P5 historical logic audit committee slice: logic audit workflow, request/report templates, a minimal-project example audit, and chapter-workflow integration notes for high-impact changes.
- Added the first P6 butterfly-effect branch simulation slice: branch simulation workflow, branch state/divergence/merge-decision templates, a minimal-project example branch, `scripts/branch_status.py`, and `branches/` in recommended verification/packaging assets.
- Added the first P9 Git snapshot and manuscript export slice: versioning/export workflows, revision branch and release note templates, `scripts/project_snapshot.py`, and `scripts/export_manuscript.py`.

## v0.3.0 - OpenClaw Public Onboarding Pack

### 中文

本版本面向开源使用者，重点降低第一次使用 OpenClaw Long Novel Architect 的门槛。

主要变化：

- 新增 `docs/openclaw-installation.md`：中英文 OpenClaw 安装与首次读取说明。
- 新增 `docs/first-project-setup.md`：中英文首个小说项目初始化指南。
- 新增 `examples/minimal-project/`：最小可用 OpenClaw 小说项目骨架。
- 新增项目启动模板：
  - `skill/templates/project-state-template.md`
  - `skill/templates/work-queue-template.md`
  - `skill/templates/project-index-template.md`
  - `skill/templates/model-routing-template.md`
- 更新 `README.md`：增加“一分钟上手 / One-minute start”。

本版本的目标是让新用户 clone 仓库后能更快理解：怎么安装 Skill、怎么初始化小说项目、OpenClaw 第一次应该读取哪些文件，以及项目完成后如何继续交接。

### English

This release focuses on public onboarding and lowers the first-use barrier for OpenClaw Long Novel Architect.

Highlights:

- Added `docs/openclaw-installation.md` with bilingual OpenClaw installation and first-read guidance.
- Added `docs/first-project-setup.md` with bilingual first-project setup instructions.
- Added `examples/minimal-project/`, a minimal usable OpenClaw novel project skeleton.
- Added project bootstrap templates:
  - `skill/templates/project-state-template.md`
  - `skill/templates/work-queue-template.md`
  - `skill/templates/project-index-template.md`
  - `skill/templates/model-routing-template.md`
- Updated `README.md` with a “One-minute start” section.

The goal is to help new users understand how to install the Skill, initialize a novel project, identify the first files OpenClaw should read, and continue through explicit file-based handoffs.

## v0.2.0 - OpenClaw Private GitHub Sync

### 中文

本版本重点增强 OpenClaw 场景下的长期小说项目交接能力，新增私有 GitHub 同步接口和对应 Skill 工作流规范。

主要变化：

- 新增 `scripts/github_private_sync.py`：用于把本地小说项目 checkpoint 同步到私有 GitHub 仓库。
- 新增 `skill/references/github-sync.md`：定义 OpenClaw 何时同步、同步前检查项、失败报告方式和完成报告格式。
- 新增 `examples/github-sync.example.json`：提供私有 GitHub 同步配置示例。
- 更新 `skill/SKILL.md`：把 GitHub 同步纳入章节完成、审计和迁移交接工作流。
- 更新 `skill/references/closeout-checklist.md`：完成报告要求记录私有 GitHub 同步状态。
- 更新 `README.md`：补充中英文 OpenClaw 私有同步说明。

安全原则：

- 不在仓库中保存 GitHub token、密码或 provider 凭据。
- 同步脚本只调用本地 git，认证交给 SSH key、Git Credential Manager 或运行环境。
- 私有 GitHub 同步是交接证据，不是凭据管理。

### English

This release improves long-form fiction handoff workflows for OpenClaw by adding a private GitHub sync interface and Skill-level operating rules.

Highlights:

- Added `scripts/github_private_sync.py` to sync local novel project checkpoints to a private GitHub repository.
- Added `skill/references/github-sync.md` to define when OpenClaw should sync, required pre-sync checks, failure reporting, and completion report format.
- Added `examples/github-sync.example.json` as a private GitHub sync configuration example.
- Updated `skill/SKILL.md` to include GitHub sync in chapter closeout, audits, and migration handoffs.
- Updated `skill/references/closeout-checklist.md` to require private GitHub sync status in closeout reports.
- Updated `README.md` with bilingual OpenClaw private sync guidance.

Security principles:

- Do not store GitHub tokens, passwords, or provider credentials in the repository.
- The sync script delegates authentication to local git, SSH keys, Git Credential Manager, or the hosting environment.
- Private GitHub sync is handoff evidence, not credential management.
