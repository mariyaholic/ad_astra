<!-- cygnus:generated-draft -->
# Known-object test, TOI-3716.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3716-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #438, calibrate_screen #394, event_census #400, fetch_products #391, known_signal_recovery #395, moving_objects #402, period_aliases #401, prior_art #440, residual_screen #399, stellar_context #396, variability_guard #439
- Runner finished (UTC): 2026-09-26T10:07:36Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 517 threshold entries forming **99 distinct event(s)**, **36 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3716.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 155351556 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 68.005803 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 36.012476 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458832.542018 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 29180.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 6.711 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.3186 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | lightcurve | 59 | False | `7565e2facca2f4e0` | True |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | lightcurve | 86 | False | `ddc7c9ac9dd67686` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | — | epoch not in this light curve | — | — | 29180 | — |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | — | epoch not in this light curve | — | — | 29180 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.38217 | -0.03532 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460641.55454 | -0.03483 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.54342 | -0.03403 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.31342 | -0.03277 | 15 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460650.06151 | -0.03099 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460644.05040 | -0.03064 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460643.99276 | -0.03004 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460650.03026 | -0.02996 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460650.08582 | -0.02983 | 23 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460650.16498 | -0.02913 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459918.26651 | -0.02839 | 36 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460644.09901 | -0.02805 | 19 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.27384 | -0.02794 | 21 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460643.93096 | -0.02766 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459918.12832 | -0.02754 | 25 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.23912 | -0.02742 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459918.20054 | -0.02734 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.38842 | -0.02713 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459918.15193 | -0.02712 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.22454 | -0.02681 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.36828 | -0.02678 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.29328 | -0.02650 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460650.01499 | -0.02621 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.48215 | -0.02593 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.33703 | -0.02569 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.59897 | -0.02566 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.44257 | -0.02561 | 42 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.53215 | -0.02402 | 31 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460641.39482 | -0.02383 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.50299 | -0.02370 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.59326 | -0.02270 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.57521 | -0.02263 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.56201 | -0.02252 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460636.91975 | -0.02128 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460636.89961 | -0.02039 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460636.92948 | -0.02012 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.83231 | -0.02825 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460641.15454 | -0.02788 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.60800 | -0.02698 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.94898 | -0.02588 | 2 | PDCSAP | 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.92953 | -0.02560 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.94481 | -0.02454 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.88509 | -0.02432 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.98231 | -0.02399 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460641.06148 | -0.02345 | 2 | PDCSAP | 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460643.90873 | -0.02339 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.40577 | -0.02318 | 9 | PDCSAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459918.30471 | -0.02214 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.34814 | -0.02209 | 9 | PDCSAP | 1 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460643.91568 | -0.02189 | 2 | PDCSAP | 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.57397 | -0.02158 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.39536 | -0.02114 | 3 | PDCSAP | 1 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.51147 | -0.02111 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.66981 | -0.02065 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460643.90457 | -0.02064 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.68786 | -0.02063 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460640.71286 | -0.02047 | 2 | PDCSAP | 3 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459918.10401 | -0.01927 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.35787 | -0.01917 | 3 | PDCSAP | 1 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460662.20995 | -0.01917 | 2 | PDCSAP | 1 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459923.34077 | -0.01891 | 3 | PDCSAP | 1, 2 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459918.29915 | -0.01888 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459916.02346 | -0.01801 | 2 | PDCSAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.49396 | -0.01794 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459923.33036 | -0.01761 | 2 | PDCSAP | 2 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459936.38702 | -0.01687 | 2 | PDCSAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.61013 | -0.01640 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.37402 | -0.01607 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.54068 | -0.01577 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.55180 | -0.01551 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.56221 | -0.01504 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.57263 | -0.01459 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460641.70315 | -0.01420 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.51499 | -0.01395 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.46846 | -0.01373 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.54763 | -0.01364 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.41569 | -0.01346 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.55596 | -0.01326 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.53652 | -0.01324 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.47819 | -0.01306 | 4 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.34763 | -0.01304 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.57680 | -0.01272 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.60041 | -0.01254 | 4 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.16985 | -0.01253 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.38374 | -0.01246 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.58096 | -0.01192 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.43235 | -0.01188 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.13652 | -0.01168 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.47263 | -0.01109 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.50180 | -0.01101 | 4 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.53235 | -0.01076 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.16152 | -0.01066 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.46291 | -0.01064 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.45527 | -0.01059 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460636.95448 | -0.01056 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.31569 | -0.01028 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460649.52471 | -0.01019 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000155351556-0283-s_lc.fits` | 2460637.02392 | -0.01001 | 2 | SAP | 3 | no |
| `tess2022330142927-s0059-0000000155351556-0248-s_lc.fits` | 2459923.24563 | -0.00909 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3716.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:07:33Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:07:35Z: TOI-3716.01 (TIC 155351556, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:07:36Z
- SIMBAD (done, 2026-09-26): 4 match(es) in SIMBAD within 30" as of 2026-09-26T10:07:36Z: TOI-3716 (*); 2MASS J04320040+3601099 (AB?); TYC 2385-6-1 (*); TOI-3716.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3716.01: Gaia DR3 174921137360545408 at 0.01" (propagated 2016.0 → J2015.5; 0.01" unpropagated) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3716.01: dwarf priors not applied — no positive parallax or G magnitude; RUWE n/a ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3716.01: 20 Gaia neighbour(s) within 52.5", contamination 79.06%; depth 29180 ppm (catalogue depth); 2 could produce it if fully eclipsed (brightest 174921029985404672, 22.9", ΔG -1.32); a centroid test is needed |
| Pointing and quality census per event | failed | 36 persistent event(s), 4 clean; BJD 2459918.1283 suspect: MOM_CENTR2 z=-8.2; BJD 2459918.1519 suspect: MOM_CENTR2 z=-7.8; BJD 2459918.2005 suspect: MOM_CENTR2 z=-10.7; BJD 2459918.2665 suspect: MOM_CENTR2 z=-8.3 |
| Moving objects at screen-event epochs | inconclusive | 36 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 8 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3716.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3716.01: TOI-3716 otype * (star_or_other) at 0.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3716-01.yaml
python -m cygnus.multi report campaigns/toi-3716-01.yaml
```
