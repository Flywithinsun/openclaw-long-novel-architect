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
9. If the chapter proposes a major reform, war, technology, economy, logistics, geography, or social-order change, prepare a logic audit request before canon prose.

## Production path

1. Create a self-contained request.
   - Include relevant timeline event ids and any expected alternate-history divergence.
   - Include required lore ids, source ids, and unresolved lore questions.
   - Include period-language constraints and forbidden modernisms.
   - Flag whether `logic_audit_required` is yes/no and why.
2. Run a logic audit committee review for high-impact historical changes, or record explicit user override.
3. Run configured side-mining/red-team.
4. Let final canon role select/compose final prose.
5. Write draft.
6. Write summary, self-audit, ledger/update suggestions.
   - If the chapter changes historical facts or consequences, update timeline files or write `ledgers/chNNN-timeline-updates.md`.
   - If the chapter adds or changes research facts, update lore cards or write proposed lore updates.
   - If a logic audit adopted or rejected changes, update ledgers/work queue and relevant canon/lore/timeline files.
7. Produce readable/de-AI candidate when required.
8. Verify count and continuity.
   - When timeline files are present, run `scripts/timeline_lint.py`.
   - When lore cards or metadata tags are present, run `scripts/lore_index.py`.
9. Update state/work queue.
10. Commit or record version status.
11. Report logic audit status and stop.

## Forbidden

- Starting next chapter without explicit instruction.
- Treating side output as canon.
- Reporting completion without files and checks.
- Using stale archive notes as current progress.
- Creating an alternate-history divergence without chapter linkage, consequence notes, and final canon review.
- Canonizing a major historical change without a logic audit or explicit user override.
