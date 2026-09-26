<!-- cygnus:generated-draft -->
# Known-object test, TOI-5394.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5394-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #642, calibrate_screen #595, event_census #600, fetch_products #594, known_signal_recovery #596, moving_objects #619, period_aliases #601, prior_art #646, residual_screen #598, stellar_context #597, variability_guard #643
- Runner finished (UTC): 2026-09-26T10:12:24Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5394.01 (BJD 2459561.6278: recovered, depth 2502 ± 81 ppm (catalogue 5720 ppm)).
Outside the catalogued epoch the screen left 96 threshold entries forming **35 distinct event(s)**, **8 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459576.8229 matches the catalogued transit's depth (3430 vs 2502 ppm), 15.195 d later; 0 of 15 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5394.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 61109252 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 154.574508 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 17.396435 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459561.627836 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5720.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.582 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.0152 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-02-15 12:03:00 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021336043614-s0046-0000000061109252-0217-s_lc.fits` | lightcurve | 46 | True | `fef09f461e798bcc` | True |
| `tess2021310001228-s0045-0000000061109252-0216-s_lc.fits` | lightcurve | 45 | False | `f08aeb73804a9c3e` | True |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | lightcurve | 48 | False | `e2de4cea81efa113` | True |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | lightcurve | 72 | False | `b9cdfde77f3e7ecd` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021336043614-s0046-0000000061109252-0217-s_lc.fits` | 2459561.62784 | recovered | 77 | 2502 ± 81 | 5720 | -0.01 |
| `tess2021310001228-s0045-0000000061109252-0216-s_lc.fits` | — | epoch not in this light curve | — | — | 5720 | — |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | — | epoch not in this light curve | — | — | 5720 | — |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | — | epoch not in this light curve | — | — | 5720 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021336043614-s0046-0000000061109252-0217-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021310001228-s0045-0000000061109252-0216-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021336043614-s0046-0000000061109252-0217-s_lc.fits` | 2459576.82290 | -0.00470 | 57 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460275.71891 | -0.00459 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021310001228-s0045-0000000061109252-0216-s_lc.fits` | 2459531.24151 | -0.00391 | 49 | PDCSAP+SAP | 1, 2 | yes |
| `tess2021310001228-s0045-0000000061109252-0216-s_lc.fits` | 2459546.43468 | -0.00390 | 57 | PDCSAP+SAP | 1, 2 | yes |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.57297 | -0.00370 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.48963 | -0.00345 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.70007 | -0.00335 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.55978 | -0.00332 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459609.82621 | -0.00408 | 67 | PDCSAP | 1, 2, 3 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459621.15151 | -0.00374 | 2 | SAP | 1, 2, 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.62437 | -0.00345 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.59936 | -0.00335 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.51186 | -0.00331 | 2 | SAP | 2, 3 | no |
| `tess2021310001228-s0045-0000000061109252-0216-s_lc.fits` | 2459539.76526 | -0.00330 | 5 | SAP | 1, 2 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.54867 | -0.00324 | 5 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.64104 | -0.00323 | 2 | SAP | 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.62020 | -0.00323 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.51811 | -0.00322 | 3 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.42574 | -0.00322 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.48546 | -0.00321 | 2 | SAP | 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.73549 | -0.00321 | 2 | SAP | 2, 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.59242 | -0.00320 | 2 | SAP | 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.53547 | -0.00318 | 2 | SAP | 3 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460267.47713 | -0.00315 | 2 | SAP | 2, 3 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459609.92413 | -0.00276 | 3 | PDCSAP | 1, 2 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459609.90955 | -0.00273 | 16 | PDCSAP | 1, 2 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459609.79635 | -0.00265 | 5 | PDCSAP | 1, 2 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459609.94497 | -0.00264 | 3 | PDCSAP | 1, 2 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459609.93038 | -0.00262 | 5 | PDCSAP | 1, 2 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459614.61248 | -0.00259 | 2 | SAP | 1 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459620.71400 | -0.00240 | 2 | SAP | 1, 2 | no |
| `tess2021310001228-s0045-0000000061109252-0216-s_lc.fits` | 2459531.20470 | -0.00226 | 2 | PDCSAP+SAP | 1 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459614.10830 | -0.00209 | 2 | SAP | 1, 2 | no |
| `tess2022027120115-s0048-0000000061109252-0219-s_lc.fits` | 2459614.36386 | -0.00195 | 2 | SAP | 1 | no |
| `tess2023315124025-s0072-0000000061109252-0267-s_lc.fits` | 2460266.56454 | -0.00183 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459576.82290 | 3430 | 2502 | 15.1954 | 0 / 15 |  |
| 2459531.24151 | 1788 | 2502 | 30.3860 | 2 / 30 | 30.386, 15.193 |
| 2459546.43468 | 2482 | 2502 | 15.1928 | 1 / 15 | 15.1928 |
| 2460267.48963 | 1899 | 2502 | 705.8621 | 16 / 705 | 705.862, 352.931, 235.287, 176.465, 141.172, 117.644, 100.837, 88.2328, 78.4291, 64.1693, 47.0575, 44.1164, 41.5213, 39.2146, 32.0846, 21.3898 |
| 2460267.55978 | 2064 | 2502 | 705.9323 | 16 / 705 | 705.932, 352.966, 235.311, 176.483, 141.186, 117.655, 100.847, 88.2415, 78.4369, 64.1757, 47.0622, 44.1208, 41.5254, 39.2185, 32.0878, 21.3919 |
| 2460267.57297 | 2046 | 2502 | 705.9455 | 16 / 705 | 705.946, 352.973, 235.315, 176.486, 141.189, 117.658, 100.849, 88.2432, 78.4384, 64.1769, 47.063, 44.1216, 41.5262, 39.2192, 32.0884, 21.3923 |
| 2460267.70007 | 1630 | 2502 | 706.0726 | 16 / 706 | 706.073, 353.036, 235.357, 176.518, 141.214, 117.679, 100.868, 88.2591, 78.4525, 64.1884, 47.0715, 44.1295, 41.5337, 39.2263, 32.0942, 21.3961 |
| 2460275.71891 | 3431 | 2502 | 714.0914 | 15 / 714 | 714.091, 357.046, 238.03, 178.523, 142.818, 119.015, 102.013, 89.2614, 79.3435, 47.6061, 44.6307, 42.0054, 39.6717, 37.5838, 15.1934 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-5394.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:12:21Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:12:22Z: TOI-5394.01 (TIC 61109252, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:12:24Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:12:24Z: HD  89277 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459561.6278: recovered, depth 2502 ± 81 ppm (catalogue 5720 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3.5, 3.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 50%, 40%, 40%, 40% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 8 repeat-candidate event(s); first at BJD 2459576.8229, ΔT = 15.195 d, 0 of 15 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5394.01: Gaia DR3 623779716969345920 at 0.00" (propagated 2016.0 → J2015.5; 0.06" unpropagated, proper-motion shift 0.06") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-5394.01: dwarf priors not applied — RUWE 1.8549249 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5394.01: 3 Gaia neighbour(s) within 52.5", contamination 1.10%; depth 2502 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 623779682609608320, 30.3", ΔG 4.94); a centroid test is needed |
| Pointing and quality census per event | failed | 8 persistent event(s), 7 clean; BJD 2460275.7189 suspect: POS_CORR1 z=+5.8, SAP_BKG z=+18.6 |
| Moving objects at screen-event epochs | inconclusive | 8 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 4 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-5394.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-5394.01: HD  89277 otype SB* (multiple) at 1.8" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5394-01.yaml
python -m cygnus.multi report campaigns/toi-5394-01.yaml
```
