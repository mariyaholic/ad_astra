# Tier runs: contracts, one command per environment, verified handbacks

Updated 2026-10-25. Read `AGENTS.md` and `docs/STATUS.md` first. This page is the operator's
guide; the contracts are enforced in `src/cygnus/handback.py` (`CONTRACTS`) and by
`tests/test_handback.py`, `tests/test_tier_cycle.py` and `tests/test_cloud_workflow.py`.
Print the live contracts with `python -m cygnus.tier contracts`.

## Run a tier: one command per environment

| Environment | Command | What still needs a person |
| --- | --- | --- |
| Local workstation | `python -m cygnus.tier cycle cloud/workflow.yaml --env local` | Scientific review of the result. |
| Cloud agent (Claude Code cloud, Codex cloud) | `python3.12 tools/setup_cloud.py && .venv/bin/python -m cygnus.tier cycle cloud/workflow.yaml --env cloud-agent` | Pulling the agent's branch/diff locally; review. |
| Google Colab | Open `notebooks/cygnus_higher_tiers_colab.ipynb` on a CPU runtime, **Run all**; then locally `python -m cygnus.tier colab ingest --latest` | Pressing Run all and approving the `drive.mount()` consent; review. |

`cycle` runs `preflight → plan → run → report → pack → deliver (ingest) → cleanup`. Each step is
journaled in ignored `state/tier_cycles/<name>/` (`CYCLE.json`, `JOURNAL.jsonl`, `PREFLIGHT.json`).
**Rerun the same command to resume:** it reuses the recorded `PLAN.json`, and stages whose
checkpoints verify are skipped. The cycle name defaults to the recipe name plus a digest of its
bytes; a changed recipe under the same name is refused (use `--name`). One writer per cycle and
per plan (lock files).

Exit codes: `0` handback verified and delivered (targets may still be honestly incomplete or
blocked; they are listed); `1` blocked, needs a person (failed preflight, rejected handback, no
target selected); `75` a transient failure remains, so rerun later. `python -m cygnus.tier status <name>`
shows the journal.

A short prompt is enough for any agent: *"Read docs/TIERS.md and run the tier cycle for
cloud/workflow.yaml in this environment; report the handback, counts and incomplete targets."*

## Tier contracts

Earned tier is **derived** from the sky record by `campaign.tiers.decide`. `run_at` is the highest
executed stage. A tier is a permission to use tools, never an evidence level.

| Stage | Inputs | Required outputs (stage directory) | Gate in | Gate out | May earn | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `screen` (T0/T1) | exact refreshed TOI/TIC row (query + tz-aware time); SPOC products by ID or acquisition-verified | `sky_record.json`, `REPORT.md`, `SEARCH_LOG.md`, `SPEC.yaml`, `STAGE.json`, `SOURCE_ROW.json`, `runner/RUN_SUMMARY.json` | selected in a verified plan; source row within `source_max_age_hours` | completed record re-derives to T2; covered positive control not failed | T0–T3, closed | null or Unverified lead |
| `T2` | verified screen checkpoint that earned T2, not escalated or closed; pinned products; saved aliases | above + `SOURCE_SPEC.yaml`, `SOURCE_RECORD.json`, `period_aliases.json`, `vetting/vetting.json`, `event_null.json`, `runner/fetch_products.json`, `FOLLOWUP_PRODUCTS.json` | upstream earned ≥ T2; no failed artifact interlock | passed localization on every defining event, passed blend census, calibrated and event-epoch nulls, plus recipe budget and question | T2, T3, closed | unchanged from `SOURCE_RECORD.json` |
| `T3` | verified T2 checkpoint that earned T3; checksummed input packets with quality receipts | above + `diagnostics.json`, `INPUTS.json` | earned T3; budget + discriminating question | none automated | T2, T3, closed | unchanged |
| `colab_T2` | manifest-verified first-stage export; re-derived T2 eligibility | `sky_record.json`, `REPORT.md`, `SEARCH_LOG.md`, `SOURCE_SPEC.yaml`, `FOLLOWUP_SPEC.yaml`, `SOURCE_RECORD.json`, `SOURCE_LINK.json`, `period_aliases.json`, `vetting/vetting.json`, `event_null.json`, `runner/fetch_products.json` | first-stage audit re-derives T2; frozen targets excluded | same as T2 | T2, T3, closed | unchanged |

T4, independent-sky confirmation, evidence promotion, publication and submission are never
automated. Missing inputs stay `not_tested`; a T3 stage without usable packets does not complete.

## Handback format and verification

A handback is a directory named by its id:

- **Cloud capsule** (`cygnus.cloud_capsule/1`): `docs/handbacks/<plan-id>/`, written by
  `cygnus.cloud` and packed by the cycle (`HANDBACK.json`). Capsules live outside `reports/` and
  `campaigns/` because every stage keeps a sky record with the target's id; nesting them under
  `reports/` would publish duplicate ids (the defect this layout fixes).
- **Colab T2 export** (`cygnus.higher_tier_export/1`): `Cygnus/colab_runs/t2-…/` as the notebook
  writes it; `HANDBACK.json` is computed locally on ingest.

`python -m cygnus.tier verify <dir>` rejects the handback (and `ingest` changes nothing in the
repository) when any of these hold:

- a file is missing from, extra to, or different from `MANIFEST.sha256`; an unsafe path or symlink;
- a FITS product, SQLite ledger or credential file (a Colab companion `ledger.sqlite` may be listed
  but is never imported); a file over 64 MiB, or 512 MiB in total;
- a private machine path (`C:\Users\…`, `/home/<user>/…`, the scratch root) or token pattern in any
  file small enough to enter git;
- plan/lineage digest mismatch; a checkpoint whose artifacts, lineage, decision or upstream receipt
  does not re-derive; a stage run without its upstream gate; `tier_board.json`, `done.json` or
  `HANDBACK.json` claims that differ from the re-derived values;
- a stage missing a contract output; a sky record that fails schema validation, has unmapped
  checks, carries evidence above Unverified lead, changes its source record's evidence, or earns a
  tier outside its contract (including T4);
- the code commit is not in local history (fetch the producing branch), or, for capsules, the
  shipped source hashes differ from that commit (run from a clean, committed checkout).

On acceptance, `ingest` imports the review set into `docs/handbacks/<id>/`. Files over 1 MiB stay
in Drive/scratch and are listed with their hashes in `reports/handback-<id>/INGEST.json`.
It also regenerates `reports/handback-<id>/{REPORT.md, SEARCH_LOG.md, sky_record.json}`, writes a
managed `docs/STATUS.md` block, and records Drive visibility in `storage/locations.jsonl`.
A resumed run may supersede an earlier handback of the same id only when it loses no completed
stage. `python -m cygnus.tier check` (run by the test suite) re-verifies every imported copy.
Nothing is copied into `campaigns/` or `publish/`. Reconciling canonical records is review work.

## Data routes, scratch and cleanup

- Drive is resolved with `python -m cygnus.storage where` (`CYGNUS_DRIVE`, a Colab mount, or the
  first rclone Drive remote with `Cygnus/`). Remote names are never hard-coded. Cloud-agent capsules
  go to `Cygnus/handbacks/<id>/` only through an rclone route (one writer kind per area,
  `storage.AREA_WRITER`); otherwise they travel in the agent's checkout/diff.
- Token visibility differs by harness: a `drive.file` token may not see folders the Colab mount
  created. A route that cannot see an export is reported as `not_visible`. Download the folder and
  run `python -m cygnus.tier colab ingest --run <id> --local <folder>`.
- Bulk inputs stay in scratch (`CYGNUS_SCRATCH`; Linux default `~/.cache/cygnus/scratch`). Cloud
  agents delete the plan's managed scratch after a verified delivery; local runs keep it
  (`--cleanup` to remove). Public inputs are re-fetchable by product ID and hash.
- Cloud-agent dependencies are pinned by `cloud/constraints-linux-py312.txt`, applied by
  `tools/setup_cloud.py` on Linux CPython 3.12 only. Regenerate it with the command in its header
  and rerun the suite; every handback records the actual package versions either way.

## Failures and retries

`handback.classify_failure` maps recorded messages to actions; tests pin each lesson below.

| Class | Seen | Action |
| --- | --- | --- |
| `storage_quota` | 2026-10-08/10 rclone shared client HTTP 403 `RATE_LIMIT_EXCEEDED` | retried with 30 s / 120 s backoff; not a verification result |
| `transient` | archive timeouts, 502–504 | bounded retry; cycle exits 75 if it persists |
| `coverage_guard` | 2026-10-10 Colab: 11 targets with no measured/covered defining event | never retried, never relaxed; reported incomplete for review |
| `not_visible` | 2026-09-26 drive.file token, exit 3 | use another route or `--local` |
| `storage_auth` | rclone shared client retirement (2026) | re-run OAuth and tell the user |
| `environment` | 2026-10-17 shared interpreter `pip check` (Gradio pins) | isolated venv; local cycles tolerate only `pip_check`, cloud agents tolerate none |
| `integrity` | altered checkpoints/manifests | stop; a person inspects |
| `budget` | scratch/time budgets | stop; not a scientific null |

## Colab specifics

`python -m cygnus.tier colab stage` uploads the reviewed notebook kit to
`Cygnus/batches/higher-tiers-<revision>/`, read-back verified with retries for quota errors.
The notebook itself discovers its source, resumes from verified checkpoints and exports to
`Cygnus/colab_runs/t2-…/`. `colab ingest --latest` picks the newest export by its
`LOCATION.json` time, fetches every manifest-listed file except the companion ledger, verifies
and ingests. `--all` ingests every visible export, and unchanged ones are skipped. The canonical
Windows task `\Cygnus-Colab-Sync` still runs only `colab_sync`. Adding ingest to it is a user
decision (`docs/STATUS.md`).

Starting a Colab runtime cannot be automated from the repository: the Drive mount needs the
owner's interactive consent. A browser-driving agent can press Run all with the user's approval,
as on 2026-10-10.
