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
- **Product kinds.** Products carry `kind` (`lightcurve`/`image`/`table`/`text`); only time series are screened. A single-channel product is screened once (`channel_mode: single`) against a red-noise systematics model (`cygnus.multi.systematics.py`) instead of the false SAP-vs-PDCSAP independence claim. Each event reports `robust_z` / `parametric_z` (the same value: the z of the event's box statistic against random epochs of the same light curve, whose spread already contains the red noise), the Gaussian-tail `parametric_p`, the empirical p and both trial-corrected FAPs. `rednoise_inflation` (sqrt(tau/cadence)) is reported as a diagnostic and **not applied** (`rednoise_inflation_applied: false`); the field was called `parametric_z_rednoise_inflated` before 2026-09-26, and records written before then still carry that name until they are regenerated.
- **Catalogue-only steps.** `context_products` (what was fetched), `source_checks` (per-product integrity; Gaia RUWE and `non_single_star` flags; MAST quality census; MPC observations via `data.minorplanetcenter.net`) and `astrometric_vetting` (Gaia DR3 NSS two-body cross-match of the target, mass function where a significant solution exists) answer questions without light curves; a campaign with no light-curve product is a recorded null, not a red run.

Runs go to the production ledger under the `cygnus_multi:` script namespace. Setting `CYGNUS_MULTI_ROOT` (any directory outside the worktree) confines specs, outputs **and ledger** to a sandbox root instead; `python -m cygnus.multi.promote --root <sandbox> --campaign <id>` (or with `CYGNUS_MULTI_ROOT` set) copies a vetted sandbox campaign into `campaigns/<id>/` of this checkout with provenance and a **draft** collection — it never deploys, and refuses when no sandbox root is given or the root is the worktree itself. The former `experimental/` safe copy was retired on 2026-09-26 (see `docs/STATUS.md`); its tests had already been mirrored in `tests/`.

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
| `event_null` | **T2 tool.** For each repeat candidate: re-measure the event depth (joint polynomial + box), then k/N empirical null at random event-free centres and injection–recovery at the event depth. Uncovered windows are excluded from N, never counted as misses. Checks `Event-epoch null exceedance (k/N)` (passed only with N ≥ 100 and k/N ≤ 5%) and `Event-depth injection-recovery` | `event_null.json` |
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
- `python -m pytest -q`: 156 passed, 2 deselected at the time of this record; 188 after the 2026-09-25 audit fixes; **241 passed, 2 deselected** after the multi-archive runner merged into production (`src/cygnus/multi/`); **243 passed, 2 deselected** on 2026-09-26 after `experimental/` was retired (its separate 36-test suite no longer exists; every one of those tests has a counterpart in `tests/`). The batch-driver additions of the same day made it **254 passed, 2 deselected**; after the suite expansion (`docs/SUITE_EXPANSION.md` §7) the offline gate is **590 passed, 37 deselected** (93 s), the 37 being the opt-in `network` (26), `slow` (7) and `replay` (4) lanes.

## Automation

`.github/workflows/ci.yml` runs the tests, validates every spec and builds the public site and the explorer on each push. `.github/workflows/scheduled-queue.yml` rebuilds the `tess-mono-01` queue weekly and cross-matches its top targets, using public services only, and uploads the result as an artifact; it never commits or publishes. `.github/workflows/network.yml` runs the `network`-marked tests weekly (and on demand) against the live public archives from a throwaway scratch root — an outage there is reported as inconclusive, never folded into the offline gate.

## Event-time prior-art and source-record gate (2026-09-27)

TOI-6695.01 exposed a queue/provenance failure: a periodic TOI row lost `pl_orbper` in the ranked CSV, creating a single-epoch veto, and a 30-arcsec cone search found the confirmed host planet without comparing event times. The S34/S61 events are TOI-6695 b (see `campaigns/toi-6695-01/REJECTION.md`).

New queue claims refresh the exact TOI/TIC row and carry period, query, archive update and retrieval UTC into the spec. `prior_art` retrieves ephemerides and screens each repeat event against published epochs; any overlap requires a primary-paper and TTV review. The screen is deliberately broad and its absence is inconclusive. Agent review and source-record reconciliation are specified in `docs/AGENT_RUNBOOK.md`; a runner `lead` remains an unverified screening outcome until that review.

## Native lead-resolution tools (2026-09-30)

Ported from the hand-written `reports/lead-resolution-2026-09-30/resolve_leads.py` (inventory: `docs/NATIVE_SUPPORT_GAPS_2026-09-30.md`). Tests: `tests/test_native_lead_tools.py`.

| Need | Module |
|---|---|
| Atomic JSON/text writes with input-hash linkage; `archive_previous` history files | `cygnus.fileio` |
| Predicted-epoch box measurement (uncovered ≠ null), k/N nulls, injection recovery, alias coverage (`untested` unless a covered window is empty) | `cygnus.analysis.events` |
| TESS PRF sampling, source preference over registration × model floors (a flip is *inconclusive*) | `cygnus.analysis.prf` |
| Block-bootstrap centroid offset; never returns *passed* | `cygnus.analysis.localize` |
| Transit-tied RV orbit fits (km/s), RV–FWHM correlation | `cygnus.analysis.rv` |
| Log-λ shifts, gap-aware mask CCFs, `precision_gate` / `require_gate` (10 m/s default) | `cygnus.analysis.spectra` |
| Barycentric-correction audit (delta only, never applied) | `cygnus.analysis.timing` |
| Access states (`ok/http_401/timeout/...`), capped streaming, gzip/TAR sniffing | `cygnus.ingest.access` |
| ESO exact-name (`names=[...]`), KOA HIRES TAP, Gaia exact-source RV/NSS row | `cygnus.multi.archives` (`eso`, `koa`, `spectroscopy.gaia_exact_source`) |
| Footers, drift checks, ppm/radius/null-count/centroid/event-time gate helpers, per-paper prior-art rows | `python -m cygnus.campaign reconcile <id> --note … [--superseded-by … --candidate-id …]`, `cygnus.campaign.reconcile` |

Not yet native: PRF/TESScut *fetching*, HARPS/FEROS bundle parsing, KOA raw/calibration download, spec-driven campaign steps wrapping these primitives. `resolve_leads.py` is unchanged and still the frozen record of this campaign.

## Tier gating (2026-09-30)

Not every target gets the full suite. `python -m cygnus.campaign tier <id>` (or `tier --all`, campaign records only) derives the tier a target has earned from its sky record (`src/cygnus/campaign/tiers.py`), reviewed by the Opus adviser the same day:

- **T0** screen (all targets, light) → **T1** triage (persistent repeat event) → **T2** vet (pixel/FFI localization) → **T3** discriminate (PRF, archive spectra, RV; heavy) → **T4** confirm (spectral extraction behind the precision gate; user go-ahead). **closed** on decisive evidence.
- **T1→T2:** aliases run; catalogue cross-match passed; an *event-time comparison vs published ephemerides* recorded (position-only never clears); null and moving-object checks run.
- **T2→T3:** localization *passed on every defining event* (events listed in the record's `rejected_events` are set aside) and no other localization check failed; blend census passed; calibrated null passed; **event-epoch null exceedance (k/N) passed** (`event_null` step, a T2 tool); the spec supplies `budget` and `discriminating_question`.
- **T3→T4:** **event-depth injection-recovery passed** (same `event_null` step); an independent-sky check passed (a second reduction of the same pixels is not independent) and evidence ≥ Vetted candidate.
- **closed:** event identified as a known signal, VSX collision or ephemeris collision failed, every localized event rejected, `REJECTION.md` present, or abandoned. A failed pointing census demotes events; it does not close a target.
- Every check name in a campaign record must map to a role in `tiers.GATE_CHECKS` (a test fails on an unmapped name).
- **Enforcement:** the runner skips a step listed in `tiers.STEP_TIER` (recorded as a `not_tested` check) unless the target earned that tier in the spec's `parent_record` (or its own record); `campaign vet` needs T2. Overrides are explicit: spec `tier_override: {tier, reason, approved_by, date}` (T4 needs `approved_by`), or `vet --tier-override REASON`.
- **Current:** T0 1072, T2 3 (toi-224-01, toi-2666-01, toi-3500-02; none has run `event_null` yet, and 2666's other T3 gates are met), closed 6 (incl. toi-6695-01, toi-7610-01). The test suite is the software gate and is not run per target.
