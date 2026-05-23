# Geography and Logistics Workflow / 地理与后勤工作流

Use this workflow when a historical or alternate-history chapter depends on place, distance, route, travel time, terrain, supply, or military movement.

本工作流用于防止人物、军队、物资、消息和制度行动出现不可能的移动或后勤错误。

## Required files / 必备文件

```text
maps/README.md
maps/places.md
maps/routes.md
maps/geo-events.json
```

## Place card rule / 地点卡规则

Each important place should have:

- stable `id` such as `place-beijing`;
- historical and modern names;
- optional latitude/longitude;
- period and type;
- source notes when used for historical claims.

## Route rule / 路线规则

Each important route should define:

- `id`;
- `from` and `to` place ids or names;
- `distance_km`;
- terrain;
- supported transport modes;
- normal and military travel days;
- supply notes.

## Chapter preflight / 章节预检

Before writing a chapter with travel, campaign, courier movement, evacuation, logistics, or supply pressure:

1. Read `maps/places.md` and `maps/routes.md` if present.
2. Identify involved places and routes.
3. Compare claimed movement with configured route days.
4. Flag unrealistic military or supply movement for logic audit.
5. Record required repairs in the chapter request or audit.

## Verification / 校验

```bash
python3 scripts/geo_lint.py --project-root . --config novel-architect.config.json --write-report
```

The report defaults to `reports/geo-lint-report.md`.
