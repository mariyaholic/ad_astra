# Known-object test, TOI-2634.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-2634-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #340, fetch_products #339, known_signal_recovery #341, period_aliases #343, prior_art #344, residual_screen #342
- Runner finished (UTC): 2026-09-25T04:50:22Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2634.01 (BJD 2459147.1336: recovered, depth 3954 ± 142 ppm (catalogue 2801 ppm)).
Outside the catalogued epoch the screen left 82 threshold entries forming **37 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **passed** at the catalogued epoch (sector 31, offset 0.57 h): recovered depth 3954 ± 142 ppm vs catalogue 2801 ppm (ratio 1.41) — a depth excess of the same order as most batch controls, reported not tuned.

Hand checks on the one persistent screen event:

| Event (BJD) | Shape | Quality/gaps | Centroid | Verdict |
|---|---|---|---|---|
| 2460249.03586 (S71, −0.57 %/2 cad) | 20-min binned PDCSAP ±0.15 d: scatter ±~0.9 ppt, no local minimum at the event | 0 flags/216, max gap 2 min | col +0.0104 vs 0.0050 (≈2σ); row −0.0125 vs 0.0082 (≈1.5σ) | two 2-cadence deep-noise spikes via shared baselines, not a dip; centroid reads ride the scatter, no jump seen on an event |

Prior art answered by all 4 services: TESS_TOI TOI-2634.01 PC; SIMBAD lists the host as TYC 50-821-1 with type Em* (emission-line star) — chromospheric activity is a live alternative for depth/noise anomalies; no period anywhere. No candidate dossiers exist.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2634.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 318812447 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 41.036551 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 3.910232 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459147.133574 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 2801.2247588 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 4.8897805 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 10.9648 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2024-09-24 10:08:02 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2020294194027-s0031-0000000318812447-0198-s_lc.fits` | 31 | True | `15e76f0e28ba91cc` | False |
| `tess2023263165758-s0070-0000000318812447-0265-s_lc.fits` | 70 | False | `fc37a2247db2a48f` | True |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 71 | False | `93505ca30c7c9a08` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020294194027-s0031-0000000318812447-0198-s_lc.fits` | 2459147.13357 | recovered | 146 | 3954 ± 142 | 2801 | 0.57 |
| `tess2023263165758-s0070-0000000318812447-0265-s_lc.fits` | — | epoch not in this light curve | — | — | 2801 | — |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | — | epoch not in this light curve | — | — | 2801 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020294194027-s0031-0000000318812447-0198-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 10000, 8h: 10000 |
| `tess2023263165758-s0070-0000000318812447-0265-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460249.03586 | -0.00573 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.09558 | -0.01023 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.17614 | -0.00950 | 4 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.15739 | -0.00929 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.08100 | -0.00887 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.91433 | -0.00853 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.01920 | -0.00844 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.02753 | -0.00781 | 8 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.17058 | -0.00742 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.18169 | -0.00709 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.06920 | -0.00703 | 4 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.05670 | -0.00701 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.90183 | -0.00686 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.15253 | -0.00686 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.72892 | -0.00676 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.98378 | -0.00671 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.78864 | -0.00666 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.97406 | -0.00659 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.91989 | -0.00655 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.08586 | -0.00646 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.90947 | -0.00640 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460246.01917 | -0.00632 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.84697 | -0.00602 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.11919 | -0.00595 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.11364 | -0.00586 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.14281 | -0.00572 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.20253 | -0.00529 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.82614 | -0.00529 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460240.26634 | -0.00529 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.06086 | -0.00527 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.04558 | -0.00526 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.85531 | -0.00509 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460253.03586 | -0.00509 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460248.74558 | -0.00491 | 2 | SAP | 1 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.77336 | -0.00482 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.96642 | -0.00482 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000318812447-0266-s_lc.fits` | 2460252.49281 | -0.00480 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2634.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T04:50:16Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T04:50:18Z: TOI-2634.01 (TIC 318812447, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T04:50:20Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T04:50:21Z: TYC   50-821-1 (Em*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459147.1336: recovered, depth 3954 ± 142 ppm (catalogue 2801 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 40% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2634-01.yaml
python -m cygnus.campaign report campaigns/toi-2634-01.yaml
```
