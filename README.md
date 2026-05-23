# OpenClaw Long Novel Architect

**OpenClaw Long Novel Architect** 是一套面向长篇小说创作的可移植工作流 Skill 模板，用于帮助 OpenClaw 在长期项目中管理上下文、章节任务、canon 裁决、修订审计、可阅读版打磨、资产打包与跨会话交接。

这个仓库按公开发布标准设计，**不包含私人小说正文、不包含 API key、不包含 provider 凭据、不包含个人路径、不包含私有模型账号标识**。

---

## 适合什么项目？

它尤其适合：

- 长篇历史小说；
- 架空历史、权谋、军事、制度流作品；
- 多人物、多阵营、多账本项目；
- 需要长期连续性维护的网文或连载小说；
- 需要在多个 OpenClaw、多个模型或多个会话之间交接的写作项目。

## 它能做什么？

它帮助 OpenClaw agent：

- 读取并判断当前小说项目状态；
- 避免依赖隐藏聊天记忆；
- 生成自洽的章节任务包；
- 区分主线 canon 裁决和旁路模型挖矿；
- 生产正文、摘要、自审、账本建议和可阅读版；
- 执行阶段审计，并锁定下一阶段推进条件；
- 打包脱敏后的迁移资产包；
- 检查迁移后的项目是否具备继续写作条件；
- 在配置允许时，把完成节点同步到私有 GitHub 仓库，方便之后从文件和 git 历史继续接手。

## 它不是什么？

- 不是一整本小说；
- 不是模型 provider 集成；
- 不是 API key 管理器；
- 不保证你的环境里有某个特定模型；
- 不替代你自己的 canon、正文、大纲、人物表、状态文件；
- 不会自动判断你的项目私有资料是否都适合公开发布；
- 不是公共历史数据库镜像，也不会默认捆绑 CBDB、SQLite 数据库或其他第三方数据集。

## 核心理念

1. **Skill 管方法，项目资产管事实。**
2. **章节任务包必须自洽，不能依赖隐藏记忆。**
3. **旁路模型输出只是矿料，不是 canon。**
4. **必须有最终 canon 角色负责正文和连续性裁决。**
5. **完成必须有文件、检查和停点。**
6. **完成一章不等于自动开始下一章。**
7. **审计不仅判断过去，还必须锁定下一阶段。**
8. **如果启用私有 GitHub 同步，同步是交接证据，不是凭据管理。**

---

## 快速开始

### 一分钟上手

```bash
git clone https://github.com/Flywithinsun/openclaw-long-novel-architect.git
cd openclaw-long-novel-architect
cp -R examples/minimal-project ../my-novel-project
cd ../my-novel-project
cp -R ../openclaw-long-novel-architect/skill ./skill
cp -R ../openclaw-long-novel-architect/scripts ./scripts
python3 scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
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

- [`docs/openclaw-installation.md`](docs/openclaw-installation.md)
- [`docs/first-project-setup.md`](docs/first-project-setup.md)
- [`examples/minimal-project/`](examples/minimal-project/)

### 安装 / 复制 Skill

把 `skill/` 复制到你的 OpenClaw 工作区，或按照你的 OpenClaw Skill 机制安装。

### 准备项目配置

复制示例配置到你的小说项目根目录：

```bash
cp examples/project-config.example.json /path/to/your/project/novel-architect.config.json
```

然后按你的项目情况编辑项目名称、章节前缀、正文目录、可阅读版目录、摘要目录、审计目录、账本目录、资产清单和模型角色映射。

### 验收项目资产

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

### 打包脱敏迁移包

```bash
python3 scripts/package_portable_assets.py \
  --project-root /path/to/your/project \
  --config /path/to/your/project/novel-architect.config.json \
  --output-dir /tmp/portable-novel
```

输出示例：

```text
<project-name>-portable-YYYYMMDD-HHMMSS.zip
<project-name>-portable-YYYYMMDD-HHMMSS-MANIFEST.txt
```

### 在新 OpenClaw 落地

```bash
mkdir -p /path/to/new/project
cd /path/to/new/project
unzip /path/to/package.zip
python3 scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
```

确认通过后，再让 OpenClaw 读取 `skill/SKILL.md` 和你的项目状态文件。

### 同步到私有 GitHub 仓库

如果你希望在每次 git 环节后自动同步到自己的私有 GitHub 项目，可以使用：

```bash
python3 scripts/github_private_sync.py --repo-root /path/to/your/project --config /path/to/your/project/github-sync.config.json --auto-commit
```

支持能力：

- 自动检测当前 git 仓库；
- 自动读取当前分支并推送到配置的远程；
- 可选自动提交未提交改动；
- 可选推送 tags；
- 支持 `--dry-run` 预演。

注意：这个接口**只负责调用本地 git**，不会在代码里保存 GitHub token。你应当通过本机 git remote、Git Credential Manager、SSH key 或其他本地凭据方案完成认证。

示例配置见：[`examples/github-sync.example.json`](examples/github-sync.example.json)。

---

## 推荐项目文件结构

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
timelines/
maps/
lore/
external-data/
standards/
context-packs/
branches/
reports/
exports/
skill/
scripts/
```

你也可以在 `novel-architect.config.json` 中改成自己的目录结构。

## 仓库目录概览

```text
openclaw-long-novel-architect/
├── README.md
├── LICENSE
├── SECURITY.md
├── skill/
│   ├── SKILL.md
│   ├── references/
│   └── templates/
├── scripts/
├── examples/
│   ├── project-config.example.json
│   ├── github-sync.example.json
│   ├── model-routing.example.md
│   └── minimal-project/
└── docs/
```

## 模型角色，而不是固定模型名

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

## 历史小说支持

本模板包含历史小说常用的项目资产与检查流程，例如：

- 双轴时间线：真实历史与架空历史并行维护；
- 地理、路线、补给、通信与人物移动约束；
- lore 卡片、来源记录与交叉引用；
- 时代语言、文体标准与上下文层控制；
- 历史逻辑审计与分支模拟；
- 用户本地自备历史数据的轻量查询与 lore 草稿生成；
- Org mode 大纲导出、项目快照和手稿导出。

历史数据源必须由用户本地自备，并在项目配置中显式启用。公共模板和默认打包流程不会捆绑 CBDB 或任何第三方历史数据库。

## 默认安全设计

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

## 发布前检查

如果你要发布自己的项目包，至少检查：

```bash
grep -RInE "(sk-|api[_-]?key|token|secret|credential|Authorization|Bearer|password|\.secrets|\.env)" .
python3 scripts/verify_portable_assets.py --project-root /path/to/project --config /path/to/project/novel-architect.config.json
```

更稳妥的做法是使用 `gitleaks` 或 `trufflehog` 等专门工具。

同时确认 `external-data/`、`*.db`、`*.sqlite`、`*.sqlite3` 以及本地 CSV / JSON 研究数据没有被误纳入公开发布包。

## 许可证

MIT。详见 [`LICENSE`](LICENSE)。
