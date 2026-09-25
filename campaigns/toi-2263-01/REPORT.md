# Known-object test, TOI-2263.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

## Escalation (2026-09-25)

The covered positive control formally failed (BJD 2458708.3844; 447 usable cadences), with measured depth 208 ± 45 ppm vs catalogue 358 ppm. At k* = 3 the 90%-completeness floor is 5000 ppm at 8 h, and the 14.92-h transit lies outside the injection duration grid; the known signal is far below tested sensitivity. Record the failure without tuning thresholds or inferring a wrong epoch. Next: compare the epoch against TOI/SPOC DV and a reduction sensitive to a few hundred ppm over a long duration.


- Campaign spec: `campaigns/toi-2263-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #496, fetch_products #495, known_signal_recovery #497, period_aliases #499, prior_art #500, residual_screen #498
- Runner finished (UTC): 2026-09-25T05:54:50Z

## Bottom line

Positive control **failed**: BJD 2458708.3844: not recovered, depth 208 ± 45 ppm (catalogue 358 ppm).
Outside the catalogued epoch the screen left 94 threshold entries forming **38 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **failed formally** at a covered epoch in sector 14 (447 usable in-transit cadences; QUALITY=0, max gap 2 min): measured 208 ± 45 ppm vs catalogue 358 ppm (ratio 0.58). The k* = 3 90%-completeness depth is 5000 ppm at 8 h; the catalogue depth is below that floor, and the 14.92-h duration is longer than the calibration grid. Treat the formal failure as sensitivity-limited on this reduction; no threshold was tuned.

The one persistent event is BJD 2458874.03948 in sector 21 (2 cadences, −0.30%). Its binned SAP/PDCSAP profile is scatter-level without a localized dip; QUALITY=0, max gap 2 min, and no significant centroid motion is apparent from the screen-entry residuals. It is not a repeat candidate. Other crossings are mostly brief single-flux excursions. All four prior-art services answered; no VSX variable match.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2263.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 159400561 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 237.961131 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 83.110888 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2458708.384365 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 357.7289632 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 14.9235889 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 9.7115 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2022-02-04 10:10:02 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2019198215352-s0014-0000000159400561-0150-s_lc.fits` | 14 | True | `55ff89fc7be45455` | True |
| `tess2019331140908-s0019-0000000159400561-0164-s_lc.fits` | 19 | False | `51bc7088b534e36b` | True |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | 20 | False | `0e4242366543cf16` | True |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 21 | False | `25536edafc9fdb6f` | True |
| `tess2020133194932-s0025-0000000159400561-0182-s_lc.fits` | 25 | False | `9c57b9a8afbd9e8c` | True |
| `tess2020160202036-s0026-0000000159400561-0188-s_lc.fits` | 26 | False | `3c88e57dc95ba009` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019198215352-s0014-0000000159400561-0150-s_lc.fits` | 2458708.38436 | not_recovered | 447 | 208 ± 45 | 358 | — |
| `tess2019331140908-s0019-0000000159400561-0164-s_lc.fits` | — | epoch not in this light curve | — | — | 358 | — |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | — | epoch not in this light curve | — | — | 358 | — |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | — | epoch not in this light curve | — | — | 358 | — |
| `tess2020133194932-s0025-0000000159400561-0182-s_lc.fits` | — | epoch not in this light curve | — | — | 358 | — |
| `tess2020160202036-s0026-0000000159400561-0188-s_lc.fits` | — | epoch not in this light curve | — | — | 358 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019198215352-s0014-0000000159400561-0150-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019331140908-s0019-0000000159400561-0164-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2020133194932-s0025-0000000159400561-0182-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020160202036-s0026-0000000159400561-0188-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458874.03948 | -0.00301 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | 2458862.48403 | -0.00587 | 2 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000159400561-0182-s_lc.fits` | 2458995.56137 | -0.00509 | 2 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000159400561-0182-s_lc.fits` | 2459009.03199 | -0.00452 | 2 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000159400561-0182-s_lc.fits` | 2458995.26416 | -0.00440 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458897.27727 | -0.00436 | 3 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458887.91010 | -0.00435 | 2 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | 2458862.27848 | -0.00430 | 2 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | 2458856.65768 | -0.00400 | 2 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000159400561-0182-s_lc.fits` | 2458984.31855 | -0.00394 | 2 | SAP | 3 | no |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | 2458857.23962 | -0.00388 | 2 | SAP | 1 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458895.39606 | -0.00379 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458887.68510 | -0.00373 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458887.47400 | -0.00370 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458896.88491 | -0.00362 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458897.59184 | -0.00350 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458885.86847 | -0.00344 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458897.09949 | -0.00335 | 3 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458887.15317 | -0.00333 | 2 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000159400561-0182-s_lc.fits` | 2458985.26159 | -0.00326 | 2 | SAP | 1 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458887.31150 | -0.00322 | 2 | SAP | 1, 2, 3 | no |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | 2458867.79233 | -0.00317 | 2 | SAP | 1, 2 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458894.63357 | -0.00317 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458897.64462 | -0.00312 | 2 | SAP | 2, 3 | no |
| `tess2019357164649-s0020-0000000159400561-0165-s_lc.fits` | 2458842.56461 | -0.00309 | 2 | PDCSAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458887.65177 | -0.00305 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458886.71568 | -0.00302 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458870.69369 | -0.00298 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458892.48501 | -0.00297 | 2 | SAP | 1, 2, 3 | no |
| `tess2020160202036-s0026-0000000159400561-0188-s_lc.fits` | 2459025.32907 | -0.00295 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458897.05158 | -0.00287 | 2 | SAP | 3 | no |
| `tess2020160202036-s0026-0000000159400561-0188-s_lc.fits` | 2459029.11933 | -0.00286 | 2 | SAP | 1, 2, 3 | no |
| `tess2020160202036-s0026-0000000159400561-0188-s_lc.fits` | 2459013.58194 | -0.00284 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458897.66823 | -0.00284 | 2 | SAP | 2, 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458877.06861 | -0.00277 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458897.62101 | -0.00267 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458893.78359 | -0.00258 | 2 | SAP | 1 | no |
| `tess2020020091053-s0021-0000000159400561-0167-s_lc.fits` | 2458897.66267 | -0.00252 | 2 | SAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2263.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:54:42Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:54:44Z: TOI-2263.01 (TIC 159400561, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:54:47Z
- SIMBAD (done, 2026-09-25): 2 match(es) in SIMBAD within 30" as of 2026-09-25T05:54:48Z: TOI-2263.01 (Pl?); BD+83   461 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2458708.3844: not recovered, depth 208 ± 45 ppm (catalogue 358 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, ≤2.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 10%, 30%, 100%, 30%, 90% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2263-01.yaml
python -m cygnus.campaign report campaigns/toi-2263-01.yaml
```
