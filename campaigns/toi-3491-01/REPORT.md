<!-- cygnus:generated-draft -->
# Known-object test, TOI-3491.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3491-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #510, calibrate_screen #410, event_census #414, fetch_products #409, known_signal_recovery #411, moving_objects #416, period_aliases #415, prior_art #512, residual_screen #413, stellar_context #412, variability_guard #511
- Runner finished (UTC): 2026-09-26T10:09:21Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 786 threshold entries forming **205 distinct event(s)**, **73 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3491.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 208719443 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 245.267413 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -59.510555 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459383.386266 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 32410.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.549 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.8844 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | lightcurve | 66 | False | `3576461f3f143e49` | True |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | lightcurve | 93 | False | `2851289e01f50e71` | True |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | lightcurve | 100 | False | `9ae2ac1002705e75` | True |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | lightcurve | 102 | False | `cea64f21ac3c488c` | True |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | lightcurve | 103 | False | `400b74993c039bf2` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | — | epoch not in this light curve | — | — | 32410 | — |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | — | epoch not in this light curve | — | — | 32410 | — |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 32410 | — |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | — | epoch not in this light curve | — | — | 32410 | — |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | — | epoch not in this light curve | — | — | 32410 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: 20000, 8h: — |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.73337 | -0.04387 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.77434 | -0.04221 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461075.71268 | -0.04165 | 91 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461080.51649 | -0.04154 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.73962 | -0.04149 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.75837 | -0.04143 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461078.11146 | -0.04112 | 87 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461094.94119 | -0.03993 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461097.34276 | -0.03975 | 91 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461085.32308 | -0.03925 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461082.92014 | -0.03908 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461092.53892 | -0.03892 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460854.55198 | -0.03873 | 96 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.74517 | -0.03872 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460852.14719 | -0.03849 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461145.43243 | -0.03828 | 30 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461140.61267 | -0.03784 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.72850 | -0.03783 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461128.59588 | -0.03761 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461145.39215 | -0.03759 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461090.12901 | -0.03738 | 86 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461143.01631 | -0.03734 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461135.80333 | -0.03724 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461130.99884 | -0.03688 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460847.34245 | -0.03668 | 88 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461099.74641 | -0.03653 | 82 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461167.05433 | -0.03611 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461174.26708 | -0.03557 | 96 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460121.37227 | -0.03551 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.71136 | -0.03527 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461169.45929 | -0.03523 | 97 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460844.93624 | -0.03502 | 91 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.84362 | -0.03448 | 92 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460116.56683 | -0.03445 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460104.54961 | -0.03423 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460837.72452 | -0.03423 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461147.82424 | -0.03419 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460118.97025 | -0.03396 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461157.43726 | -0.03378 | 92 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.74122 | -0.03366 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460114.16341 | -0.03357 | 96 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461150.22992 | -0.03333 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.70351 | -0.03306 | 32 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461133.40178 | -0.03305 | 91 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.78267 | -0.03301 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461145.47063 | -0.03293 | 23 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460832.91968 | -0.03279 | 91 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461162.24928 | -0.03275 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460840.12796 | -0.03272 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460102.13990 | -0.03268 | 92 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460106.95029 | -0.03255 | 88 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460099.73851 | -0.03253 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.77941 | -0.03250 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460835.32384 | -0.03239 | 91 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461176.66992 | -0.03238 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461155.03505 | -0.03205 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.72247 | -0.03125 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.75928 | -0.03096 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461138.20835 | -0.03079 | 88 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.79031 | -0.02985 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461099.80545 | -0.02974 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.80858 | -0.02753 | 20 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.70442 | -0.02726 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.80073 | -0.02679 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461099.81100 | -0.02614 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461145.36576 | -0.02571 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461075.64600 | -0.02459 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461147.75896 | -0.02097 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460847.27786 | -0.01910 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.69747 | -0.01887 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461155.09963 | -0.01464 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461167.12239 | -0.01405 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.70169 | -0.01387 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461080.58178 | -0.02103 | 2 | PDCSAP | 1 | no |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461082.85277 | -0.02071 | 2 | PDCSAP | 1 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461127.31522 | -0.01986 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461170.98573 | -0.01962 | 3 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461130.93147 | -0.01845 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460854.86308 | -0.01795 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461127.27286 | -0.01761 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461140.54669 | -0.01753 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461127.29508 | -0.01720 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460854.78530 | -0.01658 | 2 | PDCSAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461157.50393 | -0.01646 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.23387 | -0.01634 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.69330 | -0.01622 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461140.67795 | -0.01619 | 2 | PDCSAP | 1, 2 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461127.28814 | -0.01615 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461127.33120 | -0.01598 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461163.78059 | -0.01583 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461087.74062 | -0.01570 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460832.85371 | -0.01570 | 2 | PDCSAP+SAP | 1 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.29082 | -0.01561 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.81947 | -0.01545 | 3 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461145.49077 | -0.01543 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.61184 | -0.01537 | 2 | PDCSAP | 1 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461127.30342 | -0.01533 | 2 | PDCSAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.38274 | -0.01527 | 3 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461087.72326 | -0.01513 | 3 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461087.73368 | -0.01509 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460121.30283 | -0.01504 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461153.71206 | -0.01488 | 2 | PDCSAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.21905 | -0.01474 | 29 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461135.87556 | -0.01467 | 3 | PDCSAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.36885 | -0.01467 | 5 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461087.75937 | -0.01463 | 7 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461127.34092 | -0.01454 | 2 | PDCSAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.23803 | -0.01443 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.39177 | -0.01433 | 8 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461150.16047 | -0.01429 | 2 | PDCSAP | 2 | no |
| `tess2026033082000-s0100-0000000208719443-0302-s_lc.fits` | 2461087.74965 | -0.01428 | 5 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.15864 | -0.01426 | 44 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.26234 | -0.01425 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461170.92393 | -0.01424 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.32276 | -0.01405 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.26488 | -0.01405 | 35 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460121.44310 | -0.01375 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.19544 | -0.01342 | 3 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.11836 | -0.01335 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.34663 | -0.01330 | 5 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.30308 | -0.01329 | 6 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.26234 | -0.01328 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.37068 | -0.01326 | 3 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.37832 | -0.01324 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.40471 | -0.01323 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461174.19764 | -0.01314 | 2 | PDCSAP | 1, 2 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.34038 | -0.01304 | 7 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461153.82734 | -0.01294 | 2 | PDCSAP | 3 | no |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.85906 | -0.01291 | 2 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.34613 | -0.01284 | 8 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.49360 | -0.01279 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461133.08718 | -0.01273 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.31697 | -0.01270 | 6 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461153.79539 | -0.01261 | 2 | PDCSAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.38780 | -0.01258 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.36974 | -0.01258 | 6 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461171.48228 | -0.01252 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460849.67573 | -0.01247 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.35054 | -0.01243 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.32947 | -0.01239 | 10 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461170.69058 | -0.01233 | 2 | SAP | 1, 2 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.12669 | -0.01229 | 4 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461133.14135 | -0.01226 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.24915 | -0.01221 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.29405 | -0.01214 | 5 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.27371 | -0.01214 | 3 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.37649 | -0.01208 | 4 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.47510 | -0.01204 | 4 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.30010 | -0.01201 | 6 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.39613 | -0.01199 | 4 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461133.12329 | -0.01197 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000208719443-0290-s_lc.fits` | 2460855.01793 | -0.01190 | 3 | SAP | 2 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.44336 | -0.01190 | 4 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461133.20802 | -0.01187 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.31885 | -0.01184 | 17 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461145.34492 | -0.01183 | 2 | SAP | 1, 2 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.44246 | -0.01181 | 5 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.43482 | -0.01178 | 4 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000208719443-0304-s_lc.fits` | 2461146.56444 | -0.01168 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.35774 | -0.01166 | 9 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.41746 | -0.01159 | 5 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.28344 | -0.01147 | 4 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.45704 | -0.01143 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.29038 | -0.01132 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.40010 | -0.01130 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.25635 | -0.01121 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.15678 | -0.01117 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461171.07254 | -0.01117 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.46885 | -0.01115 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.40774 | -0.01110 | 5 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.31512 | -0.01096 | 4 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.48711 | -0.01076 | 3 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461171.16630 | -0.01075 | 3 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.35725 | -0.01069 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.50308 | -0.01065 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.43502 | -0.01060 | 4 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460111.63636 | -0.01049 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.59037 | -0.01048 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.55912 | -0.01046 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.44891 | -0.01045 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.13109 | -0.01044 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.27207 | -0.01040 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.54107 | -0.01033 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.49663 | -0.01026 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.54662 | -0.01025 | 3 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461170.47947 | -0.01017 | 2 | SAP | 1 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461170.58641 | -0.01015 | 2 | SAP | 1, 2 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.22345 | -0.01012 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.20887 | -0.01011 | 3 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.17067 | -0.01005 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.52808 | -0.01000 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.42485 | -0.00999 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.62252 | -0.00992 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.50357 | -0.00991 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460119.48135 | -0.00991 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.59752 | -0.00985 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.25679 | -0.00960 | 2 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460105.40516 | -0.00959 | 3 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.15123 | -0.00939 | 4 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.19567 | -0.00916 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461176.73937 | -0.00912 | 2 | SAP | 1 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.19984 | -0.00905 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461159.29776 | -0.00896 | 3 | SAP | 3 | no |
| `tess2023153011303-s0066-0000000208719443-0260-s_lc.fits` | 2460117.92791 | -0.00890 | 2 | SAP | 1 | no |
| `tess2026111101500-s0103-0000000208719443-0305-s_lc.fits` | 2461176.94632 | -0.00829 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3491.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:09:18Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:09:19Z: TOI-3491.01 (TIC 208719443, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:09:20Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:09:21Z: TOI-3491.01 (Pl?); TOI-3491 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 3.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 50%, 30%, 10%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3491.01: Gaia DR3 5831522739905159680 at 0.02" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3491.01: dwarf priors not applied — RUWE 7.6869884 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3491.01: 232 Gaia neighbour(s) within 52.5", contamination 62.36%; depth 32410 ppm (catalogue depth); 3 could produce it if fully eclipsed (brightest 5831522705537524992, 31.1", ΔG 0.44); a centroid test is needed |
| Pointing and quality census per event | failed | 73 persistent event(s), 15 clean; BJD 2460099.7385 suspect: MOM_CENTR2 z=+6.7, SAP_BKG z=-6.1; BJD 2460102.1399 suspect: MOM_CENTR2 z=+7.6; BJD 2460104.5496 suspect: POS_CORR2 z=-5.2, SAP_BKG z=+11.4; BJD 2460105.7017 suspect: MOM_CENTR2 z=+7.0, POS_CORR2 z=+8.5 |
| Moving objects at screen-event epochs | inconclusive | 73 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 15 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3491.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3491.01: TOI-3491 otype * (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3491-01.yaml
python -m cygnus.multi report campaigns/toi-3491-01.yaml
```
