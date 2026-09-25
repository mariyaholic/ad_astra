# Known-object test, TOI-6698.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

## Escalation (2026-09-25)

The covered positive control formally failed at BJD 2459331.0919 (110 usable cadences), while its direct depth 1210 ± 151 ppm agrees with the 1169-ppm catalogue depth. At k* = 3, the 90%-completeness floor is 5000 ppm for all tabulated durations, so the 3.67-h signal is below the pipeline's calibrated sensitivity. Report the failure without changing thresholds; it is not evidence of a wrong epoch. Next: review SPOC DV/TOI notes and test with an independent reduction of suitable sensitivity.


- Campaign spec: `campaigns/toi-6698-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #448, fetch_products #447, known_signal_recovery #449, period_aliases #451, prior_art #452, residual_screen #450
- Runner finished (UTC): 2026-09-25T05:44:35Z

## Bottom line

Positive control **failed**: BJD 2459331.0919: not recovered, depth 1210 ± 151 ppm (catalogue 1169 ppm).
Outside the catalogued epoch the screen left 54 threshold entries forming **28 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **failed formally** in covered sector 37 (110 usable in-transit cadences; QUALITY=0, max gap 2 min): measured 1210 ± 151 ppm vs catalogue 1169 ppm (ratio 1.04). The sector's k* = 3 90%-completeness floor is 5000 ppm for the 3.67-h signal, over four times deeper than the catalogue transit. The direct depth is concordant, but the screen is not sensitive enough for the calibrated gate to trigger; treat the formal failure as sensitivity-limited.

There are **0 persistent** events among 54 threshold entries / 28 groups; the listed events are short single-flux features. No repeat candidate. The four-service cross-match answered; VSX returned no variable and SIMBAD returned TYC 6697-833-1 within 30 arcsec. Pixel-level, pointing and alternate-reduction checks remain untested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6698.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 5966772 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 193.398197 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -23.119791 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459331.091898 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 1168.7878058 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 3.6676275 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 10.4795 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2026-04-02 12:05:24 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2021091135823-s0037-0000000005966772-0208-s_lc.fits` | 37 | True | `6357f52c96356299` | True |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 64 | False | `b507dd1dad5d3a4b` | True |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 101 | False | `20be08df2ba718ce` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021091135823-s0037-0000000005966772-0208-s_lc.fits` | 2459331.09190 | not_recovered | 110 | 1210 ± 151 | 1169 | — |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | — | epoch not in this light curve | — | — | 1169 | — |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 1169 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021091135823-s0037-0000000005966772-0208-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 2461101.60588 | -0.00603 | 2 | PDCSAP | 3 | no |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 2461119.72832 | -0.00591 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460062.02330 | -0.00551 | 2 | SAP | 1, 2, 3 | no |
| `tess2021091135823-s0037-0000000005966772-0208-s_lc.fits` | 2459332.43332 | -0.00536 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 2461102.13369 | -0.00529 | 2 | PDCSAP | 3 | no |
| `tess2021091135823-s0037-0000000005966772-0208-s_lc.fits` | 2459325.56679 | -0.00522 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460061.95525 | -0.00514 | 2 | SAP | 2, 3 | no |
| `tess2021091135823-s0037-0000000005966772-0208-s_lc.fits` | 2459325.65290 | -0.00508 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460054.68594 | -0.00483 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 2461124.82223 | -0.00473 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460054.74706 | -0.00471 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460061.90525 | -0.00470 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 2461119.86513 | -0.00470 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460054.85053 | -0.00462 | 3 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460054.86928 | -0.00455 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460054.71789 | -0.00433 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 2461119.60957 | -0.00429 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460054.76511 | -0.00429 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460054.44984 | -0.00428 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460061.70248 | -0.00428 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460061.48720 | -0.00427 | 4 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460054.73594 | -0.00425 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460054.81928 | -0.00423 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460061.53859 | -0.00399 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 2461101.30308 | -0.00386 | 2 | SAP | 1 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460061.40665 | -0.00381 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000005966772-0257-s_lc.fits` | 2460050.76375 | -0.00377 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000005966772-0303-s_lc.fits` | 2461125.22502 | -0.00369 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6698.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:44:30Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:44:32Z: TOI-6698.01 (TIC 5966772, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:44:34Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T05:44:34Z: TYC 6697-833-1 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2459331.0919: not recovered, depth 1210 ± 151 ppm (catalogue 1169 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 30%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-6698-01.yaml
python -m cygnus.campaign report campaigns/toi-6698-01.yaml
```
