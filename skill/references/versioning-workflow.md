# Versioning Workflow / 版本管理工作流

Use this workflow when a long-novel project needs safe Git-backed drafting, repair, audit, branch simulation, or release preparation.

本工作流用于把长篇小说项目当作可回滚、可审查、可交接的软件项目来管理。

## Goals / 目标

- Keep manuscript changes recoverable.
- Make experiments and repairs visible before they enter canon.
- Record snapshots at chapter closeout, audit closeout, and release milestones.
- Keep GitHub sync optional and credential-free.

## Suggested branch names / 推荐分支名

```text
main
experiment/history-*
repair/chNNN-*
audit/range-*
release/volume-*
```

## When to create a revision branch / 何时开修订分支

Create or recommend a branch when work:

- rewrites a completed chapter;
- changes canon, timeline, lore, or branch merge status;
- repairs a failed audit;
- prepares a volume/release export;
- explores an experimental alternate-history path.

## Snapshot rule / 快照规则

Before reporting a major stop point, run or recommend:

```bash
python3 scripts/project_snapshot.py --project-root . --config novel-architect.config.json --write-report
```

The report should include:

1. current Git branch;
2. recent commits;
3. uncommitted files;
4. current completed chapter;
5. latest draft/readable/summary/audit files;
6. current stop point;
7. GitHub sync config status.

## Closeout behavior / 收口行为

- Do not auto-commit without explicit user instruction.
- Do not push without explicit user instruction or a configured workflow that the user has approved.
- If Git is unavailable, record the limitation in the snapshot and continue with file-based handoff.
- Private GitHub sync remains optional and must not store credentials in project files.
