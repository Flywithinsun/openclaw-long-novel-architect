# OpenClaw Long Novel Architect

A portable OpenClaw Skill template for managing long-form fiction projects with structured context, chapter production, revision, audit, de-AI/readability polishing, export, and handoff workflows.

This repository is designed to be safe for public GitHub release. It contains **no private novel text, no API keys, no provider credentials, no personal paths, and no model account identifiers**.

## What this is

`openclaw-long-novel-architect` is a reusable workflow kit for long novels, especially complex historical / political / military / continuity-heavy projects.

It helps an OpenClaw agent:

- find the current project state;
- avoid relying on hidden chat memory;
- generate self-contained chapter requests;
- separate mainline canon decisions from side-model mining;
- produce drafts, summaries, audits, ledgers, and readable candidates;
- run range audits and lock the next stage;
- package a sanitized asset bundle for another OpenClaw;
- verify whether a migrated project has enough assets to continue safely.

## What this is not

- Not a complete novel.
- Not a model provider integration.
- Not a key manager.
- Not a guarantee that any specific model route exists in your environment.
- Not a replacement for your project's canon files, outlines, drafts, or state files.

## Directory layout

```text
openclaw-long-novel-architect/
├── README.md
├── LICENSE
├── SECURITY.md
├── .gitignore
├── skill/
│   ├── SKILL.md
│   ├── references/
│   │   ├── project-map.md
│   │   ├── chapter-workflow.md
│   │   ├── deai-workflow.md
│   │   ├── audit-workflow.md
│   │   ├── model-routing.md
│   │   ├── closeout-checklist.md
│   │   ├── asset-package.md
│   │   └── portability-guide.md
│   └── templates/
│       ├── chapter-request-template.md
│       ├── deai-request-template.md
│       ├── audit-report-template.md
│       └── completion-report-template.md
├── scripts/
│   ├── package_portable_assets.py
│   └── verify_portable_assets.py
├── examples/
│   ├── project-config.example.json
│   ├── model-routing.example.md
│   └── asset-manifest.example.txt
└── docs/
    ├── github-release-checklist.md
    └── migration-quickstart.md
```

## Quick start

1. Copy `skill/` into your OpenClaw workspace, or install it according to your OpenClaw Skill mechanism.
2. Copy `examples/project-config.example.json` to your project root as `novel-architect.config.json`.
3. Edit the config for your project title, root paths, file names, and model role mapping.
4. Verify your project assets:

```bash
python3 scripts/verify_portable_assets.py --project-root /path/to/your/project --config /path/to/your/project/novel-architect.config.json
```

5. Package a sanitized handoff bundle:

```bash
python3 scripts/package_portable_assets.py --project-root /path/to/your/project --config /path/to/your/project/novel-architect.config.json --output-dir /tmp/portable-novel
```

## Public safety design

The default scripts exclude:

- `.git/`
- `.env`, `.secrets/`, credential files
- raw model logs and scratch directories
- inbox/outbox transfer leftovers
- archives and large backup files
- common binary/compressed/cache artifacts

You should still run your own secret scanner before publishing any generated package.

## Core workflow philosophy

1. **Skill controls method; project assets control facts.**
2. **Every chapter request must be self-contained.**
3. **Side-model outputs are mining material, not canon.**
4. **A final canon role/model must make prose and continuity decisions.**
5. **Completion requires files, checks, and a stop point.**
6. **A completed chapter does not authorize starting the next chapter.**
7. **Audits must lock the next stage, not merely judge the past.**

## License

MIT. See `LICENSE`.
