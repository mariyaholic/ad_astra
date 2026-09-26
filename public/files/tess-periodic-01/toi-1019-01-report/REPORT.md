<!-- [private Drive store] -->
# Known-object test, TOI-1019.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1019-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #351, calibrate_screen #291, event_census #302, fetch_products #287, known_signal_recovery #295, moving_objects #336, period_aliases #303, prior_art #353, residual_screen #298, stellar_context #296, variability_guard #352
- Runner finished (UTC): 2026-09-26T10:03:31Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1019.01 (BJD 2459232.4469: recovered, depth 18282 ± 162 ppm (catalogue 20797 ppm)).
Outside the catalogued epoch the screen left 247 threshold entries forming **45 distinct event(s)**, **36 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459237.6809 matches the catalogued transit's depth (17955 vs 18282 ppm), 5.201 d later; 0 of 5 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1019.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 341420329 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 120.147994 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -54.878552 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459232.446864 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 20796.9416293 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.7078139 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.6348 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-02-16 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | lightcurve | 34 | True | `09969ac43c355748` | True |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | lightcurve | 35 | False | `d077f89f77211c6f` | True |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | lightcurve | 36 | False | `14f1102c8a501929` | True |
| `tess2023018032328-s0061-0000000341420329-0250-s_lc.fits` | lightcurve | 61 | False | `7a574d296d17577d` | True |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | lightcurve | 62 | False | `c12c3edf5abc5de2` | True |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | lightcurve | 63 | False | `3e7cb848fda09956` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459232.44686 | recovered | 111 | 18282 ± 162 | 20797 | 0.80 |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | — | epoch not in this light curve | — | — | 20797 | — |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | — | epoch not in this light curve | — | — | 20797 | — |
| `tess2023018032328-s0061-0000000341420329-0250-s_lc.fits` | — | epoch not in this light curve | — | — | 20797 | — |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | — | epoch not in this light curve | — | — | 20797 | — |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | — | epoch not in this light curve | — | — | 20797 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023018032328-s0061-0000000341420329-0250-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 10000, 4h: 5000, 8h: 10000 |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459253.40471 | -0.02032 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 2459305.75652 | -0.02030 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459253.41860 | -0.02007 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | 2460012.32941 | -0.01985 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459248.14980 | -0.01983 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460017.56201 | -0.01958 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | 2460007.07320 | -0.01957 | 71 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000341420329-0250-s_lc.fits` | 2459970.45422 | -0.01954 | 88 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460022.79251 | -0.01948 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | 2459996.62807 | -0.01939 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460038.49643 | -0.01937 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 2459305.71347 | -0.01930 | 51 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | 2459991.39263 | -0.01929 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000341420329-0250-s_lc.fits` | 2459965.22149 | -0.01926 | 91 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | 2459258.61795 | -0.01924 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 2459300.49065 | -0.01918 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000341420329-0250-s_lc.fits` | 2459986.15857 | -0.01913 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460033.26528 | -0.01913 | 96 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 2459284.79015 | -0.01912 | 95 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 2459290.02274 | -0.01908 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | 2459263.85131 | -0.01908 | 93 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459237.68090 | -0.01906 | 96 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000341420329-0250-s_lc.fits` | 2459980.92380 | -0.01903 | 91 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | 2459274.32284 | -0.01889 | 86 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459242.91501 | -0.01889 | 98 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459253.35819 | -0.01889 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460028.02924 | -0.01886 | 94 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459253.42902 | -0.01856 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | 2459279.55337 | -0.01811 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | 2460007.14056 | -0.01670 | 27 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 2459305.77597 | -0.01459 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 2459305.66833 | -0.01310 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021065132309-s0036-0000000341420329-0207-s_lc.fits` | 2459295.25530 | -0.01237 | 79 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459253.43944 | -0.01191 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | 2459279.61865 | -0.00633 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000341420329-0254-s_lc.fits` | 2459996.56209 | -0.00632 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460038.56379 | -0.00736 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460033.82916 | -0.00664 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460033.74582 | -0.00634 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460040.59777 | -0.00627 | 3 | SAP | 1, 2, 3 | no |
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459253.44985 | -0.00612 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | 2459266.47701 | -0.00607 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000341420329-0205-s_lc.fits` | 2459266.38395 | -0.00577 | 2 | SAP | 3 | no |
| `tess2021014023720-s0034-0000000341420329-0204-s_lc.fits` | 2459234.59127 | -0.00550 | 3 | PDCSAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000341420329-0255-s_lc.fits` | 2460031.32086 | -0.00543 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459237.68090 | 17955 | 18282 | 5.2008 | 0 / 5 |  |
| 2459242.91501 | 17050 | 18282 | 10.4349 | 0 / 10 |  |
| 2459248.14980 | 19050 | 18282 | 15.6697 | 0 / 15 |  |
| 2459253.35819 | 17802 | 18282 | 20.8781 | 0 / 20 |  |
| 2459253.40471 | 17788 | 18282 | 20.9246 | 0 / 20 |  |
| 2459253.41860 | 17688 | 18282 | 20.9385 | 0 / 20 |  |
| 2459253.42902 | 15690 | 18282 | 20.9489 | 0 / 20 |  |
| 2459253.43944 | 9307 | 18282 | 20.9593 | 0 / 20 |  |
| 2459258.61795 | 18165 | 18282 | 26.1378 | 0 / 26 |  |
| 2459263.85131 | 18426 | 18282 | 31.3712 | 0 / 31 |  |
| 2459274.32284 | 18414 | 18282 | 41.8427 | 0 / 41 |  |
| 2459279.55337 | 16567 | 18282 | 47.0733 | 0 / 47 |  |
| 2459284.79015 | 17636 | 18282 | 52.3100 | 0 / 52 |  |
| 2459290.02274 | 18029 | 18282 | 57.5426 | 0 / 57 |  |
| 2459300.49065 | 18545 | 18282 | 68.0105 | 0 / 68 |  |
| 2459305.66833 | 13411 | 18282 | 73.1882 | 0 / 73 |  |
| 2459305.71347 | 18105 | 18282 | 73.2334 | 0 / 73 |  |
| 2459305.75652 | 18043 | 18282 | 73.2764 | 4 / 73 | 73.2764, 36.6382, 10.4681, 5.234 |
| 2459305.77597 | 14971 | 18282 | 73.2959 | 0 / 73 |  |
| 2459965.22149 | 18516 | 18282 | 732.7414 | 16 / 732 | 732.741, 366.371, 244.247, 183.185, 146.548, 122.124, 104.677, 91.5927, 81.4157, 73.2741, 52.3387, 36.6371, 26.1693, 20.9355, 10.4677, 5.2339 |
| 2459970.45422 | 17997 | 18282 | 737.9741 | 12 / 737 | 737.974, 368.987, 245.991, 184.494, 147.595, 122.996, 105.425, 92.2468, 81.9971, 73.7974, 15.7016, 5.2339 |
| 2459980.92380 | 18179 | 18282 | 748.4437 | 14 / 748 | 748.444, 374.222, 249.481, 187.111, 149.689, 124.741, 106.921, 93.5555, 83.1604, 74.8444, 68.0403, 62.3703, 57.5726, 5.2339 |
| 2459986.15857 | 18337 | 18282 | 753.6785 | 18 / 753 | 753.678, 376.839, 251.226, 188.42, 150.736, 125.613, 107.668, 94.2098, 83.7421, 75.3678, 62.8065, 47.1049, 41.871, 31.4033, 20.9355, 15.7016, 10.4678, 5.2339 |
| 2459991.39263 | 18228 | 18282 | 758.9125 | 12 / 758 | 758.913, 379.456, 252.971, 189.728, 151.782, 126.485, 108.416, 94.8641, 84.3236, 75.8913, 26.1694, 5.2339 |
| 2459996.62807 | 18958 | 18282 | 764.1480 | 13 / 764 | 764.148, 382.074, 254.716, 191.037, 152.83, 127.358, 109.164, 95.5185, 84.9053, 76.4148, 47.7592, 10.4678, 5.2339 |
| 2460007.07320 | 17123 | 18282 | 774.5931 | 14 / 774 | 774.593, 387.296, 258.198, 193.648, 154.919, 129.099, 110.656, 96.8241, 86.0659, 77.4593, 48.4121, 20.9349, 10.4675, 5.2337 |
| 2460007.14056 | 15658 | 18282 | 774.6604 | 14 / 774 | 774.66, 387.33, 258.22, 193.665, 154.932, 129.11, 110.666, 96.8326, 86.0734, 77.466, 48.4163, 20.9368, 10.4684, 5.2342 |
| 2460012.32941 | 19049 | 18282 | 779.8493 | 13 / 779 | 779.849, 389.925, 259.95, 194.962, 155.97, 129.975, 111.407, 97.4812, 86.6499, 77.9849, 48.7406, 37.1357, 5.2339 |
| 2460017.56201 | 18276 | 18282 | 785.0819 | 17 / 785 | 785.082, 392.541, 261.694, 196.27, 157.016, 130.847, 112.155, 98.1352, 87.2313, 78.5082, 60.3909, 52.3388, 31.4033, 26.1694, 15.7016, 10.4678, 5.2339 |
| 2460022.79251 | 18866 | 18282 | 790.3124 | 12 / 790 | 790.312, 395.156, 263.438, 197.578, 158.062, 131.719, 112.902, 98.789, 87.8125, 79.0312, 60.7933, 5.2339 |
| 2460028.02924 | 18090 | 18282 | 795.5491 | 14 / 795 | 795.549, 397.775, 265.183, 198.887, 159.11, 132.591, 113.65, 99.4436, 88.3943, 79.5549, 41.871, 20.9355, 10.4678, 5.2339 |
| 2460033.26528 | 18117 | 18282 | 800.7852 | 13 / 800 | 800.785, 400.393, 266.928, 200.196, 160.157, 133.464, 114.398, 100.098, 88.9761, 80.0785, 47.105, 15.7017, 5.2339 |
| 2460038.49643 | 18904 | 18282 | 806.0163 | 16 / 806 | 806.016, 403.008, 268.672, 201.504, 161.203, 134.336, 115.145, 100.752, 89.5574, 80.6016, 73.2742, 62.0013, 57.5726, 36.6371, 10.4677, 5.2339 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1019.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:03:27Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:03:29Z: TOI-1019.01 (TIC 341420329, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:03:30Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:03:30Z: CD-54  2025 (*); TOI-1019.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459232.4469: recovered, depth 18282 ± 162 ppm (catalogue 20797 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3.5, 3.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 20%, 10%, 0%, 10%, 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 33 repeat-candidate event(s); first at BJD 2459237.6809, ΔT = 5.201 d, 0 of 5 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1019.01: Gaia DR3 5296160254722839296 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-1019.01: Teff 6823 K, R* 1.61 ± 0.13, M* 1.45 ± 0.15, ρ* 0.35 ± 0.09 ρ☉ (dwarf sequence, M_G 2.93, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1019.01: 23 Gaia neighbour(s) within 52.5", contamination 6.87%; depth 18282 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 5296160186003369088, 42.6", ΔG 4.07); a centroid test is needed |
| Pointing and quality census per event | failed | 36 persistent event(s), 12 clean; BJD 2459242.9150 suspect: MOM_CENTR1 z=+8.2, MOM_CENTR2 z=-13.4, POS_CORR1 z=+10.3, POS_CORR2 z=-13.5, SAP_BKG z=+13.0; BJD 2459248.1498 caution: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2459253.3582 caution: manual exclude (within ±0.25 d); BJD 2459253.4047 suspect: manual exclude (in event), SAP_BKG z=-5.2 |
| Moving objects at screen-event epochs | inconclusive | 36 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 4 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1019.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1019.01: CD-54  2025 otype * (star_or_other) at 0.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1019-01.yaml
python -m cygnus.multi report campaigns/toi-1019-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits** (one and two periods after the reference; predicted-transit offsets +0.02 h at sigma 0.00 h). No new signal.

Source: `campaigns/toi-1019-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
