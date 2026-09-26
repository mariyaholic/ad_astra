<!-- cygnus:generated-draft -->
# Known-object test, TOI-5149.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5149-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #386, calibrate_screen #356, event_census #369, fetch_products #349, known_signal_recovery #359, moving_objects #382, period_aliases #370, prior_art #388, residual_screen #368, stellar_context #360, variability_guard #387
- Runner finished (UTC): 2026-09-26T10:05:12Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5149.01 (BJD 2459814.8734: recovered, depth 9324 ± 87 ppm (catalogue 11053 ppm)).
Outside the catalogued epoch the screen left 122 threshold entries forming **33 distinct event(s)**, **12 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459431.6755 matches the catalogued transit's depth (9320 vs 9324 ppm), 383.197 d later; 7 of 383 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5149.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 286094277 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 310.458865 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 48.028314 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459814.873357 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 11052.8460427 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 9.708321 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.4815 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-11-01 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | lightcurve | 55 | True | `c5f1220d7424c632` | True |
| `tess2021204101404-s0041-0000000286094277-0212-s_lc.fits` | lightcurve | 41 | False | `e489bdd83b8ca63c` | True |
| `tess2022244194134-s0056-0000000286094277-0243-s_lc.fits` | lightcurve | 56 | False | `ac825e1b36baa5e0` | True |
| `tess2024030031500-s0075-0000000286094277-0270-s_lc.fits` | lightcurve | 75 | False | `ddb118dc722e1fd7` | True |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | lightcurve | 76 | False | `d106f11fb4ad42c7` | True |
| `tess2024223182411-s0082-0000000286094277-0278-s_lc.fits` | lightcurve | 82 | False | `64a05d97ab7a5065` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | 2459814.87336 | recovered | 292 | 9324 ± 87 | 11053 | -0.03 |
| `tess2021204101404-s0041-0000000286094277-0212-s_lc.fits` | — | epoch not in this light curve | — | — | 11053 | — |
| `tess2022244194134-s0056-0000000286094277-0243-s_lc.fits` | — | epoch not in this light curve | — | — | 11053 | — |
| `tess2024030031500-s0075-0000000286094277-0270-s_lc.fits` | — | epoch not in this light curve | — | — | 11053 | — |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | — | epoch not in this light curve | — | — | 11053 | — |
| `tess2024223182411-s0082-0000000286094277-0278-s_lc.fits` | — | epoch not in this light curve | — | — | 11053 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021204101404-s0041-0000000286094277-0212-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022244194134-s0056-0000000286094277-0243-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2024030031500-s0075-0000000286094277-0270-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2024223182411-s0082-0000000286094277-0278-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000286094277-0278-s_lc.fits` | 2460553.95323 | -0.01040 | 188 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022244194134-s0056-0000000286094277-0243-s_lc.fits` | 2459842.24761 | -0.00983 | 257 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021204101404-s0041-0000000286094277-0212-s_lc.fits` | 2459431.67547 | -0.00983 | 249 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460389.68952 | -0.00977 | 235 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000286094277-0278-s_lc.fits` | 2460553.77754 | -0.00975 | 63 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000286094277-0270-s_lc.fits` | 2460362.29216 | -0.00952 | 250 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460389.51590 | -0.00793 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000286094277-0270-s_lc.fits` | 2460362.48730 | -0.00599 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2021204101404-s0041-0000000286094277-0212-s_lc.fits` | 2459431.85395 | -0.00516 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460389.86105 | -0.00457 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460389.85619 | -0.00454 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022244194134-s0056-0000000286094277-0243-s_lc.fits` | 2459842.06497 | -0.00402 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | 2459803.33998 | -0.00816 | 2 | SAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460373.82617 | -0.00729 | 2 | SAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460373.65395 | -0.00533 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000286094277-0278-s_lc.fits` | 2460545.00182 | -0.00522 | 2 | SAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460389.50340 | -0.00494 | 4 | PDCSAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000286094277-0278-s_lc.fits` | 2460553.73101 | -0.00493 | 2 | PDCSAP | 3 | no |
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | 2459803.50248 | -0.00475 | 2 | SAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460372.89283 | -0.00474 | 2 | SAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460373.14978 | -0.00453 | 2 | SAP | 3 | no |
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | 2459803.40387 | -0.00453 | 2 | SAP | 1, 2, 3 | no |
| `tess2021204101404-s0041-0000000286094277-0212-s_lc.fits` | 2459426.06493 | -0.00451 | 2 | SAP | 2, 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460381.16511 | -0.00441 | 2 | SAP | 1, 2, 3 | no |
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | 2459823.86929 | -0.00439 | 2 | SAP | 1, 2, 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460373.70256 | -0.00437 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460389.49576 | -0.00424 | 2 | PDCSAP | 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460373.83034 | -0.00423 | 2 | SAP | 3 | no |
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | 2459803.16498 | -0.00421 | 2 | SAP | 2, 3 | no |
| `tess2022244194134-s0056-0000000286094277-0243-s_lc.fits` | 2459852.55783 | -0.00418 | 2 | PDCSAP | 2, 3 | no |
| `tess2022217014003-s0055-0000000286094277-0242-s_lc.fits` | 2459803.46498 | -0.00409 | 2 | SAP | 3 | no |
| `tess2024058030222-s0076-0000000286094277-0271-s_lc.fits` | 2460372.71228 | -0.00407 | 2 | SAP | 1, 2, 3 | no |
| `tess2022244194134-s0056-0000000286094277-0243-s_lc.fits` | 2459831.35120 | -0.00390 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459431.67547 | 9320 | 9324 | 383.1966 | 7 / 383 | 383.197, 191.598, 127.732, 95.7991, 63.8661, 54.7424, 27.3712 |
| 2459842.24761 | 9416 | 9324 | 27.3756 | 1 / 27 | 27.3756 |
| 2460362.29216 | 8940 | 9324 | 547.4201 | 8 / 547 | 547.42, 273.71, 136.855, 109.484, 68.4275, 54.742, 49.7655, 27.371 |
| 2460389.51590 | 6679 | 9324 | 574.6439 | 9 / 574 | 574.644, 287.322, 191.548, 143.661, 114.929, 95.774, 71.8305, 63.8493, 57.4644 |
| 2460389.68952 | 9341 | 9324 | 574.8175 | 11 / 574 | 574.817, 287.409, 191.606, 143.704, 114.963, 95.8029, 82.1168, 71.8522, 63.8686, 57.4817, 27.3723 |
| 2460553.77754 | 8595 | 9324 | 738.9055 | 5 / 738 | 738.905, 246.302, 147.781, 82.1006, 27.3669 |
| 2460553.95323 | 9767 | 9324 | 739.0812 | 5 / 739 | 739.081, 246.36, 147.816, 82.1201, 27.3734 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-5149.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:05:08Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:05:10Z: TOI-5149.01 (TIC 286094277, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:05:11Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:05:12Z: TYC 3578-1416-1 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459814.8734: recovered, depth 9324 ± 87 ppm (catalogue 11053 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, ≤2.5, 3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 50%, 10%, 30%, 30%, 50%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 7 repeat-candidate event(s); first at BJD 2459431.6755, ΔT = 383.197 d, 7 of 383 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (383.197, 191.598, 127.732, 95.7991, 63.8661, 54.7424, 27.3712 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5149.01: Gaia DR3 2167586710592820096 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-5149.01: dwarf priors not applied — RUWE 5.116401 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5149.01: 39 Gaia neighbour(s) within 52.5", contamination 14.24%; depth 9324 ppm (measured depth of the recovered catalogued transit); 5 could produce it if fully eclipsed (brightest 2167574959562304768, 42.5", ΔG 3.46); a centroid test is needed |
| Pointing and quality census per event | failed | 12 persistent event(s), 6 clean; BJD 2459431.6755 suspect: POS_CORR1 z=-5.1, POS_CORR2 z=+5.4, SAP_BKG z=-6.6; BJD 2460362.2922 suspect: MOM_CENTR1 z=-6.5, SAP_BKG z=+30.0; BJD 2460389.5159 suspect: SAP_BKG z=-5.8; BJD 2460389.6895 suspect: POS_CORR1 z=+8.7, POS_CORR2 z=-6.9 |
| Moving objects at screen-event epochs | inconclusive | 12 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-5149.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-5149.01: TYC 3578-1416-1 otype SB* (multiple) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5149-01.yaml
python -m cygnus.multi report campaigns/toi-5149-01.yaml
```
