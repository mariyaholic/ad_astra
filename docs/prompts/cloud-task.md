# Gated Cygnus cloud task

Role: Cygnus, operating the reviewed cloud controller.
Intended model: Luna; reasoning effort: xhigh. Select these in Codex controls.

## Objective

Use `cloud/scout.yaml` to gather fresh targets and public archive inputs, then
`cloud/workflow.yaml` to select a finite acquired target batch and run the
existing scientific methods through the tiers each target earns, up to T3.
The shipped pilot selects one target. Increase `limit` only within the user's
requested batch scope. No target is promised to survive screening or reach T3.

The controller follows notebook-style source identity, code/runtime lineage,
exact-product reuse, conservative missing-test states and verified checkpoints.
It keeps earned tier separate from executed stage. It does not execute T4,
promote scientific evidence, submit/contact anyone, publish, commit or push.

## Short form

For a routine batch, run `.venv/bin/python -m cygnus.tier cycle cloud/workflow.yaml --env cloud-agent`
after the preparation checks below, then report the printed handback, counts and incomplete
targets. Rerun the same command to resume. Exit 75 means rerun later; exit 1 needs a person.
[TIERS.md](../TIERS.md) has the contracts. The numbered steps are the same work done by hand.

## Prepare once

1. Read `AGENTS.md`, `docs/STATUS.md`, `docs/CODEX_CLOUD.md`,
   `docs/CLOUD_SCOUTING.md`, `docs/AGENT_RUNBOOK.md` and `DATA_SOURCES.md`. Inspect the actual checkout
   revision and local changes. Workstation results/skills do not transfer
   automatically to the cloud checkout.
2. From the repository root run `.venv/bin/python tools/setup_cloud.py --check`,
   `.venv/bin/python -m pytest -q`, then `.venv/bin/python -m cygnus.cloud --help`.
   Run verification sequentially. Stop on a failed gate; do not weaken tests,
   thresholds, source checks or tier gates to proceed.
3. Read the recipe's queue, target count, trial counts, discriminating question,
   stage/run time limits and scratch quota. Check archive access against the
   runtime's actual policy/readiness. Preserve its proxy and CA settings.
   Never dump environment/secret values.

## Select and execute

4. For a fresh multi-archive run, execute:

   ```bash
   .venv/bin/python -m cygnus.cloud sources
   .venv/bin/python -m cygnus.cloud scout cloud/scout.yaml
   ```

   Read the printed `reports/cloud-scout/<id>/SCOUT.json`, source states and
   target/product selections. Run `acquire` with that actual path. Read the
   resulting ACQUISITION.json, review routes, integrity checks and budgets.
   Only compatible, acquired SPOC inputs may enter the transit pipeline.
   Do not fabricate missing target identities, source quality or ephemerides.
   Then run `plan cloud/workflow.yaml --acquisition` with the actual printed
   ACQUISITION.json path. If no transit input is eligible, report the other
   review queues and stop that route. Do not fall back to the old queue silently.

   Read the printed `state/cloud_runs/<id>/PLAN.json` path. It contains every
   selected exact-source row, query/retrieval time, source queue hash, exclusion,
   code/runtime fingerprint, seed, budget and requested tests. No FITS/science
   has run during cloud planning (the acquisition stage downloaded inputs).
   Inspect `docs/handbacks/<id>/SELECTION.json` and the
   initial report. Failed lookups never license a stale CSV row as a substitute.
   Local reservations do not coordinate separate cloud tasks; use disjoint
   assignments if another task is working the same pool.
5. Run `.venv/bin/python -m cygnus.cloud run <the-printed-PLAN.json>`.
   Use the actual printed path, never a historical run ID or target.
   For a resume, use the existing exact plan instead of creating a new one.
   The controller verifies lineage and completed stage bytes before deciding
   whether to skip or continue. Changed lineage or a corrupt completed
   checkpoint is a blocker, not a reason to reset it.
6. Let it run the native T0/T1 screen and eligible T2 vet/null follow-up.
   Every transition is gated, without tier overrides. A covered failed positive
   control or failed native artifact check stops that target for review.
   Fresh ephemeris/known-source closure
   prevents further testing of that route. Inconclusive localization, nulls,
   blends and unavailable checks remain visible.
7. T3 is permitted only after the scientific gates pass and the recipe supplies
   its budget/question. Supported adapters are archive metadata, conditional
   transit-tied RV fits, and conditional TESS PRF source preference. Input
   packets need checksums, exact target/event identity, units, source provenance
   and a matching quality receipt. Missing inputs stay `not_tested`; T3 remains
   incomplete. Never invent packets, quality validation, calibration, an
   on-target pass, an orbit or a mass to complete a stage.

## Monitor, review and stop

8. Use `.venv/bin/python -m cygnus.cloud status <PLAN.json>` for read-only
   progress. The run uses one serial worker and one writer per plan. Worker
   time, managed scratch occupancy and free scratch space are supervised.
   Quota sampling can overshoot within one request; it is not a network-byte
   meter. Stopped workers do not receive a completed checkpoint. Stop after a
   budget stop, missing input or repeated error; do not wrap runs in a retry loop.
9. After the worker stops, run
   `.venv/bin/python -m cygnus.cloud report <PLAN.json>`. Read the top report,
   scientific stage reports/records, vetting/null diagnostics and T3 results.
   The capsule contains source/runtime lineage, checkpoint receipts, a ranked
   board, selection/search logs and a full SHA-256 manifest. Review events under
   the runbook's event-time, localization, units, null-statistics and primary-
   literature/TTV rules. Keep draft markers until that review is actually done.
10. Run `.venv/bin/python -m pytest -q` after scientific artifacts are written;
    inspect `git diff --check`. Return exact test counts, completed/blocked
    stages, gates, resource receipts, artifact links and one discriminating
    next test. Separate software, live-archive and scientific evidence.

Keep raw inputs in scratch and the ledger/resume state under ignored `state/`.
Preserve incomplete attempts. Follow `docs/STORAGE.md` for durable bulk
retention, resolve the available route, use only Drive `Cygnus/`, and verify
uploads. Never claim a backup from a listing or delete the only input copy.
Reopening the same cloud task is the supported resume path. This controller
does not automatically mount Drive or import Colab packets.
