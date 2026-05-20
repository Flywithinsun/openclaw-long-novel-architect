# Sanitization Report

This public release tree is designed to be uploaded to GitHub without private project material.

## Removed / not included

- private novel drafts;
- private project state;
- raw model prompts and logs;
- scratch directories;
- inbox/outbox transfer data;
- archive snapshots;
- `.git/` history from the source project;
- `.secrets/`, `.env`, API keys, provider credentials;
- personal home paths;
- private model/provider account identifiers.

## Intentional generic security strings

`SECURITY.md` and `docs/migration-quickstart.md` contain example grep patterns such as `api_key`, `token`, `secret`, and `Authorization` so users can scan their own projects. These are not real credentials.

## Recommended final check before GitHub upload

From the release root:

```bash
# private path/provider/project patterns should return no lines after you fill in your own terms
# Example: replace the placeholders below with strings unique to your private workspace.
grep -RInE "(<private-home-path>|<private-provider-id>|<private-project-name>)" . || true

# generic credential scanner; inspect hits manually because docs include example patterns
grep -RInE "(sk-|api[_-]?key|token|secret|credential|Authorization|Bearer|password|\.secrets|\.env)" . || true

python3 scripts/verify_portable_assets.py --help
python3 scripts/package_portable_assets.py --help
```

For stronger assurance, use a dedicated scanner such as `gitleaks` or `trufflehog` before publishing.
