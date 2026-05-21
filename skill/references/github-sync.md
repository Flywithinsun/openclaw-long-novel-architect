# GitHub Private Sync

Use this reference when the project is configured to mirror work to a private GitHub repository.

## Purpose

The private GitHub sync is an OpenClaw handoff safety layer. It records durable checkpoints outside the current chat/session so another OpenClaw can resume from files and git history.

It is not a credential manager and must not store tokens in project files.

## Configuration files

Recommended project-local names:

```text
github-sync.config.json
novel-architect.config.json
```

`github-sync.config.json` may contain:

```json
{
  "remote_name": "origin",
  "branch": "main",
  "push_tags": false,
  "auto_commit": false,
  "commit_message": "chore(sync): update private mirror",
  "remote_url": "git@github.com:your-org/your-private-repo.git"
}
```

Do not write access tokens, passwords, personal account metadata, or private provider credentials into this file.

## When OpenClaw should sync

Sync after a meaningful checkpoint, for example:

- chapter draft + support files completed;
- readable/de-AI candidate completed;
- audit completed;
- project state / work queue updated;
- asset package generated and inspected;
- migration handoff prepared.

Do not sync raw scratch, private credentials, failed partial generations, or unreviewed side-miner output unless the project explicitly treats those paths as safe.

## Required checks before sync

Before running the sync command, OpenClaw should confirm:

1. Required files for the current task exist.
2. `PROJECT_STATE.md` / `WORK_QUEUE.md` are updated when relevant.
3. Secret-bearing paths remain excluded.
4. `git status --short` is understood.
5. The destination remote is intended to be private.

Recommended dry run:

```bash
python3 scripts/github_private_sync.py \
  --repo-root /path/to/project \
  --config /path/to/project/github-sync.config.json \
  --dry-run
```

Actual sync:

```bash
python3 scripts/github_private_sync.py \
  --repo-root /path/to/project \
  --config /path/to/project/github-sync.config.json \
  --auto-commit
```

## Completion reporting

When sync is enabled, completion reports should include:

```text
GitHub private sync: PASS / SKIPPED / FAILED
Remote: ____
Branch: ____
Commit status: ____
Push status: ____
Blocker if failed: ____
```

If sync fails, do not claim the cloud handoff is complete. Report the local files written and the exact sync blocker.
