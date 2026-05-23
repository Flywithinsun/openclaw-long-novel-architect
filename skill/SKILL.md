---
name: long-novel-architect
description: A portable OpenClaw skill for managing long-form fiction projects: state discovery, chapter requests, drafting workflow, readability/de-AI polishing, audits, asset packaging, migration, and completion discipline. Public-safe template; configure project-specific paths and model routes in a separate config file.
---

# Long Novel Architect

This Skill controls a long-form fiction project through explicit files, repeatable workflows, and safe handoff packages. It is designed for fresh OpenClaw sessions and migrated workspaces where hidden chat memory is unavailable.

## 0. Public-safe design

This Skill intentionally uses generic role names and configurable paths. Do not hardcode private model provider IDs, API endpoints, personal directories, cloud account names, or credentials in this file.

Project-specific values belong in:

```text
novel-architect.config.json
PROJECT_STATE.md / CURRENT_STATE.md
WORK_QUEUE.md
workflow/model-routing.md
github-sync.config.json, if private GitHub sync is enabled
```

## 1. Non-negotiable operating rules

1. **Use files as truth.** Current progress comes from state files, chapter directories, and recent version control, not memory.
2. **No hidden-memory dependency.** Requests and handoffs must be self-contained.
3. **Separate roles.** Organizer, side-miner, engineering helper, and final canon judge are distinct responsibilities even if one model performs multiple roles.
4. **Side material is not canon.** Side-model outputs must be reviewed by the final canon role before entering drafts/readable outputs.
5. **Completion requires evidence.** Do not claim completion without file checks, verification output, and version-control status or a named blocker.
6. **Stop after completion.** Finishing one chapter does not authorize starting the next chapter.
7. **Protect private data.** Never package secrets, raw logs, credentials, personal paths, or private archives by default.
8. **Prefer reversible operations.** Avoid destructive deletes; archive or ask when unsure.
9. **Historical timeline discipline.** If historical mode is enabled, read configured timeline files before drafting or auditing chapters, and do not let alternate-history changes enter canon without final review.
10. **Logic audit discipline.** Major reforms, wars, technology shifts, logistics changes, and social-order changes require a logic audit or explicit user override before canonizing.

## 2. Mandatory first reads

For a fresh session, read the configured equivalents of:

```text
PROJECT_STATE.md or CURRENT_STATE.md
WORK_QUEUE.md
PROJECT_INDEX.md or FILES.md
workflow/model-routing.md
workflow/start-chapter.md
timelines/real-history.md, if historical mode is enabled
timelines/alt-history.md, if historical mode is enabled
lore/index.md, if lore tracking is enabled
standards/prose-style.md, if present
context-packs/chapter-context-template.md, if present
references/logic-audit-committee.md, if major historical changes are being proposed
```

For progress questions, also inspect chapter directories and recent version control:

```bash
ls drafts/ readable/ summaries/ audits/ ledgers/ 2>/dev/null
git log --oneline -5 2>/dev/null || true
```

If the project uses another directory layout, follow `novel-architect.config.json`.

## 3. Model role contract

The exact provider/model names are project-specific. This Skill uses roles:

| Role | Responsibility | Must not do |
|---|---|---|
| `organizer` | chat, compression, context packing, light editing | final canon decisions |
| `final_canon` | final prose selection, continuity, terminal review, readable/de-AI approval | silent downgrade |
| `side_miner_primary` | diagnosis, alternative scenes, red-team | direct canon writes |
| `side_miner_texture` | life texture, body reactions, voice variants | direct canon writes |
| `side_miner_structure` | continuity, structure, loopholes | replacing final canon |
| `engineering_helper` | scripts, validators, packaging, workflow tools | prose canon |

Map these roles in `workflow/model-routing.md` or your config. If a route is unavailable, record the fallback and its limitations.

## 4. Standard chapter workflow

A full chapter is complete only when all configured required assets exist and pass checks.

1. Confirm target chapter and scope: request-only, draft-only, full chapter, repair, or audit.
2. Verify current progress from state files, chapter directories, and git.
3. Load recent summaries, outline nodes, ledger constraints, and name/continuity locks.
   - If historical mode is enabled, also load relevant `timelines/real-history.md`, `timelines/alt-history.md`, and optional timeline track files.
   - If lore tracking is enabled, also load `lore/index.md` and relevant lore cards.
   - If standards/context packs are present, load relevant style standards and the chapter context pack.
4. Generate or refresh a self-contained chapter request.
   - If the chapter proposes a major reform, war, technology, economy, logistics, geography, or social-order change, mark `logic_audit_required: yes` and create a logic audit request.
5. Run a logic audit committee review for high-impact historical changes, or record explicit user override.
6. Run configured side-mining/red-team steps; store outputs in scratch/process directories, not canon directories.
7. Use the final canon role for final prose decisions.
8. Write configured draft path, e.g. `drafts/chNNN.md`.
9. Write configured support files:
   - summary;
   - self-audit;
   - ledger/update suggestions;
   - logic audit report or override record if required;
   - final-review evidence if used.
10. Create readable/de-AI candidate if part of the project standard.
11. Run local character/word count and verification.
    - If timeline files changed or constrain the chapter, run `python3 scripts/timeline_lint.py --project-root . --config novel-architect.config.json --write-report`.
    - If lore cards or metadata tags changed, run `python3 scripts/lore_index.py --project-root . --config novel-architect.config.json --write-report`.
12. Update state/work queue.
13. Commit or record version status.
14. If configured, sync the checkpoint to the private GitHub remote.
15. Report logic audit status, completion evidence, and stop.

## 5. Readability / de-AI workflow

Use this for publishable/readable candidates or style-humanization passes.

1. Confirm source draft exists.
2. Preserve canon facts, order of events, strong lines, object states, and character voice.
3. Run side diagnosis/mining if configured.
4. Use side outputs as suggestions only.
5. Let the final canon role approve the final readable text.
6. Save the readable output to the configured path.
7. Verify no canon drift and record quality state:
   - `PASS_UNCHANGED`
   - `PASS_REVISED`
   - `FAIL_NEEDS_REVISION`

## 6. Range audit workflow

A range audit must judge the completed range and lock the next stage.

Check:

- continuity;
- pacing and chapter-level consequence;
- character/name consistency;
- economics/logistics/institutional plausibility where relevant;
- antagonist/external learning;
- unresolved hooks;
- repeated beats or prose fatigue;
- next-stage risks.

Audit output must include:

- verdict;
- warnings/blockers;
- repair list;
- next chapter start point;
- next 3–5 chapter pressure;
- next stage consequence;
- hard rules for upcoming request packages.

Do not begin the next chapter after an audit unless explicitly instructed.

## 7. Asset packaging and migration

Use the public scripts:

```bash
python3 scripts/verify_portable_assets.py --project-root /path/to/project --config /path/to/project/novel-architect.config.json
python3 scripts/package_portable_assets.py --project-root /path/to/project --config /path/to/project/novel-architect.config.json --output-dir /tmp/portable-novel
```

Default packaging excludes secrets, scratch logs, inbox/outbox, archives, and large compressed files.

## 8. Private GitHub sync

If the project uses private GitHub sync, read `references/github-sync.md` before pushing.

Use:

```bash
python3 scripts/github_private_sync.py --repo-root /path/to/project --config /path/to/project/github-sync.config.json --dry-run
python3 scripts/github_private_sync.py --repo-root /path/to/project --config /path/to/project/github-sync.config.json --auto-commit
```

Never store GitHub tokens or credentials in project files. Authentication belongs to the local git client, SSH agent, Git Credential Manager, or the hosting environment.

## 9. Completion report template

```text
Chapter N "Title" is complete.
Readable/de-AI status: ____.
Count: ____.
Continuity: ____.
Files written: ____.
Verification: ____.
Logic audit required/status: ____.
Version control: ____.
GitHub private sync: ____.
Current stop point: before Chapter N+1. Waiting for instruction.
```

## 10. References

Read the most specific reference:

```text
references/project-map.md
references/chapter-workflow.md
references/timeline-workflow.md
references/lore-metadata-workflow.md
references/context-layer-workflow.md
references/deai-workflow.md
references/audit-workflow.md
references/logic-audit-committee.md
references/branch-simulation-workflow.md
references/model-routing.md
references/closeout-checklist.md
references/asset-package.md
references/portability-guide.md
references/github-sync.md
```
