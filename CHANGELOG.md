# Changelog

## Unreleased - Historical Mode P0 Groundwork

### 中文

- 新增历史模式 P0 基础文档：第三方灵感与许可证边界、历史模式路线图。
- 扩展配置安全边界：默认排除 `external-data/` 与数据库文件（`*.db`、`*.sqlite`、`*.sqlite3`），避免打包 CBDB 等外部历史数据。
- 增强验证脚本：在历史模式启用时提示时间线 / lore / 标准目录缺失，并警告包内路径下的本地数据库文件。
- 同步 README、发布检查清单与脱敏报告，强调历史数据适配器应保持轻量、可选、用户本地自备。
- 补齐 P0 完成记录与 P1 下一步交接说明，README、`AI_NEXT_STEPS.md` 和路线图不再提示从 P0 开始。

### English

- Added historical-mode P0 groundwork docs: third-party inspiration/license boundaries and the historical-mode roadmap.
- Expanded config safety boundaries: exclude `external-data/` and database files (`*.db`, `*.sqlite`, `*.sqlite3`) by default to avoid packaging CBDB or other external historical data.
- Enhanced verification: warn when historical mode is enabled but timeline / lore / standards paths are missing, and warn about local database files under package roots.
- Synced README, release checklist, and sanitization guidance to keep historical data adapters lightweight, optional, and user-provided.
- Added the P0 completion record and P1 next-step handoff so README, `AI_NEXT_STEPS.md`, and the roadmap no longer tell new sessions to start from P0.

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
