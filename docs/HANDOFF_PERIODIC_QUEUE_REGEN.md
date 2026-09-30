# Handoff: revalidate and regenerate the `tess-periodic-01` queue (1,000 periodic TOIs)

Written 2026-09-30 for the next agent. Read `AGENTS.md`, `docs/STATUS.md`, `docs/AGENT_RUNBOOK.md` (*Claim-time catalogue and candidate gates*, *Batches*) and `docs/CAMPAIGNS.md` (*Tier gating*) first.

## Why this exists

The committed periodic queue and its 1,000 campaign specs predate the queue-period repair (2026-09-27) and are **not valid to run**:

- `campaigns/tess-periodic-01/target_queue.csv` has no `period_days` column. Every spec `campaigns/toi-*.yaml` listed in `campaigns/tess-periodic-01/batch_colab-p01.txt` has `veto: {kind: single_epoch, veto_hours: 12}` and no period.
- For a periodic candidate, a single-epoch veto leaves every other catalogued transit unvetoed. The residual screen then re-finds the known signal as "repeat events" and `period_aliases` raises false leads. This is the TOI-6695.01 failure (`campaigns/toi-6695-01/REJECTION.md`).
- Current code is correct: `targets.build_queue` writes `period_days`; `targets.refresh_queue_target` re-reads the exact TOI/TIC and carries the live period; `campaign/scaffold.spec_for` writes `veto: {kind: ephemeris, period_days, t0_bjd, veto_phase}` when a period exists.

## Verified on 2026-09-30 (live NASA Exoplanet Archive `toi` table, one TAP query, 8,148 rows)

All 1,000 queued rows: still `PC`/`APC`; TIC unchanged; live `pl_orbper` present; `rowupdate` not newer than the queue's; `pl_tranmid` within 0.05 d of the queue's `t0_bjd`; names and positions unique and in range; a spec exists for each. **The only defect is the missing period and veto.** Re-verify at claim time anyway: the queue is a dated snapshot.

Current state of the 1,000 campaigns: 900 are drafts (`status: draft`, `outcome: not_run`, spec plus placeholder `sky_record.json` only), 99 completed as `pipeline_check`, 1 completed as `lead` (TOI-224.01, see below).

## Do not touch

- **TOI-224.01, TOI-2666.01, TOI-3500.02, TOI-7610.01, TOI-6695.01**: frozen leads/rejections (`docs/LEAD_PURSUIT_PLAN_2026-09-27.md`). TOI-224.01 sits in this queue although its TESS_TOI row has no period; leave its campaign alone, exclude it from regeneration, and note the anomaly.
- **Committed records that cite local ledger `run_id`s.** Never overwrite a completed campaign's outputs with a Colab or new-ledger run (`docs/COLAB_HANDOFF.md` problem 4).
- `state/`, `*.fits`, credentials, and anything outside `Cygnus/` on Drive.

## Task

### 1. Revalidate (read-only, write a dated report)

1. Re-query the live TOI table for all 1,000 (one bulk `SELECT toi, tid, pl_orbper, pl_tranmid, pl_trandep, pl_trandurh, tfopwg_disp, rowupdate FROM toi`; do not issue 1,000 single-row queries). Record the query, retrieval UTC and row counts.
2. Classify each target: `ok` (PC/APC, same TIC, period > 0, epoch present), `dispositioned` (now CP/KP/FP/other), `identity_changed` (TIC or name mismatch), `no_period`, `updated` (rowupdate newer than the queue's), `sibling` (another TOI on the same TIC; there are at least TOI-2112, 5564, 5000). `dispositioned` and `identity_changed` targets are dropped from regeneration.
3. For `sibling` targets, the sibling's ephemeris must be compared with any repeat event before a lead is kept (runbook, *Claim-time gates*, step 1).
4. Save the result as `campaigns/tess-periodic-01/REVALIDATION_<date>.json` plus a short `.md`. Include every dropped target and why.

### 2. Regenerate the specs

`campaign new` refuses an existing spec (`scaffold.write_spec`), so regeneration needs a small guarded tool. Build it with tests **first** (put it in `src/cygnus/campaign/scaffold.py` or a new module; add a `--regenerate` path to `python -m cygnus.campaign new --from-queue`):

- **Only regenerate a pure draft**: spec present, `campaigns/<slug>/sky_record.json` has `status: draft`, no `campaigns/<slug>/runner/`, no ledger runs with script prefix `cygnus.campaign:<slug>:` (or `cygnus_multi:`). Otherwise refuse.
- Call `targets.refresh_queue_target(row)` for each target (fail closed on identity mismatch), then `spec_for`. The regenerated spec must have `veto.kind: ephemeris`, the live `period_days`, `t0_bjd`, and record the catalogue query, retrieval UTC and row-update date.
- Keep the same `random_seed`; write atomically (`cygnus.fileio.atomic_write_text`); archive the old spec to `..._history_<date>_...` (`cygnus.fileio.archive_previous`) rather than deleting it.
- Rate-limit: one archive round trip per target is 900 queries. Use the existing throttle (`cygnus.throttle`) or batch the refresh with a bulk query and pass the rows in (`refresh_queue_target(row, fetch=...)` takes a fetch seam).
- Tests to write: draft regenerates; a spec with a runner dir, a completed record or a ledger run is refused; an identity mismatch is refused; period `None` still yields `single_epoch` and is reported as such; idempotent second run.
- Also rebuild the queue CSV so it carries `period_days` (`python -m cygnus.campaign run campaigns/tess-periodic-01.yaml --until target_queue` writes `target_queue.csv` from `build_queue`, whose rows include `period_days`). Do that in a copy first and diff the ranking; the new CSV must not silently reorder work.

Commit the regenerated specs in one commit per ~100 (keeps diffs reviewable). `python -m pytest -q` and `python -m cygnus.campaign check campaigns/<slug>.yaml` must pass for all of them.

### 3. The 99 completed and 1 lead

Do not re-run in place. For each of the 99 `pipeline_check` campaigns:

1. Regenerate the spec into a separately named follow-up campaign (for example `toi-XXXX-01-ephem`) or re-run in a scratch sandbox (`CYGNUS_MULTI_ROOT`) and compare.
2. Decide per target whether the old result stands: a `bounded_null` with no repeat candidate under the wrong veto stays informative; any target that reported repeat events or aliases under a single-epoch veto is suspect.
3. Annotate the old record with `python -m cygnus.campaign reconcile <id> --note "single-epoch veto on a periodic TOI; superseded by <new id>"`. Preserve the original measurements as history; never silently drop them.

### 4. Before it goes into the Colab notebook

`notebooks/cygnus_lead_colab.ipynb` (pin `0cf74ece66982c00c080c8b66c1973b7353be0dc` or later) tiers each target and only runs what it earned. For a fresh production batch:

- The regenerated specs must be committed and **pushed** to a commit you pin; the notebook clones the public repo.
- `python -m cygnus.campaign tier <id>` must show T0 for a fresh draft; `tier --all` counts only campaign records.
- Colab runs T0/T1 (`campaign run`) only for targets with no committed non-draft record, and `vet`/`event_null` only for targets that earned T2. Use `python -m cygnus.batch claim --queue campaigns/tess-periodic-01/target_queue.csv --n 100 --batch <id>` and commit the claims first.
- Rate limits: keep `--jobs` at 3 or fewer; a 1,000-target run is archive-limited, not CPU-limited (`docs/COLAB_HANDOFF.md`).

## Acceptance

- `REVALIDATION_<date>.json/.md` lists all 1,000 targets with a class, the query and the retrieval time.
- Every regenerated draft has an ephemeris veto with the live period; a test proves it.
- No completed campaign was overwritten; the 99 are annotated or superseded with their original outputs intact.
- `python -m pytest -q` passes; `python -m cygnus.publish check` passes if collections changed.
- `docs/STATUS.md` records the outcome (counts per class, dropped targets, what was not re-run).
- Nothing is submitted, published or deployed.

## Traps

- A queue CSV is a snapshot; the truth is the TOI row at claim time.
- A position-only cone search does not clear an event; compare event times against every sibling and confirmed-planet ephemeris.
- `tier --all` counts campaign records only, not `reports/` records.
- Do not run `campaign vet` on a frozen lead to "see what happens": it is gated at T2, and running it rewrites vetting outputs.
- CRLF warnings from git on Windows are expected; keep LF in committed files.
