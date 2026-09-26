<!-- cygnus:generated-draft -->
# Known-object test, TOI-706.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-706-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #610, calibrate_screen #524, event_census #553, fetch_products #519, known_signal_recovery #534, moving_objects #605, period_aliases #554, prior_art #612, residual_screen #549, stellar_context #535, variability_guard #611
- Runner finished (UTC): 2026-09-26T10:11:47Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-706.01 (BJD 2458434.9115: recovered, depth 3056 ± 35 ppm (catalogue 4851 ppm)).
Outside the catalogued epoch the screen left 224 threshold entries forming **99 distinct event(s)**, **8 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459153.8804 matches the catalogued transit's depth (2201 vs 3056 ppm), 718.975 d later; 5 of 718 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-706.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 219345200 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 74.752657 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -49.736179 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458434.911525 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 4851.4092337 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.4244096 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.3643 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-11 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | lightcurve | 4 | True | `87da9d1d664537f0` | True |
| `tess2018319095959-s0005-0000000219345200-0125-s_lc.fits` | lightcurve | 5 | False | `b17319a3e18a92ac` | True |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | lightcurve | 6 | False | `112b9b32737482a1` | True |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | lightcurve | 31 | False | `32929d955da07771` | True |
| `tess2020324010417-s0032-0000000219345200-0200-s_lc.fits` | lightcurve | 32 | False | `a4306c189d64591b` | True |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | lightcurve | 97 | False | `8d5640d75e18282b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458434.91152 | recovered | 163 | 3056 ± 35 | 4851 | -0.15 |
| `tess2018319095959-s0005-0000000219345200-0125-s_lc.fits` | — | epoch not in this light curve | — | — | 4851 | — |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | — | epoch not in this light curve | — | — | 4851 | — |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | — | epoch not in this light curve | — | — | 4851 | — |
| `tess2020324010417-s0032-0000000219345200-0200-s_lc.fits` | — | epoch not in this light curve | — | — | 4851 | — |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | — | epoch not in this light curve | — | — | 4851 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2018319095959-s0005-0000000219345200-0125-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2020324010417-s0032-0000000219345200-0200-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 1000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | 2459153.94987 | -0.00418 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460951.54670 | -0.00383 | 115 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | 2459153.88043 | -0.00256 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | 2459153.86932 | -0.00217 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460951.46545 | -0.00202 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460983.95068 | -0.00151 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460951.63073 | -0.00148 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458418.48556 | -0.00141 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.63404 | -0.00254 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.53120 | -0.00237 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | 2459158.91449 | -0.00233 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460967.48659 | -0.00232 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458425.15646 | -0.00212 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.70904 | -0.00211 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.98121 | -0.00207 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458425.49674 | -0.00204 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460981.45621 | -0.00203 | 3 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.61037 | -0.00198 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458424.78701 | -0.00197 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.84371 | -0.00194 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.36601 | -0.00194 | 2 | SAP | 2, 3 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458478.89921 | -0.00193 | 2 | SAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000219345200-0200-s_lc.fits` | 2459185.62698 | -0.00191 | 2 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.35629 | -0.00189 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.24162 | -0.00189 | 3 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.43823 | -0.00188 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460967.47548 | -0.00188 | 2 | SAP | 2, 3 | no |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | 2459150.91026 | -0.00186 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460967.35326 | -0.00186 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.05767 | -0.00184 | 2 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.56462 | -0.00183 | 2 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458471.95767 | -0.00183 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.02425 | -0.00182 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.86593 | -0.00182 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.17295 | -0.00181 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460981.62566 | -0.00180 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | 2459163.45203 | -0.00177 | 2 | SAP | 1 | no |
| `tess2020324010417-s0032-0000000219345200-0200-s_lc.fits` | 2459185.18254 | -0.00176 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460967.33381 | -0.00176 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460967.40465 | -0.00176 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.26323 | -0.00175 | 2 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.00350 | -0.00172 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.53681 | -0.00171 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460979.92981 | -0.00171 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458417.39319 | -0.00170 | 3 | SAP | 1, 2, 3 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458471.99934 | -0.00169 | 2 | SAP | 1, 2, 3 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458479.01309 | -0.00167 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.19378 | -0.00167 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.16809 | -0.00167 | 3 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460954.29537 | -0.00166 | 3 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.44865 | -0.00166 | 3 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.47987 | -0.00165 | 2 | SAP | 3 | no |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | 2459169.18399 | -0.00165 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460973.71168 | -0.00164 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.17981 | -0.00164 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460974.12419 | -0.00163 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460974.31446 | -0.00162 | 2 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.08475 | -0.00161 | 3 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.32015 | -0.00161 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.28190 | -0.00159 | 3 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.29934 | -0.00158 | 4 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.26740 | -0.00158 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.39031 | -0.00158 | 3 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.09517 | -0.00155 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.27009 | -0.00154 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.08953 | -0.00153 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460981.62011 | -0.00153 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.78260 | -0.00153 | 2 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458471.53546 | -0.00152 | 2 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460981.21316 | -0.00152 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458411.27295 | -0.00152 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460981.70344 | -0.00151 | 3 | SAP | 1, 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460936.68591 | -0.00151 | 2 | PDCSAP | 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.66662 | -0.00150 | 3 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458468.95911 | -0.00150 | 2 | SAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000219345200-0200-s_lc.fits` | 2459185.76171 | -0.00150 | 2 | SAP | 1 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.30759 | -0.00149 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460980.14926 | -0.00149 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458415.59247 | -0.00149 | 2 | SAP | 1, 2 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.20903 | -0.00148 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.85279 | -0.00148 | 3 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458414.45078 | -0.00148 | 2 | SAP | 1, 2 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458486.65460 | -0.00147 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.67292 | -0.00147 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458415.65497 | -0.00142 | 2 | SAP | 1 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458468.74939 | -0.00141 | 2 | SAP | 2, 3 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458472.17850 | -0.00141 | 2 | SAP | 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.61529 | -0.00140 | 3 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460974.22002 | -0.00140 | 2 | SAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460981.81316 | -0.00139 | 2 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458433.24263 | -0.00139 | 2 | SAP | 2 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460987.30626 | -0.00137 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458418.24667 | -0.00136 | 2 | PDCSAP | 2, 3 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460988.10070 | -0.00134 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458415.13968 | -0.00132 | 2 | SAP | 1 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460967.38382 | -0.00131 | 2 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 2458472.91460 | -0.00131 | 2 | SAP | 1 | no |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 2460950.91682 | -0.00127 | 2 | PDCSAP+SAP | 1 | no |
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 2458421.32448 | -0.00124 | 2 | PDCSAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459153.88043 | 2201 | 3056 | 718.9753 | 5 / 718 | 718.975, 239.658, 143.795, 102.711, 79.8861 |
| 2459153.94987 | 2908 | 3056 | 719.0447 | 11 / 719 | 719.045, 359.522, 239.682, 179.761, 143.809, 119.841, 102.721, 89.8806, 79.8939, 71.9045, 59.9204 |
| 2460951.46545 | 1539 | 3056 | 2516.5603 | 29 / 2516 | 2516.56, 1258.28, 838.853, 629.14, 503.312, 419.427, 359.509, 314.57, 279.618, 228.778, 209.713, 193.582, 179.754, 167.771, 157.285, 139.809, 132.451, 119.836, 114.389, 109.416 |
| 2460951.54670 | 2864 | 3056 | 2516.6416 | 29 / 2516 | 2516.64, 1258.32, 838.88, 629.16, 503.328, 419.44, 359.52, 314.58, 279.627, 228.786, 209.72, 193.588, 179.76, 167.776, 157.29, 139.813, 132.455, 119.84, 114.393, 109.419 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-706.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:11:44Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:11:45Z: TOI-706.01 (TIC 219345200, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:11:47Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:11:47Z: TOI-706.01 (Pl?); HD  32226 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458434.9115: recovered, depth 3056 ± 35 ppm (catalogue 4851 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3.5, ≤2.5, 3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100%, 100%, 100%, 100%, 90% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 4 repeat-candidate event(s); first at BJD 2459153.8804, ΔT = 718.975 d, 5 of 718 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (718.975, 239.658, 143.795, 102.711, 79.8861 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-706.01: Gaia DR3 4785405080341786368 at 0.00" (propagated 2016.0 → J2015.5; 0.03" unpropagated, proper-motion shift 0.04") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-706.01: dwarf priors not applied — RUWE 4.533328 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-706.01: 7 Gaia neighbour(s) within 52.5", contamination 0.35%; depth 3056 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 4785405011620456576, 9.7", ΔG 6.25); a centroid test is needed |
| Pointing and quality census per event | failed | 8 persistent event(s), 7 clean; BJD 2458418.4856 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+7.3 |
| Moving objects at screen-event epochs | inconclusive | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-706.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-706.01: HD  32226 otype SB* (multiple) at 1.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-706-01.yaml
python -m cygnus.multi report campaigns/toi-706-01.yaml
```
