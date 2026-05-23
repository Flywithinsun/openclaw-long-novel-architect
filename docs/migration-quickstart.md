# Migration Quickstart

## 1. Prepare source project

Copy the example config:

```bash
cp examples/project-config.example.json /path/to/project/novel-architect.config.json
```

Edit paths and model role names.

If you use historical mode, confirm the recommended directories are either present or intentionally omitted:

```text
timelines/
maps/
lore/
standards/
context-packs/
branches/
reports/
exports/
```

Keep local historical datasets in `external-data/` or another private location. Public packages should not include CBDB, third-party databases, or unreviewed local CSV / JSON research data.

## 2. Verify source project

```bash
python3 scripts/verify_portable_assets.py --project-root /path/to/project --config /path/to/project/novel-architect.config.json
```

Fix missing required paths before continuing.

## 3. Create sanitized package

```bash
python3 scripts/package_portable_assets.py --project-root /path/to/project --config /path/to/project/novel-architect.config.json --output-dir /tmp/portable-novel
```

Inspect the generated manifest.

Confirm that `external-data/`, `*.db`, `*.sqlite`, `*.sqlite3`, and any local historical research dumps are absent unless you are making a private, license-reviewed package.

## 4. Secret scan

At minimum:

```bash
grep -RInE "(sk-|api[_-]?key|token|secret|credential|Authorization|Bearer|password|\.secrets|\.env)" /tmp/portable-novel
```

Prefer a dedicated scanner before publishing.

## 5. Unpack in destination OpenClaw

```bash
mkdir -p /path/to/new/project
cd /path/to/new/project
unzip /path/to/package.zip
python3 scripts/verify_portable_assets.py --project-root . --config novel-architect.config.json
```

## 6. Before writing

Confirm:

- current completed chapter;
- current stop point;
- next hard locks;
- model role mapping;
- whether timeline / lore / map / branch reports need to be refreshed;
- completion checklist.
