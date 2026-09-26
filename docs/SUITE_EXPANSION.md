# Suite expansion: unused adapter measures and the desired full suite

Draft 2026-09-26. Evidence: two read-only source inventories of the working tree (adapters/steps/vetting, and the pytest coverage surface), spot-checks of the load-bearing claims, and a same-day gate run: `python -m pytest -q` → **250 passed, 2 deselected (90 s)**. Line numbers follow the 2026-09-26 inventories and may drift after edits; claims marked ✓ were re-verified directly. **Status (2026-09-26, end of day): implemented — see §7 for the disposition of every item.** Sections 1–6 are kept as drafted (the pre-implementation inventory); the precondition (batch driver + MAST-hang fix) landed in `f7337b3`.

## 1. Baseline

Suite history: 156 (2026-09-24) → 188 (audit fixes) → 241 (multi runner merged) → 243 (`experimental/` retired) → **250** (batch driver; `docs/CAMPAIGNS.md`, § Verification record). The 2 deselected are the `network`-marked live-archive probes, run weekly by `network.yml`, never by the offline gate. "Tests" below means pytest contracts; "measures" means quantities the pipeline could compute and record.

## 2. Measures derivable from adapter data that nothing touches today

Every campaign fetches the context below; grep across `src/cygnus` confirms what is consumed. Nothing here is a discovery claim — these are *available, uncomputed* measures.

| # | Adapter fetch (source) | Consumed today | Unused / derivable measures |
|---|---|---|---|
| 1 | **Gaia cone** (`gaia` adapter): `_GAIA_COLS` = source_id, ra, dec, parallax, pmra, pmdec, G, bp_rp, ruwe, radial_velocity, non_single_star ✓ (`multi/archives/astronomy.py:138`) | positions + nearest row (identification), RUWE/NSS/parallax counts (`multi/source_checks.py:80-93`), min ΔG note | **(a)** Teff from G−BP−RP + parallax → R*/M* priors → a *transit-duration posterior per allowed alias* (the `period_aliases` step explicitly disclaims "no stellar density, no priors"), generalizing vet's stellar-density check, which is TOI-only today (needs `st_rad`/`st_logg`). **(b)** Epoch-propagated cross-match: `nearest_gaia_source` does no propagation from Gaia's 2016.0 epoch; a high-PM flag also separates nearby M dwarfs from background stars. **(c)** RV outliers → binary corroboration against the NSS mass function already computed (`multi/nss.py`). **(d)** Per-neighbour dilution budget from the whole fetched cone at 2.5-TESS-pixel radius — vet substitutes a *build-time* sky-explorer field CSV (`campaign/vet.py:247-267`); the fetched cone upgrades it to all campaigns. |
| 2 | **AllWISE** 4-band mags (`w1mpro…w4mpro`) (`astronomy.py:383-392`) | row count / nearest match | W1−W2 (dust/AGN/young-disk excess) and W2−W3 (giant-vs-dwarf) colour measures. Multi-epoch WISE variability needs a NEOWISE table no adapter fetches (capability gap). |
| 3 | **SkyView / Legacy Survey** cutouts (`readers.read_image`) | shape / finite-fraction / background sanity only (`multi/source_checks.py:97-118`); the reader returns no WCS ✓ (`multi/readers.py:259-273`) | Multi-band aperture photometry (survey list is already parameterized; DSS2 Blue is only the default) → B−V, g−r, UV excess → Teff/extinction priors; a TESS-pixel-scale blend census — a self-contained competitor to vet's Gaia-CSV test. *Requires adding WCS to `read_image`.* |
| 4 | **Solar-system contents** (`solar_system.py`) | record counts only; MPC OBS80 rows never read; SBDB JSON sanity-parse; AstDyS returns a reachability marker, not elements; SkyBoT rows consumed as counts (nearest-match reacts only to `ra`-family column names; `epoch_iso` never injected by any step) | **Moving-object veto at every screen-event BJD** — Horizons is fetched with `MAKE_EPHEM:'NO'` ✓ (`solar_system.py:51`) despite the declared `"ephemeris"` capability: flip it and query each event's epoch; SkyBoT (per-object motion at a chosen epoch) is the natural complement. A persistent repeat with no known object nearby *supports* (not proves) a non-asteroid explanation. |
| 5 | **MAST discovery narrowed** to 120-s SPOC LCs (`dataproduct_type:"timeseries"`, `provenance_name` SPOC, subgroup LC; `-s_lc.fits` required in the legacy path; TPFs fetched ad hoc inside vet) | SPOC LCs only | Kepler/K2/HLSP light curves are *spec-reachable today* (`collection=`/`provenance=` options are forwarded; the `kepler_lc` reader exists) → independent-instrument repetition tests of any event. `fits_image` products (Pan-STARRS/GALEX) would add colour leverage (row 3). TPF-based custom-aperture photometry (vet uses TPF pixels only for difference images). |
| 6 | **Per-cadence errors** (`flux_errs`, all readers) ✓ loaded, zero consumers in `src/cygnus` | nothing | Error-weighted depth/duration fits, χ² model comparison, and cross-validation of vet's least-squares covariance errors. |
| 7 | **Engineering series**: `POS_CORR1/2` are in no production reader (the `MOM_CENTR`/`POS_CORR` lookup in `multi/lightcurve.py:63-66` can never fire ✓); centroid medians recorded in screen.json but never checked; QUALITY bits decoded only in vet (`vet.py:46-49`) | SPOC: MOM_CENTR only | Step-level pointing/centroid-shift and bit-level artifact census for *every* screen event (no GPU needed; arrays already stored in `normalized_series.csv`). |
| 8 | **VizieR/VSX** `SELECT *` rows (`astronomy.py:246-258`) | positions (≤5″ nearest match); first 10 column names | Variable type/period *collision* test (a catalogued eclipsing/rotational variable at the offset mirrors or falsifies a screen event). Any other VizieR table already supported via the `table` option. |
| 9 | **SIMBAD / NED** `otype`, `prefphytype` fetched | positions | Class-based artifact guard: known CV/giant/LPV at the target, galaxy-vs-star discrimination. (Prior-art gate's own SIMBAD fetch already uses `otype` — different path.) |
| 10 | **ESO** ObsCore rows (incl. spectroscopy via DATALINK) | metadata only; no spectral reader exists | Archival RV series (ESPRESSO/HARPS-class) → unseen-companion mass-function bounds, complementing Gaia NSS. A reader build, not a tweak. |
| 11 | **exoarchive** TOI/pscomppars rows (`pl_trandep`, `pl_trandurh`, `pl_tranmid`, `pl_orbper`, `st_tmag`) | positional tables only | Auto-populate `veto`/`known_signal_recovery`/alias inputs from fetched rows (the same values are re-fetched independently in vet, targets scoring and scaffolding). |
| 12 | **ZTF** VOTables (MAG + errors + catflags, MJD-UTC caveat recorded) | gated out of screens at <100 usable cadences or median cadence >1800 s (`multi/steps.py:265-297`) | Independent-epoch/independent-instrument single-epoch depth check at each screen event (the MAG→relative-flux path already exists, `multi/lightcurve.py:47-54`); ZTF-baseline variability flags. |
| 13 | Hygiene | `Target.mag` never used; `ProductRef.size_bytes` never set (→ pre-download size gating); SkyView `fetch` reads `extra["position"]` that `discover()` never sets; `results.json`'s `TSTART/TSTOP` dead in multi outputs for non-SPOC products; `SAP_BKG` consumed only by vet | — |

Fully consumed (do not re-inventory): the SPOC core columns (TIME/SAP/PDCSAP/QUALITY/MOM_CENTR), Gaia cone positions for identification, checksum/coverage-order provenance, the red-noise/significance mathematics, and the earth-obs/observing adapters (no-op status products by design).

## 3. Production code no test exercises (working tree)

Audit legend: **NONE** = no test reaches it; **PARTIAL** = a neighbouring path or campaign-twin only; **unasserted** = executed inside integration runs but nothing would fail if it broke.

- **Whole multi steps untested:** `step_bls_recovery` (BLS + permutation FAP, `sap_at_pdc_ephemeris`, refusal branch), `step_period_aliases` (repeat matching, alias exclusion, `flag_lead`), `step_prior_art` wrapper, `step_target_queue` writer. Only the *campaign twins* are tested — and the twins are demonstrably not identical (`_excluded` exists only in the campaign copy; 759 vs 1,166 lines), so twin-tested claims need a diff (F1).
- **multi `residual_screen`/calibration branches:** `k_mad: calibrated` (missing-calibrate RuntimeError, k\* use, UNCALIBRATED fallback), ephemeris-veto branch of `_veto_mask`, the calibrated-threshold checks, systematics-model failure fallback, screen-suitability gates (sparse/short fixtures don't exist), SPOC empty-discovery path, multi checksum-mismatch refusal and expected-bytes validation, `from_queue` fetch branch, the `MAST_DOWNLOAD` seam.
- **`campaign/vet.py` — the most safety-critical gap:** only ~5 of ~20 helpers have tests (`box_fit`, `ephemeris_hits`, `data_aliases`, `cluster`, `max_central_duration_h`). The entire orchestrator `vet()` and with it the twelve event checks — shape-vs-reference, box-fit significance, sibling-TOI ephemerides, detrending alternatives, red-noise significance, background/centroid/pointing, quality census, Gaia blend cap, **difference-image centroid**, **common mode**, **stellar-density alias limit**, **secondary eclipse** — plus `plot`/`summary_md` and the CLI wiring have **zero** coverage.
- **Adapters never probed at all:** SkyView, SIMBAD discover, ESO, IRSA (incl. ZTF-CGI fetch), Legacy Survey, exoarchive (all three modes), SBDB, AstDyS, SkyBoT (filled-rows / missing-epoch / ImportError branches), Earthdata/Copernicus fetch, Skynet. MAST is partial (the quality-flags source check never runs on a real SPOC product; product-list filtering and `_fmt_for` non-TESS branches untouched).
- **`archives/base.py` seams:** default `fetch`/`fetch_to_file` network path, `read()`, `text` check dispatch, `tap_csv` TAP-error-body detection, `register()` instance form, `all_adapters()`, `kind_for_format` fallback.
- **`systematics`:** early-return matrix (too few points, span too short, <30 nulls, non-positive scale), `product_summary`'s cadence-count duration fallback.
- **`source_checks` branches:** `text_checks` (nothing), table failure/empty/no-coords/>5″ branches, constant-image branch, `lightcurve_checks` TIMESYS/BJDREF branches, `json_checks` required-keys, the never-asserted Gaia parallax check.
- **`runner`:** full `load_spec` validation matrix for the multi copy (campaign twin tested), step-reuse/`--force`, `--until`, `Context.flag_lead`, NAME_RESOLUTIONS targets, record draft/plots blocks, TIC `product_dir` branch, `code_fingerprint` invalidation.
- **`batch.py`:** `cmd_queue`, `cmd_status`, `main` dispatch, `--spec`/`--redo`/`--jobs>1`, the report-subprocess step, the rest of the TRANSIENT keyword matrix, corrupt-payload/cross-host lock branches, the `cygnus.campaign:` arm of `close_orphan_runs`; unasserted: claim commit message, journal start/end events.
- **Two health items to check before trusting surrounding tests** ✓: `tests/test_multi_cli.py:12` sets `REPO_ROOT` to `Path(__file__).resolve().parents[2]`, which resolves to `D:\`, not this repo — its "nothing leaked into the production tree" assertions inspect `D:\campaigns`; and the working-tree `campaign` vs `multi` step twins differ visibly (drift audit, F1). Also the multi `Product integrity` check and all multi `ctx.measure` writes run unasserted inside integration tests.

## 4. The desired full suite, expanded

Layer definitions inherited from `docs/TEST_ARCHITECTURE_PLAN_DRAFT.md` §3: **L0** fast offline units/fakes; **L1** seeded synthetic scientific calibration; **L2** checksum-pinned archival replay (no implicit downloads); **L3** opt-in live `network` probes.

### 4.1 L0 — close today's untested-code gaps

1. `multi` step tests mirroring the campaign twins' guarantees, *plus* their multi-only features: `bls_recovery` end-to-end (planted dip → grid/power/FAP; cross-flux sap-at-PDC flag; refusal on too-few cadences), `period_aliases` (planted repeat → `flag_lead` + record `lead`; alias exclusion math), `prior_art` wrapper (fake `catalogue_audit`: outage ⇒ inconclusive preserved in the record), `target_queue` CSV write.
2. Branch-matrix tests: multi `_threshold` (three branches), `_veto_mask` ephemeris + unknown-kind, calibrated checks, suitability gates (sparse fixture, short fixture), SPOC empty discovery, multi checksum refusal, `from_queue`, systematics-model error fallback.
3. Adapter tests via the injectable `http` seam — one discover+fetch contract per never-probed adapter (SkyView non-FITS refusal; empty/positional branches; exoarchive's three modes; SkyBoT **filled rows** and missing-epoch refusal; MPC OBS_DF/XML columns; MAST quality-flags check on a synthetic SPOC product), plus the `base.py` seams list above.
4. `source_checks` branch matrix (text/table/image/curve/json edges listed in §3).
5. `systematics` early-return matrix + duration fallback.
6. `runner` validation matrix for multi `load_spec` (mirror the campaign twin's cases), reuse/`--force`, `--until`, `flag_lead`, NAME_RESOLUTIONS and draft-record blocks.
7. `batch.py` module tests: `cmd_queue` (spec generated / existing-id refusal), `cmd_status`, argparse dispatch, parallel `--jobs` with two fake subprocesses, `--redo`/`--spec`, the report step, the full TRANSIENT keyword matrix, corrupt/cross-host lock branches, orphan-close campaign arm.
8. **`vet.py` suite** (highest value): synthetic SPOC FITS + synthetic TPFs (constructed, checksummed fixtures); unit tests for `alt_depths`, `empirical`, `quality_near`, `gaia_neighbours`, `tpf_for`/`difference_image`, `neighbour_lcs`; then an orchestrator smoke over a planted `vetting.json` candidate: *clean null* vs *planted contamination* fixtures — acceptance: every one of the twelve checks reachable, clean null passes every artifact test, contamination fails the specific one. Plot/summary functions must run without matplotlib-interactive assertions.
9. Health fixes inside tests: correct the `REPO_ROOT` resolution; assert the multi `Product integrity` check and measure writes in the existing integration tests.

### 4.2 L0 — new measures (each lands with its own test, from §2)

Ranked by leverage; each names the record check it would add and its prerequisite:

1. **Stellar priors from the Gaia cone** → check `Stellar priors (Gaia colour and parallax)`; test: colour→Teff curve on synthetic fields, parallax→R*/M*.
2. **Duration posterior per alias** → extends `Period aliases (repeat events)` with a posterior field; test: posterior units on injected companions; *removes* the step's stated non-posterior disclaimer where the data allow.
3. **Moving-object veto** → check `Moving objects at screen-event epochs`; prerequisite: flip Horizons `MAKE_EPHEM` and inject `epoch_iso` into the SkyBoT call; test: planted asteroid rows at event epochs veto; stationary far-field does not.
4. **In-campaign blend/dilution census** → upgades vet's `Gaia neighbours able to mimic the depth` from a build-time CSV to the fetched cone; test: synthetic cone → dilution cap math.
5. **Independent-instrument repetition (Kepler/K2/HLSP)** → check `Independent repetition (other MAST collections)`; test: spec-reachable today, no adapter change.
6. **Independent-epoch depth confirmations (ZTF)** → check `Independent-epoch confirmation (ZTF)`; test: single-epoch MAG measurement + catflags handling.
7. **Error-weighted box fits** → replaces vet's unweighted covariance errors; test: χ² coverage and cross-validation vs `PDCSAP_FLUX_ERR`.
8. **Step-level artifact census** (quality bits, background, centroid/pointing shifts) → check `Pointing and quality census per event`; test: planted momentum-dump spikes detected.
9. **Variable-catalogue collision (VSX)** and **SIMBAD/NED class guard** → checks at the target offset; test: synthetic rows with/without matching types/periods.
10. **Multi-band cutout colours** (prerequisite: WCS in `read_image`) → colour measure + writers in `context.json`; test: synthetic multi-band images with planted PSFs.
11. **Epoch-propagated Gaia cross-match** (TESS epoch minus 2016.0 × PM) → identification robustness test.
12. **ESO RV reader + mass-function bounds** → new reader; L0 unit test on a synthetic HARPS-line-list file.

### 4.3 L1 — synthetic scientific calibration (seeded, slower; `slow`-marked)

- Full-path injection–recovery through screen → falsification under red noise: uniform null p for `parametric_z`/`parametric_p`, empirical coverage of the FAPs, per-duration completeness floors on grid fixtures.
- Calibration for measures 1–3 of §4.2: colour→Teff posteriors with injected bias; moving-object false-veto rate for stationary background sources; dilution-cap closure vs planted blends.
- Secondary-eclipse false-positive rate on red-noise-only nulls (vet's phase-0.5 search with measured red-noise errors), and alias-duration-limit calibration.

### 4.4 L2 — checksum-pinned replay

- A pinned replay of a sampled subset of the regenerated 76+2 records: runner output hashes (e.g. the 0-old-key invariant ✓ re-checked) catch reader/runner drift semantically.
- The WASP-12-style checksummed archival control through the multi path per release.

### 4.5 L3 — live probes (weekly `network` lane; never the offline gate)

- Extend `python -m cygnus.multi archives --check <name>` coverage to all 23 adapters with service-aware statuses (outage ⇒ inconclusive, listed; never failed).
- Live SkyBoT filled-epoch probe, MPC OBS80 parse probe, exoarchive TOI probe, IRSA ZTF probe.

## 5. Sequencing proposal

| Phase | Work | Acceptance |
|---|---|---|
| F0 | Commit the uncommitted MAST-hang fix and batch driver; then the count becomes a clean `250 passed, 2 deselected` at HEAD | `git status` clean of in-scope files; gate green twice |
| F1 | Health: diff the campaign/multi step twins (consolidate shared primitives or add an equivalence guard test); fix `REPO_ROOT` in `test_multi_cli.py` | documented diff report; regression test green |
| F2 | L0 §4.1 items 1–3, 8 (vet suite) — the safety-critical majority | every NONE/PARTIAL item in §3 has a named test or an explicitly accepted disposition |
| F3 | L0 §4.1 remainder (branches, runner, batch, source checks) | same |
| F4 | New measures L0 batches (§4.2), 2–4 at a time, each with its record check | records + `docs` updated; `pytest` green |
| F5 | L1 calibration for the landed measures; L2 replay; L3 probes | calibration numbers recorded in the suite doc; weekly lane green/inconclusive |

CI caveat carried from `docs/STATUS.md`: the GitHub `ci` lane has never been green; expanding the suite locally does not fix that. A green local gate and the eventual CI JUnit diagnosis are separate gates, not one.

## 6. Non-goals

Inherited from the test-architecture plan: no whole-sky or completeness claim from any of this; no real network in the offline gate; no test raised for bookkeeping reasons (snapshot duplication, private call order); passing units do not certify detection significance, novel objects, or archive uptime. Implementation of §4 belongs to explicit user-approved rounds.

## 7. Disposition (2026-09-26)

Worked through F1–F5 in one round (user instruction: "work through the entire suite expansion up to your own discretion"). Gate at the end of the round: `python -m pytest -q` → **590 passed, 37 deselected (93 s)**; the 37 are the three opt-in lanes, 26 `network` + 7 `slow` + 4 `replay` (627 collected). Numbers below are from runs on this machine the same day; nothing is quoted from the draft above.

### 7.1 Bugs the new tests found (all fixed in the same round)

| # | Where | Defect | Fix |
|---|---|---|---|
| 1 | `tests/test_multi_cli.py` | `REPO_ROOT = parents[2]` resolved to `D:\`: the no-leak assertions inspected the wrong tree | `parents[1]` |
| 2 | `multi/steps.py` vs `campaign/steps.py` | multi crashed on a target whose archive answered with no product; the twin records the documented exclusion | exclusion ported (`_excluded`, outcome `pipeline_check`, checks `not_tested`); an outage or misconfiguration still **fails** (retryable). Guarded by `tests/test_twin_equivalence.py` |
| 3 | both twins, `period_aliases` | alias-coverage exclusion hard-coded a 120 s cadence (wrong for 20 s / 200 s / 600 s / 1800 s products) | cadence measured per product |
| 4 | SkyView adapter | `discover()` never set `extra["position"]`; the FITS guard accepted four null bytes | position set; guard is `startswith(b"SIMPLE")` |
| 5 | SkyBoT / context adapters | `fetch()` wrote an empty file | rows written as CSV |
| 6 | MPC adapter | observation count counted XML *characters* | counts elements / OBS80 lines; `output_format` option |
| 7 | MAST adapter | "fast" filter matched anywhere in the URL path | file name only; `size_bytes` now filled (enables the new `max_product_bytes` gate) |
| 8 | `archives/base.py` `tap_csv` | accepted empty, HTML and `ERROR`/`FATAL` text bodies as a table | raises |
| 9 | `multi/runner.py` `load_spec` | ordering holes: calibrated k without a prior `calibrate_screen` (incl. `known_signal_recovery`'s calibrated default), `target_queue` after `fetch_products` | rejected at load time |
| 10 | ESO adapter | spectra/cubes typed as light curves | typed by `dataproduct_type` |
| 11 | `multi/lightcurve.py` | centroid lookup was dead code (no reader exposed `MOM_CENTR`/`POS_CORR`) | readers carry `LightCurve.engineering` |
| 12 | `campaign/vet.py` difference image | a large but *insignificant* offset was recorded `passed` | `passed` only below 0.25 px; otherwise `inconclusive`. Changes two committed readings — erratum in `campaigns/tess-mono-01/LEAD_VETTING_LOG.md` (both leads were already rejected on other grounds) |
| 13 | Legacy Survey adapter | sent `size` as float arcsec → HTTP 500 (found by the L3 probe) | integer pixels + `pixscale` |
| 14 | Gaia adapter | `parallax_error` not fetched (found by live validation) | added to `_GAIA_COLS` |
| 15 | multi `fetch_products` note | "No light-curve product was retrieved" written even when some were | conditional |

### 7.2 §3 / §4.1 (L0 gaps): every item has a named test file

| Draft item | Tests |
|---|---|
| multi steps (`bls_recovery`, `period_aliases`, `prior_art`, `target_queue`) | `tests/test_multi_steps.py` (12) |
| multi branch matrix (thresholds, vetoes, calibrated checks, suitability gates, empty discovery, checksum refusal, `from_queue`, systematics fallback) | `tests/test_multi_branches.py` (14) |
| adapters never probed + `base.py` seams | `tests/test_adapter_contracts.py` (71), `tests/test_archive_base.py` (36) |
| `source_checks` branches | `tests/test_source_checks_branches.py` (29) |
| `systematics` early returns + duration fallback | `tests/test_systematics_branches.py` (20) |
| multi `load_spec` matrix, reuse/`--force`, `--until`, `flag_lead`, NAME_RESOLUTIONS, record blocks | `tests/test_multi_runner.py` (37) |
| `batch.py` (queue, status, dispatch, `--jobs`, `--redo`, report step, TRANSIENT matrix, locks, orphan close) | `tests/test_batch_more.py` (37) |
| **vet suite**: helpers, synthetic SPOC + TPF fixtures, orchestrator over a clean null and planted contamination (every check reachable; the clean null passes every artifact test; each contamination fails its specific check; outages inconclusive) | `tests/test_vet_suite.py` (29) |
| F1 twin drift | `tests/test_twin_equivalence.py` (3): same science on both runners for the same products; same exclusion; outage = failure on both. The twins stay separate modules (consolidation is a refactor, not a test gap) |

### 7.3 §4.2 new measures: landed as steps with record checks

Pure functions in `src/cygnus/multi/measures.py`, steps in `src/cygnus/multi/measure_steps.py`, unit and end-to-end tests (fake adapters) in `tests/test_measures.py` (47). Generated specs (`multi/scaffold.py`) now include every step below; `rv_bounds` only when the spec's archives include `eso`.

| # | Measure | Step → record check | Notes |
|---|---|---|---|
| 1 | Stellar priors | `stellar_context` → `Stellar priors (Gaia colour and parallax)` | Mamajek mean-dwarf table v2022.04.16 vendored (`multi/data/`, 63 rows B9V–M9.5V; sha256 and retrieval date in the file header and `DATA_SOURCES.md`). Refuses parallax/error < 5 and > 1 mag off the dwarf sequence; RUWE > 1.4 → inconclusive. Colour interpolation stops at M8.5V (Bp−Rp turns over) |
| 2 | Duration likelihood per alias | `period_aliases` gains `duration_likelihood` when `stellar_context` ran | Seager & Mallén-Ornelas eq. 3, circular orbits, b ~ U(0,1); weights with and without the P^−2/3 transit probability. A likelihood, not a posterior over companions |
| 3 | Moving-object veto | `moving_objects` → `Moving objects at screen-event epochs` | SkyBoT per event epoch, geocentre, 600″; partial answers → inconclusive. Horizons adapter gained `epochs_jd`/`center` (MAKE_EPHEM) |
| 4 | Blend/dilution census | `stellar_context` → `Blend and dilution census (Gaia DR3 cone)` | from the fetched cone at 2.5 TESS px; vet's build-time CSV test is unchanged |
| 5 | Independent repetition | `alias_cross_instrument` → `Independent repetition (other MAST collections)` | depths at predicted alias epochs |
| 6 | ZTF independent epochs | same step → `Independent-epoch confirmation (ZTF)` | |
| 7 | Error-weighted box fit | vet event check `Error-weighted box fit` | passed if weighted and unweighted depths agree within 2σ and scatter/quoted error ∈ [0.7, 1.5]; not_tested without an error column |
| 8 | Artifact census per event | `event_census` → `Pointing and quality census per event` | quality bits in-event vs nearby (nearby only → inconclusive, matching vet); pointing/centroid shifts |
| 9 | VSX collision, SIMBAD class guard | `variability_guard` → `Variable-catalogue collision (VSX)`, `Object-class guard (SIMBAD)` | a failed guard escalates in `batch` triage (`CHECK_GUARDS`) |
| 10 | Cutout photometry | `context_products` measure `cutout_aperture_mag` | `read_image` now returns WCS |
| 11 | Epoch-propagated Gaia match | `stellar_context` → `Target-to-Gaia identification (proper motion propagated)` | Gaia epoch 2016.0 → observation epoch |
| 12 | ESO RV reader + bounds | `rv_bounds` → `Stellar-companion exclusion (archival RVs)` | `readers.read_rv`: CSV or ESO DRS/QC CCF keywords; sinusoid fit per alias; mass-function upper bound by bisection |

Also landed: a `max_product_bytes` pre-download size gate.

**Not implemented (deferred; no test gap created):** AllWISE W1−W2/W2−W3 colours (§2 row 2) and NEOWISE variability (no adapter); a NED class guard (SIMBAD only); auto-populating veto/alias inputs from exoarchive rows (row 11); Gaia `radial_velocity` outliers vs NSS (row 1c); TPF custom-aperture photometry (row 5); hygiene items `Target.mag` and non-SPOC `TSTART/TSTOP`.

### 7.4 L1: `pytest -o addopts= -m slow` (`tests/test_calibration_l1.py`, 7 tests, seeded)

| Calibration | Result |
|---|---|
| Null significance (n = 150 red-noise nulls) | empirical p uniform: KS D = 0.071 (critical 0.111); P(p_emp ≤ 0.05) = 0.073; P(p_param ≤ 0.05) = 0.067; P(p_param ≤ 0.01) = 0.013 |
| Held-out false alarms (k* from one half, applied to the other) | 24 light curves, median k* = 3.5, false-alarm fraction 0.04 |
| Completeness at k = 5, σ = 1000 ppm per cadence | depth 1000/2000/3000/5000/8000 ppm → 1 h: 0/0/0/0.75/1.00; 2 h: 0/0/0/0.92/1.00; 4 h: 0/0/0/0.83/1.00 |
| Dwarf priors | 400/400 usable; R within 1σ for 0.90; 0.3 mag unmodelled extinction biases R by −6.9 % |
| Duration likelihood | true alias ranked first in 0.41 of draws (chance ≈ 0.14); median weight on the truth 0.22 |
| Dilution-cap closure | max observed/cap = 0.9980 (cap never exceeded) |
| Secondary-eclipse false positives | 0.000 over 40 red-noise nulls × 10 aliases |

Not calibrated: the moving-object false-veto rate (needs a SkyBoT-shaped sky model or live queries; deferred).

### 7.5 L2: `pytest -o addopts= -m replay` (`tests/test_replay_l2.py`)

Committed campaigns toi-2666-01, toi-1301-02, toi-125-04 and toi-2003-01 replay from checksum-verified scratch copies (never downloading) to identical screen, calibration, known-signal and alias outputs: 4/4 in 36 s. Mutation check: re-running with seed+1 is detected as drift. Campaigns whose products are not in local scratch skip with the reason. A separate WASP-12 control replay (§4.4) was not added; the equivalence record in `docs/CAMPAIGNS.md` already covers it.

### 7.6 L3: `python -m cygnus.multi archives --check all` and `tests/test_live_probes.py`

Known-answer probes (`src/cygnus/multi/probes.py`) for 24 probe names (23 adapters + IRSA's ZTF mode); positions come from a committed spec or live Horizons, never typed in. Statuses: `ok` / `empty` / `unavailable` (outage → skip, inconclusive) / `error` (fails). The CLI exits 1 only on `error`. The weekly lane (`network.yml`) picks the test file up through the `network` marker.

Final run 2026-09-26: **19 ok, 5 unavailable, 0 empty, 0 error** (275 s). Unavailable: `eso` (TAP read timeout at 120 s on every attempt that day); `asf`, `usgs`, `firms`, `worldview` (account-only or browser-only by design). `irsa-ztf` timed out on two earlier attempts and answered on the final one.

### 7.7 Live validation of the new steps (sandbox; nothing committed from it)

- **TOI-2666.01:** identification passed (0.00″ after propagation); priors inconclusive (RUWE 1.464); blend passed (0.38 % contamination); the census marks lead event E1 (BJD_TDB 2461049.1644) *caution* (Argabrightening flag within ±0.25 d, consistent with vet's inconclusive quality check) and the other two events suspect (pointing shifts); SkyBoT: nothing bright enough; VSX: no entry; SIMBAD: HD 80133, PM*.
- **TOI-3500.02:** priors Teff 5311 K, R 0.95 ± 0.08 R☉, M 0.97 ± 0.10 M☉, ρ 1.14 ± 0.30 ρ☉; blend inconclusive (neighbour at 3.7″, ΔG 2.72, able to mimic the depth, independently matching the lead vetting log); duration likelihood peaks near 100 d and 77.8 d; 4 of 21 SkyBoT epochs returned a server-side SIGBUS (recorded unanswered → inconclusive).

### 7.8 What remains open (user decisions; see `docs/STATUS.md`)

- The code fingerprint changed, so every committed campaign would recompute on its next run; the 78 records were **not** regenerated with the new steps in this round.
- The difference-image rule change alters two past readings (erratum logged; conclusions unchanged).
- The GitHub `ci` lane is still not green; this round is a local gate only.

§6 non-goals stand unchanged.
