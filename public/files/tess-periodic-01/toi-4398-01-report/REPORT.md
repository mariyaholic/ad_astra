<!-- [private Drive store] -->
# Known-object test, TOI-4398.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4398-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1041, calibrate_screen #1034, event_census #1038, fetch_products #1030, known_signal_recovery #1035, moving_objects #1040, period_aliases #1039, prior_art #1043, residual_screen #1037, stellar_context #1036, variability_guard #1042
- Runner finished (UTC): 2026-09-26T10:30:52Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4398.01 (BJD 2460852.3662: recovered, depth 7254 ± 111 ppm (catalogue 8852 ppm)).
Outside the catalogued epoch the screen left 679 threshold entries forming **160 distinct event(s)**, **22 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460835.0445 matches the catalogued transit's depth (3867 vs 7254 ppm), 17.346 d later; 0 of 17 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4398.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 214243287 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 260.799238 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -51.024433 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460852.366238 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8852.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.718 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.933 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-08-26 16:00:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | lightcurve | 93 | True | `df0db98e9777e3f0` | True |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | lightcurve | 66 | False | `4c2b40d69aafac67` | True |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | lightcurve | 103 | False | `d668dcd9050db608` | True |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | lightcurve | 104 | False | `d2505750a6f9f752` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460852.36624 | recovered | 111 | 7254 ± 111 | 8852 | 0.58 |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | — | epoch not in this light curve | — | — | 8852 | — |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | — | epoch not in this light curve | — | — | 8852 | — |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | — | epoch not in this light curve | — | — | 8852 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461174.45403 | -0.00907 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461203.29501 | -0.00877 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461157.25170 | -0.00876 | 79 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461180.25980 | -0.00851 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461203.22973 | -0.00845 | 31 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461174.48250 | -0.00838 | 74 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461168.75862 | -0.00837 | 80 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461162.99162 | -0.00827 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460104.53760 | -0.00818 | 92 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460846.61323 | -0.00816 | 99 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461186.01209 | -0.00801 | 98 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460116.04525 | -0.00783 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460835.11323 | -0.00775 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.58316 | -0.00773 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460098.78614 | -0.00769 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461163.05899 | -0.00752 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.56164 | -0.00750 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.53664 | -0.00746 | 25 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.49497 | -0.00742 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460840.86116 | -0.00738 | 98 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.57483 | -0.00546 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460835.04448 | -0.00542 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461198.62207 | -0.01308 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461170.96568 | -0.01036 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.07263 | -0.01031 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.21985 | -0.01012 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.04207 | -0.00996 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461200.81653 | -0.00980 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.26708 | -0.00954 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.33931 | -0.00936 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461170.92331 | -0.00893 | 3 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461170.91567 | -0.00892 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461170.98582 | -0.00884 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.30180 | -0.00872 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.03304 | -0.00867 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461162.94857 | -0.00838 | 6 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461163.03677 | -0.00804 | 7 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461163.04579 | -0.00786 | 6 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.24208 | -0.00784 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.21569 | -0.00783 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.31153 | -0.00766 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.16569 | -0.00740 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.28070 | -0.00734 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.37376 | -0.00730 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.34737 | -0.00729 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.29139 | -0.00724 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.31403 | -0.00718 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.36126 | -0.00714 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.38097 | -0.00710 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.36890 | -0.00707 | 3 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.20805 | -0.00706 | 3 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461191.04831 | -0.00704 | 4 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461157.19128 | -0.00698 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461170.58649 | -0.00694 | 2 | SAP | 1, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.32514 | -0.00691 | 4 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.25153 | -0.00690 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.39598 | -0.00690 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461157.19614 | -0.00689 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.28695 | -0.00681 | 5 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461171.06568 | -0.00677 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.45154 | -0.00674 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461168.69681 | -0.00674 | 7 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461168.68917 | -0.00671 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.99484 | -0.00669 | 21 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461198.70401 | -0.00663 | 2 | SAP | 1, 2 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.53071 | -0.00657 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.47376 | -0.00651 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.33973 | -0.00646 | 3 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461191.07956 | -0.00641 | 13 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.35431 | -0.00634 | 6 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461191.09137 | -0.00633 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.26125 | -0.00630 | 4 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.29806 | -0.00626 | 3 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.44737 | -0.00624 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.97609 | -0.00620 | 4 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460111.52027 | -0.00611 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461157.31351 | -0.00611 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461191.06220 | -0.00609 | 10 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.42237 | -0.00607 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460850.12222 | -0.00601 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461166.40779 | -0.00598 | 3 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461200.86653 | -0.00594 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461191.03025 | -0.00579 | 20 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461200.86097 | -0.00574 | 2 | SAP | 1, 2 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461174.43667 | -0.00571 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.96011 | -0.00564 | 17 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461203.20543 | -0.00563 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000214243287-0305-s_lc.fits` | 2461162.94023 | -0.00562 | 2 | PDCSAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461198.67901 | -0.00557 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461203.03043 | -0.00557 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.82331 | -0.00550 | 4 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.69136 | -0.00546 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461200.84083 | -0.00537 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461198.68596 | -0.00535 | 4 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461198.66790 | -0.00531 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460841.42088 | -0.00530 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.87331 | -0.00523 | 10 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460111.66194 | -0.00520 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.91428 | -0.00520 | 13 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460836.54935 | -0.00519 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.88511 | -0.00513 | 5 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.75733 | -0.00510 | 3 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.94067 | -0.00498 | 9 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.90178 | -0.00493 | 3 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.85664 | -0.00492 | 12 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460118.72299 | -0.00489 | 2 | SAP | 1 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.92678 | -0.00489 | 3 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461191.01289 | -0.00484 | 3 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.74553 | -0.00481 | 8 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.44566 | -0.00477 | 2 | PDCSAP | 1, 2 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460849.77500 | -0.00475 | 4 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.83789 | -0.00474 | 13 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460111.73555 | -0.00474 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.79483 | -0.00474 | 9 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460841.49657 | -0.00470 | 3 | SAP | 2, 3 | no |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460118.22578 | -0.00463 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460111.52860 | -0.00461 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.80733 | -0.00458 | 7 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.59552 | -0.00456 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461200.89153 | -0.00456 | 2 | SAP | 1, 2 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.58803 | -0.00452 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.57066 | -0.00445 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461180.18966 | -0.00445 | 2 | PDCSAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461198.62623 | -0.00445 | 2 | SAP | 1, 2 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.71914 | -0.00440 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.68441 | -0.00440 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.64414 | -0.00434 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461200.87903 | -0.00432 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.73372 | -0.00425 | 7 | SAP | 2, 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460841.54032 | -0.00425 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461203.04223 | -0.00421 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461188.33437 | -0.00421 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461198.64846 | -0.00420 | 2 | SAP | 1, 2 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.62608 | -0.00418 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.51080 | -0.00415 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460830.43191 | -0.00414 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460841.50352 | -0.00411 | 3 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461196.95399 | -0.00408 | 2 | PDCSAP | 1, 2 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460846.54170 | -0.00408 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.51636 | -0.00406 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461196.76649 | -0.00404 | 2 | PDCSAP | 1, 2 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.77330 | -0.00404 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460841.43893 | -0.00404 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461182.63559 | -0.00403 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460836.56671 | -0.00402 | 2 | SAP | 1, 2, 3 | no |
| `tess2023153011303-s0066-0000000214243287-0260-s_lc.fits` | 2460111.30221 | -0.00399 | 2 | SAP | 1 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.61219 | -0.00394 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.89622 | -0.00390 | 3 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461184.80927 | -0.00390 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460841.48754 | -0.00390 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461203.05404 | -0.00386 | 2 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.25816 | -0.00382 | 2 | SAP | 1, 2, 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460846.68476 | -0.00366 | 2 | PDCSAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461197.38455 | -0.00366 | 2 | SAP | 2 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460849.75695 | -0.00364 | 2 | PDCSAP | 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460841.34866 | -0.00357 | 2 | SAP | 3 | no |
| `tess2025154050500-s0093-0000000214243287-0290-s_lc.fits` | 2460841.36949 | -0.00356 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461190.76358 | -0.00345 | 4 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461195.77897 | -0.00337 | 2 | SAP | 1 | no |
| `tess2026137223500-s0104-0000000214243287-0306-s_lc.fits` | 2461204.40542 | -0.00302 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460835.04448 | 3867 | 7254 | 17.3461 | 0 / 17 |  |
| 2460835.11323 | 7209 | 7254 | 17.2774 | 0 / 17 |  |
| 2460840.86116 | 7075 | 7254 | 11.5294 | 0 / 11 |  |
| 2460846.61323 | 7664 | 7254 | 5.7774 | 0 / 5 |  |
| 2460098.78614 | 7337 | 7254 | 753.6044 | 7 / 753 | 753.604, 376.802, 251.202, 188.401, 125.601, 94.2006, 5.7527 |
| 2460104.53760 | 7634 | 7254 | 747.8530 | 14 / 747 | 747.853, 373.926, 249.284, 186.963, 149.571, 124.642, 93.4816, 74.7853, 67.9866, 57.5272, 32.5153, 28.7636, 11.5054, 5.7527 |
| 2460116.04525 | 7319 | 7254 | 736.3453 | 13 / 736 | 736.345, 368.173, 245.448, 184.086, 147.269, 122.724, 92.0432, 73.6345, 56.6419, 46.0216, 23.0108, 11.5054, 5.7527 |
| 2461157.25170 | 7809 | 7254 | 304.8611 | 6 / 304 | 304.861, 152.431, 101.62, 76.2153, 50.8102, 33.8735 |
| 2461162.99162 | 7455 | 7254 | 310.6010 | 8 / 310 | 310.601, 155.3, 103.534, 77.6503, 62.1202, 51.7668, 34.5112, 17.2556 |
| 2461163.05899 | 5710 | 7254 | 310.6684 | 10 / 310 | 310.668, 155.334, 103.556, 77.6671, 62.1337, 51.7781, 34.5187, 17.2594, 11.5062, 5.7531 |
| 2461168.75862 | 7695 | 7254 | 316.3680 | 6 / 316 | 316.368, 158.184, 79.092, 63.2736, 45.1954, 22.5977 |
| 2461174.45403 | 5903 | 7254 | 322.0634 | 5 / 322 | 322.063, 161.032, 80.5159, 64.4127, 40.2579 |
| 2461174.48250 | 7760 | 7254 | 322.0919 | 5 / 322 | 322.092, 161.046, 80.523, 64.4184, 40.2615 |
| 2461180.25980 | 7595 | 7254 | 327.8692 | 8 / 327 | 327.869, 163.935, 109.29, 65.5738, 54.6449, 36.4299, 29.8063, 17.2563 |
| 2461186.01209 | 7562 | 7254 | 333.6215 | 5 / 333 | 333.622, 166.811, 111.207, 55.6036, 47.6602 |
| 2461197.49497 | 6740 | 7254 | 345.1044 | 7 / 345 | 345.104, 172.552, 115.035, 86.2761, 69.0209, 34.5104, 17.2552 |
| 2461197.53664 | 6705 | 7254 | 345.1461 | 12 / 345 | 345.146, 172.573, 115.049, 86.2865, 69.0292, 57.5243, 34.5146, 28.7622, 23.0097, 17.2573, 11.5049, 5.7524 |
| 2461197.56164 | 5575 | 7254 | 345.1711 | 12 / 345 | 345.171, 172.585, 115.057, 86.2928, 69.0342, 57.5285, 34.5171, 28.7643, 23.0114, 17.2586, 11.5057, 5.7529 |
| 2461197.57483 | 4580 | 7254 | 345.1842 | 12 / 345 | 345.184, 172.592, 115.061, 86.2961, 69.0368, 57.5307, 34.5184, 28.7654, 23.0123, 17.2592, 11.5061, 5.7531 |
| 2461203.22973 | 7446 | 7254 | 350.8391 | 6 / 350 | 350.839, 175.42, 116.946, 87.7098, 70.1678, 58.4732 |
| 2461203.29501 | 8001 | 7254 | 350.9044 | 7 / 350 | 350.904, 175.452, 116.968, 87.7261, 70.1809, 58.4841, 5.7525 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4398.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:30:49Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:30:50Z: TOI-4398.01 (TIC 214243287, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:30:51Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:30:52Z: CD-50 11233 (**)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460852.3662: recovered, depth 7254 ± 111 ppm (catalogue 8852 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 3.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 20%, 0%, 10%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 21 repeat-candidate event(s); first at BJD 2460835.0445, ΔT = 17.346 d, 0 of 17 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4398.01: Gaia DR3 5925395434861799424 at 0.15" (propagated 2016.0 → J2015.5; 0.15" unpropagated) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-4398.01: dwarf priors not applied — no positive parallax or G magnitude; RUWE n/a ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4398.01: 206 Gaia neighbour(s) within 52.5", contamination 50.93%; depth 7254 ppm (measured depth of the recovered catalogued transit); 7 could produce it if fully eclipsed (brightest 5925395430559181184, 28.3", ΔG 0.76); a centroid test is needed |
| Pointing and quality census per event | failed | 22 persistent event(s), 11 clean; BJD 2460840.8612 suspect: MOM_CENTR2 z=+7.6, POS_CORR1 z=-5.1, POS_CORR2 z=+7.5, SAP_BKG z=+5.9; BJD 2460098.7861 suspect: SAP_BKG z=-5.1; BJD 2460104.5376 suspect: MOM_CENTR2 z=+5.1, POS_CORR2 z=+5.4, SAP_BKG z=-12.2; BJD 2461162.9916 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 22 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 4 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-4398.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-4398.01: CD-50 11233 otype ** (multiple) at 0.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4398-01.yaml
python -m cygnus.multi report campaigns/toi-4398-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead event is the target's own catalogued ephemeris transit** (131 periods before the reference; the difference image is also 11.2 arcsec off at 3.3 sigma). No new signal.

Source: `campaigns/toi-4398-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
