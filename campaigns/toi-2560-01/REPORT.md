<!-- cygnus:generated-draft -->
# Known-object test, TOI-2560.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2560-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4319, calibrate_screen #4287, event_census #4292, fetch_independent #4315, fetch_products #4278, known_signal_recovery #4289, moving_objects #4294, period_aliases #4293, prior_art #4322, residual_screen #4291, stellar_context #4290, variability_guard #4320
- Runner finished (UTC): 2026-09-30T21:47:55Z

## Bottom line

Positive control **failed**: BJD 2460156.4392: not recovered, depth 577 ± 1060 ppm (catalogue 19660 ppm); BJD 2460159.9904: not recovered, depth -1293 ± 973 ppm (catalogue 19660 ppm); BJD 2460163.5415: not recovered, depth 1909 ± 1029 ppm (catalogue 19660 ppm); BJD 2460167.0926: gap (catalogue 19660 ppm); BJD 2460170.6437: not recovered, depth -1718 ± 1013 ppm (catalogue 19660 ppm); BJD 2460174.1948: not recovered, depth -161 ± 1026 ppm (catalogue 19660 ppm); BJD 2460177.7460: not recovered, depth -2451 ± 1059 ppm (catalogue 19660 ppm); BJD 2460181.2971: gap (catalogue 19660 ppm); BJD 2460884.4189: not recovered, depth 175 ± 1126 ppm (catalogue 19660 ppm); BJD 2460887.9700: not recovered, depth -1562 ± 1112 ppm (catalogue 19660 ppm); BJD 2460891.5211: not recovered, depth -2616 ± 1082 ppm (catalogue 19660 ppm); BJD 2460895.0723: gap (catalogue 19660 ppm); BJD 2460898.6234: not recovered, depth 1362 ± 1152 ppm (catalogue 19660 ppm); BJD 2460902.1745: not recovered, depth -1525 ± 1150 ppm (catalogue 19660 ppm); BJD 2460905.7256: not recovered, depth -1191 ± 1171 ppm (catalogue 19660 ppm); BJD 2461235.9798: not recovered, depth -1598 ± 1161 ppm (catalogue 19660 ppm); BJD 2461239.5309: not recovered, depth 807 ± 1116 ppm (catalogue 19660 ppm); BJD 2461243.0820: not recovered, depth -1416 ± 1065 ppm (catalogue 19660 ppm); BJD 2461246.6332: not recovered, depth 1781 ± 1317 ppm (catalogue 19660 ppm); BJD 2461250.1843: gap (catalogue 19660 ppm); BJD 2461253.7354: gap (catalogue 19660 ppm); BJD 2461257.2865: not recovered, depth 157 ± 1112 ppm (catalogue 19660 ppm); BJD 2461260.8376: gap (catalogue 19660 ppm).
Outside the catalogued epoch the screen left 167 threshold entries forming **38 distinct event(s)**, **24 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2560.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 441155146 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 332.759205 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -27.295719 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458348.918997 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 3.5511203 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 19660.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.634 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.5328 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | lightcurve | 68 | False | `d7a25beb8ef78d79` | True |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | lightcurve | 95 | False | `fc9c5c2420c63aec` | True |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | lightcurve | 106 | False | `b3c50f1e47c76720` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 2460156.43923 | not_recovered | 79 | 577 ± 1060 | 19660 | — |
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 2460159.99035 | not_recovered | 79 | -1293 ± 973 | 19660 | — |
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 2460163.54147 | not_recovered | 79 | 1909 ± 1029 | 19660 | — |
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 2460167.09259 | gap | 0 | — | 19660 | — |
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 2460170.64371 | not_recovered | 79 | -1718 ± 1013 | 19660 | — |
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 2460174.19483 | not_recovered | 77 | -161 ± 1026 | 19660 | — |
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 2460177.74595 | not_recovered | 79 | -2451 ± 1059 | 19660 | — |
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 2460181.29707 | gap | 0 | — | 19660 | — |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460884.41889 | not_recovered | 79 | 175 ± 1126 | 19660 | — |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460887.97001 | not_recovered | 79 | -1562 ± 1112 | 19660 | — |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460891.52113 | not_recovered | 79 | -2616 ± 1082 | 19660 | — |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460895.07225 | gap | 0 | — | 19660 | — |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460898.62337 | not_recovered | 79 | 1362 ± 1152 | 19660 | — |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460902.17449 | not_recovered | 79 | -1525 ± 1150 | 19660 | — |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460905.72561 | not_recovered | 79 | -1191 ± 1171 | 19660 | — |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461235.97980 | not_recovered | 79 | -1598 ± 1161 | 19660 | — |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461239.53092 | not_recovered | 74 | 807 ± 1116 | 19660 | — |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461243.08204 | not_recovered | 79 | -1416 ± 1065 | 19660 | — |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461246.63316 | not_recovered | 70 | 1781 ± 1317 | 19660 | — |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461250.18428 | gap | 0 | — | 19660 | — |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461253.73540 | gap | 0 | — | 19660 | — |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461257.28652 | not_recovered | 79 | 157 ± 1112 | 19660 | — |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461260.83764 | gap | 0 | — | 19660 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023209231226-s0068-0000000441155146-0262-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461246.89293 | -0.03869 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461243.31641 | -0.03732 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461257.58073 | -0.03695 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461257.53351 | -0.03656 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460898.87890 | -0.03428 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461246.92487 | -0.03412 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460898.83793 | -0.03257 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461243.33308 | -0.03236 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460905.94628 | -0.03185 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460898.84626 | -0.03133 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461243.32197 | -0.03108 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460891.77116 | -0.03085 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460884.63208 | -0.03082 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460902.39490 | -0.03074 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460884.62097 | -0.03054 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461236.19941 | -0.03026 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461236.23274 | -0.02883 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461257.50990 | -0.02883 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460902.35879 | -0.02848 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461239.80376 | -0.02834 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461246.85820 | -0.02812 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461239.78153 | -0.02774 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460899.62266 | -0.02760 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460884.66819 | -0.02628 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460900.53031 | -0.03645 | 3 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460902.38587 | -0.03162 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460905.98934 | -0.03075 | 2 | PDCSAP | 3 | no |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461239.78848 | -0.02991 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460900.28794 | -0.02927 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460900.44350 | -0.02815 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460900.63100 | -0.02716 | 2 | SAP | 2, 3 | no |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460905.96295 | -0.02624 | 2 | PDCSAP | 3 | no |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460900.57267 | -0.02620 | 2 | SAP | 2, 3 | no |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461235.22435 | -0.02503 | 2 | SAP | 1, 2, 3 | no |
| `tess2025206162959-s0095-0000000441155146-0292-s_lc.fits` | 2460900.26294 | -0.02490 | 2 | SAP | 3 | no |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461239.74820 | -0.02454 | 2 | SAP | 1, 2, 3 | no |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461243.30947 | -0.02359 | 2 | SAP | 3 | no |
| `tess2026192185000-s0106-0000000441155146-0308-s_lc.fits` | 2461235.30353 | -0.02305 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2560.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:47:48Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:47:50Z: TOI-2560.01 (TIC 441155146, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:47:52Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T21:47:53Z: UCAC4 314-249397 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2460156.4392: not recovered, depth 577 ± 1060 ppm (catalogue 19660 ppm); BJD 2460159.9904: not recovered, depth -1293 ± 973 ppm (catalogue 19660 ppm); BJD 2460163.5415: not recovered, depth 1909 ± 1029 ppm (catalogue 19660 ppm); BJD 2460167.0926: gap (catalogue 19660 ppm); BJD 2460170.6437: not recovered, depth -1718 ± 1013 ppm (catalogue 19660 ppm); BJD 2460174.1948: not recovered, depth -161 ± 1026 ppm (catalogue 19660 ppm); BJD 2460177.7460: not recovered, depth -2451 ± 1059 ppm (catalogue 19660 ppm); BJD 2460181.2971: gap (catalogue 19660 ppm); BJD 2460884.4189: not recovered, depth 175 ± 1126 ppm (catalogue 19660 ppm); BJD 2460887.9700: not recovered, depth -1562 ± 1112 ppm (catalogue 19660 ppm); BJD 2460891.5211: not recovered, depth -2616 ± 1082 ppm (catalogue 19660 ppm); BJD 2460895.0723: gap (catalogue 19660 ppm); BJD 2460898.6234: not recovered, depth 1362 ± 1152 ppm (catalogue 19660 ppm); BJD 2460902.1745: not recovered, depth -1525 ± 1150 ppm (catalogue 19660 ppm); BJD 2460905.7256: not recovered, depth -1191 ± 1171 ppm (catalogue 19660 ppm); BJD 2461235.9798: not recovered, depth -1598 ± 1161 ppm (catalogue 19660 ppm); BJD 2461239.5309: not recovered, depth 807 ± 1116 ppm (catalogue 19660 ppm); BJD 2461243.0820: not recovered, depth -1416 ± 1065 ppm (catalogue 19660 ppm); BJD 2461246.6332: not recovered, depth 1781 ± 1317 ppm (catalogue 19660 ppm); BJD 2461250.1843: gap (catalogue 19660 ppm); BJD 2461253.7354: gap (catalogue 19660 ppm); BJD 2461257.2865: not recovered, depth 157 ± 1112 ppm (catalogue 19660 ppm); BJD 2461260.8376: gap (catalogue 19660 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2560.01: Gaia DR3 6618938954148736000 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2560.01: Teff 5267 K, R* 0.90 ± 0.07, M* 0.93 ± 0.09, ρ* 1.27 ± 0.33 ρ☉ (dwarf sequence, M_G 5.15, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2560.01: 5 Gaia neighbour(s) within 52.5", contamination 22.56%; depth 19660 ppm (catalogue depth); 2 could produce it if fully eclipsed (brightest 6618938954148736128, 43.9", ΔG 1.75); a centroid test is needed |
| Pointing and quality census per event | failed | 24 persistent event(s), 15 clean; BJD 2460899.6227 caution: manual exclude (within ±0.25 d); BJD 2461239.7815 caution: argabrightening (within ±0.25 d), coarse point (within ±0.25 d), manual exclude (within ±0.25 d); BJD 2461239.8038 caution: manual exclude (within ±0.25 d); BJD 2461246.8582 suspect: manual exclude (in event), MOM_CENTR2 z=-6.8, POS_CORR2 z=-11.9, SAP_BKG z=+6.1 |
| Moving objects at screen-event epochs | inconclusive | 24 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 6 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2560.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2560.01: UCAC4 314-249397 otype * (star_or_other) at 0.6" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2560-01.yaml
python -m cygnus.multi report campaigns/toi-2560-01.yaml
```
