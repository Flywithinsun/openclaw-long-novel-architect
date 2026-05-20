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

## Generated asset package

- [ ] Manifest inspected.
- [ ] Required files only, plus intentional recommended files.
- [ ] `scratch/` excluded unless sanitized intentionally.
- [ ] `archive/` excluded unless sanitized intentionally.
- [ ] `.git/` excluded.
- [ ] `.secrets/` excluded.
- [ ] Secret scan passed.
- [ ] Destination verification passed.
