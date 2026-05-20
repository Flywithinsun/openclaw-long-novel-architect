# Model Routing

This public template does not contain private provider names. Configure roles in your project.

## Required roles

- `organizer`: lightweight chat/context work.
- `final_canon`: final prose, continuity, readable/de-AI approval.
- `side_miner_primary`: primary alternate view/red-team.
- `side_miner_texture`: human texture, voice, body/action details.
- `side_miner_structure`: structure, long-context continuity, loopholes.
- `engineering_helper`: scripts, validation, packaging.

## Example role mapping

```text
organizer = <your-fast-general-model>
final_canon = <your-best-writing-and-reasoning-model>
side_miner_primary = <your-red-team-or-alternative-style-model>
side_miner_texture = <your-human-texture-model>
side_miner_structure = <your-long-context-review-model>
engineering_helper = <your-coding-model>
```

## Invariants

- Side outputs are mining material, not canon.
- Final canon role cannot be silently downgraded.
- Fallbacks must be recorded with limitations.
- Model credentials must never be written into routing docs.
