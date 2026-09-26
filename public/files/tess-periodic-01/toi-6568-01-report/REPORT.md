<!-- [private Drive store] -->
# Known-object test, TOI-6568.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6568-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #869, calibrate_screen #861, event_census #865, fetch_products #857, known_signal_recovery #862, moving_objects #867, period_aliases #866, prior_art #871, residual_screen #864, stellar_context #863, variability_guard #870
- Runner finished (UTC): 2026-09-26T10:21:50Z

## Bottom line

Positive control **failed**: BJD 2460068.7591: not recovered, depth -0 ± 308 ppm (catalogue 15419 ppm).
Outside the catalogued epoch the screen left 400 threshold entries forming **149 distinct event(s)**, **7 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6568.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 253126207 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 194.684003 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -58.476742 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460068.759071 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 15418.7232538 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.3786259 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.1102 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-06-11 12:03:27 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | lightcurve | 65 | True | `504f765550102d1c` | True |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | lightcurve | 64 | False | `2291e15cca34c272` | True |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | lightcurve | 99 | False | `477b7a61895f4ccd` | True |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | lightcurve | 100 | False | `0f153aaf70098bc6` | True |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | lightcurve | 101 | False | `6e3a0cf9a5deae59` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460068.75907 | not_recovered | 77 | -0 ± 308 | 15419 | — |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | — | epoch not in this light curve | — | — | 15419 | — |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 15419 | — |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | — | epoch not in this light curve | — | — | 15419 | — |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 15419 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 5000, 8h: 10000 |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461114.95432 | -0.01484 | 114 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461097.51721 | -0.01481 | 112 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460086.19741 | -0.01435 | 113 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460051.32242 | -0.01424 | 113 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461080.07996 | -0.01357 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460051.40367 | -0.00928 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460089.84941 | -0.00839 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.25302 | -0.01432 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460095.99785 | -0.01380 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.25788 | -0.01334 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.14121 | -0.01276 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.20587 | -0.01262 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460096.18396 | -0.01260 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.11205 | -0.01256 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460089.82857 | -0.01147 | 2 | SAP | 1, 2 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461099.36454 | -0.01140 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.20649 | -0.01106 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461092.87942 | -0.01092 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.87054 | -0.01083 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.81846 | -0.01074 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.06344 | -0.01059 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.16274 | -0.01054 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460089.92440 | -0.01040 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461093.14611 | -0.01039 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460096.23673 | -0.01037 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.72112 | -0.01027 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461099.28537 | -0.01016 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.28566 | -0.01012 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.86291 | -0.01002 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.11281 | -0.00998 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.15309 | -0.00990 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.17531 | -0.00985 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.30093 | -0.00979 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460089.95635 | -0.00968 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.27802 | -0.00947 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460096.05201 | -0.00937 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.22732 | -0.00921 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.18782 | -0.00918 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.96205 | -0.00914 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.11837 | -0.00912 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.73790 | -0.00906 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461092.97526 | -0.00901 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.15510 | -0.00900 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.98844 | -0.00897 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.19677 | -0.00896 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.02947 | -0.00894 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.85735 | -0.00885 | 3 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461099.59789 | -0.00882 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461093.27667 | -0.00881 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.09260 | -0.00876 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460089.64108 | -0.00875 | 2 | SAP | 1, 2, 3 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461093.32112 | -0.00868 | 2 | SAP | 2 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.10510 | -0.00867 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.39899 | -0.00858 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.90863 | -0.00850 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.21143 | -0.00847 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460094.77288 | -0.00845 | 2 | PDCSAP | 1 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461092.84886 | -0.00844 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.92738 | -0.00836 | 3 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.07600 | -0.00835 | 3 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.10309 | -0.00831 | 4 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.40872 | -0.00830 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.72945 | -0.00823 | 2 | SAP | 2 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461080.15774 | -0.00822 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460090.48133 | -0.00820 | 4 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.00927 | -0.00806 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460090.05773 | -0.00806 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.00725 | -0.00806 | 4 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.50039 | -0.00805 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.16281 | -0.00804 | 4 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.72455 | -0.00803 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461101.23411 | -0.00803 | 2 | PDCSAP | 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461103.35647 | -0.00802 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.14892 | -0.00797 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.08225 | -0.00794 | 3 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461093.18083 | -0.00789 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460095.98396 | -0.00789 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.79543 | -0.00778 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.41983 | -0.00776 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.87594 | -0.00774 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460090.53272 | -0.00770 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461101.08827 | -0.00762 | 2 | PDCSAP | 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.94261 | -0.00752 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.98641 | -0.00752 | 2 | SAP | 2 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460096.10965 | -0.00749 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461101.76470 | -0.00748 | 2 | PDCSAP | 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.97038 | -0.00739 | 4 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460090.50217 | -0.00734 | 2 | SAP | 1 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.12177 | -0.00734 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.06559 | -0.00733 | 5 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.86344 | -0.00733 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460090.48967 | -0.00729 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.84400 | -0.00728 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.77818 | -0.00727 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460064.70938 | -0.00727 | 2 | PDCSAP | 2 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.17316 | -0.00726 | 2 | SAP | 2, 3 | no |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 2461099.46732 | -0.00722 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.02872 | -0.00709 | 3 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461100.89937 | -0.00706 | 2 | PDCSAP | 1, 2 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.94955 | -0.00706 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.23288 | -0.00705 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460089.79663 | -0.00701 | 2 | SAP | 1, 2 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.05031 | -0.00699 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460089.66469 | -0.00695 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.64623 | -0.00694 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.88502 | -0.00691 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460089.84385 | -0.00686 | 2 | SAP | 1 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.77112 | -0.00683 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.01691 | -0.00683 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460083.27316 | -0.00678 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461052.86633 | -0.00673 | 3 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460067.65939 | -0.00668 | 2 | PDCSAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.86415 | -0.00667 | 3 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.80596 | -0.00665 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.87179 | -0.00650 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461052.88855 | -0.00646 | 3 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461048.85982 | -0.00643 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.09198 | -0.00641 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.79332 | -0.00641 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460082.86969 | -0.00639 | 3 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.74195 | -0.00638 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461119.02259 | -0.00625 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461100.91603 | -0.00623 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.81207 | -0.00614 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 2461111.11523 | -0.00612 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460090.53689 | -0.00612 | 2 | SAP | 1 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.83012 | -0.00608 | 2 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.70653 | -0.00606 | 3 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.80651 | -0.00605 | 4 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.19198 | -0.00604 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.18226 | -0.00598 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460061.21908 | -0.00596 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.65234 | -0.00595 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.71484 | -0.00593 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.53845 | -0.00592 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460090.04037 | -0.00590 | 3 | SAP | 1 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.73568 | -0.00578 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.54472 | -0.00578 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.77807 | -0.00575 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 2460090.60078 | -0.00572 | 2 | SAP | 1 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.57111 | -0.00571 | 2 | SAP | 1 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.00030 | -0.00570 | 2 | SAP | 2 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.66068 | -0.00570 | 2 | SAP | 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.99475 | -0.00560 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.12809 | -0.00553 | 2 | SAP | 1, 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461072.89474 | -0.00528 | 2 | SAP | 2 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.84748 | -0.00526 | 3 | SAP | 2, 3 | no |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 2461073.10864 | -0.00516 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 2460054.70859 | -0.00496 | 3 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6568.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:21:47Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:21:48Z: TOI-6568.01 (TIC 253126207, disposition PC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:21:50Z: Gaia DR3 6057181524203082752 (type E, P 0.312563 d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:21:50Z: Gaia DR3 6057181524203082752 (EB*); TYC 8660-1583-1 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2460068.7591: not recovered, depth -0 ± 308 ppm (catalogue 15419 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 30%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6568.01: Gaia DR3 6057181524220247680 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6568.01: Teff 5919 K, R* 1.32 ± 0.11, M* 1.21 ± 0.12, ρ* 0.53 ± 0.14 ρ☉ (dwarf sequence, M_G 3.67, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6568.01: 208 Gaia neighbour(s) within 52.5", contamination 36.18%; depth 15419 ppm (catalogue depth); 3 could produce it if fully eclipsed (brightest 6057181524220244480, 17.1", ΔG 2.24); a centroid test is needed |
| Pointing and quality census per event | failed | 7 persistent event(s), 4 clean; BJD 2460089.8494 suspect: manual exclude (in event), SAP_BKG z=+16.3; BJD 2460051.3224 suspect: MOM_CENTR2 z=-5.5; BJD 2461080.0800 suspect: MOM_CENTR2 z=+5.4, POS_CORR2 z=+6.5, SAP_BKG z=-6.3 |
| Moving objects at screen-event epochs | passed | 7 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6568.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-6568.01: TYC 8660-1583-1 otype SB* (multiple) at 0.4" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6568-01.yaml
python -m cygnus.multi report campaigns/toi-6568-01.yaml
```
