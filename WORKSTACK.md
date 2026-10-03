# Workstack

## Shared sky appearance and target groups — 2026-10-03

- Implemented shared dark sky palette, gold coordinate mark/navigation, serif headings and console surfaces across the generated public pages. Optional light reading theme remains available.
- Default map: 19/1294 positioned targets, comprising 3 active published Unverified leads and 16 known objects/reference fields. Separate toggles retain T2 30, T1 1, T0 68, earlier tests/nulls 273 and untiered pool 903.
- Active lead membership follows public candidate manifests; audited tiers follow the newest dated source export per target, including demotions. Missing/incomplete rows stay untiered. No evidence level or measurement changed.
- Filters affect markers, picking, footprints, map image/source retrieval, rail and tour. Full-catalogue search/links can temporarily reveal a selected hidden target; closing restores the filtered view. Overlapping marker labels are suppressed.
- Verified locally: full suite 697 passed, 37 deselected, existing All-NaN warning. Targeted publication/grouping suite 59 passed; changed Python Ruff and JavaScript syntax checks pass. Publication dry build: 574 pages/581 files.
- Browser checks: desktop 1440px and phone 375px; T2 adds 30 to the default 19; Show all returns 1294; reset returns 19; empty selection is explicit; Enter finds hidden TOI-4280.01 and displays earned T1/run_at T0, then close restores 19. Reading theme toggle works; campaign/status phone pages have no horizontal page overflow. No console errors observed during those interactions.
- Publishing uses the existing site-branch workflow. Palette source is `src/cygnus/publish/static/sky-theme.css`; explorer copy is generated and ignored. Rebuild both site and explorer before the whole-bundle leak scan; do not create another publisher or scheduler.

## Colab tier sync — 2026-10-03

- Implemented: bounded manifest-verified tier sync, separate tier marks, managed STATUS updates, refreshed notebook checkpoints.
- Audited: p02-b02-2026-10-02 — T0 68, T1 1, T2 30, missing 1; 99/100 checkpointed, all run_at T0.
- Open: TOI-3941.01 has no shipped record or checkpoint. Inspect notebook failure evidence before retrying.
- Open: TOI-4280.01 needs the moving-object check before T2. The 30 T2 targets need actual pixel vetting and review.
- Open: bulk product hashes and companion ledger are outside the tier-metadata verification scope.
- Automation owner: Windows `\Cygnus-Colab-Sync`, daily 09:00 UTC+08:00, executes `cygnus.colab_sync --all --update-notes --log state/colab_sync/latest.json`. Codex heartbeat `cygnus-colab-tier-sync` PAUSED. Reuse/update the canonical Windows task; no redundant or per-batch schedules.
- Verified scheduler migration: 693 passed / 37 deselected, one existing all-NaN-centroid warning; Ruff and diff checks passed. Windows live run completed with task result 0, no errors, two unchanged exports and three skipped probe/legacy folders. Exactly one matching Windows task exists; former Codex heartbeat is confirmed PAUSED. Rclone children use CREATE_NO_WINDOW (regression covered); physical sleep/wake remains untested.

## Repository cleanup and website refresh — 2026-10-03

- Current handoff rewritten; previous status preserved in `docs/STATUS_HISTORY_2026-10-02.md`.
- Corrected stale notebook, Drive-access and autonomy descriptions; marked the completed queue-regeneration handoff as history.
- Machine-local agent/editor/browser files and Ruff cache ignored; 19 disposable browser logs/snapshots archived outside the repo. No scientific record or failed result removed.
- Added a curated operations collection for current status and post-run tier marks, with explicit metadata-only verification limits.
- Latest remote CI exposed a shallow-history notebook-pin failure and missing campaign plotting dependency. CI now fetches full history; campaign extra includes matplotlib.
- Final offline gate after renderer repair: 694 passed / 37 deselected, one existing all-NaN-centroid warning; Ruff and diff checks passed. Explorer rebuilt (1,294 targets); publication dry build and site build passed (574 pages / 581 public files). Historical status stays in Git and is excluded from the public operations collection. Cleanup commit `af07e7a` passed GitHub Linux CI (690 passed, 3 skipped, 37 deselected); the renderer follow-up also needs its own remote gate.
- Git and website updates use the existing `main` and `site` routes. The live `SITE_BUILD.json` identifies the deployed source commit; GitHub Actions records the deployment outcome. No extra publishing scheduler is created.
- Render review exposed visible sync comment markers. Publication Markdown now omits standalone single-line HTML comments outside code fences; fenced examples and HTML escaping are preserved. The regression failed before the fix; all 56 publication tests and renderer Ruff passed afterward.

## Verification commands

Run `python -m pytest -q` for the offline gate. Use `python -m cygnus.colab_sync --run <run> --update-notes` for fresh saved output audits; source integrity failure must leave notes unchanged.
