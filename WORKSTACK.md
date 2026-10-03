# Workstack

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
- Fresh offline gate: 693 passed / 37 deselected, one existing all-NaN-centroid warning; Ruff and diff checks passed. Explorer rebuilt (1,294 targets); publication dry build passed (574 pages / 581 public files). Historical status stays in Git and is excluded from the public operations collection.
- Git and website updates use the existing `main` and `site` routes. The live `SITE_BUILD.json` identifies the deployed source commit; GitHub Actions records the deployment outcome. No extra publishing scheduler is created.

## Verification commands

Run `python -m pytest -q` for the offline gate. Use `python -m cygnus.colab_sync --run <run> --update-notes` for fresh saved output audits; source integrity failure must leave notes unchanged.
