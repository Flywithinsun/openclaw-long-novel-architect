# First Project Setup / 首个项目设置

## 中文

本指南用于创建一个最小可用的长篇小说项目目录，让 OpenClaw 可以从文件而不是聊天记忆中接手。

### 1. 创建目录

```bash
mkdir my-novel-project
cd my-novel-project
mkdir workflow drafts readable summaries audits ledgers outlines characters canon writing-requests exports
```

### 2. 复制模板

从本仓库复制：

```bash
cp examples/project-config.example.json novel-architect.config.json
cp skill/templates/project-state-template.md PROJECT_STATE.md
cp skill/templates/work-queue-template.md WORK_QUEUE.md
cp skill/templates/project-index-template.md PROJECT_INDEX.md
cp skill/templates/model-routing-template.md workflow/model-routing.md
```

然后编辑这些文件，至少填入：

- 项目名称；
- 当前完成到哪一章；
- 下一步任务；
- 主要人物和 canon 文件位置；
- OpenClaw 可用模型角色映射。

### 3. 安装 Skill 和脚本

```bash
cp -R /path/to/openclaw-long-novel-architect/skill ./skill
cp -R /path/to/openclaw-long-novel-architect/scripts ./scripts
```

### 4. 验证

```bash
python scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
```

如果只是刚初始化，可能会看到没有章节文件的 warning。这是正常的；缺少 required 文件才需要先修复。

### 5. 推荐工作方式

每次新 OpenClaw 会话开始：

1. 读取 `skill/SKILL.md`。
2. 读取 `PROJECT_STATE.md`、`WORK_QUEUE.md`、`PROJECT_INDEX.md`。
3. 读取 `workflow/model-routing.md`。
4. 只根据文件判断进度。
5. 完成任务后更新状态文件并停止。

---

## English

This guide creates a minimal long-novel project layout so OpenClaw can resume from files instead of hidden chat memory.

### 1. Create directories

```bash
mkdir my-novel-project
cd my-novel-project
mkdir workflow drafts readable summaries audits ledgers outlines characters canon writing-requests exports
```

### 2. Copy templates

From this repository:

```bash
cp examples/project-config.example.json novel-architect.config.json
cp skill/templates/project-state-template.md PROJECT_STATE.md
cp skill/templates/work-queue-template.md WORK_QUEUE.md
cp skill/templates/project-index-template.md PROJECT_INDEX.md
cp skill/templates/model-routing-template.md workflow/model-routing.md
```

Then edit these files. At minimum, fill in:

- project name;
- current completed chapter;
- next tasks;
- key characters and canon file locations;
- available OpenClaw model role mapping.

### 3. Install Skill and scripts

```bash
cp -R /path/to/openclaw-long-novel-architect/skill ./skill
cp -R /path/to/openclaw-long-novel-architect/scripts ./scripts
```

### 4. Verify

```bash
python scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
```

For a freshly initialized project, warnings about missing chapter files are expected. Missing required files should be fixed first.

### 5. Recommended workflow

At the start of each fresh OpenClaw session:

1. Read `skill/SKILL.md`.
2. Read `PROJECT_STATE.md`, `WORK_QUEUE.md`, and `PROJECT_INDEX.md`.
3. Read `workflow/model-routing.md`.
4. Determine progress from files only.
5. After completing a task, update state files and stop.
