# Campaigns: specs and the runner

A campaign is a YAML spec in `campaigns/` (`schema: cygnus.campaign/1`). The runner executes it as ledgered, resumable steps and regenerates the campaign's sky record:

Known-object tests are generated rather than written: `python -m cygnus.campaign new --next | --from-queue NAME | --planet NAME | --manual …`, then `run` and `report`, then `queue` shows the board. Procedure and review rules: `docs/AGENT_RUNBOOK.md`.

```bash
pip install -e ".[campaign]"
python -m cygnus.campaign check campaigns/<id>.yaml          # validate only
python -m cygnus.campaign run campaigns/<id>.yaml            # run or resume
python -m cygnus.campaign run campaigns/<id>.yaml --until target_queue
python -m cygnus.campaign run campaigns/<id>.yaml --force    # recompute every step
```

Code: `src/cygnus/campaign/` (runner, steps, light-curve primitives), `src/cygnus/targets.py` (queue), `src/cygnus/priorart.py` (catalogue adapters). Tests: `tests/test_campaign.py`.

## Multi-archive campaigns (`cygnus.multi`)

A spec may declare `runner: cygnus.multi`; `python -m cygnus.campaign run|check|report|vet` hands such specs over whole (`python -m cygnus.multi …`), and `load_spec` rejects a `runner:` spec anywhere else, so the two runners cannot be confused. The same ledgered, resumable loop runs them, with three generalisations:

- **Any archive.** `fetch_products` discovers products through 24 registered archive adapters (the free services of `DATA_SOURCES.md` sections 1–3, 5 plus the NASA Exoplanet Archive); `python -m cygnus.multi archives` lists them, `archives --check <name>` live-probes one discovery path.
- **Product kinds.** Products carry `kind` (`lightcurve`/`image`/`table`/`text`); only time series are screened. A single-channel product is screened once (`channel_mode: single`) against a red-noise systematics model (`cygnus.multi.systematics.py`) instead of the false SAP-vs-PDCSAP independence claim.
- **Catalogue-only steps.** `context_products` (what was fetched), `source_checks` (per-product integrity; Gaia RUWE and `non_single_star` flags; MAST quality census; MPC observations via `data.minorplanetcenter.net`) and `astrometric_vetting` (Gaia DR3 NSS two-body cross-match of the target, mass function where a significant solution exists) answer questions without light curves; a campaign with no light-curve product is a recorded null, not a red run.

Runs go to the production ledger under the `cygnus_multi:` script namespace. Setting `CYGNUS_MULTI_ROOT` confines specs, outputs **and ledger** to a sandbox root instead (the `experimental/` copy is such a sandbox, with its own tests); `python -m cygnus.multi.promote` copies a vetted sandbox campaign into `campaigns/` with provenance and a **draft** collection — it never deploys.

Code: `src/cygnus/multi/` (runner, steps, scaffold, `archives/`, readers, systematics, `nss.py`). Tests: `tests/test_multi_archive_runner.py`, `tests/test_multi_cli.py`, `tests/test_multi_promote.py`, `tests/test_multi_verification.py`, `tests/test_archives.py`, `tests/test_tap.py`, `tests/test_systematics_nss.py`.

## Guarantees

- **The spec is the only source of parameters.** Steps read products, ephemerides, thresholds and grids from the spec; nothing campaign-specific is hard-coded.
- **Every step is a ledger run** (`cygnus.campaign:<id>:<step>`) opened with `Ledger.recorded_run`, so it always ends `completed`, `failed` (with the error) or `aborted`. Measurements go to the ledger with their method.
- **Resumable.** A step whose config hash (its params, the spec's shared blocks, upstream outputs, package version and a fingerprint of the campaign source files) matches a completed run with a saved output under `<outputs>/runner/` is reused.
- **Checksums.** Pinned products (`expected_sha256`) must match or the run fails; discovered products record the SHA-256 of their first retrieval.
- **Records cannot drift.** The sky record is regenerated from the spec's `record` block plus the checks the steps set. Checks no step touched stay as declared (usually `not_tested`).

## Steps

| Step | Does | Writes |
|---|---|---|
| `target_queue` | Ranked pool from the NASA Exoplanet Archive TOI table (`where`, `top`); formula and per-target rationale recorded | `target_queue.csv` |
| `fetch_products` | Finds products in scratch (`search_dirs`, `scratch:<subdir>`) or downloads them from MAST; verifies; registers new products | — |
| `residual_screen` | Negative excursions ≥ k robust-MAD, ≥ `min_cadences`, SAP and PDCSAP, several baselines; flags entries inside the known-signal `veto`. `k_mad: calibrated` uses `calibrate_screen`'s k* per light curve | `sectorNN/screen.json`, `normalized_series.csv` |
| `calibrate_screen` | Sign-flip null (brightenings, SAP∧PDCSAP) → k*, the smallest grid k with ≤ `max_null_events`; injection–recovery of box dips → completeness at the declared k and at k*, and the 90 %-completeness depth per duration | `sectorNN/calibration.json` |
| `known_signal_recovery` | Positive control: screen without veto at k*; the catalogued epoch(s) recovered if SAP and PDCSAP entries overlap ±(dur/2 + tolerance); in-transit depth measured | `runner/known_signal_recovery.json` |
| `period_aliases` | Persistent events matching the catalogued depth (0.5–2×) → periods ΔT/n; an alias is excluded when a predicted transit on usable data is absent. Raises the record to `lead` / *Unverified lead*, never higher | `period_aliases.json` |
| `bls_recovery` | Astropy BLS + permutation diagnostic on one light curve | `results.json` |
| `prior_art` | Cone search of NASA Exoplanet Archive, TESS TOI, VSX and SIMBAD around each target; dated results into the ledger `prior_art` table | — |

`k_mad: calibrated` falls back to the declared k, labelled UNCALIBRATED, for a light curve where no grid k meets the null limit. `residual_screen` groups overlapping entries into distinct events and marks those seen in SAP and PDCSAP at ≥ 2 baselines as persistent.

Vetoes: `kind: ephemeris` (period, T0, ±phase) or `kind: single_epoch` (±hours around each queued target's known transit).

Not built yet (designed in `ANALYSIS_STACK.md`): alternative detrending families, single-transit period posteriors, difference-image centroids, pointing/jitter correlation, ADS literature. Their checks stay `not_tested`.

## Campaigns

| Spec | State |
|---|---|
| `tess-wasp12-residual-01.yaml` | completed; calibrated (ledger runs #31–#34) |
| `wasp12-sector20-recovery.yaml` | completed (runs #35–#37) |
| `tess-mono-01.yaml` | draft parent spec; full declared 76-target queue built and all 76 targets completed/reviewed through the known-object loop on 2026-09-25 (see per-target campaigns and queue ledger) |
| `toi-2666-01.yaml` | completed (runs #73–#78; pilot of the known-object loop): catalogued transit recovered; repeat candidate in Sector 99, ΔT 1790.005 d, 52 aliases; **unverified lead**, reviewed |
| `toi-6666-01-nss.yaml` (`runner: cygnus.multi`) | completed 2026-09-25; Gaia DR3 NSS cross-match of the TOI-6666.01 host: no two-body solution (inconclusive); records the withdrawn ad-hoc SB2 attribution; reviewed |
| `toi-2666-01-nss.yaml` (`runner: cygnus.multi`) | completed 2026-09-25; Gaia DR3 NSS cross-match of the TOI-2666.01 host (HD 80133): no two-body solution, host RUWE 1.464 (inconclusive); reviewed |

## Verification record (2026-09-24)

- Equivalence with the original scripts on the real WASP-12 products: `normalized_series.csv` byte-identical in both sectors; all 835 and 464 screen entries identical; recovery `results.json` identical apart from its run timestamp (same seed 20260925).
- Ledger repair: ten `cygnus.ingest.tier1` runs left `open` by crashed processes were closed as `aborted` with an explanatory note (`python -m cygnus.cli close-stale-runs`); `tier1` now uses `recorded_run`.
- `python -m pytest -q`: 156 passed, 2 deselected at the time of this record; 188 after the 2026-09-25 audit fixes; **241 passed, 2 deselected** after the multi-archive runner merged into production (`src/cygnus/multi/`), plus 36 offline tests in the `experimental/` sandbox suite (run explicitly).

## Automation

`.github/workflows/ci.yml` runs the tests, validates every spec and builds the public site and the explorer on each push. `.github/workflows/scheduled-queue.yml` rebuilds the `tess-mono-01` queue weekly and cross-matches its top targets, using public services only, and uploads the result as an artifact; it never commits or publishes. `.github/workflows/network.yml` runs the `network`-marked tests weekly (and on demand) against the live public archives from a throwaway scratch root — an outage there is reported as inconclusive, never folded into the offline gate.
