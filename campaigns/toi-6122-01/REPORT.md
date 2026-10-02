<!-- cygnus:generated-draft -->
# Known-object test, TOI-6122.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6122-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4665, calibrate_screen #4633, event_census #4646, fetch_independent #4649, fetch_products #4622, known_signal_recovery #4640, moving_objects #4648, period_aliases #4647, prior_art #4667, residual_screen #4645, stellar_context #4643, variability_guard #4666
- Runner finished (UTC): 2026-09-30T22:09:23Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6122.01 (BJD 2460312.8926: partial, depth 2522 ± 314 ppm (catalogue 5689 ppm); BJD 2460317.5033: recovered, depth 4177 ± 228 ppm (catalogue 5689 ppm); BJD 2460322.1140: recovered, depth 4538 ± 203 ppm (catalogue 5689 ppm); BJD 2460326.7247: recovered, depth 4783 ± 213 ppm (catalogue 5689 ppm); BJD 2460331.3354: partial, depth 4544 ± 228 ppm (catalogue 5689 ppm); BJD 2460335.9461: recovered, depth 4717 ± 200 ppm (catalogue 5689 ppm); BJD 2460340.5568: recovered, depth 4532 ± 235 ppm (catalogue 5689 ppm); BJD 2460345.1675: recovered, depth 5000 ± 227 ppm (catalogue 5689 ppm); BJD 2460349.7782: recovered, depth 4395 ± 205 ppm (catalogue 5689 ppm); BJD 2460354.3889: recovered, depth 5529 ± 203 ppm (catalogue 5689 ppm); BJD 2460358.9996: recovered, depth 4324 ± 239 ppm (catalogue 5689 ppm); BJD 2460363.6103: recovered, depth 4550 ± 201 ppm (catalogue 5689 ppm); BJD 2460368.2210: not recovered, depth 3652 ± 215 ppm (catalogue 5689 ppm); BJD 2460372.8317: recovered, depth 5851 ± 271 ppm (catalogue 5689 ppm); BJD 2460377.4424: not recovered, depth 4373 ± 203 ppm (catalogue 5689 ppm); BJD 2460382.0531: not recovered, depth 5056 ± 210 ppm (catalogue 5689 ppm); BJD 2460386.6638: not recovered, depth 3815 ± 238 ppm (catalogue 5689 ppm); BJD 2460391.2745: not recovered, depth 4433 ± 213 ppm (catalogue 5689 ppm); BJD 2460511.1528: recovered, depth 4737 ± 211 ppm (catalogue 5689 ppm); BJD 2460515.7635: recovered, depth 2472 ± 224 ppm (catalogue 5689 ppm); BJD 2460520.3742: recovered, depth 3810 ± 215 ppm (catalogue 5689 ppm); BJD 2460524.9849: recovered, depth 4906 ± 217 ppm (catalogue 5689 ppm); BJD 2460529.5956: recovered, depth 1874 ± 350 ppm (catalogue 5689 ppm); BJD 2460534.2063: recovered, depth 4652 ± 191 ppm (catalogue 5689 ppm); BJD 2460538.8170: recovered, depth 4441 ± 213 ppm (catalogue 5689 ppm); BJD 2460543.4277: recovered, depth 4514 ± 204 ppm (catalogue 5689 ppm); BJD 2460548.0384: recovered, depth 4614 ± 206 ppm (catalogue 5689 ppm); BJD 2460552.6491: recovered, depth 4852 ± 216 ppm (catalogue 5689 ppm); BJD 2460557.2598: recovered, depth 4221 ± 210 ppm (catalogue 5689 ppm); BJD 2460561.8705: recovered, depth 4347 ± 208 ppm (catalogue 5689 ppm); BJD 2460566.4812: recovered, depth 4996 ± 206 ppm (catalogue 5689 ppm); BJD 2460571.0919: recovered, depth 4302 ± 212 ppm (catalogue 5689 ppm); BJD 2460575.7026: recovered, depth 5025 ± 206 ppm (catalogue 5689 ppm); BJD 2460580.3133: recovered, depth 5289 ± 205 ppm (catalogue 5689 ppm)).
Outside the catalogued epoch the screen left 11 threshold entries forming **9 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6122.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 352442207 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 297.503626 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 54.153548 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459847.211624 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.6107024 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5689.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.626 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.6925 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | lightcurve | 74 | False | `e5e118bea2d53e90` | True |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | lightcurve | 75 | False | `b48886d9cb71250c` | True |
| `tess2024058030222-s0076-0000000352442207-0271-s_lc.fits` | lightcurve | 76 | False | `6c168d5c85465ffc` | True |
| `tess2024196212429-s0081-0000000352442207-0276-s_lc.fits` | lightcurve | 81 | False | `66689d8fce76150a` | True |
| `tess2024223182411-s0082-0000000352442207-0278-s_lc.fits` | lightcurve | 82 | False | `c1848c0859c8522f` | True |
| `tess2024249191853-s0083-0000000352442207-0280-s_lc.fits` | lightcurve | 83 | False | `4fc41a0738a56ab5` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | 2460312.89257 | partial | 105 | 2522 ± 314 | 5689 | 0.86 |
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | 2460317.50327 | recovered | 169 | 4177 ± 228 | 5689 | 1.35 |
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | 2460322.11397 | recovered | 169 | 4538 ± 203 | 5689 | -1.18 |
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | 2460326.72467 | recovered | 168 | 4783 ± 213 | 5689 | 0.52 |
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | 2460331.33538 | partial | 169 | 4544 ± 228 | 5689 | -0.71 |
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | 2460335.94608 | recovered | 169 | 4717 ± 200 | 5689 | -1.55 |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460340.55678 | recovered | 169 | 4532 ± 235 | 5689 | -0.84 |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460345.16748 | recovered | 168 | 5000 ± 227 | 5689 | -0.40 |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460349.77819 | recovered | 169 | 4395 ± 205 | 5689 | -0.44 |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460354.38889 | recovered | 169 | 5529 ± 203 | 5689 | -0.19 |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460358.99959 | recovered | 169 | 4324 ± 239 | 5689 | -1.12 |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460363.61029 | recovered | 168 | 4550 ± 201 | 5689 | -0.47 |
| `tess2024058030222-s0076-0000000352442207-0271-s_lc.fits` | 2460368.22100 | not_recovered | 169 | 3652 ± 215 | 5689 | — |
| `tess2024058030222-s0076-0000000352442207-0271-s_lc.fits` | 2460372.83170 | recovered | 169 | 5851 ± 271 | 5689 | 1.61 |
| `tess2024058030222-s0076-0000000352442207-0271-s_lc.fits` | 2460377.44240 | not_recovered | 168 | 4373 ± 203 | 5689 | — |
| `tess2024058030222-s0076-0000000352442207-0271-s_lc.fits` | 2460382.05310 | not_recovered | 169 | 5056 ± 210 | 5689 | — |
| `tess2024058030222-s0076-0000000352442207-0271-s_lc.fits` | 2460386.66380 | not_recovered | 169 | 3815 ± 238 | 5689 | — |
| `tess2024058030222-s0076-0000000352442207-0271-s_lc.fits` | 2460391.27451 | not_recovered | 168 | 4433 ± 213 | 5689 | — |
| `tess2024196212429-s0081-0000000352442207-0276-s_lc.fits` | 2460511.15277 | recovered | 169 | 4737 ± 211 | 5689 | 0.02 |
| `tess2024196212429-s0081-0000000352442207-0276-s_lc.fits` | 2460515.76347 | recovered | 169 | 2472 ± 224 | 5689 | 0.13 |
| `tess2024196212429-s0081-0000000352442207-0276-s_lc.fits` | 2460520.37417 | recovered | 169 | 3810 ± 215 | 5689 | 0.87 |
| `tess2024196212429-s0081-0000000352442207-0276-s_lc.fits` | 2460524.98488 | recovered | 169 | 4906 ± 217 | 5689 | -0.55 |
| `tess2024196212429-s0081-0000000352442207-0276-s_lc.fits` | 2460529.59558 | recovered | 73 | 1874 ± 350 | 5689 | -2.24 |
| `tess2024223182411-s0082-0000000352442207-0278-s_lc.fits` | 2460534.20628 | recovered | 169 | 4652 ± 191 | 5689 | -0.63 |
| `tess2024223182411-s0082-0000000352442207-0278-s_lc.fits` | 2460538.81698 | recovered | 168 | 4441 ± 213 | 5689 | 0.78 |
| `tess2024223182411-s0082-0000000352442207-0278-s_lc.fits` | 2460543.42769 | recovered | 169 | 4514 ± 204 | 5689 | 0.67 |
| `tess2024223182411-s0082-0000000352442207-0278-s_lc.fits` | 2460548.03839 | recovered | 168 | 4614 ± 206 | 5689 | -0.73 |
| `tess2024223182411-s0082-0000000352442207-0278-s_lc.fits` | 2460552.64909 | recovered | 169 | 4852 ± 216 | 5689 | 2.24 |
| `tess2024223182411-s0082-0000000352442207-0278-s_lc.fits` | 2460557.25979 | recovered | 169 | 4221 ± 210 | 5689 | 0.09 |
| `tess2024249191853-s0083-0000000352442207-0280-s_lc.fits` | 2460561.87050 | recovered | 169 | 4347 ± 208 | 5689 | -0.67 |
| `tess2024249191853-s0083-0000000352442207-0280-s_lc.fits` | 2460566.48120 | recovered | 169 | 4996 ± 206 | 5689 | -0.26 |
| `tess2024249191853-s0083-0000000352442207-0280-s_lc.fits` | 2460571.09190 | recovered | 166 | 4302 ± 212 | 5689 | 0.70 |
| `tess2024249191853-s0083-0000000352442207-0280-s_lc.fits` | 2460575.70260 | recovered | 169 | 5025 ± 206 | 5689 | 0.15 |
| `tess2024249191853-s0083-0000000352442207-0280-s_lc.fits` | 2460580.31331 | recovered | 169 | 5289 ± 205 | 5689 | 0.13 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024058030222-s0076-0000000352442207-0271-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2024196212429-s0081-0000000352442207-0276-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024223182411-s0082-0000000352442207-0278-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024249191853-s0083-0000000352442207-0280-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460345.65630 | -0.00887 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460360.00762 | -0.00856 | 2 | SAP | 1 | no |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460343.43966 | -0.00840 | 2 | SAP | 2 | no |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460345.77991 | -0.00832 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460359.81040 | -0.00820 | 2 | PDCSAP+SAP | 1 | no |
| `tess2024003055635-s0074-0000000352442207-0269-s_lc.fits` | 2460316.78314 | -0.00787 | 2 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460345.88685 | -0.00776 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460342.09662 | -0.00773 | 2 | PDCSAP | 1 | no |
| `tess2024030031500-s0075-0000000352442207-0270-s_lc.fits` | 2460362.68540 | -0.00755 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6122.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:09:09Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:09:12Z: TOI-6122.01 (TIC 352442207, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:09:14Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:09:16Z: UCAC4 721-066467 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460312.8926: partial, depth 2522 ± 314 ppm (catalogue 5689 ppm); BJD 2460317.5033: recovered, depth 4177 ± 228 ppm (catalogue 5689 ppm); BJD 2460322.1140: recovered, depth 4538 ± 203 ppm (catalogue 5689 ppm); BJD 2460326.7247: recovered, depth 4783 ± 213 ppm (catalogue 5689 ppm); BJD 2460331.3354: partial, depth 4544 ± 228 ppm (catalogue 5689 ppm); BJD 2460335.9461: recovered, depth 4717 ± 200 ppm (catalogue 5689 ppm); BJD 2460340.5568: recovered, depth 4532 ± 235 ppm (catalogue 5689 ppm); BJD 2460345.1675: recovered, depth 5000 ± 227 ppm (catalogue 5689 ppm); BJD 2460349.7782: recovered, depth 4395 ± 205 ppm (catalogue 5689 ppm); BJD 2460354.3889: recovered, depth 5529 ± 203 ppm (catalogue 5689 ppm); BJD 2460358.9996: recovered, depth 4324 ± 239 ppm (catalogue 5689 ppm); BJD 2460363.6103: recovered, depth 4550 ± 201 ppm (catalogue 5689 ppm); BJD 2460368.2210: not recovered, depth 3652 ± 215 ppm (catalogue 5689 ppm); BJD 2460372.8317: recovered, depth 5851 ± 271 ppm (catalogue 5689 ppm); BJD 2460377.4424: not recovered, depth 4373 ± 203 ppm (catalogue 5689 ppm); BJD 2460382.0531: not recovered, depth 5056 ± 210 ppm (catalogue 5689 ppm); BJD 2460386.6638: not recovered, depth 3815 ± 238 ppm (catalogue 5689 ppm); BJD 2460391.2745: not recovered, depth 4433 ± 213 ppm (catalogue 5689 ppm); BJD 2460511.1528: recovered, depth 4737 ± 211 ppm (catalogue 5689 ppm); BJD 2460515.7635: recovered, depth 2472 ± 224 ppm (catalogue 5689 ppm); BJD 2460520.3742: recovered, depth 3810 ± 215 ppm (catalogue 5689 ppm); BJD 2460524.9849: recovered, depth 4906 ± 217 ppm (catalogue 5689 ppm); BJD 2460529.5956: recovered, depth 1874 ± 350 ppm (catalogue 5689 ppm); BJD 2460534.2063: recovered, depth 4652 ± 191 ppm (catalogue 5689 ppm); BJD 2460538.8170: recovered, depth 4441 ± 213 ppm (catalogue 5689 ppm); BJD 2460543.4277: recovered, depth 4514 ± 204 ppm (catalogue 5689 ppm); BJD 2460548.0384: recovered, depth 4614 ± 206 ppm (catalogue 5689 ppm); BJD 2460552.6491: recovered, depth 4852 ± 216 ppm (catalogue 5689 ppm); BJD 2460557.2598: recovered, depth 4221 ± 210 ppm (catalogue 5689 ppm); BJD 2460561.8705: recovered, depth 4347 ± 208 ppm (catalogue 5689 ppm); BJD 2460566.4812: recovered, depth 4996 ± 206 ppm (catalogue 5689 ppm); BJD 2460571.0919: recovered, depth 4302 ± 212 ppm (catalogue 5689 ppm); BJD 2460575.7026: recovered, depth 5025 ± 206 ppm (catalogue 5689 ppm); BJD 2460580.3133: recovered, depth 5289 ± 205 ppm (catalogue 5689 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3.5, ≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 20%, 0%, 0%, 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6122.01: Gaia DR3 2137831756974531072 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-6122.01: dwarf priors not applied — 1.15 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6122.01: 17 Gaia neighbour(s) within 52.5", contamination 7.70%; depth 4177 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 2137843477944778880, 37.4", ΔG 3.10); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6122.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6122.01: UCAC4 721-066467 otype * (star_or_other) at 0.0" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6122-01.yaml
python -m cygnus.multi report campaigns/toi-6122-01.yaml
```
