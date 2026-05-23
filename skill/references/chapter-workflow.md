# Chapter Workflow

Use only when the user clearly asks to start/write/generate a chapter.

## Preflight

1. Confirm target chapter.
2. Read state/work queue/index/routing files.
3. Check latest draft/readable directories.
4. Check recent git if available.
5. Load relevant outline, summary, audit, ledger, and continuity locks.
6. If historical mode is enabled, load relevant timeline files: `timelines/real-history.md`, `timelines/alt-history.md`, and optional character/military/policy tracks.
7. If lore tracking is enabled, load `lore/index.md` and relevant lore cards / source notes.
8. If standards or context packs exist, load relevant `standards/` files and a chapter context pack.

## Production path

1. Create a self-contained request.
   - Include relevant timeline event ids and any expected alternate-history divergence.
   - Include required lore ids, source ids, and unresolved lore questions.
   - Include period-language constraints and forbidden modernisms.
2. Run configured side-mining/red-team.
3. Let final canon role select/compose final prose.
4. Write draft.
5. Write summary, self-audit, ledger/update suggestions.
   - If the chapter changes historical facts or consequences, update timeline files or write `ledgers/chNNN-timeline-updates.md`.
   - If the chapter adds or changes research facts, update lore cards or write proposed lore updates.
6. Produce readable/de-AI candidate when required.
7. Verify count and continuity.
   - When timeline files are present, run `scripts/timeline_lint.py`.
   - When lore cards or metadata tags are present, run `scripts/lore_index.py`.
8. Update state/work queue.
9. Commit or record version status.
10. Report and stop.

## Forbidden

- Starting next chapter without explicit instruction.
- Treating side output as canon.
- Reporting completion without files and checks.
- Using stale archive notes as current progress.
- Creating an alternate-history divergence without chapter linkage, consequence notes, and final canon review.
