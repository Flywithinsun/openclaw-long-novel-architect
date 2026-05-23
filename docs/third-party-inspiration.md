# Third-Party Inspiration / 第三方灵感来源

This document records the clean-room boundary for the historical-novel enhancement plan.

本文件记录历史小说增强计划的干净实现边界：只保留可公开说明的灵感，不复制受限代码，不默认打包外部数据。

## Boundary rules / 边界规则

1. Use concepts, workflows, and public-facing UX ideas as inspiration only.
2. Do not copy GPL-licensed code into this MIT repository.
3. Do not bundle third-party historical databases by default.
4. Treat user-provided research data as external data, not project-owned template content.
5. Implement all features here with clean-room Markdown schemas, Python scripts, and repository docs.

## Reviewed references / 已评估参考

| Project | License / status | What it inspires | Code copying? | Data packaging? | Implementation boundary |
|---|---|---|---|---|---|
| markdown-timeline | MIT | Markdown-first timeline entries, BCE/CE support, readable event format | No direct copy needed | No bundled data | Clean-room timeline schema and linter |
| timelines / Timelines Studio | GPL-3.0 | Timeline + map + note-linking concept | Concept only | No bundled data | Rebuild workflow ideas from scratch |
| novelWriter | GPL-3.0 | Metadata, cross-reference, and research-note workflows | Concept only | No bundled data | Plain-text metadata and index generation only |
| Novel-OS / book-os | likely MIT for the confirmed reference, otherwise concept-only | Context layering and project framing | No direct copy needed | No bundled data | Lightweight context-pack and style layer docs |
| AutoGen | maintenance-mode / code-license constrained | Multi-role review committee idea | Concept only | No bundled data | Manual multi-role audit workflow only |
| StoryCraftr | MIT | CLI-driven story/outline flow | No direct copy needed | No bundled data | Branch and outline management ideas only |
| CBDB SQLite | data terms separate from code | Historical person/entity research source | No code copying issue; data license must be checked separately | Do not package by default | Optional external-data adapter only |
| ancient-chinese-data class of projects | unknown / mixed | Historical data adapter concept | Concept only | Do not package by default | Generic adapters for user-provided local data |
| org-novelist | GPL-3.0 | Org-tree export for large outline projects | Concept only | No bundled data | Optional Org export generated from local files |
| git-scribe | MIT | Git-backed writing and export workflow | No direct copy needed | No bundled data | Versioning, snapshot, and release workflow only |

## Practical rules for this repository / 本仓库的实际规则

- Public docs may mention third-party ideas, but the implementation must remain clean-room.
- If a source is GPL, only the concept may be used; no code, structure, or text should be copied verbatim.
- If a source is a database or corpus, assume it is user-provided external data until the user confirms its terms.
- If a file or feature depends on local research assets, keep those assets outside public packaging by default.

## Summary / 小结

The enhancement plan is allowed to learn from other projects, but the repository must remain safe for public release.

增强计划可以吸收其他项目的思路，但仓库本身必须保持适合公开发布。