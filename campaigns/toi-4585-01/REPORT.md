# Known-object test, TOI-4585.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-4585-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #478, fetch_products #477, known_signal_recovery #479, period_aliases #481, prior_art #482, residual_screen #480
- Runner finished (UTC): 2026-09-25T05:47:12Z

## Bottom line

Positive control **inconclusive**: BJD 2458915.9891: partial, depth 354 ± 48 ppm (catalogue 385 ppm).
Outside the catalogued epoch the screen left 124 threshold entries forming **52 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control is **inconclusive/partial** at BJD 2458915.9891 in sector 22: measured 354 ± 48 ppm vs catalogue 385 ppm, with the runner marking partial (380 usable cadences; entry offset −1.71 h). The calibrated 90%-completeness floor is 5000 ppm for the tabulated 1–8-h durations; the TOI signal is far below tested sensitivity, and 12.90 h is beyond that duration grid. Retain the partial state; do not interpret the shallow depth as a miss or pass.

The two persistent entries are short and artifact-prone:

| Event | Hand check | Verdict |
|---|---|---|
| S16, 2458762.47369 (3 cadences) | event lies at the product's end (the profile has only ~8 min after it); broad SAP/PDCSAP depression, centroid residuals <1σ | sector-edge / baseline feature, not a transit |
| S15, 2458730.90932 (2 cadences) | scatter-level profile with no localized minimum; QUALITY=0, max gap 2 min; centroids within scatter | noise, not a repeat |

No repeat candidate. All four catalogue services answered; no VSX variable match. Pixel, pointing and alternate-reduction tests remain untested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4585.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 233529335 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 280.203329 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 62.506346 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2458915.989125 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 384.7552746 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 12.8976378 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 9.64656 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2022-11-15 16:02:02 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2020049080258-s0022-0000000233529335-0174-s_lc.fits` | 22 | True | `95dafc6d52652dac` | True |
| `tess2019198215352-s0014-0000000233529335-0150-s_lc.fits` | 14 | False | `e3c27096611eaf25` | True |
| `tess2019226182529-s0015-0000000233529335-0151-s_lc.fits` | 15 | False | `1c6ea0d74b3efef4` | True |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 16 | False | `a1be62984daeb56d` | True |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 17 | False | `d2369602be6cc744` | True |
| `tess2019331140908-s0019-0000000233529335-0164-s_lc.fits` | 19 | False | `61b485cba8703ac0` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020049080258-s0022-0000000233529335-0174-s_lc.fits` | 2458915.98912 | partial | 380 | 354 ± 48 | 385 | -1.71 |
| `tess2019198215352-s0014-0000000233529335-0150-s_lc.fits` | — | epoch not in this light curve | — | — | 385 | — |
| `tess2019226182529-s0015-0000000233529335-0151-s_lc.fits` | — | epoch not in this light curve | — | — | 385 | — |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | — | epoch not in this light curve | — | — | 385 | — |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | — | epoch not in this light curve | — | — | 385 | — |
| `tess2019331140908-s0019-0000000233529335-0164-s_lc.fits` | — | epoch not in this light curve | — | — | 385 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020049080258-s0022-0000000233529335-0174-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019198215352-s0014-0000000233529335-0150-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019226182529-s0015-0000000233529335-0151-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 2000, 4h: 5000, 8h: 5000 |
| `tess2019331140908-s0019-0000000233529335-0164-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 2458762.47369 | -0.00311 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019226182529-s0015-0000000233529335-0151-s_lc.fits` | 2458730.90932 | -0.00276 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019331140908-s0019-0000000233529335-0164-s_lc.fits` | 2458839.93472 | -0.00489 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458785.81028 | -0.00468 | 2 | SAP | 1, 2, 3 | no |
| `tess2019331140908-s0019-0000000233529335-0164-s_lc.fits` | 2458829.24177 | -0.00455 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.09786 | -0.00430 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458781.81865 | -0.00414 | 2 | SAP | 1, 2, 3 | no |
| `tess2019331140908-s0019-0000000233529335-0164-s_lc.fits` | 2458829.03622 | -0.00409 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.34786 | -0.00398 | 2 | SAP | 3 | no |
| `tess2019331140908-s0019-0000000233529335-0164-s_lc.fits` | 2458829.09177 | -0.00366 | 2 | SAP | 3 | no |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 2458762.36605 | -0.00364 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.05203 | -0.00358 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.06036 | -0.00355 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458764.88132 | -0.00355 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.15620 | -0.00352 | 2 | SAP | 2, 3 | no |
| `tess2019331140908-s0019-0000000233529335-0164-s_lc.fits` | 2458832.42507 | -0.00345 | 2 | SAP | 1, 2 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458765.87992 | -0.00343 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.22981 | -0.00338 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458782.00337 | -0.00336 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458766.44936 | -0.00334 | 2 | SAP | 1, 2, 3 | no |
| `tess2020049080258-s0022-0000000233529335-0174-s_lc.fits` | 2458923.06371 | -0.00327 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458786.67832 | -0.00325 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458768.96322 | -0.00324 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458779.46451 | -0.00323 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458781.81032 | -0.00317 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458777.93398 | -0.00315 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458772.80346 | -0.00315 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458785.97972 | -0.00315 | 2 | SAP | 1, 2, 3 | no |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 2458762.24800 | -0.00312 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458784.28807 | -0.00312 | 2 | SAP | 1, 2, 3 | no |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 2458762.41883 | -0.00307 | 2 | SAP | 2, 3 | no |
| `tess2019226182529-s0015-0000000233529335-0151-s_lc.fits` | 2458714.58159 | -0.00306 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458764.77716 | -0.00304 | 2 | SAP | 2, 3 | no |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 2458760.85912 | -0.00304 | 2 | SAP | 1 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458765.82367 | -0.00303 | 3 | SAP | 3 | no |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 2458762.42855 | -0.00302 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458764.80980 | -0.00296 | 3 | SAP | 2, 3 | no |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 2458762.10078 | -0.00295 | 2 | SAP | 3 | no |
| `tess2019226182529-s0015-0000000233529335-0151-s_lc.fits` | 2458733.39542 | -0.00295 | 2 | PDCSAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458777.94092 | -0.00293 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458777.81453 | -0.00292 | 2 | SAP | 2 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458779.46035 | -0.00290 | 2 | SAP | 1, 2, 3 | no |
| `tess2019253231442-s0016-0000000233529335-0152-s_lc.fits` | 2458762.25911 | -0.00289 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.64925 | -0.00286 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458768.95072 | -0.00281 | 2 | SAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.17842 | -0.00278 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458764.91188 | -0.00265 | 2 | PDCSAP | 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.73952 | -0.00261 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458764.69799 | -0.00239 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458764.71744 | -0.00235 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458764.70494 | -0.00232 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000233529335-0161-s_lc.fits` | 2458778.22147 | -0.00219 | 2 | PDCSAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-4585.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:47:02Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:47:09Z: TOI-4585.01 (TIC 233529335, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:47:10Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T05:47:11Z: TYC 4219-131-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2458915.9891: partial, depth 354 ± 48 ppm (catalogue 385 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3.5, ≤2.5, 3, ≤2.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 40%, 0%, 100%, 40%, 80%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-4585-01.yaml
python -m cygnus.campaign report campaigns/toi-4585-01.yaml
```
