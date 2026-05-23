# Maps / 地理与后勤

This directory tracks places, routes, and movement constraints for historical-mode projects.

本目录记录地点、路线、行军、运输、后勤和地理约束。

## Files

- `places.md` — place cards with historical names and optional coordinates.
- `routes.md` — route cards with distance, terrain, travel days, and supply notes.
- `geo-events.json` — optional machine-readable movement/event notes.

## Check

```bash
python3 scripts/geo_lint.py --project-root . --config novel-architect.config.json --write-report
```
