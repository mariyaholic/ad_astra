<!-- [private Drive store] -->
# Known-object test, TOI-2645.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2645-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #724, calibrate_screen #705, event_census #716, fetch_products #704, known_signal_recovery #709, moving_objects #718, period_aliases #717, prior_art #726, residual_screen #712, stellar_context #710, variability_guard #725
- Runner finished (UTC): 2026-09-26T10:16:33Z

## Bottom line

Positive control **inconclusive**: BJD 2460014.4226: gap (catalogue 43370 ppm).
Outside the catalogued epoch the screen left 674 threshold entries forming **115 distinct event(s)**, **111 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2645.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 372818426 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 67.136823 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -56.515644 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460014.422616 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 43370.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.134 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.3956 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-07-09 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | lightcurve | 63 | True | `5b3daff05972d582` | True |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | lightcurve | 65 | False | `536dc5eb7432ff75` | True |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | lightcurve | 66 | False | `0ff04cb364dc71ea` | True |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | lightcurve | 69 | False | `49cf11bf4e7cc9f4` | True |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | lightcurve | 90 | False | `830e71bc6fa7db4e` | True |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | lightcurve | 93 | False | `fab752241276ad6b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460014.42262 | gap | 0 | — | 43370 | — |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | — | epoch not in this light curve | — | — | 43370 | — |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | — | epoch not in this light curve | — | — | 43370 | — |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | — | epoch not in this light curve | — | — | 43370 | — |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | — | epoch not in this light curve | — | — | 43370 | — |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | — | epoch not in this light curve | — | — | 43370 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 3 | False | 1h: —, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 3 | False | 1h: —, 2h: 20000, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 3 | False | 1h: 20000, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460040.39078 | -0.04621 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460040.42897 | -0.04490 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460040.39911 | -0.04353 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460190.54927 | -0.04040 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460040.38175 | -0.03981 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460769.46154 | -0.03971 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460121.25533 | -0.03962 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460831.54026 | -0.03931 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460200.64112 | -0.03908 | 36 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460189.10828 | -0.03904 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460186.21864 | -0.03903 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460191.99583 | -0.03893 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460845.97802 | -0.03890 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460114.03504 | -0.03886 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460017.31053 | -0.03881 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460765.13102 | -0.03873 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460101.04245 | -0.03872 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460851.75315 | -0.03870 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460755.02698 | -0.03868 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460837.31329 | -0.03864 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460075.05674 | -0.03859 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460832.98195 | -0.03858 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460187.66242 | -0.03855 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460028.85896 | -0.03853 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460749.25137 | -0.03849 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460835.87090 | -0.03848 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460762.24285 | -0.03848 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460753.58325 | -0.03832 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460088.04922 | -0.03828 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460750.69371 | -0.03825 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460103.93000 | -0.03823 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460020.19798 | -0.03818 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460076.49980 | -0.03805 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460118.36708 | -0.03800 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460102.48692 | -0.03800 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460752.13605 | -0.03798 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460763.68589 | -0.03797 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460033.19225 | -0.03793 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460196.32507 | -0.03793 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460080.83177 | -0.03790 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460034.63459 | -0.03786 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460199.21263 | -0.03782 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460038.96649 | -0.03782 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460184.77694 | -0.03781 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460023.08404 | -0.03779 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460036.07902 | -0.03775 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460116.92191 | -0.03774 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460018.75217 | -0.03773 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460756.46793 | -0.03772 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460077.94356 | -0.03771 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460747.80625 | -0.03770 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460040.41092 | -0.03767 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460030.30339 | -0.03766 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460202.09948 | -0.03765 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460200.68140 | -0.03758 | 22 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460853.19485 | -0.03755 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460031.74574 | -0.03755 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460766.57406 | -0.03755 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460037.52067 | -0.03753 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460082.27414 | -0.03750 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460070.72476 | -0.03747 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460183.33107 | -0.03747 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460834.42782 | -0.03746 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460089.49229 | -0.03743 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460015.86749 | -0.03739 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460112.59265 | -0.03735 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460119.81016 | -0.03729 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460197.77024 | -0.03726 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460073.61298 | -0.03720 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460021.64171 | -0.03720 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460838.75776 | -0.03718 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460093.82151 | -0.03718 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460115.48021 | -0.03713 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460092.37913 | -0.03707 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460840.20223 | -0.03705 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460025.97010 | -0.03701 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460844.53355 | -0.03699 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460770.90528 | -0.03696 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460069.28170 | -0.03692 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460848.86351 | -0.03688 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460204.98771 | -0.03680 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460203.54186 | -0.03679 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460105.37378 | -0.03674 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460098.15490 | -0.03648 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460095.26874 | -0.03643 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460099.59937 | -0.03633 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460847.41903 | -0.03630 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460024.52777 | -0.03629 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460768.02058 | -0.03619 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460072.16922 | -0.03619 | 60 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460090.93536 | -0.03600 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460079.38663 | -0.03599 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460850.30729 | -0.03592 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460083.72347 | -0.03578 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460040.37481 | -0.03519 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460027.38328 | -0.03001 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460040.44564 | -0.02113 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460095.22916 | -0.01953 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460098.19726 | -0.01715 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460121.31297 | -0.01641 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000372818426-0264-s_lc.fits` | 2460183.37135 | -0.01630 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460093.86387 | -0.01624 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000372818426-0260-s_lc.fits` | 2460121.29908 | -0.01599 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460851.71079 | -0.01560 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000372818426-0255-s_lc.fits` | 2460017.26955 | -0.01525 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460752.17980 | -0.01492 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460077.98592 | -0.01488 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460845.93705 | -0.01367 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460754.98393 | -0.01221 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460762.28660 | -0.01166 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460756.51168 | -0.01162 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000372818426-0259-s_lc.fits` | 2460082.31512 | -0.01658 | 2 | PDCSAP | 1, 2 | no |
| `tess2025071122000-s0090-0000000372818426-0287-s_lc.fits` | 2460766.53240 | -0.01289 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460837.35565 | -0.01227 | 3 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000372818426-0290-s_lc.fits` | 2460836.55911 | -0.01115 | 2 | PDCSAP+SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2645.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:16:29Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:16:31Z: TOI-2645.01 (TIC 372818426, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:16:32Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:16:32Z: TOI-2645 (*); TOI-2645.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2460014.4226: gap (catalogue 43370 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, ≤2.5, 3, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 20%, 0%, 30%, 0%, 0%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2645.01: Gaia DR3 4775424641496743808 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2645.01: Teff 5444 K, R* 0.92 ± 0.07, M* 0.94 ± 0.09, ρ* 1.23 ± 0.32 ρ☉ (dwarf sequence, M_G 5.09, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2645.01: 5 Gaia neighbour(s) within 52.5", contamination 9.44%; depth 43370 ppm (catalogue depth); 1 could produce it if fully eclipsed (brightest 4775424641496743680, 33.7", ΔG 2.61); a centroid test is needed |
| Pointing and quality census per event | failed | 111 persistent event(s), 56 clean; BJD 2460015.8675 suspect: MOM_CENTR1 z=+6.1, POS_CORR1 z=+8.7, POS_CORR2 z=+9.7, SAP_BKG z=+42.7; BJD 2460021.6417 suspect: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR2 z=+19.0, POS_CORR2 z=+23.1; BJD 2460027.3833 suspect: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), POS_CORR1 z=+5.6; BJD 2460030.3034 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 111 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 5 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2645.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2645.01: TOI-2645 otype * (star_or_other) at 0.4" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2645-01.yaml
python -m cygnus.multi report campaigns/toi-2645-01.yaml
```
