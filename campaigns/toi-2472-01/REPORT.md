# Known-object test, TOI-2472.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-2472-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #472, fetch_products #471, known_signal_recovery #473, period_aliases #475, prior_art #476, residual_screen #474
- Runner finished (UTC): 2026-09-25T05:46:25Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 63 threshold entries forming **24 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **not tested**: the two retrieved products (sectors 5 and 98) are explicitly marked as not covering catalogue epoch BJD 2459198.8525. The catalogued 390-ppm, 6.71-h signal is also below sector 98's k* = 4 90%-completeness depths (5000 ppm at 8 h; 5000 ppm at the shorter tabulated durations), so a null cannot constrain it.

The one persistent row is BJD 2461024.20240 in sector 98 (4 cadences, −0.47%). Its SAP/PDCSAP profile shows a short depression on a broadly low-frequency baseline, not a distinct transit shape; QUALITY=0, max gap 8 min, and centroid residuals are below 1σ. The remaining entries are short, mostly single-flux SAP features. No repeat candidate. Four-service cross-match answered; no VSX variable match. Image-level/alternate-reduction checks remain untested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2472.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 248650906 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 67.042733 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -3.145653 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459198.852539 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 390.0 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 6.71 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 8.94848 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2018319095959-s0005-0000000248650906-0125-s_lc.fits` | 5 | False | `e2e13b8cac6a677c` | True |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 98 | False | `e455dd550fb414c9` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2018319095959-s0005-0000000248650906-0125-s_lc.fits` | — | epoch not in this light curve | — | — | 390 | — |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | — | epoch not in this light curve | — | — | 390 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2018319095959-s0005-0000000248650906-0125-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.20240 | -0.00468 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.29684 | -0.00479 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.18990 | -0.00459 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461037.61021 | -0.00430 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461038.03519 | -0.00429 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.28295 | -0.00426 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461038.60044 | -0.00425 | 3 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461038.18518 | -0.00424 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.21351 | -0.00414 | 3 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461038.22268 | -0.00410 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.19407 | -0.00386 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461037.57549 | -0.00380 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.30656 | -0.00375 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.16351 | -0.00368 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.23990 | -0.00353 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461038.58447 | -0.00348 | 3 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.29198 | -0.00342 | 3 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461038.45878 | -0.00332 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.22879 | -0.00332 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461038.48308 | -0.00318 | 3 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461024.28712 | -0.00316 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461037.76992 | -0.00279 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461037.81992 | -0.00275 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000248650906-0298-s_lc.fits` | 2461023.33576 | -0.00270 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2472.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:46:20Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:46:22Z: TOI-2472.01 (TIC 248650906, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:46:24Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T05:46:24Z: BD-03   785 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 4; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 90%, 50% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2472-01.yaml
python -m cygnus.campaign report campaigns/toi-2472-01.yaml
```
