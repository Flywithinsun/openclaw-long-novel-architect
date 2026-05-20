# Asset Package

The asset package lets another OpenClaw continue the project without hidden memory.

## Required categories

- project state;
- work queue;
- file index;
- workflow docs;
- model role mapping without credentials;
- canon bible / outlines;
- characters;
- drafts;
- readable chapters;
- summaries;
- audits;
- ledgers;
- this Skill.

## Excluded by default

- `.git/`;
- `.env`, `.secrets/`, credentials;
- scratch/raw model logs;
- inbox/outbox;
- archive;
- backup zips and compressed files;
- caches and generated binaries.

Use `scripts/package_portable_assets.py` and inspect the manifest before sharing.
