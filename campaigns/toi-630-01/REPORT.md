<!-- cygnus:generated-draft -->
# Known-object test, TOI-630.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-630-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #520, calibrate_screen #320, event_census #324, fetch_products #319, known_signal_recovery #321, moving_objects #450, period_aliases #325, prior_art #522, residual_screen #323, stellar_context #322, variability_guard #521
- Runner finished (UTC): 2026-09-26T10:09:27Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-630.01 (BJD 2459226.3610: recovered, depth 12092 ± 117 ppm (catalogue 13100 ppm)).
Outside the catalogued epoch the screen left 218 threshold entries forming **38 distinct event(s)**, **33 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459201.8718 matches the catalogued transit's depth (6252 vs 12092 ppm), 24.489 d later; 0 of 24 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-630.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 123898871 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 90.916011 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -19.04084 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459226.360983 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 13100.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.042 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.84786 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-19 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | lightcurve | 33 | True | `0fd98701aa267fd6` | True |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | lightcurve | 87 | False | `938724f857adf3a0` | True |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | lightcurve | 98 | False | `3b6964f227210d0f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 2459226.36098 | recovered | 122 | 12092 ± 117 | 13100 | -0.01 |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | — | epoch not in this light curve | — | — | 13100 | — |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | — | epoch not in this light curve | — | — | 13100 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 5000, 4h: 10000, 8h: 10000 |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 5000, 4h: 10000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.29947 | -0.01444 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.30850 | -0.01409 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2461013.29939 | -0.01330 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 2459221.42096 | -0.01300 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 2459221.50082 | -0.01292 | 39 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2461023.12039 | -0.01286 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460684.38571 | -0.01277 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.28628 | -0.01264 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.31614 | -0.01259 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 2459211.63081 | -0.01255 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2461042.75580 | -0.01248 | 108 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2461028.03086 | -0.01241 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.33211 | -0.01229 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2461037.84612 | -0.01225 | 102 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2460998.57183 | -0.01210 | 108 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.32308 | -0.01209 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 2459216.54325 | -0.01208 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.25572 | -0.01205 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.34461 | -0.01199 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.27239 | -0.01191 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460679.47607 | -0.01181 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460674.56782 | -0.01181 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 2459206.72459 | -0.01170 | 105 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.26336 | -0.01132 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.23628 | -0.01119 | 20 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2460993.66328 | -0.01074 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2461008.38953 | -0.01058 | 105 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.36127 | -0.00966 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 2459201.87179 | -0.00828 | 100 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2461037.77251 | -0.00685 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2461037.91973 | -0.00640 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460669.73451 | -0.00619 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2460988.74013 | -0.00596 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 2460689.01406 | -0.00633 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2460988.71027 | -0.00574 | 2 | PDCSAP | 1, 2 | no |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2460988.77555 | -0.00546 | 2 | SAP | 3 | no |
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 2459221.37512 | -0.00528 | 2 | SAP | 2 | no |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 2460988.71443 | -0.00517 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459201.87179 | 6252 | 12092 | 24.4886 | 0 / 24 |  |
| 2459206.72459 | 11245 | 12092 | 19.6358 | 0 / 19 |  |
| 2459211.63081 | 12038 | 12092 | 14.7296 | 0 / 14 |  |
| 2459216.54325 | 11916 | 12092 | 9.8172 | 0 / 9 |  |
| 2459221.42096 | 11664 | 12092 | 4.9395 | 0 / 4 |  |
| 2459221.50082 | 11809 | 12092 | 4.8596 | 0 / 4 |  |
| 2460674.56782 | 11569 | 12092 | 1448.2074 | 30 / 1448 | 1448.21, 724.104, 482.736, 362.052, 289.642, 241.368, 206.887, 181.026, 144.821, 131.655, 120.684, 103.443, 96.5472, 90.513, 76.2214, 72.4104, 68.9623, 65.8276, 62.9655, 60.342 |
| 2460679.47607 | 11185 | 12092 | 1453.1157 | 28 / 1453 | 1453.12, 726.558, 484.372, 363.279, 290.623, 242.186, 207.588, 181.639, 145.312, 132.101, 121.093, 103.794, 96.8744, 90.8197, 85.4774, 76.4798, 72.6558, 60.5465, 51.897, 48.4372 |
| 2460684.38571 | 12168 | 12092 | 1458.0253 | 31 / 1458 | 1458.03, 729.013, 486.008, 364.506, 291.605, 243.004, 208.289, 182.253, 162.003, 145.803, 132.548, 121.502, 112.156, 97.2017, 91.1266, 81.0014, 76.7382, 72.9013, 60.7511, 58.321 |
| 2460689.23628 | 10486 | 12092 | 1462.8759 | 24 / 1462 | 1462.88, 731.438, 487.625, 365.719, 292.575, 243.813, 208.982, 182.859, 146.288, 132.989, 121.906, 97.5251, 91.4297, 86.0515, 73.1438, 66.4944, 63.6033, 47.1895, 43.0258, 36.5719 |
| 2460689.25572 | 10980 | 12092 | 1462.8953 | 24 / 1462 | 1462.9, 731.448, 487.632, 365.724, 292.579, 243.816, 208.985, 182.862, 146.29, 132.99, 121.908, 97.5264, 91.431, 86.0527, 73.1448, 66.4952, 63.6041, 47.1902, 43.0263, 36.5724 |
| 2460689.26336 | 11106 | 12092 | 1462.9029 | 24 / 1462 | 1462.9, 731.452, 487.634, 365.726, 292.581, 243.817, 208.986, 182.863, 146.29, 132.991, 121.909, 97.5269, 91.4314, 86.0531, 73.1451, 66.4956, 63.6045, 47.1904, 43.0266, 36.5726 |
| 2460689.27239 | 11226 | 12092 | 1462.9120 | 23 / 1462 | 1462.91, 731.456, 487.637, 365.728, 292.582, 243.819, 208.987, 182.864, 146.291, 132.992, 121.909, 97.5275, 91.432, 86.0536, 73.1456, 66.496, 63.6049, 47.1907, 43.0268, 36.5728 |
| 2460689.28628 | 11246 | 12092 | 1462.9259 | 22 / 1462 | 1462.93, 731.463, 487.642, 365.731, 292.585, 243.821, 208.989, 182.866, 146.293, 132.993, 121.91, 97.5284, 91.4329, 86.0545, 73.1463, 66.4966, 63.6055, 47.1912, 43.0272, 36.5731 |
| 2460689.29947 | 11226 | 12092 | 1462.9391 | 22 / 1462 | 1462.94, 731.47, 487.646, 365.735, 292.588, 243.823, 208.991, 182.867, 146.294, 132.994, 121.912, 97.5293, 91.4337, 86.0552, 73.147, 66.4972, 63.606, 47.1916, 43.0276, 36.5735 |
| 2460689.30850 | 11215 | 12092 | 1462.9481 | 23 / 1462 | 1462.95, 731.474, 487.649, 365.737, 292.59, 243.825, 208.993, 182.869, 146.295, 132.995, 121.912, 97.5299, 91.4343, 86.0558, 73.1474, 66.4976, 63.6064, 47.1919, 43.0279, 36.5737 |
| 2460689.31614 | 11175 | 12092 | 1462.9557 | 25 / 1462 | 1462.96, 731.478, 487.652, 365.739, 292.591, 243.826, 208.994, 182.869, 146.296, 132.996, 121.913, 104.497, 97.5304, 91.4347, 86.0562, 73.1478, 66.498, 63.6068, 52.2484, 47.1921 |
| 2460689.32308 | 11162 | 12092 | 1462.9627 | 25 / 1462 | 1462.96, 731.481, 487.654, 365.741, 292.592, 243.827, 208.995, 182.87, 146.296, 132.997, 121.914, 104.497, 97.5308, 91.4352, 86.0566, 73.1481, 66.4983, 63.6071, 52.2487, 47.1923 |
| 2460689.33211 | 11024 | 12092 | 1462.9717 | 25 / 1462 | 1462.97, 731.486, 487.657, 365.743, 292.594, 243.829, 208.996, 182.871, 146.297, 132.997, 121.914, 104.498, 97.5314, 91.4357, 86.0572, 73.1486, 66.4987, 63.6075, 52.249, 47.1926 |
| 2460689.34461 | 10761 | 12092 | 1462.9842 | 26 / 1462 | 1462.98, 731.492, 487.661, 365.746, 292.597, 243.831, 208.998, 182.873, 146.298, 132.999, 121.915, 104.499, 97.5323, 91.4365, 86.0579, 73.1492, 66.4993, 63.608, 52.2494, 47.193 |
| 2460689.36127 | 7393 | 12092 | 1463.0009 | 25 / 1463 | 1463, 731.5, 487.667, 365.75, 292.6, 243.833, 209, 182.875, 146.3, 133, 121.917, 104.5, 97.5334, 91.4376, 86.0589, 73.15, 66.5, 63.6087, 52.25, 47.1936 |
| 2460993.66328 | 10435 | 12092 | 1767.3029 | 38 / 1767 | 1767.3, 883.651, 589.101, 441.826, 353.461, 294.55, 252.472, 220.913, 196.367, 176.73, 147.275, 135.946, 126.236, 117.82, 110.456, 98.1835, 93.0159, 88.3651, 84.1573, 73.6376 |
| 2460998.57183 | 11584 | 12092 | 1772.2114 | 31 / 1772 | 1772.21, 886.106, 590.737, 443.053, 354.442, 295.369, 253.173, 221.526, 196.912, 177.221, 147.684, 136.324, 126.587, 118.147, 98.4562, 93.2743, 88.6106, 84.391, 77.0527, 73.8421 |
| 2461008.38953 | 9918 | 12092 | 1782.0291 | 43 / 1782 | 1782.03, 891.015, 594.01, 445.507, 356.406, 297.005, 254.576, 222.754, 198.003, 178.203, 162.003, 148.502, 137.079, 127.288, 118.802, 104.825, 99.0016, 93.791, 89.1015, 81.0013 |
| 2461013.29939 | 12800 | 12092 | 1786.9390 | 39 / 1786 | 1786.94, 893.47, 595.646, 446.735, 357.388, 297.823, 255.277, 223.367, 198.549, 178.694, 148.912, 137.457, 127.638, 119.129, 111.684, 105.114, 99.2744, 94.0494, 89.3469, 77.693 |
| 2461023.12039 | 12590 | 12092 | 1796.7600 | 45 / 1796 | 1796.76, 898.38, 598.92, 449.19, 359.352, 299.46, 256.68, 224.595, 199.64, 179.676, 163.342, 149.73, 138.212, 128.34, 119.784, 105.692, 99.82, 94.5663, 89.838, 81.6709 |
| 2461028.03086 | 12018 | 12092 | 1801.6704 | 35 / 1801 | 1801.67, 900.835, 600.557, 450.418, 300.278, 257.382, 225.209, 200.186, 163.788, 150.139, 138.59, 128.691, 112.604, 105.981, 100.093, 94.8248, 81.8941, 78.3335, 75.0696, 66.7285 |
| 2461037.77251 | 6489 | 12092 | 1811.4121 | 33 / 1811 | 1811.41, 905.706, 603.804, 452.853, 301.902, 258.773, 226.427, 201.268, 164.674, 150.951, 139.339, 129.387, 113.213, 106.554, 100.634, 95.3375, 86.2577, 82.3369, 78.757, 75.4755 |
| 2461037.84612 | 11776 | 12092 | 1811.4857 | 33 / 1811 | 1811.49, 905.743, 603.829, 452.871, 301.914, 258.784, 226.436, 201.276, 164.68, 150.957, 139.345, 129.392, 113.218, 106.558, 100.638, 95.3414, 86.2612, 82.3403, 78.7602, 75.4786 |
| 2461037.91973 | 6074 | 12092 | 1811.5593 | 36 / 1811 | 1811.56, 905.78, 603.853, 452.89, 301.927, 258.794, 226.445, 201.284, 164.687, 150.963, 139.351, 129.397, 113.222, 106.562, 100.642, 95.3452, 86.2647, 82.3436, 78.7634, 75.4816 |
| 2461042.75580 | 11592 | 12092 | 1816.3954 | 40 / 1816 | 1816.4, 908.198, 605.465, 454.099, 363.279, 302.733, 259.485, 227.049, 201.822, 181.639, 165.127, 151.366, 139.723, 129.743, 121.093, 113.525, 106.847, 100.911, 95.5998, 90.8198 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-630.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:09:24Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:09:25Z: TOI-630.01 (TIC 123898871, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:09:26Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:09:27Z: TOI-630.01 (err); BD-19  1337 (EB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459226.3610: recovered, depth 12092 ± 117 ppm (catalogue 13100 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 4, 4; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 20%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 31 repeat-candidate event(s); first at BJD 2459201.8718, ΔT = 24.489 d, 0 of 24 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-630.01: Gaia DR3 2942380703200115200 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-630.01: dwarf priors not applied — RUWE 4.836458 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-630.01: 12 Gaia neighbour(s) within 52.5", contamination 3.16%; depth 12092 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 2942380703200588800, 31.4", ΔG 4.06); a centroid test is needed |
| Pointing and quality census per event | failed | 33 persistent event(s), 7 clean; BJD 2459201.8718 suspect: earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=+26.5, MOM_CENTR2 z=-21.6, POS_CORR1 z=+28.5, POS_CORR2 z=-24.6, SAP_BKG z=+11.4; BJD 2459211.6308 suspect: SAP_BKG z=-5.4; BJD 2459221.4210 caution: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2459221.5008 caution: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 33 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 4 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-630.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | failed | TOI-630.01: BD-19  1337 otype EB* (eclipsing_or_ellipsoidal) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-630-01.yaml
python -m cygnus.multi report campaigns/toi-630-01.yaml
```
