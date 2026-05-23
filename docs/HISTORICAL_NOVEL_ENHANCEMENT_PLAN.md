# Historical Novel Enhancement Plan / 历史长篇增强计划

> AI handoff note: This is the canonical next-step plan for upgrading `openclaw-long-novel-architect` from a general long-novel OpenClaw workflow template into a rigorous historical / alternate-history / time-travel novel engineering system.
>
> If you are an AI assistant continuing this work in another chat, **read this file first**, then implement the phases in order. Do not skip the safety and licensing phase. Do not start coding from the middle of the plan unless the user explicitly asks.

---

## 0. Immediate next step for the next AI session

The next AI session should start with **Phase P0**.

### First command to run

```bash
git status --short --branch
```

### First files to read

```text
README.md
skill/SKILL.md
docs/HISTORICAL_NOVEL_ENHANCEMENT_PLAN.md
scripts/verify_portable_assets.py
scripts/package_portable_assets.py
examples/project-config.example.json
examples/minimal-project/novel-architect.config.json
```

### First implementation target

Create the licensing / safety boundary documents and config exclusions:

```text
docs/third-party-inspiration.md
docs/historical-mode-roadmap.md
```

Then update:

```text
README.md
examples/project-config.example.json
examples/minimal-project/novel-architect.config.json
scripts/package_portable_assets.py
scripts/verify_portable_assets.py
```

### Do not do first

Do **not** begin by integrating AutoGen, CBDB, Electron, Obsidian, Emacs, or any external AI provider. The correct first step is documenting the clean-room migration boundary and adding safe config / packaging exclusions.

---

## 1. Current project baseline

`openclaw-long-novel-architect` is currently a portable OpenClaw Skill template for long-form fiction projects. It is file-first, safety-first, and migration-oriented.

Current strengths:

1. It does not rely on hidden chat memory.
2. It uses explicit project files as truth.
3. It separates OpenClaw operating rules from project facts.
4. It includes chapter, de-AI/readability, audit, packaging, migration, and GitHub sync workflows.
5. It has a minimal project example.
6. It has verification and packaging scripts.
7. It excludes private data and credentials by default.

Core current files:

```text
skill/SKILL.md
skill/references/
skill/templates/
scripts/verify_portable_assets.py
scripts/package_portable_assets.py
scripts/github_private_sync.py
examples/minimal-project/
docs/
README.md
```

Current philosophy that must remain unchanged:

1. **Skill controls method; project assets control facts.**
2. **Every chapter request must be self-contained.**
3. **Side-model outputs are mining material, not canon.**
4. **A final canon role must make prose and continuity decisions.**
5. **Completion requires files, checks, and a stop point.**
6. **A completed chapter does not authorize starting the next chapter.**
7. **Audits must lock the next stage.**
8. **Private GitHub sync is handoff evidence, not credential management.**

---

## 2. Upgrade goal

Upgrade the project into a workflow system suitable for:

- rigorous historical novels;
- alternate-history fiction;
- time-travel / transmigration fiction;
- military and logistics-heavy fiction;
- institution-heavy fiction;
- multi-faction political fiction;
- long serial novels requiring strict continuity;
- projects that must survive handoff across multiple OpenClaw sessions or model routes.

The upgraded system should manage:

1. real-history and alternate-history timelines;
2. historical geography and travel/logistics constraints;
3. lore cards for institutions, economy, military, technology, customs, and language;
4. metadata cross-references between prose and research notes;
5. context layers for period voice and anti-AI-style controls;
6. multi-role historical logic audits;
7. branch simulations for butterfly effects;
8. optional external historical datasets such as CBDB;
9. optional Org mode outline export;
10. Git-based revision, release, and manuscript export workflows.

---

## 3. Third-party inspiration summary

The following projects were reviewed or considered as references. The implementation must be clean-room unless explicitly safe.

| # | Project | URL / likely URL | License / status | Use in this project |
|---|---|---|---|---|
| 1 | markdown-timeline | `https://github.com/recklyss/markdown-timeline` | MIT | Timeline syntax inspiration; BCE/CE support; Markdown-first event format |
| 2 | timelines / Timelines Studio | `https://github.com/sreegjl/timelines` | GPL-3.0 | Concept only: timeline + map + Markdown notes; do not copy code |
| 3 | novelWriter | `https://github.com/vkbo/novelWriter` | GPL-3.0 | Concept only: metadata and cross-reference workflows; do not copy code |
| 4 | Novel-OS / book-os | user URL `book-os/novel-os` returned 404; likely `https://github.com/forsonny/book-os` | likely MIT for `forsonny/book-os` | Context-layering inspiration |
| 5 | AutoGen | `https://github.com/microsoft/autogen` | maintenance mode; project has code license constraints | Concept only: multi-agent review committee; no provider integration |
| 6 | StoryCraftr | `https://github.com/raestrada/storycraftr` | MIT | CLI and branch/outline workflow inspiration |
| 7 | CBDB SQLite | `https://github.com/cbdb-project/cbdb_sqlite` | data terms must be checked separately | Optional external local data source; do not package database |
| 8 | ancient-chinese-data class | no single confirmed repository | unknown | Generic historical data adapter layer only |
| 9 | org-novelist | user URL 404; likely `https://github.com/sympodius/org-novelist` | GPL-3.0 | Concept only: Org logical tree export; do not copy code |
| 10 | git-scribe | `https://github.com/schacon/git-scribe` | MIT | Git writing/versioning/export workflow inspiration |

Important rule:

> Do not copy GPL project code into this MIT repository. Use clean-room Markdown schemas, Python scripts, and workflow documentation.

---

## 4. Proposed final project structure

The enhanced minimal project should eventually look like this:

```text
PROJECT_STATE.md
WORK_QUEUE.md
PROJECT_INDEX.md
novel-architect.config.json

skill/
scripts/
workflow/

drafts/
readable/
summaries/
audits/
ledgers/
outlines/
characters/
canon/
writing-requests/

standards/
  prose-style.md
  historical-dialogue.md
  forbidden-modernisms.md
  deai-style-rules.md
  chapter-rhythm.md

timelines/
  README.md
  real-history.md
  alt-history.md
  character-events.md
  military-events.md
  policy-events.md

maps/
  README.md
  places.md
  routes.md
  geo-events.json

lore/
  README.md
  index.md
  制度/
  物价/
  官制/
  军制/
  地理/
  技术/
  风俗/
  generated/

branches/
  README.md
  branch-history-A/
    BRANCH_STATE.md
    divergence-point.md
    simulated-outline.md
    consequences.md
    logic-audit.md
    merge-decision.md

context-packs/
  chapter-context-template.md
  audit-context-template.md
  deai-context-template.md

reports/
  timeline-lint-report.md
  lore-index-report.md
  historical-data-report.md
  branch-simulation-report.md

external-data/
  README.md
  .gitkeep

exports/
  manuscript.md
  org/
  release/
```

---

## 5. Config changes to add

Update these files:

```text
examples/project-config.example.json
examples/minimal-project/novel-architect.config.json
```

Add optional historical-mode fields:

```json
{
  "timeline_dir": "timelines",
  "map_dir": "maps",
  "lore_dir": "lore",
  "standards_dir": "standards",
  "context_pack_dir": "context-packs",
  "branch_dir": "branches",
  "reports_dir": "reports",
  "external_data_dir": "external-data",
  "exports_dir": "exports",
  "historical_mode": {
    "enabled": false,
    "primary_calendar": "CE",
    "allow_bce": true,
    "date_precision": ["year", "month", "day"],
    "require_source_for_real_history": true,
    "require_chapter_link_for_alt_events": true
  },
  "timeline_rules": {
    "event_id_required": true,
    "allowed_tracks": [
      "real_history",
      "alt_history",
      "character",
      "military",
      "policy",
      "economy",
      "technology",
      "local"
    ],
    "allowed_confidence": [
      "confirmed",
      "probable",
      "fictional",
      "unknown"
    ]
  },
  "metadata_tags": {
    "characters": "@char",
    "places": "@place",
    "lore": "@lore",
    "events": "@event",
    "sources": "@source",
    "chapters": "@chapter"
  },
  "historical_data_sources": []
}
```

Add to default exclude dirs:

```json
"external-data"
```

Add to default exclude patterns:

```json
"*.db",
"*.sqlite",
"*.sqlite3"
```

Reason:

- external datasets may be huge;
- historical datasets may have separate licenses;
- generated local research files should not be published by accident;
- SQLite databases should not be included in public asset packages by default.

---

## 6. Phase P0 — Licensing, safety, and scope boundary

### Goal

Establish a safe migration boundary before implementing new features.

### Reference projects

All ten reviewed projects.

### Files to add

```text
docs/third-party-inspiration.md
docs/historical-mode-roadmap.md
```

### Files to update

```text
README.md
docs/github-release-checklist.md
docs/sanitization-report.md
examples/project-config.example.json
examples/minimal-project/novel-architect.config.json
scripts/package_portable_assets.py
scripts/verify_portable_assets.py
```

### What `docs/third-party-inspiration.md` must explain

For each project:

1. What it inspires.
2. License status.
3. Whether code can be copied.
4. Whether only the concept is used.
5. Whether data may be packaged.
6. Implementation boundary.

Minimum table:

```text
Project | License | Code copying? | Data packaging? | Use
```

### What `docs/historical-mode-roadmap.md` must explain

1. Historical novel mode purpose.
2. New directory categories.
3. Implementation phases P0–P10.
4. First MVP scope.
5. Non-goals.
6. AI handoff instructions.

### Acceptance criteria

- Public safety docs explicitly mention no GPL code copying.
- Public safety docs explicitly mention no bundled CBDB or licensed third-party historical database.
- Packaging excludes `external-data/` and SQLite database patterns.
- README has a visible pointer to the historical enhancement plan.
- `verify_portable_assets.py --help` still works.
- `package_portable_assets.py --help` still works.

---

## 7. Phase P1 — Dual-axis historical timeline system

### Goal

Create a Markdown-first timeline system for real history and alternate-history events.

### Reference project

`markdown-timeline` for BCE/CE and Markdown timeline inspiration.  
`timelines` for event grouping and note-linking inspiration.

### Files to add

```text
skill/references/timeline-workflow.md
skill/templates/timeline-event-template.md
skill/templates/timeline-audit-template.md
examples/minimal-project/timelines/README.md
examples/minimal-project/timelines/real-history.md
examples/minimal-project/timelines/alt-history.md
scripts/timeline_lint.py
```

### Timeline event format

```markdown
# Timeline Event

- id: event-1644-03-19-li-zicheng-beijing
- date: 1644-03-19
- calendar: CE
- track: real_history
- title: 李自成进入北京
- place: 北京
- source: TODO
- confidence: confirmed
- related_chapters: []
- related_characters: []
- consequence: 明朝中央统治崩溃
- notes: TODO
```

Alternate-history example:

```markdown
# Timeline Event

- id: alt-1644-03-18-protagonist-action
- date: 1644-03-18
- calendar: CE
- track: alt_history
- title: 主角暗中转移某批火药
- place: 北京外城
- source: fictional
- confidence: fictional
- related_chapters: [ch012]
- related_characters: [主角]
- consequence: 改变次日城防局势
- notes: 不能与真实时间线冲突
```

### `timeline_lint.py` should check

1. Event id exists.
2. Event id is unique.
3. Date format is valid.
4. Negative years / BCE dates are accepted if enabled.
5. Track is in allowed tracks.
6. Confidence value is in allowed confidence values.
7. Real-history events have source if required.
8. Alternate-history events have chapter links if required.
9. Required fields are not empty.
10. Output report can be written to `reports/timeline-lint-report.md`.

### Workflow rule to add

Before writing a historical chapter, OpenClaw should read:

```text
timelines/real-history.md
timelines/alt-history.md
timelines/character-events.md, if present
timelines/military-events.md, if present
timelines/policy-events.md, if present
```

After completing a chapter, OpenClaw should either update timeline files or write a proposed update file:

```text
ledgers/chNNN-timeline-updates.md
```

### Acceptance criteria

- Minimal project includes timeline examples.
- Timeline lint script runs without external dependencies.
- README explains the timeline workflow.
- Chapter request template references relevant timeline events.
- Audit workflow checks timeline consistency.

---

## 8. Phase P2 — Geography, map, route, and logistics constraints

### Goal

Bind events to places and travel routes to prevent impossible movement, logistics, and geography errors.

### Reference project

`timelines` for map view and coordinate support as a product idea.

### Files to add

```text
skill/references/geo-logistics-workflow.md
skill/templates/place-card-template.md
skill/templates/route-template.md
skill/templates/logistics-check-template.md
examples/minimal-project/maps/README.md
examples/minimal-project/maps/places.md
examples/minimal-project/maps/routes.md
examples/minimal-project/maps/geo-events.json
scripts/geo_lint.py
```

### Place card format

```markdown
# 北京

- id: place-beijing
- names:
  - 北京
  - 顺天府
- modern_name: 北京市
- lat: TODO
- lon: TODO
- period: 明末
- type: capital
- notes: TODO
- sources:
  - TODO
```

### Route format

```markdown
# Route

- id: route-tongzhou-beijing
- from: 通州
- to: 北京
- distance_km: TODO
- terrain: 平原 / 河道 / 山地
- transport_modes:
  - foot
  - horse
  - cart
  - boat
- normal_travel_days: TODO
- military_travel_days: TODO
- supply_notes: TODO
```

### `geo_lint.py` should check

1. Place id uniqueness.
2. Coordinate format.
3. Route start/end places exist.
4. Travel duration sanity.
5. Movement in chapter metadata does not exceed configured limits.
6. Military and supply movements are flagged if unrealistic.
7. Report goes to `reports/geo-lint-report.md`.

### Acceptance criteria

- Example project has at least two place cards.
- Example project has at least one route.
- Chapter request template includes geography/logistics constraints.
- Audit report template includes geography/logistics checks.

---

## 9. Phase P3 — Lore metadata and cross-reference system

### Goal

Add a plain-text metadata system for research notes, historical details, characters, places, events, and source references.

### Reference project

`novelWriter` for metadata and cross-reference concepts.  
Do not copy GPL code.

### Files to add

```text
skill/references/lore-metadata-workflow.md
skill/templates/lore-card-template.md
skill/templates/source-note-template.md
examples/minimal-project/lore/README.md
examples/minimal-project/lore/index.md
examples/minimal-project/lore/制度/.gitkeep
examples/minimal-project/lore/物价/.gitkeep
examples/minimal-project/lore/官制/.gitkeep
examples/minimal-project/lore/军制/.gitkeep
examples/minimal-project/lore/地理/.gitkeep
examples/minimal-project/lore/技术/.gitkeep
examples/minimal-project/lore/风俗/.gitkeep
examples/minimal-project/lore/generated/.gitkeep
scripts/lore_index.py
```

### Lore card format

```markdown
# 明代俸禄制度

- id: lore-ming-salary-system
- category: 官制
- period: 明代
- confidence: researched
- sources:
  - TODO
- related_places:
  - TODO
- related_characters:
  - TODO
- related_chapters:
  - ch012

## Summary

TODO

## Hard rules

- TODO

## Common mistakes to avoid

- TODO

## Open questions

- TODO
```

### Metadata tags in prose and notes

```text
@char: 李自成
@place: place-beijing
@lore: lore-ming-salary-system
@event: event-1644-03-19-li-zicheng-beijing
@source: source-mingshi-xxx
@chapter: ch012
```

### `lore_index.py` should check

1. Lore ids are unique.
2. Metadata tags point to existing cards where possible.
3. Draft/readable/summary files can be scanned.
4. Broken references are reported.
5. Orphan lore cards are reported.
6. Output goes to `reports/lore-index-report.md`.

### Acceptance criteria

- Minimal project contains lore directories and at least one sample card.
- `PROJECT_INDEX.md` explains lore.
- Chapter request template includes “required lore”.
- `verify_portable_assets.py` can warn if historical mode is enabled but lore is missing.

---

## 10. Phase P4 — Context layers and period-language controls

### Goal

Prevent AI-style prose, modern translation tone, modern slang in historical dialogue, and character voice drift.

### Reference project

Novel-OS / book-os context layering.

### Files to add

```text
skill/references/context-layer-workflow.md
skill/templates/context-pack-template.md
skill/templates/style-standard-template.md
examples/minimal-project/standards/prose-style.md
examples/minimal-project/standards/historical-dialogue.md
examples/minimal-project/standards/forbidden-modernisms.md
examples/minimal-project/standards/deai-style-rules.md
examples/minimal-project/standards/chapter-rhythm.md
examples/minimal-project/context-packs/chapter-context-template.md
examples/minimal-project/context-packs/audit-context-template.md
examples/minimal-project/context-packs/deai-context-template.md
```

### Context layers

```text
Layer 1: Standards
- prose-style.md
- historical-dialogue.md
- forbidden-modernisms.md
- deai-style-rules.md
- chapter-rhythm.md

Layer 2: Novel canon
- canon/
- outlines/
- characters/
- lore/
- timelines/
- maps/

Layer 3: Manuscript state
- drafts/
- readable/
- summaries/
- audits/
- ledgers/
- PROJECT_STATE.md
- WORK_QUEUE.md
```

### Chapter context pack template

```markdown
# Chapter N Context Pack

## Must read

- PROJECT_STATE.md
- WORK_QUEUE.md
- standards/prose-style.md
- standards/historical-dialogue.md
- timelines/real-history.md
- timelines/alt-history.md
- lore/index.md

## This chapter style constraints

- 禁止现代词：
- 角色口吻：
- 叙事节奏：
- 历史术语：

## Canon locks

- TODO

## Open risks

- TODO
```

### Acceptance criteria

- `skill/SKILL.md` mandatory first reads mention configured standards/context files when present.
- `deai-workflow.md` references `standards/deai-style-rules.md`.
- Chapter workflow references context packs.
- Minimal project contains standards examples.

---

## 11. Phase P5 — Historical logic audit committee

### Goal

Add a structured multi-role logic audit workflow for reforms, wars, technology changes, social reaction, and historical plausibility.

### Reference project

AutoGen multi-agent concept only.  
Do not integrate AutoGen runtime in the first version.

### Files to add

```text
skill/references/logic-audit-committee.md
skill/templates/logic-audit-request-template.md
skill/templates/logic-audit-report-template.md
```

### Suggested audit roles

```text
historian_reviewer
- Checks real-history conflict.

institution_reviewer
- Checks bureaucracy, institutions, law, official procedure.

logistics_reviewer
- Checks food, transport, roads, military supply.

economics_reviewer
- Checks fiscal logic, tax, price, labor, incentives.

military_reviewer
- Checks warfare, training, weapons, terrain, timing.

commoner_reviewer
- Checks common people reaction.

gentry_reviewer
- Checks landlords, gentry, local elites.

final_canon
- Decides what becomes canon.
```

### Logic audit request format

```markdown
# Logic Audit Request

## Target

- Chapter / outline node:
- Proposed change:
- Historical period:
- Place:
- Involved groups:

## Proposal

TODO

## Review roles required

- historian_reviewer
- institution_reviewer
- logistics_reviewer
- economics_reviewer
- military_reviewer
- commoner_reviewer
- gentry_reviewer

## Required output

- objections
- hidden costs
- likely resistance
- second-order consequences
- required repairs
- final canon decision
```

### Workflow

1. OpenClaw drafts a proposal.
2. Side-review roles produce objections and consequences.
3. Output is written to `audits/`.
4. `final_canon` decides what is adopted.
5. Adopted decisions update `ledgers/`, `WORK_QUEUE.md`, and relevant canon/lore/timeline files.
6. A major historical change must not enter prose without audit or explicit user override.

### Acceptance criteria

- Audit workflow references logic audit for major changes.
- Chapter workflow flags high-impact events for logic audit.
- Completion report includes whether logic audit was required and whether it passed.

---

## 12. Phase P6 — Butterfly-effect branch simulation

### Goal

Allow alternate history branches and major plot divergences to be simulated, audited, accepted, rejected, or merged.

### Reference projects

StoryCraftr for CLI story/outline flow.  
git-scribe for Git-backed writing branches.

### Files to add

```text
skill/references/branch-simulation-workflow.md
skill/templates/branch-state-template.md
skill/templates/divergence-point-template.md
skill/templates/branch-merge-decision-template.md
examples/minimal-project/branches/README.md
scripts/branch_status.py
```

### Branch directory pattern

```text
branches/
  branch-history-A/
    BRANCH_STATE.md
    divergence-point.md
    simulated-outline.md
    consequences.md
    logic-audit.md
    merge-decision.md
```

### Divergence point format

```markdown
# Divergence Point

- branch_id: branch-history-A
- source_chapter: ch050
- source_event: TODO
- original_history: TODO
- changed_event: TODO
- immediate_consequence: TODO
- canon_status: experimental

## Invalidated assumptions

- TODO

## Required simulations

- next 3 chapters
- next 10 chapters
- next 1 year
- affected factions
- affected locations
```

### Branch rules

1. Branch work is not canon by default.
2. Every branch needs a divergence point.
3. Every branch needs a consequence file.
4. Every branch needs a merge decision.
5. Merging a branch requires final canon decision.
6. Accepted branch consequences must update timelines, outlines, ledgers, project state, and work queue.

### Acceptance criteria

- Branch status script lists branch states.
- Example branch README explains workflow.
- Closeout checklist includes branch impact if a chapter creates divergence.

---

## 13. Phase P7 — Historical data source adapter

### Goal

Allow local external historical datasets such as CBDB or user-provided JSON/CSV/SQLite to assist lore generation and fact checks without bundling the data.

### Reference projects

CBDB SQLite and generic ancient-Chinese-data repositories.

### Files to add

```text
skill/references/historical-data-workflow.md
skill/templates/historical-data-source-template.md
skill/templates/generated-lore-card-template.md
examples/minimal-project/external-data/README.md
scripts/historical_data_query.py
scripts/generate_lore_from_data.py
```

### Data source config pattern

```json
{
  "historical_data_sources": [
    {
      "name": "cbdb",
      "type": "sqlite",
      "path": "external-data/cbdb/latest.db",
      "enabled": false,
      "package": false,
      "license_note": "User must download and comply with CBDB terms."
    }
  ]
}
```

### Supported source types

Start with:

```text
sqlite
csv
json
markdown-table
```

Later optional:

```text
geojson
parquet
```

### `historical_data_query.py`

Example future command:

```bash
python3 scripts/historical_data_query.py \
  --project-root . \
  --config novel-architect.config.json \
  --source cbdb \
  --query-person "李自成"
```

### `generate_lore_from_data.py`

Example future command:

```bash
python3 scripts/generate_lore_from_data.py \
  --project-root . \
  --config novel-architect.config.json \
  --source cbdb \
  --person "某人"
```

Expected output:

```text
lore/generated/persons/某人.md
```

### Acceptance criteria

- No database is committed.
- No database is packaged by default.
- Missing database produces a clear warning, not a crash.
- Generated lore cards clearly mark their source and confidence.
- README explains that users must comply with dataset licenses.

---

## 14. Phase P8 — Org mode outline export

### Goal

Provide an optional export for users who want an Emacs Org mode logical tree for very large novels.

### Reference project

org-novelist concept only.  
Do not copy GPL code.

### Files to add

```text
skill/references/org-export-workflow.md
scripts/export_org_outline.py
```

### Input files

```text
PROJECT_STATE.md
WORK_QUEUE.md
outlines/
characters/
lore/
timelines/
branches/
```

### Output file

```text
exports/org/project-outline.org
```

### Example output

```org
* Project State
** Current chapter
** Current stop point

* Timeline
** 1644-03-19 李自成进京

* Characters
** 李自成

* Lore
** 明代俸禄制度

* Branches
** branch-history-A
```

### Acceptance criteria

- Script uses Python standard library only.
- Emacs is not required.
- Output is optional and goes under `exports/`.
- No GPL code is copied.

---

## 15. Phase P9 — Git writing, revision, snapshot, and export workflow

### Goal

Make long-novel writing as safe as a software project: branchable, reviewable, exportable, and recoverable.

### Reference project

git-scribe workflow concept.

### Files to add

```text
skill/references/versioning-workflow.md
skill/references/export-workflow.md
skill/templates/revision-branch-template.md
skill/templates/release-note-template.md
scripts/export_manuscript.py
scripts/project_snapshot.py
```

### Suggested Git branch names

```text
main
experiment/history-*
repair/chNNN-*
audit/range-*
release/volume-*
```

### `project_snapshot.py` should report

1. Current Git branch.
2. Recent Git commits.
3. Uncommitted files.
4. Current completed chapter from project state.
5. Latest draft chapter.
6. Latest readable chapter.
7. Latest summary.
8. Latest audit.
9. Current stop point.
10. GitHub sync config status if present.

Expected output:

```text
reports/project-snapshot-YYYYMMDD-HHMMSS.md
```

### `export_manuscript.py` should generate

From:

```text
readable/ch001.md
readable/ch002.md
...
```

To:

```text
exports/manuscript.md
exports/manuscript.txt
exports/release/volume-01.md
```

### Acceptance criteria

- Export script works with Markdown files.
- Snapshot script works even when Git is unavailable, but reports the limitation.
- Closeout checklist references snapshot/export where applicable.
- GitHub sync remains optional and does not store credentials.

---

## 16. Phase P10 — Verification, packaging, README, and example sync

### Goal

Ensure every new workflow is documented, represented in the minimal project, and safely handled by scripts.

### Files to update

```text
README.md
CHANGELOG.md
docs/openclaw-installation.md
docs/first-project-setup.md
docs/migration-quickstart.md
docs/github-release-checklist.md
docs/sanitization-report.md
examples/minimal-project/PROJECT_INDEX.md
examples/minimal-project/PROJECT_STATE.md
examples/minimal-project/WORK_QUEUE.md
examples/minimal-project/novel-architect.config.json
examples/project-config.example.json
scripts/verify_portable_assets.py
scripts/package_portable_assets.py
```

### `verify_portable_assets.py` should eventually check

1. Required paths still exist.
2. Recommended historical-mode paths exist if historical mode is enabled.
3. Skill text still contains critical invariants.
4. Latest draft/readable/summary status still works.
5. Timeline lint can be invoked or recommended.
6. Lore index can be invoked or recommended.
7. `external-data/` is not required.
8. Database files are warned about if found in package-included paths.

### `package_portable_assets.py` should eventually ensure

Default excluded dirs include:

```text
external-data
```

Default excluded patterns include:

```text
*.db
*.sqlite
*.sqlite3
```

### Acceptance criteria

- Example minimal project verifies successfully.
- New docs explain historical mode without requiring it.
- Old users are not forced to adopt historical mode.
- Public packages do not include third-party databases.
- README has a visible historical-mode section.

---

## 17. Recommended implementation order

Implement in this exact order unless the user explicitly says otherwise:

1. P0 — Licensing, safety, scope boundary.
2. P1 — Timeline workflow and `timeline_lint.py`.
3. P3 — Lore metadata and `lore_index.py`.
4. P4 — Context layers and style standards.
5. P10 partial — Verification, packaging, README sync for P1/P3/P4.
6. P5 — Logic audit committee.
7. P6 — Branch simulation.
8. P9 — Git snapshot and manuscript export.
9. P2 — Geography and logistics.
10. P7 — Historical data adapter.
11. P8 — Org mode export.
12. P10 final — Full docs, examples, verification, changelog.

Reason:

- P1/P3/P4 deliver immediate value with low risk.
- P5/P6/P9 improve long-term workflow.
- P2/P7/P8 require more data design and are better after the core schemas stabilize.

---

## 18. MVP scope

If the user wants the smallest useful implementation, build this first:

```text
docs/third-party-inspiration.md
docs/historical-mode-roadmap.md

skill/references/timeline-workflow.md
skill/templates/timeline-event-template.md
examples/minimal-project/timelines/README.md
examples/minimal-project/timelines/real-history.md
examples/minimal-project/timelines/alt-history.md
scripts/timeline_lint.py

skill/references/lore-metadata-workflow.md
skill/templates/lore-card-template.md
examples/minimal-project/lore/README.md
examples/minimal-project/lore/index.md
scripts/lore_index.py

examples/minimal-project/standards/prose-style.md
examples/minimal-project/standards/historical-dialogue.md
examples/minimal-project/standards/forbidden-modernisms.md

README.md updates
verify_portable_assets.py updates
package_portable_assets.py external-data/database exclusions
```

MVP should support:

1. Real historical timeline.
2. Alternate-history timeline.
3. Historical lore cards.
4. Metadata references.
5. Basic style and period-language standards.
6. Basic verification and safe packaging.

---

## 19. Single-feature implementation rule

For each feature, follow this sequence:

1. Add reference doc.
2. Add template.
3. Add minimal-project example.
4. Add script, if needed.
5. Update config.
6. Update verify script.
7. Update package script, if needed.
8. Update README.
9. Run verification.
10. Update changelog.
11. Commit.
12. Stop and report.

Do not write scripts first and leave docs/examples behind.

---

## 20. Completion checklist for each phase

Before reporting a phase complete:

```text
- [ ] New docs added.
- [ ] New templates added.
- [ ] Minimal example updated.
- [ ] Config updated.
- [ ] Verification script updated if needed.
- [ ] Packaging exclusions updated if needed.
- [ ] README updated.
- [ ] CHANGELOG updated.
- [ ] Local verification run.
- [ ] Git status reviewed.
- [ ] Commit created.
- [ ] Push completed if user requested GitHub upload.
- [ ] Stop point reported.
```

---

## 21. Non-goals

Do not turn this repository into:

1. a GUI writing application;
2. an Obsidian plugin;
3. an Electron timeline app;
4. an Emacs package;
5. a provider-specific AI client;
6. an API-key manager;
7. a public historical database mirror;
8. a full CBDB redistribution package;
9. a direct clone of novelWriter, timelines, StoryCraftr, AutoGen, or org-novelist.

The repository should remain:

- Markdown-first;
- OpenClaw Skill-first;
- file-based;
- portable;
- safe for public GitHub;
- model/provider neutral;
- easy to copy into a private writing project.

---

## 22. Ideal future chapter workflow after enhancement

After the enhancement is implemented, a historical chapter workflow should look like this:

1. Read `skill/SKILL.md`.
2. Read `PROJECT_STATE.md`, `WORK_QUEUE.md`, `PROJECT_INDEX.md`.
3. Read `workflow/model-routing.md`.
4. Read relevant `standards/`.
5. Read relevant `timelines/`.
6. Read relevant `maps/` if geography matters.
7. Read relevant `lore/`.
8. Generate a chapter context pack.
9. Generate or refresh the chapter request.
10. Run logic audit if the chapter changes institutions, war, economy, geography, or technology.
11. Draft chapter.
12. Produce readable/de-AI candidate if required.
13. Write summary, self-audit, and ledger suggestions.
14. Update alternate-history timeline or write proposed timeline updates.
15. Update lore references or write proposed lore updates.
16. Run timeline/lore/asset verification.
17. Update project state and work queue.
18. Commit or report version status.
19. Optionally sync private GitHub.
20. Report completion and stop.

---

## 23. Final target

The final target is to turn `openclaw-long-novel-architect` into:

> A portable, Markdown-first, OpenClaw-compatible engineering system for rigorous long historical fiction, supporting timeline discipline, historical lore, geography/logistics constraints, multi-role logic audits, branch simulation, safe historical-data adapters, and Git-based handoff.

The project must preserve its original safety contract:

- no private drafts in public template;
- no credentials;
- no provider lock-in;
- no hidden-memory dependency;
- no unreviewed side-model output entering canon;
- no automatic next-chapter continuation after completion.
