# Known-object test, TOI-4509.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-4509-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #315, fetch_products #314, known_signal_recovery #316, period_aliases #318, prior_art #319, residual_screen #317
- Runner finished (UTC): 2026-09-25T04:33:19Z

## Bottom line

Positive control **failed**: BJD 2459231.7639: not recovered, depth 3741 ± 230 ppm (catalogue 3178 ppm).
Outside the catalogued epoch the screen left 156 threshold entries forming **72 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **failed formally** with the epoch covered (sector 34, 194 usable in-transit cadences; 0 flagged cadences, max gap 2 min). Two readings, both from the runner's outputs:

- Sensitivity first: at sector 34's k* = 3.0 the calibrated 90 %-completeness depths are 20000 ppm (1 h) and 10000 ppm (2–8 h) — three times the catalogue depth (3178 ppm over 6.46 h) and three times the measured dip itself, so no present transit of catalogue depth can clear the gate here; the formality of the failure is expected.
- The direct measurement is concordant: 3741 ± 230 ppm at the epoch (ratio 1.18), i.e. a dip of nearly catalogue depth exists at the catalogue epoch; like the other ≥6 h-duration cases, it fails the calibrated screen rather than the sky.

Hand checks on the one persistent screen event:

| Event (BJD) | Shape | Quality/gaps | Centroid | Verdict |
|---|---|---|---|---|
| 2459964.18189 (S61, −1.04 %/2 cad) | extended ≥0.7 d soft depression (−0.15…−0.55 ppt over ~30 bins, deepest near the event, partial recovery afterwards), no local minimum and no sharp edges | 0 flags/155, max gap 2 min | col −0.0079 vs 0.0032 (≈2.5σ); row −0.0205 vs 0.0085 (≈2.4σ) — but smooth over the same drift | long-timescale trend wrapped by the merging windows; systematic class; the marginal centroid drift rides the same smooth down-and-up, not a centroid jump on a dip |

NOTES: the deeper patched core (~−0.5 ppt, −52…−12 min) has a roughly transit-like depth but its width is anchored to the window, not measured alone; not vettable from screen.json at this precision (few entries, smooth motion). Reviewer flag, not a lead (no reference block: PC not recovered).

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4509.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 319610598 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 100.953422 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -52.638381 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459231.763893 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 3177.6204985 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 6.4567709 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 11.4003 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2024-04-23 10:09:23 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2021014023720-s0034-0000000319610598-0204-s_lc.fits` | 34 | True | `4fe5b381118442aa` | True |
| `tess2020238165205-s0029-0000000319610598-0193-s_lc.fits` | 29 | False | `554a5505c48128ad` | True |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 32 | False | `1a76b89a5e013610` | True |
| `tess2020351194500-s0033-0000000319610598-0203-s_lc.fits` | 33 | False | `c61ac19c60ca2b24` | True |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 61 | False | `c54a42dd3bee73f0` | True |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 62 | False | `626d757dfd95c98d` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000319610598-0204-s_lc.fits` | 2459231.76389 | not_recovered | 194 | 3741 ± 230 | 3178 | — |
| `tess2020238165205-s0029-0000000319610598-0193-s_lc.fits` | — | epoch not in this light curve | — | — | 3178 | — |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | — | epoch not in this light curve | — | — | 3178 | — |
| `tess2020351194500-s0033-0000000319610598-0203-s_lc.fits` | — | epoch not in this light curve | — | — | 3178 | — |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | — | epoch not in this light curve | — | — | 3178 | — |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | — | epoch not in this light curve | — | — | 3178 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021014023720-s0034-0000000319610598-0204-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2020238165205-s0029-0000000319610598-0193-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2020351194500-s0033-0000000319610598-0203-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459964.18189 | -0.01039 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459199.90772 | -0.01930 | 49 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.24572 | -0.01651 | 34 | SAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.46030 | -0.01516 | 3 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459199.95008 | -0.01425 | 10 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.31933 | -0.01419 | 70 | SAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.40475 | -0.01348 | 51 | SAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.44919 | -0.01232 | 11 | SAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459987.79839 | -0.01229 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459199.86675 | -0.01214 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.46933 | -0.01190 | 4 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459199.84314 | -0.01176 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459199.86119 | -0.01161 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459987.74145 | -0.01139 | 2 | PDCSAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459987.80395 | -0.01127 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459185.67694 | -0.01111 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.50058 | -0.01090 | 23 | SAP | 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459987.79353 | -0.01072 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.47836 | -0.01056 | 7 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000319610598-0193-s_lc.fits` | 2459102.40905 | -0.01047 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459199.85147 | -0.01043 | 2 | PDCSAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.62489 | -0.01027 | 2 | SAP | 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459987.82409 | -0.01003 | 4 | PDCSAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.55267 | -0.01001 | 16 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.52906 | -0.01000 | 16 | SAP | 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459987.83034 | -0.00995 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.57628 | -0.00961 | 6 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.59086 | -0.00957 | 7 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.69295 | -0.00957 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459185.68180 | -0.00943 | 2 | PDCSAP | 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.30921 | -0.00925 | 2 | SAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459987.76367 | -0.00910 | 2 | PDCSAP | 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459964.73328 | -0.00905 | 2 | PDCSAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.56864 | -0.00901 | 3 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.62072 | -0.00878 | 2 | SAP | 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459982.17763 | -0.00872 | 2 | SAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459982.15541 | -0.00867 | 2 | SAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459969.30827 | -0.00861 | 2 | SAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.63600 | -0.00854 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.67906 | -0.00837 | 2 | SAP | 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459969.32772 | -0.00836 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2459994.19693 | -0.00828 | 2 | PDCSAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459178.75529 | -0.00827 | 2 | PDCSAP | 1 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.62975 | -0.00818 | 3 | SAP | 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459969.23744 | -0.00814 | 2 | SAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.65961 | -0.00802 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.70475 | -0.00790 | 3 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.20644 | -0.00785 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460006.96617 | -0.00775 | 3 | SAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000319610598-0200-s_lc.fits` | 2459187.64156 | -0.00773 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460006.94394 | -0.00762 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.21061 | -0.00761 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460013.90768 | -0.00757 | 2 | SAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459982.18735 | -0.00748 | 2 | SAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459982.13319 | -0.00712 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460013.86741 | -0.00706 | 2 | SAP | 2 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.14741 | -0.00684 | 3 | SAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459982.16860 | -0.00675 | 4 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.05644 | -0.00662 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.23144 | -0.00655 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460013.91463 | -0.00651 | 2 | SAP | 2 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459982.01097 | -0.00632 | 2 | SAP | 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459980.64153 | -0.00630 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.25505 | -0.00626 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460013.44381 | -0.00622 | 2 | SAP | 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459969.32077 | -0.00620 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.27449 | -0.00620 | 3 | SAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459969.16799 | -0.00616 | 2 | SAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459982.14430 | -0.00615 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.18908 | -0.00609 | 3 | SAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000319610598-0250-s_lc.fits` | 2459982.11096 | -0.00597 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000319610598-0254-s_lc.fits` | 2460007.30366 | -0.00594 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-4509.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T04:33:07Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T04:33:11Z: TOI-4509.01 (TIC 319610598, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T04:33:16Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T04:33:17Z: TYC 8536-665-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2459231.7639: not recovered, depth 3741 ± 230 ppm (catalogue 3178 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, ≤2.5, 3.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-4509-01.yaml
python -m cygnus.campaign report campaigns/toi-4509-01.yaml
```
