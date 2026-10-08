# Seamless first-stage to T2 Colab follow-up

The reusable second notebook is `notebooks/cygnus_higher_tiers_colab.ipynb`.
It consumes the exports of `notebooks/cygnus_lead_colab.ipynb`; it is not a
second screen with a manually copied target list. Scientific work is performed
by the existing native campaign tools, not a newly implemented transit pipeline.

## Run a new batch

1. Run the first notebook and complete its export under
   `Cygnus/colab_runs/<source-run>/`.
2. Open the second notebook in a CPU Colab runtime and choose **Run all**.
   Leave `SOURCE_RUN = 'latest'` to use the newest first-stage export by its
   recorded UTC. When several batches run concurrently, set `SOURCE_RUN` to
   the exact first-stage run identifier instead.
3. Read cell 4's source, exclusions, selected-target count, exact light-curve
   byte estimate, and output/resume directory before the target loop begins.
4. Read the final checkpoint counts and errors. A finished loop is not an
   assertion that every target succeeded or every scientific test passed.

A future first-stage batch uses the same notebook without editing target lists,
campaign identifiers or output-directory names. Starting it remains a user
operation; there is no background Colab launch or remote-compute scheduler.

## Source contract and eligibility

The source must identify the first notebook as its producer and contain a
consistent `LOCATION.json`, `MANIFEST.sha256`, `tier_board.json`, `done.json`
and campaign sky records. The existing `cygnus.colab_sync.audit` validates
identity, tier-input checksums and recognized check names. It re-derives earned
tiers from the actual post-run record, never from the starting board.

Only completed, checkpointed targets that earned at least T2 are selected.
T0, T1, missing, failed and closed rows are accounted for in `SOURCE_AUDIT.json`
and the final exclusions, rather than silently discarded or promoted. The
specialist/frozen targets TOI-224.01, TOI-2666.01, TOI-3500.02 and TOI-7610.01
remain excluded from routine reruns; use
`docs/LEAD_PURSUIT_PLAN_2026-09-27.md` for their specialized work.

A corrupt newest source is an error, not permission to use an older batch.
Second-stage exports are never selected as first-stage inputs. Finish/export
the first notebook before starting the second; do not run the two writers
against the same source while it is being changed.

The recorded `p02-b02-2026-10-02` audit has 30 T2, one T1, 68 T0 and one
missing target. These are eligibility marks, not completed T2 vetting or
evidence promotion. Every new run re-audits its own packet.

## What T2 executes

- Load each campaign specification from the **source batch's exact Git commit**.
- Verify the saved source sky record, product-fetch receipt, known-signal
  recovery receipt and period-alias table against the first-stage manifest.
- Rehydrate exact TESS SPOC light curves through their product IDs, expected
  sizes and SHA-256 hashes; never reuse source-VM absolute paths as input files.
- Reuse the original event/alias selection without a new T0/T1 screening pass.
- Run native pixel, neighbour and sibling-ephemeris vetting.
- Run native event-epoch empirical nulls and event-depth injection recovery.
  Default parameters are `n_null=300`, `n_inject=100`, `min_n=100`; the campaign
  random seed and actual parameters are recorded.
- Preserve unavailable tests as `not_tested` or `inconclusive`. If fresh
  vetting closes a target's route through a known-event collision, checkpoint
  that closure and explicitly skip further event-null testing.

One target is processed at a time. FITS and bulk intermediates stay in the
Colab VM scratch directory, not the Drive export. Pixel-download volume and
execution time depend on archive availability, sectors, events and aliases;
no unconditional whole-batch ETA is asserted.

T3 spectra/RV/calibrated PRF adapters, T4 execution, independent-sky confirmation,
primary-literature/TTV clearance and evidence promotion are **not implemented
by this notebook**. Event-epoch nulls are selection-touched diagnostics, not a
search-wide false-alarm calibration. Zero empirical exceedances never mean
zero probability. A workflow tier is not an astrophysical evidence level.

## Resume without mixing batches or revisions

The output is `Cygnus/colab_runs/t2-<source-run>-<contract-digest>/`.
`LINEAGE.json` binds it to the source manifest hash, source commit, reviewed
science-code commit, notebook source revision, selected target set and null
parameters. A different source, revision or parameter set gets separate state.
A nonempty directory without matching lineage is refused.

`CHECKPOINTS.json` contains the hashes of each completed target's saved files,
its decision digest and its lineage digest. Completion also re-derives the
saved decision from the verified sky record and enforces completed status and
T2 execution. Missing, extra or mutated files and altered decision labels
invalidate that checkpoint. Export refuses invalid completed targets before
rewriting any manifest; unfinished campaign leftovers are not included in the
export. Old hash-only checkpoints cannot license a skip under this revision.
Failed targets carry `errors/<target>.json` and are retried on the next run;
only their disposable attempt files are replaced, while source and ledger
history remain intact. Reopen the same revision and **Run all** after an interruption; the setup and discovery cells
reconstruct context, and verified completed targets skip. Only one runtime may
write a given output directory.

## Outputs and existing workstation sync

Each target has a derived `sky_record.json`, `REPORT.md`, `SEARCH_LOG.md`,
`SOURCE_SPEC.yaml`, `FOLLOWUP_SPEC.yaml`, `SOURCE_RECORD.json`, `SOURCE_LINK.json`,
`period_aliases.json`, native `vetting/` outputs, `event_null.json`, and exact
light-curve/ancillary product receipts. Evidence labels are not promoted.
Original first-stage exports and reviewed canonical records stay read-only.

The run contains `READOUT.md`, `READOUT.json`, `SOURCE_AUDIT.json`,
`LINEAGE.json`, `CHECKPOINTS.json`, `ENVIRONMENT.txt`, a separate companion
`ledger.sqlite`, refreshed `tier_board.json`, `done.json`, `MANIFEST.sha256`
and `LOCATION.json`. Each export is read back, hashed and audited before it
is reported as valid. The companion ledger is never merged automatically.

The existing Windows `\\Cygnus-Colab-Sync` task already discovers compatible
exports. Do not add another scheduled task. For a manual, non-overlapping sync:

```bash
python -m cygnus.colab_sync --run <printed-stage-two-run-id> --update-notes
```

## Release preflight

The initial 31 passing fixtures did not cover four defects found by independent
review: missing product-digest pinning, no-fit completion, re-authentication of
altered checkpoint outputs, and mutable done-tier assertions. These now have
focused red/green regressions and corrections. Product receipts require explicit
record membership, a full hash and positive integer size; defining fits and
covered null measurements are required for completion; corrupt completed
artifacts stop export; and decisions are bound to lineage and re-derived records.
Closed routes save an explicit skipped-null receipt instead of a stale success.

The corrected revision is `t2-v1-c3f37cbbb62b`, notebook SHA-256
`04e2009fd47b3e6741017817224df4030eac886d33bc3c252c2a0dd453b38d5a`.
The focused independent re-review passed with no remaining findings for those
four blockers or the stale closure receipt. This is a software release check,
not validation of a live Colab run.

## Delivery and cloud staging

The canonical reviewed notebook is attached directly for local download and
Colab upload. The copy attempt at
`Cygnus/batches/higher-tiers-t2-v1-c3f37cbbb62b/` reached Drive: the notebook,
operation note, selection example, build receipt and manifest were listed.
However, remote byte verification and `LOCATION.json` registration were blocked
by HTTP 403 `RATE_LIMIT_EXCEEDED` on rclone's shared Google client. A bounded
retry after a quota window also failed. The cloud copy is **not checksum
certified** and is not the recommended delivery until read-back succeeds.
`storage/locations.jsonl` retains this partial-staging limitation; no remote
Colab execution or authorization change was performed.

Use the verified attached `.ipynb`: upload/open it in Colab, choose a CPU
runtime and **Run all** after the first-stage export is complete. Prefer saving
the notebook under `Cygnus/` to keep its storage provenance together.
The shared-client retirement warning is a separate operational warning, not
evidence that this error requires a new sign-in; the observed blocker is quota.

## Agent maintenance and reproducibility

Reviewable sources live in `notebooks/higher_tiers/`, one file per cell plus
`workflow.py`. `tools/build_higher_tier_notebook.py` compiles and embeds them,
adds per-cell definitions, and derives the revision from normalized source
bytes. Never hand-edit the assembled notebook or invent a second target planner.

```bash
python tools/build_higher_tier_notebook.py
python -m pytest -q tests/test_higher_tier_notebook.py tests/test_colab_sync.py tests/test_colab.py
```

The science pin is the pushed commit
`05ba4f4ee6e2053c256240ab04f7fbb527e32afe`. The notebook embeds its new
orchestration, so delivering this artifact does not require committing or
pushing the new files. Later code pins require review and a rebuilt notebook.

Verification on 2026-10-08: the corrected notebook suite passed 35 tests
(including the synthetic native-pipeline integration). A separate parent check
of the integrity/selection/resume regressions and existing Colab/sync tests
passed 60 tests with one integration test deliberately deselected to avoid
repeating the numerical fixture. Ruff, diff checks, all six cell compilations,
and embedded-helper/source equality passed. The integration
test executes the assembled notebook's configuration, helpers, discovery,
target loop, export/readout and resume cells against explicitly synthetic FITS;
only live archive boundaries are replaced. It verifies source immutability,
exact-product reuse, native vet/null execution, conservative unavailable-pixel
states, valid scheduler audit, completed-target skip and newly closed routes.
Discovery/eligibility, corrupt-packet refusal and lineage/hash guards also have
regression tests. The assembled selector was also executed against the cached,
manifest-verified `p02-b02-2026-10-02` metadata: 30 eligible and 70 excluded
rows account for all 100 requested targets, with 99 checkpointed. This was a
real-source eligibility check, not a live T2 science run. One native empty-legend
plotting warning was observed.

No Google Colab mount/install or live astronomical T2 batch has been executed
as part of the build. An attempted whole-project offline gate exceeded its
180-second local budget; a broader native/setup gate exceeded 90 seconds.
Neither is reported as passed. The user-run Colab execution is the outstanding
full environmental and live-archive check; test fixtures are not sky evidence.
