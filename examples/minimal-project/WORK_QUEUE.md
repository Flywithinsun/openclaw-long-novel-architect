# WORK_QUEUE

## Active task

- Status: ready
- Target chapter / range: Chapter 1
- Task type: request-only
- Required output files: `writing-requests/ch001-request.md`

## Next tasks

1. Create a self-contained Chapter 1 request package.
2. Draft `drafts/ch001.md` after the request is approved.
3. Write `summaries/ch001-summary.md` and update project state.
4. If historical mode is used, run timeline, lore, geo/logistics, and asset validation before reporting completion.
5. Use standards and context packs when preparing chapter requests.
6. If the chapter changes institutions, war, economy, logistics, geography, or social order, prepare a logic audit request first.
7. If the chapter creates a durable alternate-history divergence, create or update a branch simulation under `branches/`.
8. If local historical data is used, query through `scripts/historical_data_query.py` and treat generated lore as non-canon until `final_canon` review.
9. If a large-project navigation outline is needed, run `scripts/export_org_outline.py` and inspect `exports/org/project-outline.org`.

## Blockers

- Fill in project-specific canon, outline, and character details.
- Replace example timeline/lore/source placeholders with project-owned research.
- Decide whether the first chapter needs a logic audit committee review.
- Decide whether any proposed divergence needs a branch simulation.
- Decide whether project snapshots or manuscript exports are needed at this stop point.
- Decide whether any local historical dataset is available, enabled, and license-reviewed before use.
- Decide whether an optional Org outline export is needed for handoff or navigation.

## Stop rule

After completing the active task, update `PROJECT_STATE.md`, record files changed, report the stop point, and wait for instruction.
