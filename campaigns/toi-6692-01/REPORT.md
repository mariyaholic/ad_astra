# Known-object test, TOI-6692.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-6692-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #243, fetch_products #242, known_signal_recovery #244, period_aliases #246, prior_art #247, residual_screen #245
- Runner finished (UTC): 2026-09-25T04:00:53Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6692.01 (BJD 2459378.4176: recovered, depth 5187 ± 106 ppm (catalogue 3281 ppm)).
Outside the catalogued epoch the screen left 106 threshold entries forming **44 distinct event(s)**, **6 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **passed**: the sector-39 profile (`sector39/normalized_series.csv`) shows a
flat-bottomed dip centred on the catalogued epoch (BJD 2459378.4176), recovered at 5187 ± 106 ppm
against a catalogue depth of 3281 ppm. No repeat candidate was raised (`period_aliases` `not_tested`).

Six persistent events were flagged, in sectors 67 and 101:

- **Sector 67 (2460140.60131 / .62631 / .82492 / 2460141.01798)** — one contiguous feature (mid-times
  spanning ≈ 0.42 d); binned profiles are broad, shallow (~500–640 ppm) depressions without a flat
  floor. Nearest-excursion centroid residual MOM_CENTR1 −0.0052 px against sd 0.0082 (≈ 0.6σ).
- **Sector 101 (2461101.45436 / 2461119.19269)** — the 2461119.19269 event is at the very end of the
  sector (sector spans 2461101.44–2461125.25) and shows centroid residual MOM_CENTR2 +0.0051 px against
  sd 0.0159 (≈ 0.3σ); 2461101.45436 is at the sector start. Both are broad and non-transit-shaped.

Read as systematics (sector-edge / low-frequency); nothing advanced. Catalogue cross-match answered by
all four services.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6692.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 324609409 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 312.694044 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -81.272398 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459378.417556 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 3281.1685561 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 10.7778244 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 11.1163 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2025-07-22 12:04:25 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2021146024351-s0039-0000000324609409-0210-s_lc.fits` | 39 | True | `01c331937b2a764f` | True |
| `tess2023153011303-s0066-0000000324609409-0260-s_lc.fits` | 66 | False | `f4b1c8a327c41b2d` | True |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 67 | False | `ef1807aa45cb70e3` | True |
| `tess2025154050500-s0093-0000000324609409-0290-s_lc.fits` | 93 | False | `9278ff1c98d05e22` | True |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 94 | False | `bb8855223fe9b487` | True |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 101 | False | `246abc1366158e97` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021146024351-s0039-0000000324609409-0210-s_lc.fits` | 2459378.41756 | recovered | 323 | 5187 ± 106 | 3281 | -0.12 |
| `tess2023153011303-s0066-0000000324609409-0260-s_lc.fits` | — | epoch not in this light curve | — | — | 3281 | — |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | — | epoch not in this light curve | — | — | 3281 | — |
| `tess2025154050500-s0093-0000000324609409-0290-s_lc.fits` | — | epoch not in this light curve | — | — | 3281 | — |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | — | epoch not in this light curve | — | — | 3281 | — |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 3281 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021146024351-s0039-0000000324609409-0210-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2023153011303-s0066-0000000324609409-0260-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025154050500-s0093-0000000324609409-0290-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.19269 | -0.00765 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 2460141.01798 | -0.00636 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 2460140.82492 | -0.00624 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461101.45436 | -0.00553 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 2460140.60131 | -0.00518 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 2460140.62631 | -0.00503 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.85314 | -0.00753 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.69688 | -0.00740 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.85939 | -0.00736 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461114.72788 | -0.00707 | 3 | SAP | 1, 2, 3 | no |
| `tess2021146024351-s0039-0000000324609409-0210-s_lc.fits` | 2459389.62526 | -0.00707 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.16352 | -0.00659 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461101.56548 | -0.00645 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461101.60853 | -0.00637 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.86703 | -0.00634 | 3 | SAP | 1, 2, 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460874.84912 | -0.00631 | 2 | SAP | 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460874.71717 | -0.00625 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461114.62579 | -0.00616 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000324609409-0290-s_lc.fits` | 2460849.77139 | -0.00610 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460874.29287 | -0.00610 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.72883 | -0.00605 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460867.78945 | -0.00599 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.37187 | -0.00584 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460868.09639 | -0.00584 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000324609409-0290-s_lc.fits` | 2460849.73111 | -0.00584 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461101.49464 | -0.00561 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.40798 | -0.00556 | 2 | SAP | 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460874.66440 | -0.00556 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461119.80939 | -0.00555 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460874.59912 | -0.00555 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460881.11151 | -0.00550 | 2 | PDCSAP | 1, 2 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460874.28246 | -0.00546 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461101.85785 | -0.00545 | 3 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000324609409-0303-s_lc.fits` | 2461101.51547 | -0.00539 | 2 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000324609409-0290-s_lc.fits` | 2460849.79917 | -0.00527 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460875.02828 | -0.00521 | 2 | SAP | 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460874.89356 | -0.00520 | 2 | SAP | 3 | no |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 2460136.28051 | -0.00510 | 2 | SAP | 2, 3 | no |
| `tess2025180145000-s0094-0000000324609409-0291-s_lc.fits` | 2460874.99634 | -0.00509 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000324609409-0290-s_lc.fits` | 2460849.81861 | -0.00508 | 2 | SAP | 2, 3 | no |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 2460141.18742 | -0.00503 | 2 | PDCSAP | 3 | no |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 2460150.99561 | -0.00493 | 2 | PDCSAP | 2, 3 | no |
| `tess2023181235917-s0067-0000000324609409-0261-s_lc.fits` | 2460146.94430 | -0.00488 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000324609409-0290-s_lc.fits` | 2460854.89085 | -0.00459 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6692.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): 1 match(es) in NASA_Exoplanet_Archive within 30" as of 2026-09-25T04:00:45Z: TOI-6692 b (host TOI-6692)
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T04:00:47Z: TOI-6692.01 (TIC 324609409, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T04:00:49Z
- SIMBAD (done, 2026-09-25): 2 match(es) in SIMBAD within 30" as of 2026-09-25T04:00:51Z: TOI-6692b (Pl); TYC 9473-833-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459378.4176: recovered, depth 5187 ± 106 ppm (catalogue 3281 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3.5, ≤2.5, ≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 10%, 20%, 20%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-6692-01.yaml
python -m cygnus.campaign report campaigns/toi-6692-01.yaml
```
