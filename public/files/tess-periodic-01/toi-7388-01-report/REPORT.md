<!-- [private Drive store] -->
# Known-object test, TOI-7388.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-7388-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1093, calibrate_screen #873, event_census #880, fetch_products #872, known_signal_recovery #874, moving_objects #985, period_aliases #881, prior_art #1095, residual_screen #876, stellar_context #875, variability_guard #1094
- Runner finished (UTC): 2026-09-26T10:34:23Z

## Bottom line

Positive control **inconclusive**: BJD 2460718.2887: gap (catalogue 767910 ppm).
Outside the catalogued epoch the screen left 1283 threshold entries forming **236 distinct event(s)**, **201 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-7388.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 124573902 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 158.903163 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -5.355998 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460718.288712 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 767910.313098 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 0.3988306 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 17.007 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-09-05 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | lightcurve | 89 | True | `ec0634d388f8727a` | True |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | lightcurve | 35 | False | `173bcf94642cede8` | True |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | lightcurve | 62 | False | `df62cbc637511122` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460718.28871 | gap | 0 | — | 767910 | — |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | — | epoch not in this light curve | — | — | 767910 | — |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | — | epoch not in this light curve | — | — | 767910 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: 500 |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: 500 |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: 500 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460011.35754 | -1.12407 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460006.69782 | -1.11829 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459999.37555 | -1.10168 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459275.13566 | -1.08512 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459998.37692 | -1.07080 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460005.69920 | -1.05912 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460009.36032 | -1.05509 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460727.94065 | -1.04015 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460745.24835 | -1.03031 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460736.92824 | -1.02820 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460005.36656 | -1.02756 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459257.16309 | -1.02713 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.81473 | -1.02438 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459994.38170 | -1.02153 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460006.36448 | -1.01550 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459258.82703 | -1.00115 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460009.69366 | -1.00007 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460740.59004 | -0.99901 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460736.59491 | -0.99670 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459256.82974 | -0.98354 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459992.05247 | -0.98235 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459276.46900 | -0.97669 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460740.25879 | -0.97306 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460011.02421 | -0.97052 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460742.58517 | -0.96886 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460012.02281 | -0.96834 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459262.82021 | -0.96502 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460732.60184 | -0.95857 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459994.71643 | -0.95747 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459995.38103 | -0.95746 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460732.26781 | -0.95611 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460734.26713 | -0.95560 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459273.80509 | -0.93982 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460743.25253 | -0.93797 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459996.71300 | -0.93382 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459259.49025 | -0.92775 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460721.61829 | -0.92586 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460010.69226 | -0.92349 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459260.49098 | -0.92306 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459991.05244 | -0.91736 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460730.93723 | -0.91602 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459272.13980 | -0.91516 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459279.13219 | -0.91463 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459991.72052 | -0.91412 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460744.25044 | -0.91396 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460722.95096 | -0.91215 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460735.26574 | -0.91089 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460004.03530 | -0.90974 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460738.59213 | -0.90682 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459991.05661 | -0.90641 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460733.60046 | -0.90405 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460743.58517 | -0.90204 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459997.04565 | -0.90063 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460727.27675 | -0.90047 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460011.68879 | -0.89844 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460007.36310 | -0.89580 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459277.79816 | -0.89572 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460008.69435 | -0.89342 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460735.93033 | -0.89209 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459272.47314 | -0.89080 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459996.37966 | -0.88960 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460737.26158 | -0.88940 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459990.38923 | -0.88897 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459990.05588 | -0.88698 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459994.04836 | -0.88560 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459992.38790 | -0.88524 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459256.16444 | -0.88491 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460720.61965 | -0.88303 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459261.48962 | -0.88242 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460731.60321 | -0.88221 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460006.03254 | -0.88153 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459995.71367 | -0.88090 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460723.94821 | -0.88028 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459997.37829 | -0.88004 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460721.95094 | -0.87986 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460728.27677 | -0.87782 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460013.35474 | -0.87670 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460000.37417 | -0.87483 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459990.72118 | -0.87475 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459279.12802 | -0.87385 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459259.82568 | -0.87150 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459262.48825 | -0.87021 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459264.81748 | -0.86793 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460003.70336 | -0.86455 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460728.94067 | -0.86413 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459264.15218 | -0.86326 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460729.27332 | -0.86076 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460733.93310 | -0.85915 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460740.92338 | -0.85868 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460734.59630 | -0.85593 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460731.27057 | -0.85436 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460004.36864 | -0.85396 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460728.60803 | -0.85384 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459989.72393 | -0.85338 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459998.70956 | -0.84943 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460000.04014 | -0.84849 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460737.59491 | -0.84606 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459991.38717 | -0.84569 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460725.27949 | -0.84510 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460010.35893 | -0.84425 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460738.92269 | -0.84385 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460007.03046 | -0.84371 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460741.25324 | -0.84207 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459278.79608 | -0.84194 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460741.25740 | -0.84194 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460742.91781 | -0.84110 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460012.35545 | -0.83940 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459996.04771 | -0.83840 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460720.95300 | -0.83782 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460742.25323 | -0.83687 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459276.13427 | -0.83674 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459992.38303 | -0.83599 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459998.04358 | -0.83383 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460013.02141 | -0.83264 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460010.02560 | -0.83253 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459274.80232 | -0.82731 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460739.59213 | -0.82540 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460721.28495 | -0.82394 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460719.62101 | -0.82349 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460003.37002 | -0.82128 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460737.92755 | -0.82028 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459264.48414 | -0.81998 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459993.71710 | -0.81966 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460740.25463 | -0.81560 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460744.58377 | -0.81486 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459993.05180 | -0.81290 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460738.26019 | -0.81265 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460729.60665 | -0.81181 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459997.71163 | -0.80801 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459262.15630 | -0.80773 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460741.58865 | -0.80667 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459276.46413 | -0.80354 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459993.38376 | -0.80105 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459276.79955 | -0.79992 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460724.94684 | -0.79964 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460724.28086 | -0.79777 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459992.71846 | -0.79619 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460744.91849 | -0.79427 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460726.61077 | -0.79081 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459278.13080 | -0.78949 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460728.27260 | -0.78877 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460736.26158 | -0.78793 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460734.93171 | -0.78785 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459273.13842 | -0.78682 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460741.92059 | -0.78624 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460720.28492 | -0.78519 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459259.49442 | -0.78237 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460723.28292 | -0.77721 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460008.02838 | -0.77546 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459274.13704 | -0.77483 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460722.61554 | -0.77256 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460730.27125 | -0.77141 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459263.81884 | -0.76942 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459272.80717 | -0.76920 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459273.47176 | -0.76801 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460730.60459 | -0.76789 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459265.81611 | -0.76699 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460008.36171 | -0.76613 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459994.05252 | -0.76337 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460722.28636 | -0.76228 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460743.91780 | -0.76168 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459278.46344 | -0.76137 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460724.61350 | -0.76065 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460729.93860 | -0.75671 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459999.70819 | -0.75660 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459259.16038 | -0.74568 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459261.15697 | -0.74121 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459279.46135 | -0.73929 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460005.03392 | -0.73887 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459277.46552 | -0.73870 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459275.80163 | -0.73661 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460012.68808 | -0.73512 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460735.59699 | -0.73454 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459275.46830 | -0.73354 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459279.79607 | -0.73241 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2459999.04082 | -0.73181 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460726.27604 | -0.73096 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459265.15012 | -0.72894 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459260.15833 | -0.72330 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459257.82839 | -0.72208 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459256.49709 | -0.71833 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460719.95575 | -0.71731 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459267.14876 | -0.71646 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460004.70059 | -0.71407 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460723.61487 | -0.70620 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460003.03669 | -0.70500 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460726.94341 | -0.69418 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459260.82362 | -0.69258 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459263.48620 | -0.68894 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459265.48346 | -0.68852 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459263.15355 | -0.68338 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460739.25741 | -0.68318 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459277.13358 | -0.68085 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.48139 | -0.68061 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459258.16034 | -0.67028 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459261.82226 | -0.66805 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459257.49504 | -0.65987 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459258.49300 | -0.64760 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000124573902-0254-s_lc.fits` | 2460009.02768 | -0.64067 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460734.60046 | -0.62930 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459274.47038 | -0.61098 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459256.22764 | -0.49242 | 2 | PDCSAP | 3 | no |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460739.92477 | -0.20368 | 3 | SAP | 1, 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.50639 | -0.19905 | 3 | SAP | 1, 2, 3 | no |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460725.94686 | -0.19473 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.59459 | -0.18799 | 2 | SAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000124573902-0286-s_lc.fits` | 2460731.93377 | -0.18494 | 2 | SAP | 1, 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.57028 | -0.17125 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.39875 | -0.16469 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.46820 | -0.16444 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.54112 | -0.16123 | 7 | SAP | 1, 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.52237 | -0.15980 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.48973 | -0.15967 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.46264 | -0.15397 | 4 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.50014 | -0.15312 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.45292 | -0.15208 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.44667 | -0.15112 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.66820 | -0.14992 | 2 | SAP | 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.42306 | -0.14894 | 4 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.40987 | -0.14520 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.51751 | -0.14284 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.40570 | -0.14271 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.62098 | -0.14259 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.75154 | -0.14129 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.37931 | -0.13956 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.52792 | -0.13807 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.43278 | -0.13699 | 3 | SAP | 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.55362 | -0.13574 | 5 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.65570 | -0.13468 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.58278 | -0.13349 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.41403 | -0.13134 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.60987 | -0.13057 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.57723 | -0.12818 | 3 | SAP | 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.44181 | -0.12668 | 2 | SAP | 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.43764 | -0.12621 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000124573902-0205-s_lc.fits` | 2459266.62584 | -0.11815 | 3 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-7388.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:34:20Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:34:22Z: TOI-7388.01 (TIC 124573902, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:34:23Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:34:23Z: WT 1814 (WD*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2460718.2887: gap (catalogue 767910 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 40%, 50%, 50% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-7388.01: Gaia DR3 3777499843652893824 at 0.00" (propagated 2016.0 → J2015.5; 0.09" unpropagated, proper-motion shift 0.10") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-7388.01: dwarf priors not applied — 9.72 mag below (subdwarf or bad photometry) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-7388.01: 6 Gaia neighbour(s) within 52.5", contamination 83.93%; depth 767910 ppm (catalogue depth); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 201 persistent event(s), 155 clean; BJD 2460719.6210 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=-8.2, POS_CORR1 z=-12.3, POS_CORR2 z=+13.0, SAP_BKG z=+39.7; BJD 2460719.9557 suspect: SAP_BKG z=+86.3; BJD 2460720.2849 suspect: SAP_BKG z=+22.0; BJD 2460724.6135 suspect: MOM_CENTR2 z=-5.3 |
| Moving objects at screen-event epochs | inconclusive | 201 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 27 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-7388.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-7388.01: WT 1814 otype WD* (star_or_other) at 3.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-7388-01.yaml
python -m cygnus.multi report campaigns/toi-7388-01.yaml
```
