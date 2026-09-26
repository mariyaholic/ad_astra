<!-- [private Drive store] -->
# Known-object test, TOI-527.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-527-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #877, calibrate_screen #805, event_census #815, fetch_products #802, known_signal_recovery #807, moving_objects #868, period_aliases #816, prior_art #879, residual_screen #813, stellar_context #808, variability_guard #878
- Runner finished (UTC): 2026-09-26T10:22:05Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-527.01 (BJD 2458470.7384: recovered, depth 3446 ± 51 ppm (catalogue 5527 ppm)).
Outside the catalogued epoch the screen left 156 threshold entries forming **57 distinct event(s)**, **10 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2458488.8270 matches the catalogued transit's depth (3360 vs 3446 ppm), 18.089 d later; 1 of 18 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-527.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 148228019 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 101.188744 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -36.657354 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458470.73838 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5526.7158766 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.5607235 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.2488 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-07 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2018349182500-s0006-0000000148228019-0126-s_lc.fits` | lightcurve | 6 | True | `4f9b211fff7e2446` | True |
| `tess2019006130736-s0007-0000000148228019-0131-s_lc.fits` | lightcurve | 7 | False | `6b73c0f5e5d9406d` | True |
| `tess2020351194500-s0033-0000000148228019-0203-s_lc.fits` | lightcurve | 33 | False | `2221bfc3ca7ade9d` | True |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | lightcurve | 34 | False | `83c13b4c44d452c5` | True |
| `tess2024353092137-s0087-0000000148228019-0284-s_lc.fits` | lightcurve | 87 | False | `9219889dbc8c9340` | True |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | lightcurve | 88 | False | `d4cd6f173a3ce72e` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2018349182500-s0006-0000000148228019-0126-s_lc.fits` | 2458470.73838 | recovered | 77 | 3446 ± 51 | 5527 | -0.01 |
| `tess2019006130736-s0007-0000000148228019-0131-s_lc.fits` | — | epoch not in this light curve | — | — | 5527 | — |
| `tess2020351194500-s0033-0000000148228019-0203-s_lc.fits` | — | epoch not in this light curve | — | — | 5527 | — |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | — | epoch not in this light curve | — | — | 5527 | — |
| `tess2024353092137-s0087-0000000148228019-0284-s_lc.fits` | — | epoch not in this light curve | — | — | 5527 | — |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | — | epoch not in this light curve | — | — | 5527 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2018349182500-s0006-0000000148228019-0126-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2019006130736-s0007-0000000148228019-0131-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2020351194500-s0033-0000000148228019-0203-s_lc.fits` | 3 | False | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2024353092137-s0087-0000000148228019-0284-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459230.48364 | -0.00468 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000148228019-0126-s_lc.fits` | 2458488.82704 | -0.00464 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460713.80433 | -0.00462 | 52 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000148228019-0203-s_lc.fits` | 2459212.39752 | -0.00460 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459248.57435 | -0.00442 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460695.70953 | -0.00440 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019006130736-s0007-0000000148228019-0131-s_lc.fits` | 2458506.91722 | -0.00408 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000148228019-0203-s_lc.fits` | 2459212.35585 | -0.00208 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460713.76197 | -0.00193 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459248.53268 | -0.00159 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.45840 | -0.00316 | 3 | SAP | 1, 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.68409 | -0.00278 | 3 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.02507 | -0.00253 | 2 | SAP | 1, 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.44729 | -0.00251 | 2 | SAP | 1, 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.38896 | -0.00243 | 4 | SAP | 1, 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460703.86705 | -0.00235 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.34382 | -0.00231 | 3 | SAP | 1, 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.38201 | -0.00227 | 2 | SAP | 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459252.67493 | -0.00226 | 2 | SAP | 1, 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.46395 | -0.00226 | 2 | SAP | 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459253.70962 | -0.00222 | 2 | SAP | 1, 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460717.01674 | -0.00221 | 2 | SAP | 1, 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460717.27229 | -0.00213 | 2 | SAP | 1 | no |
| `tess2024353092137-s0087-0000000148228019-0284-s_lc.fits` | 2460689.07417 | -0.00197 | 2 | SAP | 1, 2 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459253.60407 | -0.00195 | 2 | SAP | 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459253.06937 | -0.00195 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459253.08048 | -0.00195 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.53617 | -0.00194 | 2 | SAP | 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.99311 | -0.00192 | 2 | SAP | 1, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.07785 | -0.00192 | 4 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.09729 | -0.00189 | 2 | SAP | 1, 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460703.79899 | -0.00188 | 2 | SAP | 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.97644 | -0.00187 | 2 | SAP | 1, 2, 3 | no |
| `tess2018349182500-s0006-0000000148228019-0126-s_lc.fits` | 2458479.01447 | -0.00186 | 2 | SAP | 1, 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459253.29436 | -0.00183 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460717.32506 | -0.00180 | 2 | SAP | 1, 2, 3 | no |
| `tess2019006130736-s0007-0000000148228019-0131-s_lc.fits` | 2458493.08815 | -0.00179 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.58478 | -0.00178 | 2 | SAP | 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.92367 | -0.00177 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.43340 | -0.00173 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460703.73719 | -0.00173 | 3 | SAP | 2, 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.63617 | -0.00172 | 3 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460716.47648 | -0.00170 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460703.70177 | -0.00169 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.16674 | -0.00167 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460703.72399 | -0.00167 | 2 | SAP | 3 | no |
| `tess2020351194500-s0033-0000000148228019-0203-s_lc.fits` | 2459215.50309 | -0.00166 | 2 | SAP | 1, 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460703.76982 | -0.00166 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460716.43898 | -0.00162 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460717.10701 | -0.00161 | 2 | SAP | 1, 2 | no |
| `tess2020351194500-s0033-0000000148228019-0203-s_lc.fits` | 2459202.53489 | -0.00159 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460711.34745 | -0.00157 | 2 | SAP | 1, 2, 3 | no |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 2460703.61844 | -0.00156 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459247.79589 | -0.00155 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459254.05961 | -0.00150 | 2 | SAP | 1, 2 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459253.21797 | -0.00150 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 2459230.52462 | -0.00146 | 3 | PDCSAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2458488.82704 | 3360 | 3446 | 18.0891 | 1 / 18 | 18.0891 |
| 2458506.91722 | 3440 | 3446 | 36.1793 | 0 / 36 |  |
| 2459212.35585 | 1802 | 3446 | 741.6179 | 0 / 741 |  |
| 2459212.39752 | 3247 | 3446 | 741.6596 | 17 / 741 | 741.66, 370.83, 247.22, 185.415, 148.332, 123.61, 105.951, 92.7074, 82.4066, 74.166, 67.4236, 61.805, 57.0507, 52.9757, 49.444, 46.3537, 18.0893 |
| 2459230.48364 | 3805 | 3446 | 759.7457 | 11 / 759 | 759.746, 379.873, 253.249, 189.936, 151.949, 126.624, 108.535, 94.9682, 54.2675, 36.1784, 18.0892 |
| 2459248.57435 | 3514 | 3446 | 777.8364 | 8 / 777 | 777.836, 388.918, 259.279, 194.459, 155.567, 77.7836, 70.7124, 18.0892 |
| 2460695.70953 | 3626 | 3446 | 2224.9716 | 38 / 2224 | 2224.97, 1112.49, 741.657, 556.243, 444.994, 370.829, 317.853, 278.121, 247.219, 222.497, 202.27, 185.414, 171.152, 158.927, 148.331, 139.061, 130.881, 123.609, 117.104, 105.951 |
| 2460713.76197 | 1801 | 3446 | 2243.0240 | 24 / 2243 | 2243.02, 1121.51, 560.756, 448.605, 320.432, 280.378, 224.302, 203.911, 172.54, 160.216, 140.189, 131.943, 118.054, 112.151, 101.956, 89.721, 80.108, 72.3556, 70.0945, 65.9713 |
| 2460713.80433 | 3388 | 3446 | 2243.0664 | 24 / 2243 | 2243.07, 1121.53, 560.767, 448.613, 320.438, 280.383, 224.307, 203.915, 172.544, 160.219, 140.192, 131.945, 118.056, 112.153, 101.958, 89.7227, 80.1095, 72.357, 70.0958, 65.9725 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-527.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:22:02Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:22:03Z: TOI-527.01 (TIC 148228019, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:22:04Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:22:04Z: TOI-527.01 (Pl?); HD  49030 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458470.7384: recovered, depth 3446 ± 51 ppm (catalogue 5527 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3, 3, 3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100%, 100%, 100%, 100%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 9 repeat-candidate event(s); first at BJD 2458488.8270, ΔT = 18.089 d, 1 of 18 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (18.0891 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-527.01: Gaia DR3 5577598363432438656 at 0.01" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-527.01: dwarf priors not applied — RUWE 10.380204 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-527.01: 8 Gaia neighbour(s) within 52.5", contamination 0.19%; depth 3446 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | passed | 10 persistent event(s), 10 clean; no artifact quality bit within ±0.25 d and no centroid, pointing or background shift beyond 5σ |
| Moving objects at screen-event epochs | inconclusive | 10 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-527.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-527.01: HD  49030 otype * (star_or_other) at 0.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-527-01.yaml
python -m cygnus.multi report campaigns/toi-527-01.yaml
```
