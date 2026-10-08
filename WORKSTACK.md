# Workstack

## Reusable higher-tier Colab notebook — 2026-10-08

- Built `notebooks/cygnus_higher_tiers_colab.ipynb` from reviewable source cells and a deterministic builder. It consumes first-stage exports, derives earned T2 targets and uses source/revision-bound resume state; no manual per-batch target list.
- Existing native vetting and event-null/injection adapters are reused with exact first-stage product/event selection. T3/T4 and evidence promotion are not executed, and the frozen specialist leads stay excluded.
- Corrected notebook suite: 35 passed, one native empty-legend plotting warning. Parent guard/sync checks: 60 passed, the already-exercised integration deliberately deselected. Ruff, diff checks, all six shipped-cell compilations and helper/source equality passed. Cached manifest-verified p02-b02 source selection: 30 eligible, 70 excluded, all 100 requested rows accounted, 99 checkpointed. This is not a live T2 science run.
- Independent review found four integrity/completion defects that initial passing fixtures did not cover: missing digest pinning, no-fit completion, corrupted checkpoint export, and mutable done-tier assertions. Red/green regressions and corrections address all four plus stale closure receipts; focused independent re-review passed with no remaining findings in that scope. Corrected revision `t2-v1-c3f37cbbb62b`, notebook SHA-256 `04e2009fd47b3e6741017817224df4030eac886d33bc3c252c2a0dd453b38d5a`.
- Full-project offline gate exceeded the 180-second local budget; broader native/setup gate exceeded 90 seconds. Neither was passed. Colab mount/install and live archives remain user-run. The build/staging phase performed no commit, remote compute, publication, companion-ledger merge or new scheduler; commit/push were subsequently authorized by the user.
- Delivery: the reviewed local notebook is provided directly. Drive listed the staged kit under `Cygnus/batches/higher-tiers-t2-v1-c3f37cbbb62b/`, but remote-byte verification and LOCATION registration were blocked by shared-client HTTP 403 `RATE_LIMIT_EXCEEDED`, including a bounded retry. The cloud copy is not checksum certified; the storage index records partial staging. No authorization change or cloud compute was attempted.
- Operation and maintenance: [docs/HIGHER_TIERS_COLAB.md](docs/HIGHER_TIERS_COLAB.md). Use the existing `\\Cygnus-Colab-Sync` task for eventual exports.

## Shared sky appearance and target groups — 2026-10-03

- Implemented shared dark sky palette, gold coordinate mark/navigation, serif headings and console surfaces across the generated public pages. Optional light reading theme remains available.
- Default map: 19/1294 positioned targets, comprising 3 active published Unverified leads and 16 known objects/reference fields. Separate toggles retain T2 30, T1 1, T0 68, earlier tests/nulls 273 and untiered pool 903.
- Active lead membership follows public candidate manifests; audited tiers follow the newest dated source export per target, including demotions. Missing/incomplete rows stay untiered. No evidence level or measurement changed.
- Filters affect markers, picking, footprints, map image/source retrieval, rail and tour. Full-catalogue search/links can temporarily reveal a selected hidden target; closing restores the filtered view. Overlapping marker labels are suppressed.
- Verified locally: full suite 697 passed, 37 deselected, existing All-NaN warning. Targeted publication/grouping suite 59 passed; changed Python Ruff and JavaScript syntax checks pass. Publication dry build: 574 pages/581 files.
- Browser checks: desktop 1440px and phone 375px; T2 adds 30 to the default 19; Show all returns 1294; reset returns 19; empty selection is explicit; Enter finds hidden TOI-4280.01 and displays earned T1/run_at T0, then close restores 19. Reading theme toggle works; campaign/status phone pages have no horizontal page overflow. No console errors observed during those interactions.
- Publishing uses the existing site-branch workflow. Palette source is `src/cygnus/publish/static/sky-theme.css`; explorer copy is generated and ignored. Rebuild both site and explorer before the whole-bundle leak scan; do not create another publisher or scheduler.
- Final link audit caught collection item IDs differing from canonical dossier IDs. A failing regression now verifies the map uses `CandidateRecord.candidate_id`; rebuild and deploy the corrected explorer data with the same workflow.
- Publication refresh: document tables now use fixed, wrapping wide layouts and labelled card rows below 760px, so the p02 tier-mark table keeps its rightmost column readable. The methods page now offers a compact view and a full suite-definition view with an accessible no-JavaScript fallback.
- Updated the public candidate and historical batch wording to the current three-lead interpretation and linked `cygnus.multi`, tier gates and the full methods definitions from the methods, candidate and batch pages. The bounded `src/cygnus/analysis` project document now states its relationship to the production runner.
- Verification for this refresh: targeted publication tests 3/3 passed; full gate 700 passed, 0 failed, 0 skipped; publication check and build completed at 574 pages / 581 public files. Deployment remains pending until the site bundle is pushed and the live pages are rechecked.

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
