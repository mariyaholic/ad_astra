# How autonomous is the Cygnus pipeline? (study, 2026-09-24)

Question: once started, which parts of the AGENTS.md research loop run without a person or agent steering each step, and which are still hand-driven or only designed? Evidence is the code, the ledger and the records as of commit `e25dbcb`.

> **Update, later on 2026-09-24:** problems 1–4 and steps 1–6 below were acted on the same day.
> Campaigns now run from YAML specs through a ledgered, resumable runner (`docs/CAMPAIGNS.md`); the
> WASP-12 analyses were re-run through it with identical results and are in the ledger; open runs
> were closed and can no longer be left open; the residual screen is calibrated (sign-flip null,
> injection–recovery), which showed it only excludes dips ≳ 1.5 % deep at k = 5; four catalogue
> adapters (NASA Exoplanet Archive, TOI, VSX, SIMBAD) replace `not_tested` stubs; `tess-mono-01`
> has a ranked 73-member target pool; CI and a weekly public-archive queue job exist. Rough scale:
> about **2.5 of 4**. Still missing: detrending families, centroid/blend and pointing audits,
> single-transit period posteriors, ADS literature, and running `tess-mono-01` itself (awaiting a
> go-ahead). The text below is the original study.
>
> **Update 2 (2026-09-24):** known-object tests are now generated, not written: `cygnus.campaign new/run/report/queue`
> with a positive control, grouped events and period aliases, portable across machines (`docs/AGENT_RUNBOOK.md`).
> Piloted on TOI-2666.01. Rough scale: about **3 of 4** for known-object work; discovery vetting still needs a reviewer.

## Short answer

**Data acquisition is automated; science is not.** A single command fetches, checksums, budgets and ledgers archive products from eight services, and failures become visible records rather than silent gaps. Everything after that — choosing targets, running an analysis, vetting, prior-art checks, writing the report — is done by an agent writing a one-off script per campaign. The campaign runner, the vetting modules and the prior-art adapters exist only as designs. Nothing runs between sessions.

On a rough five-step scale (0 manual → 4 closed-loop campaigns with scheduling), Cygnus is at **about 1.5**: automated, provenance-safe ingest (1) plus automated guardrails on outputs, but no automated analysis chain (2), vetting (3) or scheduling (4).

## Stage by stage (AGENTS.md staged strategy)

| Stage | What exists | Autonomy | Evidence |
|---|---|---|---|
| **Scout** (targets, footprints, hypotheses) | Target lists are hand-written in the ingest config; names resolved automatically through CDS Sesame. No ranked target/lead queue in code. | manual choice, automated resolution | `ingest/tier1.py` `resolve_name`; `RUN_CONFIG.json` lists |
| **Screen** (metadata first, budgets) | Per-service byte budgets; over-budget items recorded as `excluded`; metadata probes before downloads. | **automated** | `ingest/pack.py` `PackBuilder`; 132 manifest rows incl. failed/excluded |
| **Acquire + provenance** | 8 archive collectors, checksums, manifests, ledger `products`/`runs`; upload → MD5 verify → retire local copy. | **automated per command**; upload launched per service by hand | `python -m cygnus.ingest.tier1 --services all`; `tools/upload_verify_retire.py`; ledger: 134 products |
| **Analyze** | Two campaign analyses, each a bespoke script with product IDs, ephemeris and thresholds hard-coded. Reusable utilities in `analysis/` are tested on synthetic data only. | **manual (agent-written scripts)** | `campaigns/run_wasp12_sector20.py`, `tools/analyze_tess_residual.py`; `docs/ANALYSIS_SUITE.md` |
| **Stress-test** (detrending families, injection–recovery, nulls, pixel/centroid audits) | Designed: `detrend_lab`, `injection_recovery`, `nulllab`, `blendmap`, `jitterwatch`. Not built. The residual screen varied baselines by hand. | **not built** | `ANALYSIS_STACK.md` register ("designed — Sprint 1") |
| **Validate** (prior art, catalogs, independent data) | Known-Object Gate framework: only the SkyBoT adapter is real; every other service returns `not_tested (adapter not implemented)`. Ledger `prior_art` has 0 rows. | **framework only** | `priorart.py` `apply_gate` |
| **Report and rank** | Dossier renderer and leads board exist and are driven by records; campaign REPORT/SEARCH_LOG and sky records are hand-written. | partial: rendering automated, content manual | `reporting/`, `docs/SKY_RECORDS.md` |
| **Publish / explore** | Site build + leak scan, explorer build, sky-record collection: all one command, all offline. | **automated per command** | `python -m cygnus.publish build`; `build_explorer.py` |
| **Scheduling / continuity** | No runner, no scheduler, no CI. AGENTS.md itself notes no background process is implied. | **none** | no `.github/`, no job definitions |

## Guardrails that already run by themselves

These are the strongest part of the system and would carry over to a more autonomous pipeline unchanged:

- `CandidateRecord` refuses to raise evidence above *unverified lead* while any audit item is not `passed`, and rejects states outside passed/failed/inconclusive/not_tested.
- Checksum gates in every analysis script and in the pack reader.
- Publication boundary and leak scan on every site build.
- `tests/test_skyrecord.py` fails if an analysis lacks a valid sky record, so results cannot silently vanish from the explorer.
- Failures and exclusions are written as rows, not dropped.

## Gaps that block autonomy (found in this study)

1. **The campaign YAML is documentation, not configuration.** Nothing in the package reads `campaigns/*.yaml` (only the publisher parses YAML). The residual-screen script hard-codes its inputs, and the spec and code have already drifted: the YAML gives the period as a rounded `1.0914` d "provisional veto" and describes one light curve; the script uses `1.09141890100` d and two sectors.
2. **Analyses do not write to the ledger.** The ledger holds only ingest and probe runs (`cygnus.ingest.tier1`: 13 completed, 5 failed, 10 open; `data_probe.mast_tesscut`: 2), 4 measurements, 0 candidates, 0 prior-art rows. The WASP-12 results live only in report folders, so AGENTS.md's "every measurement traces to a logged run" is not yet true for analyses.
3. **Runs are left open.** Ten ingest runs never recorded a close, so the ledger cannot tell interrupted from in-progress.
4. **Thresholds are uncalibrated by design.** `tess-mono-01` keeps `robustness_min` and `fa_alpha` null until injection–recovery and null tests exist — correct, but it means no discovery campaign can run unattended yet.
5. **Prior-art is almost entirely `not_tested`.** Without adapters, any automated lead would be capped at *unverified lead* (correctly) and would still need a person for the literature.
6. **Credentials pin bulk data to one machine.** Drive access is an OAuth token on the workstation; a cloud session can fetch public archives but cannot read the Tier-1 products on Drive.

## Smallest steps to real autonomy (in order of leverage)

1. **Campaign runner v0.** Read a campaign YAML, run its steps, open and close ledger runs, write measurements, emit `results.json`, a SEARCH_LOG skeleton and a draft sky record. Port the residual screen onto it first; this removes the spec/code drift at once.
2. **Close runs reliably.** Context-managed ledger runs that record `failed` on exceptions; a one-off repair marking the ten open ingest runs `abandoned`, with a note.
3. **Minimal injection–recovery and null tests** on real light curves, so screens report completeness and calibrated thresholds instead of a bare −5 MAD cut. This unblocks `tess-mono-01`.
4. **Cheap prior-art adapters** using the existing TAP client: NASA Exoplanet Archive (planets, TOI), VizieR VSX, SIMBAD. Each one turns a `not_tested` into a dated result.
5. **A target queue.** A ranked list generated from a declared pool (for example TOIs with single transits), with the ranking rationale recorded, as AGENTS.md requires.
6. **Scheduled offline jobs.** CI (for example GitHub Actions) for tests, site and explorer builds on every push; later, scheduled public-archive screening that needs no Drive credentials.

Until steps 1–4 exist, "autonomous research" in practice means an agent in a session choosing a target and writing a script, with the guardrails above keeping the claims honest.
