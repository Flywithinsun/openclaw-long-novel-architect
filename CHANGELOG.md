# Changelog

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
