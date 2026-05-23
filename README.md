# OpenClaw Long Novel Architect

[中文说明](#中文说明) | [长期规则与进度记录](#长期规则与进度记录)

---

## 中文说明

**OpenClaw Long Novel Architect** 是一套可移植的 OpenClaw 长篇小说项目工作流 Skill 模板，用于管理复杂长篇小说的上下文、章节生产、修订、审计、可阅读版 / de-AI 打磨、资产打包和跨 OpenClaw 交接。

这个仓库按公开发布标准设计，**不包含私人小说正文、不包含 API key、不包含 provider 凭据、不包含个人路径、不包含私有模型账号标识**。

### 下一步开发计划与交接入口

如果你是在另一个对话里接手本项目的 AI，请先读：

```text
AI_NEXT_STEPS.md
docs/historical-mode-roadmap.md
docs/HISTORICAL_NOVEL_ENHANCEMENT_PLAN.md
```

当前状态：**P5：历史逻辑审计委员会进行中**。P1/P3/P4/P10 partial 已完成可用版本，当前加入多角色历史合理性审计工作流。

当前路线图顺序是 P1 → P3 → P4 → P10 partial → P5。不要先集成 AutoGen、CBDB、Electron、Obsidian、Emacs 或任何外部模型 provider；历史数据适配器仍应保持用户本地自备、默认不打包。

历史模式路线图见：[`docs/historical-mode-roadmap.md`](docs/historical-mode-roadmap.md)<br>
第三方灵感与许可证边界见：[`docs/third-party-inspiration.md`](docs/third-party-inspiration.md)<br>
完整 AI 交接实施计划见：[`docs/HISTORICAL_NOVEL_ENHANCEMENT_PLAN.md`](docs/HISTORICAL_NOVEL_ENHANCEMENT_PLAN.md)

历史数据适配器应保持**轻量、可选、用户本地自备**：优先读取 SQLite / CSV / JSON 等简单格式；公共模板和默认打包流程不捆绑 CBDB 或任何第三方历史数据库。

### 历史模式阶段进度

| 阶段 | 状态 | 说明 |
|---|---|---|
| P0：许可、安全与范围边界 | 已完成 | 已建立第三方灵感 / GPL 边界、CBDB 与外部数据不打包规则、`external-data/` 与数据库文件排除、路线图与 README 指针。 |
| P1：双轴历史时间线 | 已完成首版 | 已建立真实历史与架空历史时间线目录、事件模板、时间线工作流和 `scripts/timeline_lint.py`。 |
| P3：Lore 元数据与交叉引用 | 已完成首版 | 已建立 lore 工作流、卡片模板、来源模板、minimal project 示例卡片和 `scripts/lore_index.py`。 |
| P4：上下文层与时代语言控制 | 已完成首版 | 已建立 standards、context-packs、上下文层工作流与 de-AI 规则引用。 |
| P5：历史逻辑审计委员会 | 进行中 | 已加入逻辑审计工作流、请求/报告模板、示例审计和章节审计接入说明。 |

#### P1 交付物

- `skill/references/timeline-workflow.md`
- `skill/templates/timeline-event-template.md`
- `skill/templates/timeline-audit-template.md`
- `examples/minimal-project/timelines/README.md`
- `examples/minimal-project/timelines/real-history.md`
- `examples/minimal-project/timelines/alt-history.md`
- `scripts/timeline_lint.py`

P1 完成标准：示例时间线可被脚本检查；真实历史事件要求来源字段；架空历史事件要求章节关联；旧的非历史项目仍可通过基础验证。

#### P1 时间线检查

在启用或维护历史模式的项目中运行：

```bash
python3 scripts/timeline_lint.py --project-root . --config novel-architect.config.json --write-report
```

检查报告默认写入：

```text
reports/timeline-lint-report.md
```

时间线事件使用 `# Timeline Event` Markdown 段落和 `- key: value` 元数据；真实历史事件使用 `track: real_history`，架空历史事件使用 `track: alt_history` 并关联章节。

#### P3 Lore 检查

在启用或维护 lore 元数据的项目中运行：

```bash
python3 scripts/lore_index.py --project-root . --config novel-architect.config.json --write-report
```

检查报告默认写入：

```text
reports/lore-index-report.md
```

Lore 卡片使用 `- id: lore-...` 元数据，并可在正文、摘要、审计、账本中使用 `@lore:`、`@source:`、`@event:`、`@chapter:` 等标签交叉引用。

### 长期规则与进度记录

1. 本 README 以后只保留中文说明；只有文件名、命令、路径、代码块、参数名、链接锚点等必要内容可以保留原样。
2. 每次开始一个明确阶段前，先确认或更新本节进度记录；不要为每个微小命令制造噪音。
3. Git 提交 / 推送前，必须把本节更新到“准备同步”的稳定状态。
4. Git 推送完成后，在完成报告中记录同步结果；除非还有实质内容变化，不再只为时间戳新增提交，避免“更新记录 → 提交 → 推送 → 再更新记录”的循环。
5. 如果有新的对话接手，请先看本 README、`AI_NEXT_STEPS.md` 和本节记录。

#### 当前进度记录

| 项目 | 当前值 |
|---|---|
| 记录时间 | 2026-05-23 21:15:00 +08 |
| 当前阶段 | P5：历史逻辑审计委员会 |
| P0 状态 | 已完成 |
| 下一步 | 继续完善逻辑审计流程与示例，验证 P5 工作流 |
| 最近一次 Git 同步本地时间 | 2026-05-23 21:29 +08 |
| 当前状态 | P1/P3/P4/P10 partial 已提交并同步；P5 资产已加入工作区，准备继续完善审计流程 |

#### 下次更新格式

- 当前阶段：……
- P0 状态：……
- 下一步：……
- 最近一次 Git 同步本地时间：YYYY-MM-DD HH:MM:SS +08
- 当前状态：……

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
- 不是公共历史数据库镜像，也不会默认捆绑 CBDB、SQLite 数据库或其他第三方数据集；

### 目录结构

```text
openclaw-long-novel-architect/
├── README.md
├── AI_NEXT_STEPS.md
├── LICENSE
├── SECURITY.md
├── .gitignore
├── skill/
│   ├── SKILL.md
│   ├── references/
│   │   ├── project-map.md
│   │   ├── chapter-workflow.md
│   │   ├── timeline-workflow.md
│   │   ├── lore-metadata-workflow.md
│   │   ├── context-layer-workflow.md
│   │   ├── deai-workflow.md
│   │   ├── audit-workflow.md
│   │   ├── logic-audit-committee.md
│   │   ├── model-routing.md
│   │   ├── closeout-checklist.md
│   │   ├── asset-package.md
│   │   ├── portability-guide.md
│   │   └── github-sync.md
│   └── templates/
│       ├── chapter-request-template.md
│       ├── timeline-event-template.md
│       ├── timeline-audit-template.md
│       ├── lore-card-template.md
│       ├── source-note-template.md
│       ├── context-pack-template.md
│       ├── style-standard-template.md
│       ├── deai-request-template.md
│       ├── audit-report-template.md
│       ├── logic-audit-request-template.md
│       ├── logic-audit-report-template.md
│       ├── completion-report-template.md
│       ├── project-state-template.md
│       ├── work-queue-template.md
│       ├── project-index-template.md
│       └── model-routing-template.md
├── scripts/
│   ├── package_portable_assets.py
│   ├── verify_portable_assets.py
│   ├── timeline_lint.py
│   ├── lore_index.py
│   └── github_private_sync.py
├── examples/
│   ├── project-config.example.json
│   ├── github-sync.example.json
│   ├── model-routing.example.md
│   ├── asset-manifest.example.txt
│   └── minimal-project/
└── docs/
    ├── HISTORICAL_NOVEL_ENHANCEMENT_PLAN.md
    ├── historical-mode-roadmap.md
    ├── third-party-inspiration.md
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
- `external-data/`；
- SQLite / 本地数据库文件，例如 `*.db`、`*.sqlite`、`*.sqlite3`；
- 压缩包、日志、缓存文件。

用户本地研究数据、CSV / JSON 数据集和第三方历史数据库副本应默认留在 `external-data/` 或其他私有位置；只有在你明确确认许可证、脱敏和体积后，才应主动纳入自己的私有包。

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

同时确认 `external-data/`、`*.db`、`*.sqlite`、`*.sqlite3` 以及本地 CSV / JSON 研究数据没有被误纳入公开发布包。

### 许可证

MIT。详见 `LICENSE`。
