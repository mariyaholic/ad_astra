# Known-object test, TOI-2435.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

## Escalation (2026-09-25)

The calibrated positive control formally failed despite epoch coverage (BJD 2458743.3741; 152 usable cadences). The measured depth is 1639 ± 138 ppm vs catalogue 1840 ppm, but the sector's 90%-completeness floor is 5000 ppm for all durations and 2000-ppm/4-h injection completeness is 0%; the failure is therefore sensitivity-limited on the available reduction. It is reported as-is; no threshold was adjusted. Highest-value next test: inspect ExoFOP/SPOC DV and an independent reduction for the catalogued epoch, then verify the SIMBAD emission-star match before treating it as a host property.


- Campaign spec: `campaigns/toi-2435-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #358, fetch_products #357, known_signal_recovery #359, period_aliases #361, prior_art #362, residual_screen #360
- Runner finished (UTC): 2026-09-25T05:08:00Z

## Bottom line

Positive control **failed**: BJD 2458743.3741: not recovered, depth 1639 ± 138 ppm (catalogue 1840 ppm).
Outside the catalogued epoch the screen left 46 threshold entries forming **23 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **failed formally** at a covered epoch in sector 16 (152 usable in-transit cadences; 0 threshold entries). The measured depth, 1639 ± 138 ppm vs catalogue 1840 ppm (ratio 0.89), is reasonably close, but the sector's k* = 3 90%-completeness depth is 5000 ppm at every duration and 2000-ppm/4-h injection completeness is 0%. Thus the 1840-ppm signal lies well below the tested sensitivity; record the formal failure without inferring a wrong epoch or tuning the threshold. The binned profile has a shallow broad depression around the epoch, with no calibrated-screen crossing.

There are **0 persistent** events among 46 entries / 23 groups; all rows in the report are short, single-flux events, with the strongest two-cadence entries consistent with non-persistent noise/systematics. No repeat lead was raised. Cross-match answered at all four services; SIMBAD returned TYC 3863-1448-1 (Em*) within 30 arcsec, a possible activity alternative whose association with the TIC is not established. Difference images, alternate reduction and pointing audit remain untested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2435.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 298164705 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 219.338411 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 56.666184 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2458743.374055 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 1840.1196782 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 5.0482027 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 10.5142 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2019253231442-s0016-0000000298164705-0152-s_lc.fits` | 16 | True | `4ef543c18b3e2a5e` | True |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 15 | False | `0b1f0f7e50ebf399` | True |
| `tess2020049080258-s0022-0000000298164705-0174-s_lc.fits` | 22 | False | `6d9918ec2cbe02a3` | True |
| `tess2020078014623-s0023-0000000298164705-0177-s_lc.fits` | 23 | False | `d8c77c17bc604c38` | True |
| `tess2022057073128-s0049-0000000298164705-0221-s_lc.fits` | 49 | False | `d67e26d9cf8e63e6` | True |
| `tess2024058030222-s0076-0000000298164705-0271-s_lc.fits` | 76 | False | `37f9b58f4e1c1926` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019253231442-s0016-0000000298164705-0152-s_lc.fits` | 2458743.37406 | not_recovered | 152 | 1639 ± 138 | 1840 | — |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | — | epoch not in this light curve | — | — | 1840 | — |
| `tess2020049080258-s0022-0000000298164705-0174-s_lc.fits` | — | epoch not in this light curve | — | — | 1840 | — |
| `tess2020078014623-s0023-0000000298164705-0177-s_lc.fits` | — | epoch not in this light curve | — | — | 1840 | — |
| `tess2022057073128-s0049-0000000298164705-0221-s_lc.fits` | — | epoch not in this light curve | — | — | 1840 | — |
| `tess2024058030222-s0076-0000000298164705-0271-s_lc.fits` | — | epoch not in this light curve | — | — | 1840 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019253231442-s0016-0000000298164705-0152-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020049080258-s0022-0000000298164705-0174-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2020078014623-s0023-0000000298164705-0177-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 10000, 8h: 10000 |
| `tess2022057073128-s0049-0000000298164705-0221-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024058030222-s0076-0000000298164705-0271-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020078014623-s0023-0000000298164705-0177-s_lc.fits` | 2458949.14984 | -0.00662 | 2 | SAP | 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458716.60802 | -0.00599 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458721.34126 | -0.00586 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458728.29114 | -0.00569 | 2 | SAP | 1, 2, 3 | no |
| `tess2019253231442-s0016-0000000298164705-0152-s_lc.fits` | 2458742.44796 | -0.00560 | 2 | PDCSAP | 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458719.63712 | -0.00520 | 2 | SAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458720.39128 | -0.00520 | 2 | PDCSAP | 2, 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458716.54413 | -0.00518 | 2 | SAP | 2, 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458722.13430 | -0.00471 | 2 | SAP | 1, 2, 3 | no |
| `tess2019253231442-s0016-0000000298164705-0152-s_lc.fits` | 2458738.72576 | -0.00461 | 2 | PDCSAP | 1, 2 | no |
| `tess2024058030222-s0076-0000000298164705-0271-s_lc.fits` | 2460390.24936 | -0.00451 | 2 | SAP | 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458728.83558 | -0.00448 | 2 | SAP | 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458711.44842 | -0.00437 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458711.42203 | -0.00428 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458711.47203 | -0.00425 | 2 | PDCSAP | 1, 2 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458725.36480 | -0.00424 | 2 | SAP | 1, 2 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458720.04545 | -0.00402 | 2 | PDCSAP | 2, 3 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458725.69535 | -0.00402 | 2 | SAP | 1 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458725.40647 | -0.00401 | 2 | SAP | 1, 2 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458725.17869 | -0.00399 | 2 | SAP | 1 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458711.43036 | -0.00397 | 2 | PDCSAP | 1, 2 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458725.16480 | -0.00394 | 2 | SAP | 1 | no |
| `tess2019226182529-s0015-0000000298164705-0151-s_lc.fits` | 2458711.43869 | -0.00372 | 2 | PDCSAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2435.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:07:54Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:07:56Z: TOI-2435.01 (TIC 298164705, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:07:57Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T05:07:59Z: TYC 3863-1448-1 (Em*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2458743.3741: not recovered, depth 1639 ± 138 ppm (catalogue 1840 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, 3, 3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 30%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2435-01.yaml
python -m cygnus.campaign report campaigns/toi-2435-01.yaml
```
