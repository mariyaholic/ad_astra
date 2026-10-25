# Agent runbook: known-object tests

For any agent (any model, any tool) running one target through the pipeline. You do not write analysis code. You run five commands, read what they produce, and write a short review. Read `AGENTS.md` once for the rules on evidence and claims. This page is the procedure.

## Setup (once per machine)

```bash
git clone https://github.com/mariyaholic/ad_astra && cd ad_astra
python -m pip install -e ".[test,campaign]"
```

- **Scratch.** Light curves go to `CYGNUS_SCRATCH` if it is set, otherwise `~/.cache/cygnus/scratch`. Each target takes about 2 MB per sector, six sectors at most. Scratch is safe to delete.
- **Ledger.** It lives at `state/ledger.sqlite`, or at `CYGNUS_LEDGER` if set, and is created on first use. On a machine other than the project workstation, use your own ledger. Name the run IDs in your report so they can be merged later. Several agents on one machine may share a ledger.
- **Credentials.** No credentials are needed. Every service used is public and anonymous: MAST, NASA Exoplanet Archive, VizieR and SIMBAD.

## The loop (one target)

```bash
git pull                                              # see what others have claimed
python -m cygnus.campaign queue                       # rank, target, state, positive control, review
python -m cygnus.campaign new --next                  # claims the top unclaimed target -> campaigns/<slug>.yaml
git add campaigns/<slug>.yaml && git commit -m "Claim <target>" && git push   # the claim; if the push conflicts, pull and run new --next again
python -m cygnus.campaign run campaigns/<slug>.yaml   # 1–5 min; resumable, rerun after a failure
python -m cygnus.campaign report campaigns/<slug>.yaml
python -m pytest -q                                   # must pass
```

Other targets:
- a named target: `new --from-queue TOI-2423.01`;
- any known planet: `new --planet "WASP-12 b"` (NASA Exoplanet Archive name; every predicted transit becomes a positive control);
- anything else: `new --manual NAME --tic N --ra DEG --dec DEG --t0 BJD [--period D --depth-ppm X --duration-h H] --source "where the numbers came from"`.

Never edit a generated spec's numbers by hand. If a value is wrong, fix the source and generate the spec again.

## Claim-time catalogue and candidate gates

The queue is a dated prioritization snapshot. `new --next` and `new --from-queue` must re-query the exact TOI/TIC from the NASA Exoplanet Archive and record the query, retrieval UTC and row-update date in the spec. Verify `period_days` and the veto kind: a current period requires an ephemeris veto across every retrieved sector. If identity, epoch or service access fails, stop the claim and record an inconclusive lookup; never silently fall back to the stale CSV. For an existing historical spec with `period_days: null`, check the current TOI row before interpreting any repeat event.

For every proposed lead, use this review sequence before creating or retaining a candidate dossier:

1. **Identify the event.** Match TIC/TOI/Gaia identity and propagated position, then query the current TOI table, confirmed planet table, sibling ephemerides and primary literature. Record the exact query, release and retrieval date. Compare each local BJD_TDB event to predicted *and individually published* transit times, including TTVs and uncertainty. `prior_art`'s one-day event-time overlap is a broad alert, not a proof of identity; a non-match cannot clear missing ephemerides or TTVs. Check the local time scale before subtracting epochs.
2. **Reconcile units.** Keep source depths in ppm and show `ppt = ppm/1000`, `% = ppm/10000`. Compute a central, undiluted radius scale only as a conditional check; grazing, dilution, uncertain host radius and poor RUWE invalidate a precise radius estimate. Check durations, radius and RV units against the source table.
3. **Audit localization.** Read the difference-image offset in arcseconds *and* its uncertainty/significance, the centroid and pointing time series, PRF registration, aperture changes, neighbours and background. A coarse three-pixel inclusion test does not override a significant displacement. If any relevant test fails or is unavailable, keep localization failed/inconclusive; do not call the event on-target.
4. **Audit statistics and coverage.** Report the empirical null exceedance count and number of trials (for example 0/300), red-noise treatment, searched targets/epochs/widths, and injection–recovery completeness. Zero exceedances is finite null resolution, not p=0 or a Gaussian sigma. A nondetection constrains only covered windows at demonstrated sensitivity; keep unobserved aliases and eccentric cases open.
5. **Compare all allowed interpretations.** Reject pointing, off-target, known-object and sibling-transit explanations first. An event rejected as an artifact cannot select an alias even if it is near one predicted phase. Use multi-epoch RV to constrain a binary; one visit at unknown phase is not an orbital upper bound. A second reduction of the same pixels tests reduction robustness, not independent sky support.
6. **Reconcile outputs.** Put the reasoning and null results in `REPORT.md`, `SEARCH_LOG.md` and `vetting/`; update or regenerate `sky_record.json`. Edit the canonical `publish/candidates/*.json` source before regenerating `DOSSIER.md`, update every collection description/status and retire false candidate records through `Ledger.retire_candidate(candidate_id, reason=..., reference=...)`, which archives the old row while preserving measurements and prior-art history. Keep a dated rejection note for withdrawn leads. Run `python -m pytest -q`, `python -m cygnus.publish check`, and inspect the rendered candidate route before any site build/deploy.

TOI-6695.01 is the regression example: S34 and S61 belong to the published TOI-6695 b transit sequence with TTVs; see `campaigns/toi-6695-01/REJECTION.md`. The original TOI queue row lacked a period in the CSV, so its spec used a single-epoch veto; a position-only prior-art audit then missed the event-time identity.

### Revisit of the four 2026-09-27 leads

Before working on TOI-224.01, TOI-2666.01, TOI-3500.02 or TOI-7610.01, read `docs/LEAD_PURSUIT_PLAN_2026-09-27.md` **Next-agent execution contract** and the dated verification report. Their older specs still have `period_days: null` / `veto: single_epoch` and are frozen provenance, not a template for a fresh run. Do not run `--force`, `vet`, or regenerate reviewed outputs in those campaign directories; use a separately named campaign or report from an exact current TOI/TIC query, retaining the historical inputs for comparison. Follow the per-lead falsification and promotion gates in the plan, and keep every failed/inconclusive/not-tested check visible.

## Batches (many targets, unattended)

`python -m cygnus.batch` (`src/cygnus/batch.py`) drives the same loop for tens to hundreds of targets. It calls the same commands (`cygnus.multi new`, `run` and `report`), so every campaign it produces is identical to one made by hand.

```bash
# 1. a new ranked queue (once per pool; skip it to keep working an existing queue)
python -m cygnus.batch queue tess-mono-02 --where "pl_orbper IS NULL AND tfopwg_disp IN ('PC','APC')" --top 500
# 2. claim the next N unclaimed targets into a named batch, then commit the claims (command printed)
python -m cygnus.batch claim --queue campaigns/tess-mono-02/target_queue.csv --n 100 --batch b01
# 3. run everything unfinished in the batch; safe to re-run after a crash or Ctrl-C
python -m cygnus.batch run --batch b01 --jobs 3
# 4. triage
python -m cygnus.batch status --batch b01      # state/batches/b01/SUMMARY.md
python -m pytest -q
```

What `run` guarantees:

- **One batch per ledger.** Batches share a ledger through a lock file, `<ledger>.batch.lock`. A second batch refuses to start. A lock left behind by a dead process on the same host is taken over, and the takeover is recorded in the journal.
  - Don't run single campaigns by hand on the same ledger while a batch is running.
  - `--jobs` runs campaigns in parallel inside the one batch. 3 jobs were tested on one ledger (2026-09-26: 3 campaigns, 19 ledger runs, no lock errors, 87 s wall time vs about 195 s one at a time). The archives' rate limits, not the CPU, set the ceiling.
- **Crash safety.**
  - Each campaign runs in its own process, with a wall-clock limit (`--timeout`, default 1800 s).
  - Runs left `open` by a killed attempt are closed as `aborted`, with a note, before that campaign is retried. Only that campaign's own steps are touched.
  - MAST requests time out after 120 s instead of astroquery's 600 s.
- **Retries.**
  - Transient failures are retried up to `--retries` times (default 2), with 30 s and then 120 s backoff. Transient means 5xx responses, timeouts, proxy and connection errors, or a locked database.
  - A deterministic error (a traceback that is not a network error) is not retried. It is listed under *Failed after retries*. Report it; do not patch code.
- **Resume.**
  - `state/batches/<id>/journal.jsonl` records every attempt, with per-attempt logs in `logs/`.
  - A re-run skips campaigns that finished with a record. The runner also reuses completed steps.
  - `--redo` forces a re-run.
- **Triage.**
  - `SUMMARY.md` lists the escalations first: a repeat candidate (`outcome: lead`), a positive control `failed`, every catalogue service errored, or no record.
  - Then come failures, then routine finishes.
  - Claiming skips queue rows that cannot be scaffolded (e.g. no catalogued epoch) and records why, instead of stalling.

`run` never reviews, publishes or commits anything. Every campaign still needs the review below before its draft marker is removed. Batch state lives under `state/`, which is never committed.

## Reviewing the draft

`report` writes `campaigns/<slug>/REPORT.md` and `SEARCH_LOG.md`. The numbers in them are copied from the runner's outputs. Your job:

1. **Read the checks table.** Each state has a fixed meaning:
   - `passed`, `failed`, `inconclusive` mean the test ran, with that result;
   - `not_tested` means it did not run, which is never the same as passed.
   Do not silently change a generated state. If its decision rule is wrong, fix the rule, reclassify the stored source output with provenance, regenerate downstream records and run the gate.
2. **Read the positive control.** It is the first thing to judge.

   | Positive-control state | Meaning | What you do |
   |---|---|---|
   | `passed` (recovered) | The catalogued transit was found where the catalogue puts it. | Continue. |
   | `failed` (not recovered) | The epoch was covered with usable data, but nothing was found. | Say so in the bottom line. Possible causes: wrong epoch, a shallow transit below the sensitivity, a wrong TIC. Do not tune thresholds. |
   | `inconclusive` / `not_tested` | The data had a gap at the epoch, or no retrieved sector covers it. | Record it and move on. |

3. **Read *Screen events* and *Repeat candidates*.** Non-persistent events are almost always systematics. For each *persistent* event and each *repeat candidate*, write one line in a **Reviewer notes** section. Say what you checked from the outputs already on disk:
   - `sectorNN/normalized_series.csv`, which has the time, quality, SAP and PDCSAP flux, and residuals;
   - `screen.json`, which has centroids per entry;
   - `period_aliases.json`.

   Use the table in `campaigns/toi-2666-01/REPORT.md` as the model.
4. **Keep claims inside the evidence rules.** The runner sets the record's outcome to `lead` with evidence *Unverified lead* when it finds a repeat candidate. **Never raise the evidence level or claim a new planet from a runner flag.** A documented falsification may lower `outcome` to `pipeline_check`; reconcile the record, report, ledger and publication artifacts together as described above.
5. **Mark the draft reviewed** by deleting the first line of both files, `<!-- cygnus:generated-draft -->`. `report` never overwrites a reviewed file; later drafts go to `REPORT.draft.md`.
6. **Commit.** Commit the spec, the `campaigns/<slug>/` directory and nothing else. Never commit `*.fits`, `state/` or your scratch paths. Use this message:

   ```
   <target>: known-object test (<positive-control state>[, lead])
   ```

## When to stop and escalate

Stop and write an `## Escalation` section at the top of the report, then tell the user, when:

- a **repeat candidate** appears (`period_aliases` found one);
- the **positive control fails** on data that covers the epoch;
- the run fails twice with the same error. Paste the error and do not patch the code.
- a catalogue service errors for every target. A service may be down; record it and leave the check `inconclusive`.

A stronger agent or a person then runs `python -m cygnus.campaign vet campaigns/<slug>.yaml` (add `--events BJD,…` for events the runner did not flag). It writes `campaigns/<slug>/vetting/`: sibling-TOI ephemerides, shape against the reference transit, detrending alternatives, red-noise significance, background/centroid/pointing, quality flags, a difference image, Gaia neighbours, same-CCD common mode, and alias limits. Record the reading in *Reviewer notes*. The log is `campaigns/tess-mono-01/LEAD_VETTING_LOG.md`.

Do not change code in `src/`, thresholds in a generated spec, or anyone else's campaign. Code changes go through a stronger agent or a person, with tests.

## What each step does

| Step | Output | Check it sets |
|---|---|---|
| `fetch_products` | SPOC 120-s light curves; sectors covering the catalogued epoch are fetched first; SHA-256 recorded | Product integrity |
| `calibrate_screen` | k* per light curve (sign-flip null) and completeness by injection–recovery (`sectorNN/calibration.json`) | Calibrated threshold, injection–recovery |
| `known_signal_recovery` | whether the catalogued transit is recovered, and its depth | Known-signal recovery (positive control) |
| `residual_screen` | dips outside the catalogued transit, grouped into distinct events, persistent or not | (updates the threshold checks) |
| `period_aliases` | repeat candidates and the periods ΔT/n not excluded by the data (`period_aliases.json`) | Period aliases (repeat events) |
| `prior_art` | NASA Exoplanet Archive, TOI, VSX and SIMBAD cone searches, dated, into the ledger | Catalogue cross-match |
| `stellar_context` | Gaia DR3 cone: proper-motion-propagated identification, Teff/R*/M*/ρ* from colour and parallax (Mamajek dwarf table), dilution cap per neighbour (`stellar_context.json`) | Target-to-Gaia identification; Stellar priors; Blend and dilution census |
| `event_census` | quality bits in and near each screen event, pointing/centroid shifts | Pointing and quality census per event |
| `moving_objects` | SkyBoT at each event epoch (600″) | Moving objects at screen-event epochs |
| `variability_guard` | VSX type/period collision with the aliases; SIMBAD object class | Variable-catalogue collision (VSX); Object-class guard (SIMBAD) |
| `fetch_independent` | Kepler/K2 long-cadence products (MAST, searched by position) and ZTF light curves (IRSA), fetched, checksummed and ledgered like any other product; empty answers and outages are recorded, never read as "no data" | — |
| `alias_cross_instrument` | depths at predicted alias epochs in the independent light curves (`fetch_independent`) and in other collections fetched by `fetch_products` | Independent repetition; Independent-epoch confirmation (ZTF) |
| `rv_bounds` (only with `eso`) | archival RVs → per-alias companion mass upper bound | Stellar-companion exclusion (archival RVs) |

With `stellar_context` in the spec, `period_aliases` also writes a per-alias duration likelihood (circular orbits; a ranking aid, not a period). A failed VSX or SIMBAD guard escalates in `cygnus.batch` triage. `inconclusive` from these steps usually means a service did not answer (e.g. SkyBoT server errors at some epochs): record it, do not re-run in a loop.

Still `not_tested` in the runner (vet covers them for leads): detrending alternatives, difference-image centroids and ADS.

**Test lanes.** `python -m pytest -q` is the offline gate (run it before committing). Opt-in: `python -m pytest -o addopts= -m slow` (seeded calibration, minutes), `-m replay` (re-runs four committed campaigns from scratch copies; skips if the products are not local) and `-m network` (live archives). `python -m cygnus.multi archives --check all` prints a status table of every archive; `unavailable` is an outage, only `error` is a code problem.

## Operational notes (added 2026-09-25)

1. **Empty ≠ absent, and absent ≠ outage.** When a healthy source returns no rows for a supposedly observed target, poke around before concluding anything: (a) run a **control query** that must return data on the same path; (b) try the target-name format the archive actually indexes — for MAST TESS this is the bare TIC number, `query_criteria(target_name=str(tic), obs_collection='TESS', provenance_name='SPOC', dataproduct_type='timeseries')` (see `DATA_SOURCES.md` §0); (c) loosen filters step by step; (d) fall back to a cone search around the coordinates. Only then conclude "no data at this archive", **record the evidence in the target's claim/report**, skip the target, and continue with the queue — never pause a queue-population run on a single emptiness.
2. **DSH runtime note.** The harness's web-search helper runs on a separate endpoint from chat and can fail independently (e.g., HTTP 402 balance errors) without implying anything about the archives. Prefer **direct fetches** (`web_fetch`, `astroquery`, native archive APIs) and verify any query path with a control before judging a failure from its output.
3. **Pre-screen claims (optional but cheap).** Before `new --next`, probe each unclaimed TIC with the exact fetch filter ladder of step 1 above; claim only targets with SPOC timeseries rows. Saves dead claims like TOI-7176.01 (TIC 44161614 has no SPOC LC at MAST; only SPOC FFI at its position).
