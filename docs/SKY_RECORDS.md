# Sky records

Every analysis in this worktree leaves a `sky_record.json` beside its report. The sky explorer (and later the public site) collects them automatically: a new analysis shows up on the map, on its target's panel and in the counts without any code change.

The test suite enforces this. `tests/test_skyrecord.py` fails when:

- a campaign spec `campaigns/*.yaml` exists that no record references (`spec`);
- a `REPORT.md` exists in `campaigns/<id>/` or `reports/<id>/` without a record in that directory or referencing it;
- a record breaks the schema (below), for example a check state that is not one of the four allowed, a completed run without checks, or a candidate without an evidence level.

Code: `src/cygnus/skyrecord.py` (stdlib only). Explorer build: `design-system/mockups/build_explorer.py`.

Campaigns run through the runner (`docs/CAMPAIGNS.md`) get their record regenerated automatically from the spec's `record` block; hand-written records are only for analyses outside the runner.

## Where to put it

`campaigns/<id>/sky_record.json` or `reports/<id>/sky_record.json`. A draft campaign that only has a spec gets its own directory, `campaigns/<id>/sky_record.json`, with `status: "draft"`.

## Fields (`schema: "cygnus.sky_record/1"`)

| Field | Meaning |
|---|---|
| `id` | slug, unique |
| `title`, `kind`, `summary` | human text; the summary condenses the report's bottom line and adds nothing to it |
| `status` | `draft` · `running` · `completed` · `abandoned` |
| `outcome` | `not_run` · `pipeline_check` · `bounded_null` · `lead` · `candidate` |
| `evidence` | `null`, or one AGENTS.md evidence level; required for, and only allowed with, `lead` / `candidate` |
| `date` | run date, `YYYY-MM-DD`; `null` only for drafts |
| `spec`, `report`, `search_log` | repository paths; must exist |
| `targets` | `[{name, position_source}]` where the name is in `docs/tier1_pack/NAME_RESOLUTIONS.json`, or `[{name, ra_deg, dec_deg, frame, epoch, position_source}]` for a new position. Empty only for drafts. |
| `products` | `[{id, archive, sha256?}]` exactly as in the report |
| `footprints` | optional `[{shape: "circle", ra, dec, r}]` or `[{shape: "box", ra, dec, w, h}]` in degrees, with `what` |
| `checks` | every artifact/audit test from the report with `state` `passed` · `failed` · `inconclusive` · `not_tested`. If the report used other wording, map it and keep the original in `reported_as`. Untested checks are listed, not omitted. |
| `plots` | optional; `type` `fold` or `timeseries`, the CSV `file` the analysis wrote, `time_col`, `flux_col`, `quality_col`, `time_offset_bjd`, and for folds `period_days`, `t0_bjd`, `window_hours`, `veto_phase`, `depth_window_hours`. The explorer draws plots only from these files. |

A depth computed from `depth_window_hours` is labelled in the explorer as computed at build time, not as a reported result.

## When the explorer shows it

- `completed` → the target is marked *analysed*, and the panel shows the record card, plots and checks.
- `draft` / `running` → *analysis planned*; a draft with no targets is listed under "Campaigns, no position yet".
- A target given with explicit coordinates becomes a new point on the sky. Run `python design-system/mockups/fetch_sky_data.py --missing` to fetch its Gaia field and survey image, then `python design-system/mockups/build_explorer.py`.
