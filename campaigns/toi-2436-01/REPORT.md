# Known-object test, TOI-2436.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

## Escalation (2026-09-25)

The positive control formally failed at a covered epoch (BJD 2458722.3937; 262 usable cadences), despite a measured depth of 392 ± 31 ppm being consistent with the 368-ppm catalogue value. The per-light-curve k* = 4 calibration has a 90%-completeness depth of 5000 ppm at the longest tabulated duration (8 h), while the transit is 8.73 h and 368 ppm; it is far below tested sensitivity. Record this as a sensitivity-limited pipeline failure, not a wrong-epoch inference. No threshold or state was changed. Next: verify the TOI/SPOC DV epoch and compare an independent reduction that can measure a few-hundred-ppm signal.


- Campaign spec: `campaigns/toi-2436-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #418, fetch_products #417, known_signal_recovery #419, period_aliases #421, prior_art #422, residual_screen #420
- Runner finished (UTC): 2026-09-25T05:37:36Z

## Bottom line

Positive control **failed**: BJD 2458722.3937: not recovered, depth 392 ± 31 ppm (catalogue 368 ppm).
Outside the catalogued epoch the screen left 100 threshold entries forming **41 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **failed formally** with the epoch covered in sector 15 (262 usable in-transit cadences; QUALITY=0, max gap 2 min): measured 392 ± 31 ppm vs catalogue 368 ppm (ratio 1.07), a depth-consistent broad signal. The sector's k* = 4 90%-completeness depth is 5000 ppm at the longest tabulated duration (8 h; 2000 ppm for 1–4 h); the 368-ppm, 8.73-h catalogue event is far below the tested floor. Do not infer a wrong ephemeris or tune the threshold.

There are **0 persistent** events among 100 threshold entries / 41 groups. Report rows are mostly brief, single-flux SAP excursions; no repeated feature survives both SAP and PDCSAP. The check remains a bounded pipeline test with no candidate. NASA Exoplanet Archive, TOI, VSX and SIMBAD all answered; no VSX variable match. Pixel/difference-image, pointing and alternate-reduction tests remain not tested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2436.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 154568734 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 191.297899 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 72.123084 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2458722.393707 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 367.8233419 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 8.7302689 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 8.55595 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2022-11-15 16:02:02 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2019226182529-s0015-0000000154568734-0151-s_lc.fits` | 15 | True | `4ca450696044712a` | True |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 14 | False | `91fe777953f54a78` | True |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 21 | False | `5e4b810b7ff73be8` | True |
| `tess2021175071901-s0040-0000000154568734-0211-s_lc.fits` | 40 | False | `275c0ab3c042e643` | True |
| `tess2021204101404-s0041-0000000154568734-0212-s_lc.fits` | 41 | False | `d29cd6c3487486a3` | True |
| `tess2021364111932-s0047-0000000154568734-0218-s_lc.fits` | 47 | False | `398330d371b515c9` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019226182529-s0015-0000000154568734-0151-s_lc.fits` | 2458722.39371 | not_recovered | 262 | 392 ± 31 | 368 | — |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | — | epoch not in this light curve | — | — | 368 | — |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | — | epoch not in this light curve | — | — | 368 | — |
| `tess2021175071901-s0040-0000000154568734-0211-s_lc.fits` | — | epoch not in this light curve | — | — | 368 | — |
| `tess2021204101404-s0041-0000000154568734-0212-s_lc.fits` | — | epoch not in this light curve | — | — | 368 | — |
| `tess2021364111932-s0047-0000000154568734-0218-s_lc.fits` | — | epoch not in this light curve | — | — | 368 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019226182529-s0015-0000000154568734-0151-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021175071901-s0040-0000000154568734-0211-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2021204101404-s0041-0000000154568734-0212-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021364111932-s0047-0000000154568734-0218-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 2458895.39726 | -0.00418 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 2458887.17648 | -0.00394 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 2458895.44032 | -0.00369 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 2458887.57509 | -0.00353 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 2458887.39037 | -0.00344 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 2458887.31260 | -0.00342 | 2 | SAP | 3 | no |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 2458894.55699 | -0.00309 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458687.94515 | -0.00308 | 2 | SAP | 1, 2, 3 | no |
| `tess2020020091053-s0021-0000000154568734-0167-s_lc.fits` | 2458893.78478 | -0.00306 | 2 | SAP | 1 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458693.43122 | -0.00302 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458703.17009 | -0.00297 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458690.64374 | -0.00287 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458708.40621 | -0.00283 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000154568734-0151-s_lc.fits` | 2458719.63687 | -0.00274 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458697.75690 | -0.00259 | 3 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458699.04092 | -0.00253 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458684.29797 | -0.00252 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458708.52566 | -0.00252 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458697.45412 | -0.00251 | 3 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458684.44797 | -0.00250 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458691.85206 | -0.00246 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458688.06112 | -0.00244 | 3 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458702.36870 | -0.00243 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458698.02704 | -0.00240 | 2 | SAP | 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458683.59868 | -0.00229 | 3 | SAP | 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458696.30343 | -0.00225 | 2 | SAP | 1, 2 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458705.32565 | -0.00215 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458688.30626 | -0.00211 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458708.19788 | -0.00210 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458697.56454 | -0.00210 | 2 | SAP | 2 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458683.43271 | -0.00208 | 2 | SAP | 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458697.92148 | -0.00207 | 2 | SAP | 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458684.08409 | -0.00204 | 2 | SAP | 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458683.44798 | -0.00199 | 2 | SAP | 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458706.35065 | -0.00197 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458709.85067 | -0.00196 | 2 | SAP | 1, 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458698.25620 | -0.00192 | 2 | SAP | 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458689.05903 | -0.00191 | 2 | SAP | 1 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458683.64381 | -0.00157 | 2 | PDCSAP | 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458683.57298 | -0.00156 | 2 | PDCSAP | 2, 3 | no |
| `tess2019198215352-s0014-0000000154568734-0150-s_lc.fits` | 2458690.89791 | -0.00144 | 2 | PDCSAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2436.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:37:30Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:37:32Z: TOI-2436.01 (TIC 154568734, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:37:34Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T05:37:35Z: BD+72   581 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2458722.3937: not recovered, depth 392 ± 31 ppm (catalogue 368 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, ≤2.5, 3.5, 3, 4.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100%, 80%, 100%, 20%, 90% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2436-01.yaml
python -m cygnus.campaign report campaigns/toi-2436-01.yaml
```
