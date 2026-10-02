<!-- cygnus:generated-draft -->
# Known-object test, TOI-2255.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2255-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4440, calibrate_screen #4408, event_census #4423, fetch_independent #4426, fetch_products #4393, known_signal_recovery #4417, moving_objects #4425, period_aliases #4424, prior_art #4442, residual_screen #4419, stellar_context #4418, variability_guard #4441
- Runner finished (UTC): 2026-09-30T21:52:48Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2255.01 (BJD 2459727.1174: not recovered, depth 6379 ± 362 ppm (catalogue 9860 ppm); BJD 2459739.0700: recovered, depth 6431 ± 388 ppm (catalogue 9860 ppm); BJD 2458962.1503: recovered, depth 5952 ± 413 ppm (catalogue 9860 ppm); BJD 2458974.1029: recovered, depth 6336 ± 417 ppm (catalogue 9860 ppm); BJD 2458986.0556: not recovered, depth 3090 ± 1727 ppm (catalogue 9860 ppm); BJD 2458998.0082: not recovered, depth 6403 ± 1422 ppm (catalogue 9860 ppm); BJD 2459021.9134: not recovered, depth 5154 ± 465 ppm (catalogue 9860 ppm); BJD 2459033.8660: partial, depth 6327 ± 471 ppm (catalogue 9860 ppm); BJD 2459858.5961: recovered, depth 6109 ± 348 ppm (catalogue 9860 ppm); BJD 2459870.5487: recovered, depth 7135 ± 355 ppm (catalogue 9860 ppm); BJD 2459918.3592: recovered, depth 6690 ± 329 ppm (catalogue 9860 ppm); BJD 2459930.3118: not recovered, depth 2085 ± 729 ppm (catalogue 9860 ppm)).
Outside the catalogued epoch the screen left 86 threshold entries forming **57 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2255.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 265146266 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 316.892698 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 74.383252 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459727.117395 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 11.9526103 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 9860.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.74 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.0836 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-12-20 12:02:56 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022138205153-s0052-0000000265146266-0224-s_lc.fits` | lightcurve | 52 | True | `4ba6f41ba0e8b973` | True |
| `tess2020106103520-s0024-0000000265146266-0180-s_lc.fits` | lightcurve | 24 | False | `baf8fa2a814cccc2` | True |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | lightcurve | 25 | False | `3afe7f83d08584e8` | True |
| `tess2020160202036-s0026-0000000265146266-0188-s_lc.fits` | lightcurve | 26 | False | `b780de05f8229280` | True |
| `tess2022273165103-s0057-0000000265146266-0245-s_lc.fits` | lightcurve | 57 | False | `909bc09f5cff9045` | True |
| `tess2022330142927-s0059-0000000265146266-0248-s_lc.fits` | lightcurve | 59 | False | `5c3b012038367b6a` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022138205153-s0052-0000000265146266-0224-s_lc.fits` | 2459727.11740 | not_recovered | 82 | 6379 ± 362 | 9860 | — |
| `tess2022138205153-s0052-0000000265146266-0224-s_lc.fits` | 2459739.07001 | recovered | 83 | 6431 ± 388 | 9860 | 0.42 |
| `tess2020106103520-s0024-0000000265146266-0180-s_lc.fits` | 2458962.15034 | recovered | 80 | 5952 ± 413 | 9860 | 0.43 |
| `tess2020106103520-s0024-0000000265146266-0180-s_lc.fits` | 2458974.10295 | recovered | 82 | 6336 ± 417 | 9860 | -0.00 |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458986.05556 | not_recovered | 79 | 3090 ± 1727 | 9860 | — |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458998.00817 | not_recovered | 82 | 6403 ± 1422 | 9860 | — |
| `tess2020160202036-s0026-0000000265146266-0188-s_lc.fits` | 2459021.91339 | not_recovered | 81 | 5154 ± 465 | 9860 | — |
| `tess2020160202036-s0026-0000000265146266-0188-s_lc.fits` | 2459033.86600 | partial | 78 | 6327 ± 471 | 9860 | 0.67 |
| `tess2022273165103-s0057-0000000265146266-0245-s_lc.fits` | 2459858.59611 | recovered | 82 | 6109 ± 348 | 9860 | 0.29 |
| `tess2022273165103-s0057-0000000265146266-0245-s_lc.fits` | 2459870.54872 | recovered | 82 | 7135 ± 355 | 9860 | 0.08 |
| `tess2022330142927-s0059-0000000265146266-0248-s_lc.fits` | 2459918.35916 | recovered | 82 | 6690 ± 329 | 9860 | -0.49 |
| `tess2022330142927-s0059-0000000265146266-0248-s_lc.fits` | 2459930.31177 | not_recovered | 17 | 2085 ± 729 | 9860 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022138205153-s0052-0000000265146266-0224-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2020106103520-s0024-0000000265146266-0180-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | — | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2020160202036-s0026-0000000265146266-0188-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2022273165103-s0057-0000000265146266-0245-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2022330142927-s0059-0000000265146266-0248-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458984.45001 | -0.03672 | 170 | PDCSAP+SAP | 1, 2 | yes |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458986.44655 | -0.05068 | 85 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458986.53405 | -0.04921 | 78 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458999.46885 | -0.04604 | 13 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458999.49941 | -0.04492 | 29 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458999.44663 | -0.04422 | 17 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.52021 | -0.04176 | 5 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.48340 | -0.04130 | 4 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458999.42719 | -0.04108 | 25 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458999.52719 | -0.04104 | 17 | SAP | 1, 2, 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.55285 | -0.04103 | 2 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.54868 | -0.04076 | 2 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.53826 | -0.04053 | 5 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.50562 | -0.04032 | 2 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.58757 | -0.04026 | 4 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.52924 | -0.04023 | 6 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.47646 | -0.04006 | 2 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.56257 | -0.04003 | 10 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.61813 | -0.04001 | 8 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.57507 | -0.03969 | 6 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.41812 | -0.03958 | 2 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.51187 | -0.03958 | 5 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.59799 | -0.03943 | 9 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.58201 | -0.03943 | 2 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.49104 | -0.03934 | 5 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.60771 | -0.03926 | 3 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.62924 | -0.03908 | 6 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.43410 | -0.03903 | 7 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.42298 | -0.03892 | 3 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.39590 | -0.03859 | 2 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.45771 | -0.03822 | 3 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458995.49937 | -0.03815 | 5 | SAP | 3 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458999.56677 | -0.03541 | 16 | SAP | 1, 2 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458997.48759 | -0.03243 | 2 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458999.39455 | -0.03225 | 4 | SAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458997.51120 | -0.03137 | 8 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458998.25426 | -0.03073 | 2 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458987.48891 | -0.03014 | 2 | SAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458999.57094 | -0.03004 | 2 | SAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458997.50078 | -0.02999 | 5 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458997.52509 | -0.02990 | 10 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458998.45287 | -0.02981 | 2 | SAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458985.50974 | -0.02975 | 2 | SAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458997.54314 | -0.02959 | 2 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458997.53689 | -0.02958 | 5 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458987.51808 | -0.02949 | 2 | SAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458998.45773 | -0.02924 | 3 | SAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458984.31668 | -0.02918 | 2 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458985.45071 | -0.02898 | 7 | SAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458985.47779 | -0.02881 | 4 | SAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458997.49314 | -0.02874 | 4 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458997.55078 | -0.02834 | 7 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458998.26954 | -0.02804 | 2 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458984.57154 | -0.02775 | 3 | PDCSAP | 1 | no |
| `tess2020133194932-s0025-0000000265146266-0182-s_lc.fits` | 2458997.48273 | -0.02748 | 3 | PDCSAP | 1 | no |
| `tess2020106103520-s0024-0000000265146266-0180-s_lc.fits` | 2458975.37917 | -0.01273 | 2 | SAP | 1, 2, 3 | no |
| `tess2020106103520-s0024-0000000265146266-0180-s_lc.fits` | 2458969.97989 | -0.00996 | 3 | PDCSAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2255.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:52:40Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:52:42Z: TOI-2255.01 (TIC 265146266, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:52:44Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:52:45Z: TOI-2255.01 (Pl?); TOI-2255 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459727.1174: not recovered, depth 6379 ± 362 ppm (catalogue 9860 ppm); BJD 2459739.0700: recovered, depth 6431 ± 388 ppm (catalogue 9860 ppm); BJD 2458962.1503: recovered, depth 5952 ± 413 ppm (catalogue 9860 ppm); BJD 2458974.1029: recovered, depth 6336 ± 417 ppm (catalogue 9860 ppm); BJD 2458986.0556: not recovered, depth 3090 ± 1727 ppm (catalogue 9860 ppm); BJD 2458998.0082: not recovered, depth 6403 ± 1422 ppm (catalogue 9860 ppm); BJD 2459021.9134: not recovered, depth 5154 ± 465 ppm (catalogue 9860 ppm); BJD 2459033.8660: partial, depth 6327 ± 471 ppm (catalogue 9860 ppm); BJD 2459858.5961: recovered, depth 6109 ± 348 ppm (catalogue 9860 ppm); BJD 2459870.5487: recovered, depth 7135 ± 355 ppm (catalogue 9860 ppm); BJD 2459918.3592: recovered, depth 6690 ± 329 ppm (catalogue 9860 ppm); BJD 2459930.3118: not recovered, depth 2085 ± 729 ppm (catalogue 9860 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | inconclusive | screen run at each light curve's own k* (3.5, ≤2.5, none, 3, 3, 3; ≤ 0 persistent null events outside the veto); 1 light curve(s) reached no k* on the grid and used the declared k, uncalibrated |
| Synthetic signal injection–recovery | inconclusive | completeness for 2000 ppm, 4.0 h boxes at the declared threshold: 0%, 0%, 0%, 0%, 0%, 0% per light curve (pass mark 90%) |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2255.01: Gaia DR3 2276846933380823936 at 0.05" (propagated 2016.0 → J2015.5; 0.05" unpropagated) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-2255.01: dwarf priors not applied — no positive parallax or G magnitude; RUWE n/a ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2255.01: 12 Gaia neighbour(s) within 52.5", contamination 17.63%; depth 6431 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 2276847139539677824, 41.2", ΔG 2.44); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2458984.4500 suspect: POS_CORR1 z=-6.7, POS_CORR2 z=-6.9, SAP_BKG z=+6.5 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2255.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2255.01: TOI-2255 otype * (star_or_other) at 0.4" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2255-01.yaml
python -m cygnus.multi report campaigns/toi-2255-01.yaml
```
