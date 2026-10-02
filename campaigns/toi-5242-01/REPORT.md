<!-- cygnus:generated-draft -->
# Known-object test, TOI-5242.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5242-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4465, calibrate_screen #4444, event_census #4459, fetch_independent #4463, fetch_products #4436, known_signal_recovery #4445, moving_objects #4461, period_aliases #4460, prior_art #4468, residual_screen #4453, stellar_context #4446, variability_guard #4466
- Runner finished (UTC): 2026-09-30T21:54:18Z

## Bottom line

Positive control **inconclusive**: BJD 2460313.1404: not recovered, depth -4169 ± 2197 ppm (catalogue 16500 ppm); BJD 2460315.5442: not recovered, depth 20741 ± 1760 ppm (catalogue 16500 ppm); BJD 2460317.9481: partial, depth 20496 ± 2060 ppm (catalogue 16500 ppm); BJD 2460320.3519: partial, depth 20219 ± 1692 ppm (catalogue 16500 ppm); BJD 2460322.7558: partial, depth 17481 ± 1586 ppm (catalogue 16500 ppm); BJD 2460325.1596: not recovered, depth 18775 ± 1936 ppm (catalogue 16500 ppm); BJD 2460327.5635: gap (catalogue 16500 ppm); BJD 2460329.9673: not recovered, depth 19211 ± 1866 ppm (catalogue 16500 ppm); BJD 2460332.3712: not recovered, depth 14589 ± 1811 ppm (catalogue 16500 ppm); BJD 2460334.7750: not recovered, depth 16496 ± 1514 ppm (catalogue 16500 ppm); BJD 2460337.1789: partial, depth 22604 ± 1476 ppm (catalogue 16500 ppm); BJD 2460481.4098: not recovered, depth 12910 ± 2035 ppm (catalogue 16500 ppm); BJD 2460483.8136: not recovered, depth 9278 ± 2103 ppm (catalogue 16500 ppm); BJD 2460486.2175: not recovered, depth 10358 ± 2823 ppm (catalogue 16500 ppm); BJD 2460488.6213: gap (catalogue 16500 ppm); BJD 2460491.0252: not recovered, depth 3367 ± 3412 ppm (catalogue 16500 ppm); BJD 2460493.4290: gap (catalogue 16500 ppm); BJD 2460495.8329: not recovered, depth 11566 ± 1848 ppm (catalogue 16500 ppm); BJD 2460498.2367: not recovered, depth 14139 ± 2025 ppm (catalogue 16500 ppm); BJD 2460500.6406: not recovered, depth 27329 ± 2307 ppm (catalogue 16500 ppm); BJD 2460503.0444: not recovered, depth 18851 ± 2354 ppm (catalogue 16500 ppm); BJD 2460505.4483: not recovered, depth 2249 ± 2730 ppm (catalogue 16500 ppm); BJD 2460507.8521: not recovered, depth 25375 ± 2529 ppm (catalogue 16500 ppm); BJD 2460510.2560: not recovered, depth 10277 ± 2512 ppm (catalogue 16500 ppm); BJD 2460512.6598: partial, depth 26099 ± 3393 ppm (catalogue 16500 ppm); BJD 2460515.0637: not recovered, depth 11515 ± 2309 ppm (catalogue 16500 ppm); BJD 2460517.4675: not recovered, depth 19520 ± 2955 ppm (catalogue 16500 ppm); BJD 2460519.8714: partial, depth 24220 ± 2827 ppm (catalogue 16500 ppm); BJD 2460522.2752: not recovered, depth 15449 ± 2301 ppm (catalogue 16500 ppm); BJD 2460524.6791: not recovered, depth 17131 ± 2312 ppm (catalogue 16500 ppm); BJD 2460527.0829: not recovered, depth 21164 ± 2348 ppm (catalogue 16500 ppm); BJD 2460529.4868: not recovered, depth 18018 ± 2311 ppm (catalogue 16500 ppm); BJD 2460531.8906: gap (catalogue 16500 ppm).
Outside the catalogued epoch the screen left 88 threshold entries forming **37 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5242.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 426122503 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 287.658473 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 35.4957 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459445.351035 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.4038486 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 16500.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.87 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.789 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-09-19 12:04:41 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | lightcurve | 74 | False | `cda0385178357b37` | True |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | lightcurve | 80 | False | `2ce3e80736d23bfe` | True |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | lightcurve | 81 | False | `e14044baef1910b4` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460313.14038 | not_recovered | 56 | -4169 ± 2197 | 16500 | — |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460315.54423 | not_recovered | 56 | 20741 ± 1760 | 16500 | — |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460317.94808 | partial | 56 | 20496 ± 2060 | 16500 | 0.17 |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460320.35193 | partial | 56 | 20219 ± 1692 | 16500 | 0.01 |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460322.75577 | partial | 56 | 17481 ± 1586 | 16500 | 0.41 |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460325.15962 | not_recovered | 56 | 18775 ± 1936 | 16500 | — |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460327.56347 | gap | 0 | — | 16500 | — |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460329.96732 | not_recovered | 56 | 19211 ± 1866 | 16500 | — |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460332.37117 | not_recovered | 56 | 14589 ± 1811 | 16500 | — |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460334.77502 | not_recovered | 56 | 16496 ± 1514 | 16500 | — |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460337.17887 | partial | 56 | 22604 ± 1476 | 16500 | -0.17 |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460481.40978 | not_recovered | 56 | 12910 ± 2035 | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460483.81363 | not_recovered | 56 | 9278 ± 2103 | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460486.21748 | not_recovered | 56 | 10358 ± 2823 | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460488.62133 | gap | 0 | — | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460491.02518 | not_recovered | 46 | 3367 ± 3412 | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460493.42902 | gap | 0 | — | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460495.83287 | not_recovered | 56 | 11566 ± 1848 | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460498.23672 | not_recovered | 56 | 14139 ± 2025 | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460500.64057 | not_recovered | 56 | 27329 ± 2307 | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460503.04442 | not_recovered | 56 | 18851 ± 2354 | 16500 | — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460505.44827 | not_recovered | 56 | 2249 ± 2730 | 16500 | — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460507.85212 | not_recovered | 56 | 25375 ± 2529 | 16500 | — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460510.25596 | not_recovered | 56 | 10277 ± 2512 | 16500 | — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460512.65981 | partial | 56 | 26099 ± 3393 | 16500 | 0.22 |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460515.06366 | not_recovered | 56 | 11515 ± 2309 | 16500 | — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460517.46751 | not_recovered | 56 | 19520 ± 2955 | 16500 | — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460519.87136 | partial | 56 | 24220 ± 2827 | 16500 | -0.99 |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460522.27521 | not_recovered | 57 | 15449 ± 2301 | 16500 | — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460524.67906 | not_recovered | 56 | 17131 ± 2312 | 16500 | — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460527.08290 | not_recovered | 56 | 21164 ± 2348 | 16500 | — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460529.48675 | not_recovered | 56 | 18018 ± 2311 | 16500 | — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460531.89060 | gap | 0 | — | 16500 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460312.86341 | -0.09938 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.94651 | -0.08924 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.96317 | -0.08065 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460312.91897 | -0.09346 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460312.89050 | -0.08460 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460312.87730 | -0.07673 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.97567 | -0.07115 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460312.88494 | -0.06552 | 3 | PDCSAP | 1 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.89512 | -0.06544 | 2 | PDCSAP | 1, 2 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.91109 | -0.06516 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460492.98553 | -0.06399 | 2 | PDCSAP | 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.90137 | -0.06397 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460493.17581 | -0.06066 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.87984 | -0.05987 | 2 | PDCSAP | 2 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460493.30637 | -0.05955 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.99651 | -0.05779 | 2 | PDCSAP | 1, 2 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460312.89953 | -0.05743 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.91803 | -0.05683 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460312.92800 | -0.04876 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460479.91859 | -0.02731 | 2 | SAP | 1, 2 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460493.29804 | -0.02630 | 2 | SAP | 1 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.67983 | -0.02561 | 2 | SAP | 1, 2 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460492.62302 | -0.02444 | 2 | SAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460492.23274 | -0.02340 | 2 | SAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460486.68402 | -0.02159 | 2 | SAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460485.93678 | -0.02106 | 2 | SAP | 1 | no |
| `tess2024170053053-s0080-0000000426122503-0275-s_lc.fits` | 2460492.66469 | -0.01976 | 2 | SAP | 2, 3 | no |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460506.56205 | -0.01771 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460312.87036 | -0.01748 | 2 | SAP | 1 | no |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460513.62038 | -0.01722 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460326.29664 | -0.01694 | 2 | SAP | 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460326.11469 | -0.01629 | 2 | SAP | 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460326.75775 | -0.01487 | 2 | SAP | 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460326.51886 | -0.01441 | 2 | SAP | 3 | no |
| `tess2024003055635-s0074-0000000426122503-0269-s_lc.fits` | 2460326.47025 | -0.01436 | 2 | SAP | 3 | no |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460511.38150 | -0.01249 | 2 | SAP | 1 | no |
| `tess2024196212429-s0081-0000000426122503-0276-s_lc.fits` | 2460511.39261 | -0.01245 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5242.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:54:08Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:54:11Z: TOI-5242.01 (TIC 426122503, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:54:14Z
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T21:54:16Z: TYC 2648-208-1 (*); TYC 2648-756-1 (*); UCAC4 628-067053 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2460313.1404: not recovered, depth -4169 ± 2197 ppm (catalogue 16500 ppm); BJD 2460315.5442: not recovered, depth 20741 ± 1760 ppm (catalogue 16500 ppm); BJD 2460317.9481: partial, depth 20496 ± 2060 ppm (catalogue 16500 ppm); BJD 2460320.3519: partial, depth 20219 ± 1692 ppm (catalogue 16500 ppm); BJD 2460322.7558: partial, depth 17481 ± 1586 ppm (catalogue 16500 ppm); BJD 2460325.1596: not recovered, depth 18775 ± 1936 ppm (catalogue 16500 ppm); BJD 2460327.5635: gap (catalogue 16500 ppm); BJD 2460329.9673: not recovered, depth 19211 ± 1866 ppm (catalogue 16500 ppm); BJD 2460332.3712: not recovered, depth 14589 ± 1811 ppm (catalogue 16500 ppm); BJD 2460334.7750: not recovered, depth 16496 ± 1514 ppm (catalogue 16500 ppm); BJD 2460337.1789: partial, depth 22604 ± 1476 ppm (catalogue 16500 ppm); BJD 2460481.4098: not recovered, depth 12910 ± 2035 ppm (catalogue 16500 ppm); BJD 2460483.8136: not recovered, depth 9278 ± 2103 ppm (catalogue 16500 ppm); BJD 2460486.2175: not recovered, depth 10358 ± 2823 ppm (catalogue 16500 ppm); BJD 2460488.6213: gap (catalogue 16500 ppm); BJD 2460491.0252: not recovered, depth 3367 ± 3412 ppm (catalogue 16500 ppm); BJD 2460493.4290: gap (catalogue 16500 ppm); BJD 2460495.8329: not recovered, depth 11566 ± 1848 ppm (catalogue 16500 ppm); BJD 2460498.2367: not recovered, depth 14139 ± 2025 ppm (catalogue 16500 ppm); BJD 2460500.6406: not recovered, depth 27329 ± 2307 ppm (catalogue 16500 ppm); BJD 2460503.0444: not recovered, depth 18851 ± 2354 ppm (catalogue 16500 ppm); BJD 2460505.4483: not recovered, depth 2249 ± 2730 ppm (catalogue 16500 ppm); BJD 2460507.8521: not recovered, depth 25375 ± 2529 ppm (catalogue 16500 ppm); BJD 2460510.2560: not recovered, depth 10277 ± 2512 ppm (catalogue 16500 ppm); BJD 2460512.6598: partial, depth 26099 ± 3393 ppm (catalogue 16500 ppm); BJD 2460515.0637: not recovered, depth 11515 ± 2309 ppm (catalogue 16500 ppm); BJD 2460517.4675: not recovered, depth 19520 ± 2955 ppm (catalogue 16500 ppm); BJD 2460519.8714: partial, depth 24220 ± 2827 ppm (catalogue 16500 ppm); BJD 2460522.2752: not recovered, depth 15449 ± 2301 ppm (catalogue 16500 ppm); BJD 2460524.6791: not recovered, depth 17131 ± 2312 ppm (catalogue 16500 ppm); BJD 2460527.0829: not recovered, depth 21164 ± 2348 ppm (catalogue 16500 ppm); BJD 2460529.4868: not recovered, depth 18018 ± 2311 ppm (catalogue 16500 ppm); BJD 2460531.8906: gap (catalogue 16500 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5242.01: Gaia DR3 2050575068253331968 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5242.01: Teff 5106 K, R* 0.79 ± 0.06, M* 0.84 ± 0.08, ρ* 1.70 ± 0.44 ρ☉ (dwarf sequence, M_G 5.73, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5242.01: 45 Gaia neighbour(s) within 52.5", contamination 95.01%; depth 16500 ppm (catalogue depth); 2 could produce it if fully eclipsed (brightest 2050575068253338240, 23.9", ΔG -2.58); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 0 clean; BJD 2460312.8634 suspect: coarse point (in event), earth point (in event), manual exclude (in event), momentum dump (in event), MOM_CENTR1 z=+10.6, POS_CORR1 z=-18.1, POS_CORR2 z=-5.0; BJD 2460485.9465 suspect: manual exclude (in event), MOM_CENTR1 z=+10.1, POS_CORR1 z=+25.8; BJD 2460485.9632 suspect: manual exclude (in event), MOM_CENTR1 z=+12.5, POS_CORR1 z=+33.2 |
| Moving objects at screen-event epochs | passed | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5242.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5242.01: UCAC4 628-067053 otype * (star_or_other) at 0.7" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5242-01.yaml
python -m cygnus.multi report campaigns/toi-5242-01.yaml
```
