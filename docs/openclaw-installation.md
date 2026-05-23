# OpenClaw Installation / OpenClaw 安装说明

## 中文

本项目是一个面向 OpenClaw 的长篇小说工作流 Skill 模板。它的目标不是替你写完整小说，而是帮助 OpenClaw 通过明确文件、固定流程和可迁移资产来管理长期创作项目。

### 1. 获取项目

```bash
git clone https://github.com/Flywithinsun/openclaw-long-novel-architect.git
cd openclaw-long-novel-architect
```

### 2. 复制 Skill

把 `skill/` 复制到你的 OpenClaw Skill 工作区，或按你的 OpenClaw 客户端支持的方式安装。

如果你的小说项目本身也要保存这套 Skill，可以复制到项目根目录：

```bash
cp -R skill /path/to/your-novel-project/skill
cp -R scripts /path/to/your-novel-project/scripts
```

Windows PowerShell 示例：

```powershell
Copy-Item -Recurse skill C:\path\to\your-novel-project\skill
Copy-Item -Recurse scripts C:\path\to\your-novel-project\scripts
```

### 3. 第一次让 OpenClaw 读取

新会话开始时，让 OpenClaw 先读取：

```text
skill/SKILL.md
PROJECT_STATE.md 或 CURRENT_STATE.md
WORK_QUEUE.md
PROJECT_INDEX.md
workflow/model-routing.md
```

如果项目启用了私有 GitHub 同步，再读取：

```text
skill/references/github-sync.md
github-sync.config.json
```

如果项目启用了历史模式，或项目存在这些目录，再按任务需要读取：

```text
standards/
context-packs/
timelines/
maps/
lore/
branches/
reports/
```

### 4. 验证项目资产

```bash
python scripts/verify_portable_assets.py --project-root /path/to/your-novel-project --config /path/to/your-novel-project/novel-architect.config.json
```

历史模式常用附加检查：

```bash
python scripts/timeline_lint.py --project-root /path/to/your-novel-project --config /path/to/your-novel-project/novel-architect.config.json --write-report
python scripts/lore_index.py --project-root /path/to/your-novel-project --config /path/to/your-novel-project/novel-architect.config.json --write-report
python scripts/geo_lint.py --project-root /path/to/your-novel-project --config /path/to/your-novel-project/novel-architect.config.json --write-report
```

### 5. 推荐给 OpenClaw 的第一句话

```text
请先读取 skill/SKILL.md、PROJECT_STATE.md、WORK_QUEUE.md、PROJECT_INDEX.md 和 workflow/model-routing.md，判断当前项目状态。不要依赖隐藏聊天记忆。完成任何章节或审计后，必须更新文件并报告停止点。
```

---

## English

This repository is an OpenClaw Skill template for long-form fiction workflows. It does not write a complete novel by itself; it helps OpenClaw manage long-running projects through explicit files, repeatable workflows, and portable assets.

### 1. Clone the repository

```bash
git clone https://github.com/Flywithinsun/openclaw-long-novel-architect.git
cd openclaw-long-novel-architect
```

### 2. Copy the Skill

Copy `skill/` into your OpenClaw Skill workspace, or install it using your OpenClaw client's supported mechanism.

If your novel project should carry the Skill with it, copy it into the project root:

```bash
cp -R skill /path/to/your-novel-project/skill
cp -R scripts /path/to/your-novel-project/scripts
```

Windows PowerShell example:

```powershell
Copy-Item -Recurse skill C:\path\to\your-novel-project\skill
Copy-Item -Recurse scripts C:\path\to\your-novel-project\scripts
```

### 3. First OpenClaw reads

At the beginning of a fresh session, ask OpenClaw to read:

```text
skill/SKILL.md
PROJECT_STATE.md or CURRENT_STATE.md
WORK_QUEUE.md
PROJECT_INDEX.md
workflow/model-routing.md
```

If private GitHub sync is enabled, also read:

```text
skill/references/github-sync.md
github-sync.config.json
```

If historical mode is enabled, or these directories exist, read them as needed for the task:

```text
standards/
context-packs/
timelines/
maps/
lore/
branches/
reports/
```

### 4. Verify project assets

```bash
python scripts/verify_portable_assets.py --project-root /path/to/your-novel-project --config /path/to/your-novel-project/novel-architect.config.json
```

Common historical-mode checks:

```bash
python scripts/timeline_lint.py --project-root /path/to/your-novel-project --config /path/to/your-novel-project/novel-architect.config.json --write-report
python scripts/lore_index.py --project-root /path/to/your-novel-project --config /path/to/your-novel-project/novel-architect.config.json --write-report
python scripts/geo_lint.py --project-root /path/to/your-novel-project --config /path/to/your-novel-project/novel-architect.config.json --write-report
```

### 5. Suggested first prompt for OpenClaw

```text
Please read skill/SKILL.md, PROJECT_STATE.md, WORK_QUEUE.md, PROJECT_INDEX.md, and workflow/model-routing.md first, then determine the current project state. Do not rely on hidden chat memory. After any chapter or audit is completed, update files and report the stop point.
```
