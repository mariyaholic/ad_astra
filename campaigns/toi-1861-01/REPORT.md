<!-- cygnus:generated-draft -->
# Known-object test, TOI-1861.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1861-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #567, calibrate_screen #559, event_census #564, fetch_products #552, known_signal_recovery #560, moving_objects #566, period_aliases #565, prior_art #569, residual_screen #563, stellar_context #561, variability_guard #568
- Runner finished (UTC): 2026-09-26T10:10:10Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 93 threshold entries forming **35 distinct event(s)**, **5 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1861.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 323295479 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 130.80013 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -83.061258 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460782.962341 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8950.6397547 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 6.5036652 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.9486 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-08-13 16:00:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019112060037-s0011-0000000323295479-0143-s_lc.fits` | lightcurve | 11 | False | `28ab49c5484cd3f6` | True |
| `tess2019140104343-s0012-0000000323295479-0144-s_lc.fits` | lightcurve | 12 | False | `4c8256006a53e381` | True |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | lightcurve | 13 | False | `b89dd59a78e0485f` | True |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | lightcurve | 38 | False | `32f9861d16fa8aea` | True |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | lightcurve | 39 | False | `e35c392116f9d1c4` | True |
| `tess2023124020739-s0065-0000000323295479-0259-s_lc.fits` | lightcurve | 65 | False | `da2958cfa7bcd62b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019112060037-s0011-0000000323295479-0143-s_lc.fits` | — | epoch not in this light curve | — | — | 8951 | — |
| `tess2019140104343-s0012-0000000323295479-0144-s_lc.fits` | — | epoch not in this light curve | — | — | 8951 | — |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | — | epoch not in this light curve | — | — | 8951 | — |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | — | epoch not in this light curve | — | — | 8951 | — |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | — | epoch not in this light curve | — | — | 8951 | — |
| `tess2023124020739-s0065-0000000323295479-0259-s_lc.fits` | — | epoch not in this light curve | — | — | 8951 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019112060037-s0011-0000000323295479-0143-s_lc.fits` | 3 | False | 1h: 5000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019140104343-s0012-0000000323295479-0144-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023124020739-s0065-0000000323295479-0259-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019112060037-s0011-0000000323295479-0143-s_lc.fits` | 2458622.92238 | -0.00761 | 144 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459365.44089 | -0.00746 | 132 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459365.54228 | -0.00456 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019112060037-s0011-0000000323295479-0143-s_lc.fits` | 2458623.03418 | -0.00435 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459365.34644 | -0.00364 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459382.32559 | -0.00543 | 2 | SAP | 1, 2, 3 | no |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459380.29088 | -0.00543 | 2 | SAP | 1, 2, 3 | no |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 2459345.94350 | -0.00519 | 2 | SAP | 1, 2, 3 | no |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 2459346.00878 | -0.00508 | 2 | SAP | 1, 2, 3 | no |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459382.44781 | -0.00485 | 2 | SAP | 1, 2, 3 | no |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459382.36309 | -0.00482 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000323295479-0259-s_lc.fits` | 2460083.10714 | -0.00460 | 2 | SAP | 3 | no |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459387.65749 | -0.00441 | 2 | SAP | 1, 2, 3 | no |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 2459345.73933 | -0.00441 | 2 | SAP | 2, 3 | no |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459381.03393 | -0.00433 | 2 | SAP | 3 | no |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459381.88948 | -0.00406 | 2 | SAP | 3 | no |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 2459345.93517 | -0.00404 | 2 | SAP | 2, 3 | no |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459380.72282 | -0.00400 | 2 | SAP | 1, 2, 3 | no |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459381.95476 | -0.00397 | 2 | SAP | 3 | no |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 2459346.31295 | -0.00372 | 2 | SAP | 1, 2 | no |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | 2458657.10086 | -0.00371 | 2 | SAP | 1, 2, 3 | no |
| `tess2021146024351-s0039-0000000323295479-0210-s_lc.fits` | 2459365.53533 | -0.00369 | 2 | PDCSAP | 2, 3 | no |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 2459345.73516 | -0.00366 | 2 | SAP | 2, 3 | no |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 2459345.68794 | -0.00361 | 2 | SAP | 3 | no |
| `tess2019140104343-s0012-0000000323295479-0144-s_lc.fits` | 2458628.82034 | -0.00357 | 2 | SAP | 1 | no |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 2459345.93933 | -0.00348 | 2 | SAP | 3 | no |
| `tess2019140104343-s0012-0000000323295479-0144-s_lc.fits` | 2458643.71343 | -0.00343 | 2 | SAP | 2, 3 | no |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | 2458657.11475 | -0.00314 | 2 | SAP | 1, 2, 3 | no |
| `tess2021118034608-s0038-0000000323295479-0209-s_lc.fits` | 2459346.28517 | -0.00310 | 2 | SAP | 2 | no |
| `tess2019140104343-s0012-0000000323295479-0144-s_lc.fits` | 2458638.41343 | -0.00308 | 2 | SAP | 2, 3 | no |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | 2458661.47166 | -0.00286 | 2 | SAP | 1, 2, 3 | no |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | 2458658.24252 | -0.00284 | 2 | SAP | 1, 3 | no |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | 2458657.08281 | -0.00269 | 2 | SAP | 2 | no |
| `tess2019140104343-s0012-0000000323295479-0144-s_lc.fits` | 2458638.92038 | -0.00263 | 2 | PDCSAP | 1 | no |
| `tess2019169103026-s0013-0000000323295479-0146-s_lc.fits` | 2458657.22586 | -0.00251 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-1861.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:10:07Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:10:08Z: TOI-1861.01 (TIC 323295479, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:10:09Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:10:10Z: TOI-1861.01 (Pl?); CPD-82   282 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, ≤2.5, 3, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 30%, 60%, 100%, 40%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1861.01: Gaia DR3 5195197358981981824 at 0.00" (propagated 2016.0 → J2015.5; 0.03" unpropagated, proper-motion shift 0.04") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-1861.01: Teff 5463 K, R* 0.98 ± 0.08, M* 0.98 ± 0.10, ρ* 1.03 ± 0.27 ρ☉ (dwarf sequence, M_G 4.78, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-1861.01: 5 Gaia neighbour(s) within 52.5", contamination 0.39%; depth 8951 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 5 persistent event(s), 4 clean; BJD 2458622.9224 suspect: SAP_BKG z=-5.8 |
| Moving objects at screen-event epochs | inconclusive | 5 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-1861.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1861.01: CPD-82   282 otype PM* (star_or_other) at 1.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1861-01.yaml
python -m cygnus.multi report campaigns/toi-1861-01.yaml
```
