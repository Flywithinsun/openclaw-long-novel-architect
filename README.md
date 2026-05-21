# OpenClaw Long Novel Architect

[中文说明](#中文说明) | [English](#english)

---

## 中文说明

**OpenClaw Long Novel Architect** 是一套可移植的 OpenClaw 长篇小说项目工作流 Skill 模板，用于管理复杂长篇小说的上下文、章节生产、修订、审计、可阅读版 / de-AI 打磨、资产打包和跨 OpenClaw 交接。

这个仓库按公开发布标准设计，**不包含私人小说正文、不包含 API key、不包含 provider 凭据、不包含个人路径、不包含私有模型账号标识**。

### 它适合什么项目？

尤其适合这些类型：

- 长篇历史小说；
- 架空历史 / 权谋 / 军事 / 制度流；
- 多人物、多阵营、多账本项目；
- 需要长期连续性维护的网文 / 连载小说；
- 需要在多个 OpenClaw、多个模型或多个会话之间交接的写作项目。

### 它能做什么？

它帮助 OpenClaw agent：

- 读取并判断当前项目状态；
- 避免依赖隐藏聊天记忆；
- 生成自洽的章节任务包；
- 区分主线 canon 裁决和旁路模型挖矿；
- 生产正文、摘要、自审、账本建议和可阅读版；
- 做十章 / 阶段审计，并锁定下一阶段推进；
- 打包一个脱敏后的迁移资产包；
- 检查迁移后的项目是否具备继续写作条件。
- 在配置允许时，把完成节点同步到私有 GitHub 仓库，方便另一个 OpenClaw 从文件和 git 历史继续接手。

### 它不是什么？

- 不是一整本小说；
- 不是模型 provider 集成；
- 不是 API key 管理器；
- 不保证你的环境里有某个特定模型；
- 不替代你自己的 canon、正文、大纲、人物表、状态文件；
- 不会自动判断你的项目私有资料是否都适合公开发布。

### 目录结构

```text
openclaw-long-novel-architect/
├── README.md
├── LICENSE
├── SECURITY.md
├── .gitignore
├── skill/
│   ├── SKILL.md
│   ├── references/
│   │   ├── project-map.md
│   │   ├── chapter-workflow.md
│   │   ├── deai-workflow.md
│   │   ├── audit-workflow.md
│   │   ├── model-routing.md
│   │   ├── closeout-checklist.md
│   │   ├── asset-package.md
│   │   ├── portability-guide.md
│   │   └── github-sync.md
│   └── templates/
│       ├── chapter-request-template.md
│       ├── deai-request-template.md
│       ├── audit-report-template.md
│       ├── completion-report-template.md
│       ├── project-state-template.md
│       ├── work-queue-template.md
│       ├── project-index-template.md
│       └── model-routing-template.md
├── scripts/
│   ├── package_portable_assets.py
│   ├── verify_portable_assets.py
│   └── github_private_sync.py
├── examples/
│   ├── project-config.example.json
│   ├── github-sync.example.json
│   ├── model-routing.example.md
│   ├── asset-manifest.example.txt
│   └── minimal-project/
└── docs/
    ├── github-release-checklist.md
    ├── migration-quickstart.md
    ├── sanitization-report.md
    ├── openclaw-installation.md
    └── first-project-setup.md
```

### 快速开始

#### 0. 一分钟上手

如果你只是想快速试用：

```bash
git clone https://github.com/Flywithinsun/openclaw-long-novel-architect.git
cd openclaw-long-novel-architect
cp -R examples/minimal-project ../my-novel-project
cd ../my-novel-project
cp -R ../openclaw-long-novel-architect/skill ./skill
cp -R ../openclaw-long-novel-architect/scripts ./scripts
python scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
```

然后让 OpenClaw 先读取：

```text
skill/SKILL.md
PROJECT_STATE.md
WORK_QUEUE.md
PROJECT_INDEX.md
workflow/model-routing.md
```

更多说明见：

- `docs/openclaw-installation.md`
- `docs/first-project-setup.md`
- `examples/minimal-project/`

#### 1. 安装 / 复制 Skill

把 `skill/` 复制到你的 OpenClaw 工作区，或按照你的 OpenClaw Skill 机制安装。

#### 2. 准备项目配置

复制示例配置到你的小说项目根目录：

```bash
cp examples/project-config.example.json /path/to/your/project/novel-architect.config.json
```

然后编辑：

- 项目名称；
- 章节前缀；
- 正文目录；
- 可阅读版目录；
- 摘要 / 审计 / 账本目录；
- 必需资产；
- 推荐资产；
- 模型角色映射。

#### 3. 验收项目资产

```bash
python3 scripts/verify_portable_assets.py \
  --project-root /path/to/your/project \
  --config /path/to/your/project/novel-architect.config.json
```

严格模式：

```bash
python3 scripts/verify_portable_assets.py \
  --project-root /path/to/your/project \
  --config /path/to/your/project/novel-architect.config.json \
  --strict
```

#### 4. 打包脱敏迁移包

```bash
python3 scripts/package_portable_assets.py \
  --project-root /path/to/your/project \
  --config /path/to/your/project/novel-architect.config.json \
  --output-dir /tmp/portable-novel
```

输出：

```text
<project-name>-portable-YYYYMMDD-HHMMSS.zip
<project-name>-portable-YYYYMMDD-HHMMSS-MANIFEST.txt
```

#### 5. 在新 OpenClaw 落地

```bash
mkdir -p /path/to/new/project
cd /path/to/new/project
unzip /path/to/package.zip
python3 scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
```

确认通过后，再让 OpenClaw 读取 `skill/SKILL.md` 和你的项目状态文件。

#### 6. 同步到私有 GitHub 仓库

如果你希望在每次 git 环节后自动同步到自己的私有 GitHub 项目，可以使用：

```bash
python3 scripts/github_private_sync.py --repo-root /path/to/your/project --config /path/to/your/project/github-sync.config.json --auto-commit
```

支持的能力：

- 自动检测当前 git 仓库；
- 自动读取当前分支并推送到配置的远程；
- 可选自动提交未提交改动；
- 可选推送 tags；
- 支持 `--dry-run` 预演。

注意：这个接口**只负责调用本地 git**，不会在代码里保存 GitHub token。你应当通过本机 git remote、Git Credential Manager、SSH key 或其他本地凭据方案完成认证。

示例配置见：`examples/github-sync.example.json`

OpenClaw 使用时，应该先读取 `skill/references/github-sync.md`，并把同步结果写进完成报告：`PASS / SKIPPED / FAILED`。

### 推荐项目文件结构

默认建议：

```text
PROJECT_STATE.md 或 CURRENT_STATE.md
WORK_QUEUE.md
PROJECT_INDEX.md
workflow/
drafts/
readable/ 或 de-ai/
summaries/
audits/
ledgers/
outlines/
characters/
canon/ 或 bible/
skill/
scripts/
```

你也可以在 `novel-architect.config.json` 中改成自己的目录结构。

### 模型角色，而不是固定模型名

公共版不绑定任何 provider 或模型名。你需要把自己的模型映射到这些角色：

| 角色 | 用途 |
|---|---|
| `organizer` | 日常交流、上下文压缩、任务整理 |
| `final_canon` | 最终正文、canon 守门、可阅读版终审 |
| `side_miner_primary` | 旁路挖矿、反方审查、漏洞检查 |
| `side_miner_texture` | 人味、动作、口吻、生活细节 |
| `side_miner_structure` | 结构、连续性、长上下文检查 |
| `engineering_helper` | 脚本、验收、打包、工程修补 |

原则：**旁路模型只提供材料，不能直接入 canon。最终版本必须由 `final_canon` 角色裁决。**

### 默认安全设计

打包脚本默认排除：

- `.git/`
- `.env`、`.secrets/`、credential 文件；
- raw model logs；
- `scratch/`；
- `inbox/`、`outbox/`；
- `archive/`；
- `backups/`；
- 压缩包、日志、缓存文件。

发布或分享任何生成包之前，仍建议你运行自己的 secret scanner。

### 工作流哲学

1. **Skill 管方法，项目资产管事实。**
2. **章节任务包必须自洽，不能依赖隐藏记忆。**
3. **旁路模型输出只是矿料，不是 canon。**
4. **必须有最终 canon 角色负责正文和连续性裁决。**
5. **完成必须有文件、检查和停点。**
6. **完成一章不等于自动开始下一章。**
7. **审计不仅判断过去，还必须锁定下一阶段。**
8. **如果启用私有 GitHub 同步，同步是交接证据，不是凭据管理。**

### 发布前检查

如果你要发布自己的项目包，至少检查：

```bash
grep -RInE "(sk-|api[_-]?key|token|secret|credential|Authorization|Bearer|password|\.secrets|\.env)" .
python3 scripts/verify_portable_assets.py --project-root /path/to/project --config /path/to/project/novel-architect.config.json
```

更稳妥的做法是使用 `gitleaks` 或 `trufflehog` 等专门工具。

### License

MIT。详见 `LICENSE`。

---

## English

**OpenClaw Long Novel Architect** is a portable OpenClaw Skill template for managing long-form fiction projects with structured context, chapter production, revision, audit, readability / de-AI polishing, asset packaging, and cross-OpenClaw handoff workflows.

This repository is designed for public GitHub release. It contains **no private novel text, no API keys, no provider credentials, no personal paths, and no private model account identifiers**.

### What kind of project is this for?

It is especially useful for:

- long historical novels;
- alternate-history, political, military, or institution-heavy fiction;
- multi-character, multi-faction, continuity-heavy projects;
- serialized fiction requiring long-term state management;
- projects handed across multiple OpenClaw agents, model routes, or chat sessions.

### What does it help with?

It helps an OpenClaw agent:

- discover the current project state;
- avoid relying on hidden chat memory;
- generate self-contained chapter requests;
- separate final canon decisions from side-model mining;
- produce drafts, summaries, self-audits, ledger updates, and readable candidates;
- run range audits and lock the next stage;
- package a sanitized asset bundle for another OpenClaw;
- verify whether a migrated project has enough assets to continue safely.
- sync completed checkpoints to a private GitHub repository when configured, so another OpenClaw can resume from files and git history.

### What this is not

- Not a complete novel.
- Not a model provider integration.
- Not an API key manager.
- Not a guarantee that any specific model route exists in your environment.
- Not a replacement for your canon files, drafts, outlines, character files, or state files.
- Not an automatic privacy auditor for every project package you generate.

### Directory layout

```text
openclaw-long-novel-architect/
├── README.md
├── LICENSE
├── SECURITY.md
├── .gitignore
├── skill/
│   ├── SKILL.md
│   ├── references/
│   │   ├── project-map.md
│   │   ├── chapter-workflow.md
│   │   ├── deai-workflow.md
│   │   ├── audit-workflow.md
│   │   ├── model-routing.md
│   │   ├── closeout-checklist.md
│   │   ├── asset-package.md
│   │   ├── portability-guide.md
│   │   └── github-sync.md
│   └── templates/
│       ├── chapter-request-template.md
│       ├── deai-request-template.md
│       ├── audit-report-template.md
│       ├── completion-report-template.md
│       ├── project-state-template.md
│       ├── work-queue-template.md
│       ├── project-index-template.md
│       └── model-routing-template.md
├── scripts/
│   ├── package_portable_assets.py
│   ├── verify_portable_assets.py
│   └── github_private_sync.py
├── examples/
│   ├── project-config.example.json
│   ├── github-sync.example.json
│   ├── model-routing.example.md
│   ├── asset-manifest.example.txt
│   └── minimal-project/
└── docs/
    ├── github-release-checklist.md
    ├── migration-quickstart.md
    ├── sanitization-report.md
    ├── openclaw-installation.md
    └── first-project-setup.md
```

### Quick start

#### 0. One-minute start

If you just want to try it quickly:

```bash
git clone https://github.com/Flywithinsun/openclaw-long-novel-architect.git
cd openclaw-long-novel-architect
cp -R examples/minimal-project ../my-novel-project
cd ../my-novel-project
cp -R ../openclaw-long-novel-architect/skill ./skill
cp -R ../openclaw-long-novel-architect/scripts ./scripts
python scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
```

Then ask OpenClaw to read:

```text
skill/SKILL.md
PROJECT_STATE.md
WORK_QUEUE.md
PROJECT_INDEX.md
workflow/model-routing.md
```

See also:

- `docs/openclaw-installation.md`
- `docs/first-project-setup.md`
- `examples/minimal-project/`

#### 1. Install / copy the Skill

Copy `skill/` into your OpenClaw workspace, or install it according to your OpenClaw Skill mechanism.

#### 2. Prepare project config

Copy the example config into your novel project root:

```bash
cp examples/project-config.example.json /path/to/your/project/novel-architect.config.json
```

Then edit:

- project name;
- chapter prefix;
- draft directory;
- readable directory;
- summary / audit / ledger directories;
- required assets;
- recommended assets;
- model role mapping.

#### 3. Verify project assets

```bash
python3 scripts/verify_portable_assets.py \
  --project-root /path/to/your/project \
  --config /path/to/your/project/novel-architect.config.json
```

Strict mode:

```bash
python3 scripts/verify_portable_assets.py \
  --project-root /path/to/your/project \
  --config /path/to/your/project/novel-architect.config.json \
  --strict
```

#### 4. Package a sanitized migration bundle

```bash
python3 scripts/package_portable_assets.py \
  --project-root /path/to/your/project \
  --config /path/to/your/project/novel-architect.config.json \
  --output-dir /tmp/portable-novel
```

Output:

```text
<project-name>-portable-YYYYMMDD-HHMMSS.zip
<project-name>-portable-YYYYMMDD-HHMMSS-MANIFEST.txt
```

#### 5. Deploy in another OpenClaw workspace

```bash
mkdir -p /path/to/new/project
cd /path/to/new/project
unzip /path/to/package.zip
python3 scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
```

After verification passes, let OpenClaw read `skill/SKILL.md` and your project state files.

#### 6. Sync to a private GitHub repository

If the project enables private GitHub sync, use:

```bash
python3 scripts/github_private_sync.py --repo-root /path/to/your/project --config /path/to/your/project/github-sync.config.json --auto-commit
```

OpenClaw should read `skill/references/github-sync.md` first and report the sync result as `PASS / SKIPPED / FAILED`.

This script delegates authentication to local git, SSH agent, Git Credential Manager, or the hosting environment. Do not store GitHub tokens in project files.

### Recommended project layout

Default recommendation:

```text
PROJECT_STATE.md or CURRENT_STATE.md
WORK_QUEUE.md
PROJECT_INDEX.md
workflow/
drafts/
readable/ or de-ai/
summaries/
audits/
ledgers/
outlines/
characters/
canon/ or bible/
skill/
scripts/
```

You can override this in `novel-architect.config.json`.

### Model roles, not fixed model names

The public template does not bind to any provider or model name. Map your own models to these roles:

| Role | Purpose |
|---|---|
| `organizer` | chat, context compression, task structuring |
| `final_canon` | final prose, canon gate, readable approval |
| `side_miner_primary` | side mining, red-team review, loophole checks |
| `side_miner_texture` | human texture, action detail, voice variants |
| `side_miner_structure` | structure, continuity, long-context review |
| `engineering_helper` | scripts, verification, packaging, workflow tooling |

Principle: **side models provide material only. They do not write directly into canon. Final output must be approved by the `final_canon` role.**

### Public safety design

The packaging script excludes by default:

- `.git/`
- `.env`, `.secrets/`, credential files;
- raw model logs;
- `scratch/`;
- `inbox/`, `outbox/`;
- `archive/`;
- `backups/`;
- compressed files, logs, and caches.

Before publishing or sharing any generated package, you should still run your own secret scanner.

### Core workflow philosophy

1. **Skill controls method; project assets control facts.**
2. **Every chapter request must be self-contained.**
3. **Side-model outputs are mining material, not canon.**
4. **A final canon role/model must make prose and continuity decisions.**
5. **Completion requires files, checks, and a stop point.**
6. **A completed chapter does not authorize starting the next chapter.**
7. **Audits must lock the next stage, not merely judge the past.**
8. **Private GitHub sync is handoff evidence, not credential management.**

### Pre-release checks

If you publish your own project package, at minimum run:

```bash
grep -RInE "(sk-|api[_-]?key|token|secret|credential|Authorization|Bearer|password|\.secrets|\.env)" .
python3 scripts/verify_portable_assets.py --project-root /path/to/project --config /path/to/project/novel-architect.config.json
```

For stronger assurance, use dedicated tools such as `gitleaks` or `trufflehog`.

### License

MIT. See `LICENSE`.
