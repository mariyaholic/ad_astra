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
