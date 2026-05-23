# Butterfly-Effect Branch Simulation

Use this workflow when a proposal creates an alternate-history divergence, major plot branch, or experimental timeline path that might later be accepted, merged, or rejected.

This is a Markdown-first workflow. Do not require a GUI or provider-specific runtime.

## When to branch

Create or document a branch when a chapter or outline node:

- changes a major historical event;
- changes who controls a city, army, institution, or route;
- changes a reform, battle, supply chain, or technology path;
- creates a long-lived alternate-history consequence;
- needs side simulations before final canon review.

## Required branch files

Each branch directory should contain:

```text
BRANCH_STATE.md
divergence-point.md
simulated-outline.md
consequences.md
logic-audit.md
merge-decision.md
```

## Suggested branch flow

1. Write `divergence-point.md`.
2. Run a logic audit if the branch changes institutions, war, economy, logistics, geography, or social order.
3. Draft `simulated-outline.md` for the next 3 chapters, next 10 chapters, and next 1 year.
4. Write `consequences.md` for affected factions, locations, canon locks, and invalidated assumptions.
5. Record `logic-audit.md` if the branch needs or received logic audit committee review.
6. Write `merge-decision.md` with one of:
   - `KEEP_AS_BRANCH`
   - `MERGE_INTO_CANON`
   - `REJECT`
   - `NEEDS_USER_DECISION`
7. Update `WORK_QUEUE.md`, `PROJECT_STATE.md`, and relevant timelines or ledgers if the branch is accepted.

## Branch rules

- Branch work is not canon by default.
- Every branch needs a divergence point.
- Every branch needs a consequence file.
- Every branch needs a merge decision.
- Accepted branch consequences must update timelines, outlines, ledgers, project state, and work queue.

## Review questions

- What historical assumption changed?
- Which factions benefit or lose?
- What logistics, money, or law constraints changed?
- What chapters become invalid or need rewrites?
- Is the branch still useful after 3 chapters, 10 chapters, and 1 year of fallout?

## Stop rule

After recording the branch state and decision, stop and wait for instruction. Do not auto-merge or auto-continue.
