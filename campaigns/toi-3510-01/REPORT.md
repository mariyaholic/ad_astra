<!-- cygnus:generated-draft -->
# Known-object test, TOI-3510.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3510-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4271, calibrate_screen #4248, event_census #4256, fetch_independent #4259, fetch_products #4239, known_signal_recovery #4251, moving_objects #4258, period_aliases #4257, prior_art #4274, residual_screen #4255, stellar_context #4252, variability_guard #4272
- Runner finished (UTC): 2026-09-30T21:45:20Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3510.01 (BJD 2459772.0354: recovered, depth 11301 ± 1007 ppm (catalogue 13480 ppm); BJD 2459774.9079: recovered, depth 13705 ± 1132 ppm (catalogue 13480 ppm); BJD 2459777.7804: gap (catalogue 13480 ppm); BJD 2459780.6529: gap (catalogue 13480 ppm); BJD 2459783.5254: not recovered, depth 3357 ± 1563 ppm (catalogue 13480 ppm); BJD 2459786.3979: recovered, depth 11492 ± 1012 ppm (catalogue 13480 ppm); BJD 2459789.2704: recovered, depth 15745 ± 1186 ppm (catalogue 13480 ppm); BJD 2459792.1429: gap (catalogue 13480 ppm); BJD 2459795.0154: recovered, depth 16671 ± 1415 ppm (catalogue 13480 ppm); BJD 2459797.8878: not recovered, depth 19154 ± 1384 ppm (catalogue 13480 ppm); BJD 2459800.7603: not recovered, depth 15089 ± 1397 ppm (catalogue 13480 ppm); BJD 2459803.6328: not recovered, depth 15541 ± 1365 ppm (catalogue 13480 ppm); BJD 2459806.5053: not recovered, depth 9062 ± 1554 ppm (catalogue 13480 ppm); BJD 2459809.3778: partial, depth 37701 ± 3557 ppm (catalogue 13480 ppm); BJD 2459812.2503: not recovered, depth 17104 ± 1300 ppm (catalogue 13480 ppm); BJD 2459815.1228: not recovered, depth 15352 ± 1258 ppm (catalogue 13480 ppm); BJD 2459817.9953: not recovered, depth 11453 ± 1350 ppm (catalogue 13480 ppm); BJD 2459820.8678: not recovered, depth 24568 ± 1682 ppm (catalogue 13480 ppm); BJD 2459823.7402: not recovered, depth 15779 ± 1608 ppm (catalogue 13480 ppm); BJD 2460314.9359: recovered, depth 13476 ± 1456 ppm (catalogue 13480 ppm); BJD 2460317.8084: not recovered, depth 16506 ± 1220 ppm (catalogue 13480 ppm); BJD 2460320.6809: not recovered, depth 17214 ± 1069 ppm (catalogue 13480 ppm); BJD 2460323.5534: not recovered, depth 13027 ± 1066 ppm (catalogue 13480 ppm); BJD 2460326.4259: not recovered, depth 13251 ± 1068 ppm (catalogue 13480 ppm); BJD 2460329.2984: not recovered, depth 12933 ± 1374 ppm (catalogue 13480 ppm); BJD 2460332.1709: not recovered, depth 16909 ± 1160 ppm (catalogue 13480 ppm); BJD 2460335.0434: not recovered, depth 15050 ± 1087 ppm (catalogue 13480 ppm); BJD 2460337.9158: not recovered, depth 17263 ± 1080 ppm (catalogue 13480 ppm); BJD 2460340.7883: not recovered, depth 17082 ± 1308 ppm (catalogue 13480 ppm); BJD 2460343.6608: recovered, depth 18355 ± 1177 ppm (catalogue 13480 ppm); BJD 2460346.5333: recovered, depth 15618 ± 1034 ppm (catalogue 13480 ppm); BJD 2460349.4058: recovered, depth 16520 ± 1051 ppm (catalogue 13480 ppm); BJD 2460352.2783: not recovered, depth 14906 ± 1041 ppm (catalogue 13480 ppm); BJD 2460355.1508: recovered, depth 18353 ± 1138 ppm (catalogue 13480 ppm); BJD 2460358.0233: partial, depth 16878 ± 1077 ppm (catalogue 13480 ppm); BJD 2460360.8958: not recovered, depth 15960 ± 1070 ppm (catalogue 13480 ppm); BJD 2460363.7683: not recovered, depth 13918 ± 1075 ppm (catalogue 13480 ppm); BJD 2460366.6407: recovered, depth 16956 ± 969 ppm (catalogue 13480 ppm); BJD 2460507.3927: not recovered, depth 16121 ± 1022 ppm (catalogue 13480 ppm); BJD 2460510.2652: not recovered, depth 13017 ± 921 ppm (catalogue 13480 ppm); BJD 2460513.1377: not recovered, depth 12641 ± 1107 ppm (catalogue 13480 ppm); BJD 2460516.0102: gap (catalogue 13480 ppm); BJD 2460518.8827: gap (catalogue 13480 ppm); BJD 2460521.7552: not recovered, depth 14622 ± 947 ppm (catalogue 13480 ppm); BJD 2460524.6277: not recovered, depth 12293 ± 909 ppm (catalogue 13480 ppm); BJD 2460527.5002: recovered, depth 15297 ± 979 ppm (catalogue 13480 ppm); BJD 2460530.3726: recovered, depth 17782 ± 1129 ppm (catalogue 13480 ppm)).
Outside the catalogued epoch the screen left 24 threshold entries forming **6 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459776.8702 matches the catalogued transit's depth (8142 vs 11301 ppm), 4.810 d later; 0 of 4 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3510.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 57753734 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 296.354017 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 30.779967 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459772.035438 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.8724894 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 13480.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.772 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.7595 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | lightcurve | 54 | True | `9d8b348d1984d8e9` | True |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | lightcurve | 55 | False | `a7c6ff99fd211daa` | True |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | lightcurve | 74 | False | `7657833184ad85df` | True |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | lightcurve | 75 | False | `6f236bc8497521ad` | True |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | lightcurve | 81 | False | `9ecb327527fb820c` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459772.03544 | recovered | 84 | 11301 ± 1007 | 13480 | 0.60 |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459774.90793 | recovered | 83 | 13705 ± 1132 | 13480 | -0.01 |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459777.78042 | gap | 0 | — | 13480 | — |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459780.65291 | gap | 0 | — | 13480 | — |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459783.52540 | not_recovered | 35 | 3357 ± 1563 | 13480 | — |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459786.39789 | recovered | 83 | 11492 ± 1012 | 13480 | -0.63 |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459789.27037 | recovered | 84 | 15745 ± 1186 | 13480 | -0.77 |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459792.14286 | gap | 0 | — | 13480 | — |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459795.01535 | recovered | 83 | 16671 ± 1415 | 13480 | -0.30 |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459797.88784 | not_recovered | 83 | 19154 ± 1384 | 13480 | — |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459800.76033 | not_recovered | 83 | 15089 ± 1397 | 13480 | — |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459803.63282 | not_recovered | 83 | 15541 ± 1365 | 13480 | — |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459806.50531 | not_recovered | 83 | 9062 ± 1554 | 13480 | — |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459809.37780 | partial | 83 | 37701 ± 3557 | 13480 | 0.88 |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459812.25029 | not_recovered | 83 | 17104 ± 1300 | 13480 | — |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459815.12278 | not_recovered | 84 | 15352 ± 1258 | 13480 | — |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459817.99527 | not_recovered | 83 | 11453 ± 1350 | 13480 | — |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459820.86776 | not_recovered | 83 | 24568 ± 1682 | 13480 | — |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 2459823.74025 | not_recovered | 83 | 15779 ± 1608 | 13480 | — |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460314.93593 | recovered | 83 | 13476 ± 1456 | 13480 | -0.35 |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460317.80842 | not_recovered | 83 | 16506 ± 1220 | 13480 | — |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460320.68091 | not_recovered | 84 | 17214 ± 1069 | 13480 | — |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460323.55340 | not_recovered | 83 | 13027 ± 1066 | 13480 | — |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460326.42589 | not_recovered | 83 | 13251 ± 1068 | 13480 | — |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460329.29838 | not_recovered | 83 | 12933 ± 1374 | 13480 | — |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460332.17087 | not_recovered | 83 | 16909 ± 1160 | 13480 | — |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460335.04336 | not_recovered | 84 | 15050 ± 1087 | 13480 | — |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460337.91585 | not_recovered | 83 | 17263 ± 1080 | 13480 | — |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460340.78834 | not_recovered | 83 | 17082 ± 1308 | 13480 | — |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460343.66083 | recovered | 83 | 18355 ± 1177 | 13480 | -0.49 |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460346.53332 | recovered | 83 | 15618 ± 1034 | 13480 | -0.86 |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460349.40581 | recovered | 84 | 16520 ± 1051 | 13480 | 0.64 |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460352.27830 | not_recovered | 82 | 14906 ± 1041 | 13480 | — |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460355.15079 | recovered | 83 | 18353 ± 1138 | 13480 | 0.59 |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460358.02328 | partial | 83 | 16878 ± 1077 | 13480 | -0.18 |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460360.89577 | not_recovered | 83 | 15960 ± 1070 | 13480 | — |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460363.76825 | not_recovered | 83 | 13918 ± 1075 | 13480 | — |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 2460366.64074 | recovered | 83 | 16956 ± 969 | 13480 | -0.09 |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 2460507.39272 | not_recovered | 83 | 16121 ± 1022 | 13480 | — |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 2460510.26521 | not_recovered | 84 | 13017 ± 921 | 13480 | — |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 2460513.13770 | not_recovered | 81 | 12641 ± 1107 | 13480 | — |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 2460516.01019 | gap | 0 | — | 13480 | — |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 2460518.88268 | gap | 0 | — | 13480 | — |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 2460521.75517 | not_recovered | 83 | 14622 ± 947 | 13480 | — |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 2460524.62766 | not_recovered | 83 | 12293 ± 909 | 13480 | — |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 2460527.50015 | recovered | 84 | 15297 ± 979 | 13480 | -1.02 |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 2460530.37264 | recovered | 83 | 17782 ± 1129 | 13480 | -0.34 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2022217014003-s0055-0000000057753734-0242-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024030031500-s0075-0000000057753734-0270-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024196212429-s0081-0000000057753734-0276-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459794.15084 | -0.03862 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459776.87019 | -0.03678 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459777.00075 | -0.03296 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459794.44112 | -0.02711 | 2 | PDCSAP | 2 | no |
| `tess2024003055635-s0074-0000000057753734-0269-s_lc.fits` | 2460312.87424 | -0.02574 | 2 | SAP | 1, 2, 3 | no |
| `tess2022190063128-s0054-0000000057753734-0227-s_lc.fits` | 2459775.47156 | -0.01678 | 2 | SAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459776.87019 | 8142 | 11301 | 4.8098 | 0 / 4 |  |
| 2459777.00075 | 8636 | 11301 | 4.9404 | 0 / 4 |  |
| 2459794.15084 | 8997 | 11301 | 22.0904 | 0 / 22 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3510.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:45:10Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:45:13Z: TOI-3510.01 (TIC 57753734, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:45:16Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:45:18Z: TOI-3510 (*); TOI-3510.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459772.0354: recovered, depth 11301 ± 1007 ppm (catalogue 13480 ppm); BJD 2459774.9079: recovered, depth 13705 ± 1132 ppm (catalogue 13480 ppm); BJD 2459777.7804: gap (catalogue 13480 ppm); BJD 2459780.6529: gap (catalogue 13480 ppm); BJD 2459783.5254: not recovered, depth 3357 ± 1563 ppm (catalogue 13480 ppm); BJD 2459786.3979: recovered, depth 11492 ± 1012 ppm (catalogue 13480 ppm); BJD 2459789.2704: recovered, depth 15745 ± 1186 ppm (catalogue 13480 ppm); BJD 2459792.1429: gap (catalogue 13480 ppm); BJD 2459795.0154: recovered, depth 16671 ± 1415 ppm (catalogue 13480 ppm); BJD 2459797.8878: not recovered, depth 19154 ± 1384 ppm (catalogue 13480 ppm); BJD 2459800.7603: not recovered, depth 15089 ± 1397 ppm (catalogue 13480 ppm); BJD 2459803.6328: not recovered, depth 15541 ± 1365 ppm (catalogue 13480 ppm); BJD 2459806.5053: not recovered, depth 9062 ± 1554 ppm (catalogue 13480 ppm); BJD 2459809.3778: partial, depth 37701 ± 3557 ppm (catalogue 13480 ppm); BJD 2459812.2503: not recovered, depth 17104 ± 1300 ppm (catalogue 13480 ppm); BJD 2459815.1228: not recovered, depth 15352 ± 1258 ppm (catalogue 13480 ppm); BJD 2459817.9953: not recovered, depth 11453 ± 1350 ppm (catalogue 13480 ppm); BJD 2459820.8678: not recovered, depth 24568 ± 1682 ppm (catalogue 13480 ppm); BJD 2459823.7402: not recovered, depth 15779 ± 1608 ppm (catalogue 13480 ppm); BJD 2460314.9359: recovered, depth 13476 ± 1456 ppm (catalogue 13480 ppm); BJD 2460317.8084: not recovered, depth 16506 ± 1220 ppm (catalogue 13480 ppm); BJD 2460320.6809: not recovered, depth 17214 ± 1069 ppm (catalogue 13480 ppm); BJD 2460323.5534: not recovered, depth 13027 ± 1066 ppm (catalogue 13480 ppm); BJD 2460326.4259: not recovered, depth 13251 ± 1068 ppm (catalogue 13480 ppm); BJD 2460329.2984: not recovered, depth 12933 ± 1374 ppm (catalogue 13480 ppm); BJD 2460332.1709: not recovered, depth 16909 ± 1160 ppm (catalogue 13480 ppm); BJD 2460335.0434: not recovered, depth 15050 ± 1087 ppm (catalogue 13480 ppm); BJD 2460337.9158: not recovered, depth 17263 ± 1080 ppm (catalogue 13480 ppm); BJD 2460340.7883: not recovered, depth 17082 ± 1308 ppm (catalogue 13480 ppm); BJD 2460343.6608: recovered, depth 18355 ± 1177 ppm (catalogue 13480 ppm); BJD 2460346.5333: recovered, depth 15618 ± 1034 ppm (catalogue 13480 ppm); BJD 2460349.4058: recovered, depth 16520 ± 1051 ppm (catalogue 13480 ppm); BJD 2460352.2783: not recovered, depth 14906 ± 1041 ppm (catalogue 13480 ppm); BJD 2460355.1508: recovered, depth 18353 ± 1138 ppm (catalogue 13480 ppm); BJD 2460358.0233: partial, depth 16878 ± 1077 ppm (catalogue 13480 ppm); BJD 2460360.8958: not recovered, depth 15960 ± 1070 ppm (catalogue 13480 ppm); BJD 2460363.7683: not recovered, depth 13918 ± 1075 ppm (catalogue 13480 ppm); BJD 2460366.6407: recovered, depth 16956 ± 969 ppm (catalogue 13480 ppm); BJD 2460507.3927: not recovered, depth 16121 ± 1022 ppm (catalogue 13480 ppm); BJD 2460510.2652: not recovered, depth 13017 ± 921 ppm (catalogue 13480 ppm); BJD 2460513.1377: not recovered, depth 12641 ± 1107 ppm (catalogue 13480 ppm); BJD 2460516.0102: gap (catalogue 13480 ppm); BJD 2460518.8827: gap (catalogue 13480 ppm); BJD 2460521.7552: not recovered, depth 14622 ± 947 ppm (catalogue 13480 ppm); BJD 2460524.6277: not recovered, depth 12293 ± 909 ppm (catalogue 13480 ppm); BJD 2460527.5002: recovered, depth 15297 ± 979 ppm (catalogue 13480 ppm); BJD 2460530.3726: recovered, depth 17782 ± 1129 ppm (catalogue 13480 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 4, 3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2459776.8702, ΔT = 4.810 d, 0 of 4 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3510.01: Gaia DR3 2032206627049041280 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3510.01: Teff 5490 K, R* 1.02 ± 0.08, M* 1.00 ± 0.10, ρ* 0.95 ± 0.25 ρ☉ (dwarf sequence, M_G 4.62, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3510.01: 182 Gaia neighbour(s) within 52.5", contamination 60.11%; depth 11301 ppm (measured depth of the recovered catalogued transit); 9 could produce it if fully eclipsed (brightest 2032206592689295104, 52.2", ΔG 1.04); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 0 clean; BJD 2459776.8702 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+44.8; BJD 2459777.0008 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+36.5; BJD 2459794.1508 suspect: scattered light 2 (within ±0.25 d), POS_CORR2 z=-5.3, SAP_BKG z=+17.0 |
| Moving objects at screen-event epochs | passed | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3510.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3510.01: TOI-3510 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | 3 possible published-ephemeris overlap(s) within 1 d (TOI-3510.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3510-01.yaml
python -m cygnus.multi report campaigns/toi-3510-01.yaml
```
