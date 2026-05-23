# Org Export Workflow / Org mode 大纲导出工作流

Use this workflow when a large project needs a navigable Emacs Org-mode outline generated from local Markdown project files.

本工作流用于把本地 Markdown 项目文件导出为可导航的 Emacs Org-mode 大纲，适合超长篇项目做结构浏览和交接。

## Default inputs / 默认输入

```text
PROJECT_STATE.md
WORK_QUEUE.md
outlines/
characters/
lore/
timelines/
branches/
```

If a project uses custom paths, read `novel-architect.config.json` first.

如果项目使用自定义路径，先读取 `novel-architect.config.json`。

## Default output / 默认输出

```text
exports/org/project-outline.org
```

## Export command / 导出命令

```bash
python3 scripts/export_org_outline.py --project-root . --config novel-architect.config.json
```

Use `--no-body` if you only want headings and metadata summaries:

```bash
python3 scripts/export_org_outline.py --project-root . --config novel-architect.config.json --no-body
```

## Rules / 规则

- This is an optional generated navigation aid, not a canon approval step.
- Emacs is not required to generate the file; the script writes plain `.org` text with Python standard library only.
- Keep generated Org files under `exports/` unless the user explicitly chooses another private path.
- Do not include `external-data/`, databases, raw model logs, credentials, or scratch material in public exports.
- Do not copy GPL code from `org-novelist`; this workflow uses only the Org outline concept.

- 这是可选的导航导出物，不等于 canon 审批。
- 生成文件不需要 Emacs；脚本只用 Python 标准库写出普通 `.org` 文本。
- 生成的 Org 文件默认放在 `exports/` 下，除非用户明确选择其他私有路径。
- 公开导出不要包含 `external-data/`、数据库、原始模型日志、凭据或 scratch 材料。
- 不复制 `org-novelist` 的 GPL 代码；这里只使用 Org 大纲概念。

## Recommended refresh points / 建议刷新时机

Refresh the Org outline when any of these change:

- project state or work queue;
- major outline files;
- timeline events;
- lore cards;
- character files;
- branch simulations or merge decisions.

以下内容变化后，建议刷新 Org 大纲：

- 项目状态或工作队列；
- 主要大纲文件；
- 时间线事件；
- lore 卡；
- 人物文件；
- 分支模拟或合并决策。