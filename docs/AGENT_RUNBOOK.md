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
   Do not change any state.
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
4. **Keep claims inside the evidence rules.** The runner sets the record's outcome to `lead` with evidence *Unverified lead* when it finds a repeat candidate. **Never raise the evidence level, change `outcome`, or call anything a planet, discovery or period.** Escalate instead (below).
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

The following checks stay `not_tested`: detrending alternatives, difference-image centroids, pointing correlation and ADS. They are designed in `ANALYSIS_STACK.md` but not built.

## Operational notes (added 2026-09-25)

1. **Empty ≠ absent, and absent ≠ outage.** When a healthy source returns no rows for a supposedly observed target, poke around before concluding anything: (a) run a **control query** that must return data on the same path; (b) try the target-name format the archive actually indexes — for MAST TESS this is the bare TIC number, `query_criteria(target_name=str(tic), obs_collection='TESS', provenance_name='SPOC', dataproduct_type='timeseries')` (see `DATA_SOURCES.md` §0); (c) loosen filters step by step; (d) fall back to a cone search around the coordinates. Only then conclude "no data at this archive", **record the evidence in the target's claim/report**, skip the target, and continue with the queue — never pause a queue-population run on a single emptiness.
2. **DSH runtime note.** The harness's web-search helper runs on a separate endpoint from chat and can fail independently (e.g., HTTP 402 balance errors) without implying anything about the archives. Prefer **direct fetches** (`web_fetch`, `astroquery`, native archive APIs) and verify any query path with a control before judging a failure from its output.
3. **Pre-screen claims (optional but cheap).** Before `new --next`, probe each unclaimed TIC with the exact fetch filter ladder of step 1 above; claim only targets with SPOC timeseries rows. Saves dead claims like TOI-7176.01 (TIC 44161614 has no SPOC LC at MAST; only SPOC FFI at its position).
