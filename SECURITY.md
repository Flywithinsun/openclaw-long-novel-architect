# Security Policy

This repository is intended to be safe for public release, but generated asset packages may contain private project data if you configure them to include it.

## Never commit

- API keys or provider tokens;
- `.env` or `.secrets/` directories;
- OAuth/rclone/Drive credentials;
- raw model logs containing private prompts;
- private novel drafts unless you intentionally publish them;
- personal paths, account names, email addresses, phone numbers, or billing metadata.

## Before publishing

Run at least:

```bash
grep -RInE "(sk-|api[_-]?key|token|secret|credential|Authorization|Bearer|password|\.secrets|\.env)" .
python3 scripts/verify_portable_assets.py --project-root /path/to/project --config /path/to/project/novel-architect.config.json
```

Also consider a dedicated secret scanner such as `gitleaks` or `trufflehog`.

## Reporting issues

If you discover that a sample file includes private data, remove it from history and rotate the affected credentials immediately.
