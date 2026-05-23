# GitHub Release Checklist

Before publishing this repository or a generated asset package:

## Repository template

- [ ] No real API keys.
- [ ] No `.env` or `.secrets/`.
- [ ] No personal home paths.
- [ ] No private provider account IDs.
- [ ] No private novel text unless intentionally included.
- [ ] Scripts run with `--help`.
- [ ] README explains installation and limitations.
- [ ] LICENSE present.
- [ ] SECURITY.md present.
- [ ] GPL or license-restricted projects are concept-only; no restricted code copied into this MIT repository.
- [ ] Historical data adapters remain lightweight and optional; no provider-specific or GUI dependency added by accident.

## Generated asset package

- [ ] Manifest inspected.
- [ ] Required files only, plus intentional recommended files.
- [ ] `scratch/` excluded unless sanitized intentionally.
- [ ] `archive/` excluded unless sanitized intentionally.
- [ ] `.git/` excluded.
- [ ] `.secrets/` excluded.
- [ ] `external-data/` excluded unless intentionally private and license-reviewed.
- [ ] SQLite / local database files excluded by default: `*.db`, `*.sqlite`, `*.sqlite3`.
- [ ] CBDB or other third-party historical databases not bundled in public packages.
- [ ] Local CSV / JSON research data reviewed before sharing.
- [ ] Generated Org outline exports under `exports/org/` inspected if included.
- [ ] Secret scan passed.
- [ ] Destination verification passed.
