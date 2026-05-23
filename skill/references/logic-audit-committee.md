# Historical Logic Audit Committee

Use this workflow when a chapter, outline node, or alternate-history proposal changes institutions, warfare, economy, logistics, technology, geography, social order, or real-history outcomes.

This is a Markdown-first review workflow. Do not integrate AutoGen or any provider-specific runtime by default.

## Trigger conditions

Run a logic audit, or record an explicit user override, before canonizing any of these changes:

- a reform to law, taxes, bureaucracy, military command, land, prices, currency, or labor;
- a battle, campaign, siege, training program, weapons change, or supply decision;
- a technology introduction or accelerated invention;
- a major travel, transport, geography, food, disease, weather, or logistics claim;
- a social reaction involving commoners, gentry, officials, soldiers, merchants, clans, or religious groups;
- an alternate-history divergence that affects later chapters or real-history events.

## Review roles

| Role | Review focus |
|---|---|
| `historian_reviewer` | Real-history conflict, chronology, source tension, anachronism. |
| `institution_reviewer` | Bureaucracy, law, official procedure, court/local governance. |
| `logistics_reviewer` | Food, transport, roads, rivers, animals, military supply, travel time. |
| `economics_reviewer` | Fiscal logic, tax, prices, labor, incentives, winners and losers. |
| `military_reviewer` | Warfare, training, weapons, terrain, timing, command friction. |
| `commoner_reviewer` | Common people reaction, rumor, livelihood pressure, compliance cost. |
| `gentry_reviewer` | Landlords, gentry, local elites, clans, scholars, patronage networks. |
| `final_canon` | Decides what enters canon and which repairs are mandatory. |

One model may perform multiple roles, but the output must preserve separate role sections.

## Workflow

1. Create a `Logic Audit Request` using `skill/templates/logic-audit-request-template.md`.
2. Load relevant timelines, lore cards, source notes, standards, context packs, chapter drafts, ledgers, and outline nodes.
3. Each requested side-review role writes objections, hidden costs, likely resistance, second-order consequences, and repairs.
4. Write the report to `audits/`, for example `audits/ch001-logic-audit.md` or `audits/logic-reform-tax-system.md`.
5. The `final_canon` role records one of:
   - `ACCEPT_AS_CANON`
   - `ACCEPT_WITH_REPAIRS`
   - `REJECT`
   - `NEEDS_USER_DECISION`
6. Adopted decisions update `ledgers/`, `WORK_QUEUE.md`, and relevant canon/lore/timeline files.
7. Stop after reporting the decision. Do not draft the next chapter automatically.

## Required report checks

- real-history compatibility;
- institutional procedure;
- logistics and travel/supply constraints;
- economic incentives and fiscal side effects;
- military feasibility;
- commoner reaction;
- gentry/local elite reaction;
- second-order and third-order consequences;
- canon decision and required repairs.

## Override rule

If the user explicitly chooses to skip a logic audit, record:

```text
logic_audit_required: yes
logic_audit_status: USER_OVERRIDE
override_reason: ...
```

The override must appear in the chapter request, completion report, or relevant audit file.
