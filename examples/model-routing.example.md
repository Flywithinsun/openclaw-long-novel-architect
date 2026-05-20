# Model Routing Example

Do not put API keys or provider credentials here.

| Role | Route | Notes |
|---|---|---|
| organizer | `<fast-general-model>` | context packing, chat, light edits |
| final_canon | `<best-writing-review-model>` | final prose, canon gate, readable approval |
| side_miner_primary | `<red-team-model>` | alternatives, loopholes, critique |
| side_miner_texture | `<style-texture-model>` | human texture, voice, action detail |
| side_miner_structure | `<long-context-model>` | continuity and structure |
| engineering_helper | `<coding-model>` | scripts and validators |

Fallbacks must be recorded with limitations. Side outputs do not become canon without final review.
