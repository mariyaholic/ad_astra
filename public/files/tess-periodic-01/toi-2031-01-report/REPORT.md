<!-- [private Drive store] -->
# Known-object test, TOI-2031.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2031-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1062, calibrate_screen #1045, event_census #1049, fetch_products #1044, known_signal_recovery #1046, moving_objects #1051, period_aliases #1050, prior_art #1064, residual_screen #1048, stellar_context #1047, variability_guard #1063
- Runner finished (UTC): 2026-09-26T10:32:30Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2031.01 (BJD 2459886.0463: recovered, depth 11177 ± 139 ppm (catalogue 12241 ppm)).
Outside the catalogued epoch the screen left 205 threshold entries forming **43 distinct event(s)**, **29 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459891.7642 matches the catalogued transit's depth (11275 vs 11177 ppm), 5.754 d later; 0 of 5 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2031.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 470127886 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 331.117808 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 81.565951 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459886.04634 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 12240.9298817 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.0584797 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.7609 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-02-21 16:02:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | lightcurve | 58 | True | `8de5f4d40ae0a419` | True |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | lightcurve | 52 | False | `b15caef6bbbd8b92` | True |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | lightcurve | 53 | False | `3014dbd3488d1484` | True |
| `tess2022330142927-s0059-0000000470127886-0248-s_lc.fits` | lightcurve | 59 | False | `44983e8f042875b6` | True |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | lightcurve | 60 | False | `55a55a1189510e89` | True |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | lightcurve | 73 | False | `780f6f5efbae002d` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | 2459886.04634 | recovered | 122 | 11177 ± 139 | 12241 | -0.86 |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | — | epoch not in this light curve | — | — | 12241 | — |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | — | epoch not in this light curve | — | — | 12241 | — |
| `tess2022330142927-s0059-0000000470127886-0248-s_lc.fits` | — | epoch not in this light curve | — | — | 12241 | — |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | — | epoch not in this light curve | — | — | 12241 | — |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | — | epoch not in this light curve | — | — | 12241 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022330142927-s0059-0000000470127886-0248-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | 2459897.47612 | -0.01226 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 2459943.16759 | -0.01221 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 2459943.24190 | -0.01204 | 46 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | 2460291.84611 | -0.01188 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 2459960.34777 | -0.01173 | 103 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459726.01389 | -0.01164 | 105 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | 2459760.30786 | -0.01164 | 102 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | 2459754.59181 | -0.01160 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | 2459891.76425 | -0.01155 | 108 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | 2460308.99172 | -0.01150 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459731.72916 | -0.01146 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | 2459903.19213 | -0.01144 | 110 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | 2460297.55995 | -0.01138 | 106 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | 2459908.90814 | -0.01133 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | 2459748.87369 | -0.01132 | 109 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000470127886-0248-s_lc.fits` | 2459914.62272 | -0.01129 | 104 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000470127886-0248-s_lc.fits` | 2459926.05600 | -0.01129 | 104 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | 2459766.02116 | -0.01127 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000470127886-0248-s_lc.fits` | 2459920.33799 | -0.01123 | 108 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 2459948.92096 | -0.01121 | 98 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459737.44514 | -0.01118 | 108 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000470127886-0248-s_lc.fits` | 2459931.77262 | -0.01105 | 104 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459720.29655 | -0.01085 | 108 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 2459948.84804 | -0.00630 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | 2459760.23356 | -0.00615 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000470127886-0248-s_lc.fits` | 2459914.54911 | -0.00561 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 2459960.42208 | -0.00527 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459725.93820 | -0.00474 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459726.08958 | -0.00474 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | 2459760.38426 | -0.00586 | 2 | SAP | 2, 3 | no |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | 2460286.07740 | -0.00570 | 3 | PDCSAP | 3 | no |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | 2460286.08920 | -0.00561 | 6 | PDCSAP | 3 | no |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 2459943.27662 | -0.00559 | 2 | SAP | 3 | no |
| `tess2023341045131-s0073-0000000470127886-0268-s_lc.fits` | 2460286.06629 | -0.00528 | 3 | PDCSAP | 3 | no |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459731.65208 | -0.00513 | 2 | SAP | 1, 2, 3 | no |
| `tess2022164095748-s0053-0000000470127886-0226-s_lc.fits` | 2459749.81884 | -0.00509 | 2 | SAP | 3 | no |
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | 2459895.97124 | -0.00487 | 2 | SAP | 2 | no |
| `tess2022357055054-s0060-0000000470127886-0249-s_lc.fits` | 2459939.70029 | -0.00479 | 2 | PDCSAP | 2, 3 | no |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459722.85626 | -0.00471 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459720.37433 | -0.00468 | 2 | SAP | 2, 3 | no |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459718.93129 | -0.00459 | 2 | PDCSAP | 2, 3 | no |
| `tess2022138205153-s0052-0000000470127886-0224-s_lc.fits` | 2459719.02851 | -0.00456 | 2 | PDCSAP | 3 | no |
| `tess2022302161335-s0058-0000000470127886-0247-s_lc.fits` | 2459895.85041 | -0.00415 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459891.76425 | 11275 | 11177 | 5.7539 | 0 / 5 |  |
| 2459897.47612 | 12012 | 11177 | 11.4658 | 0 / 11 |  |
| 2459903.19213 | 11178 | 11177 | 17.1818 | 0 / 17 |  |
| 2459908.90814 | 10793 | 11177 | 22.8978 | 0 / 22 |  |
| 2459720.29655 | 10177 | 11177 | 165.7138 | 2 / 165 | 165.714, 82.8569 |
| 2459726.01389 | 11285 | 11177 | 159.9965 | 2 / 159 | 159.996, 53.3322 |
| 2459731.72916 | 9607 | 11177 | 154.2812 | 2 / 154 | 154.281, 77.1406 |
| 2459737.44514 | 10756 | 11177 | 148.5652 | 2 / 148 | 148.565, 74.2826 |
| 2459748.87369 | 10975 | 11177 | 137.1367 | 0 / 137 |  |
| 2459754.59181 | 11168 | 11177 | 131.4185 | 2 / 131 | 131.418, 65.7093 |
| 2459760.30786 | 10781 | 11177 | 125.7025 | 2 / 125 | 125.703, 62.8512 |
| 2459766.02116 | 10930 | 11177 | 119.9892 | 1 / 119 | 119.989 |
| 2459914.62272 | 10905 | 11177 | 28.6124 | 0 / 28 |  |
| 2459920.33799 | 10720 | 11177 | 34.3276 | 0 / 34 |  |
| 2459926.05600 | 10225 | 11177 | 40.0457 | 0 / 40 |  |
| 2459931.77262 | 10738 | 11177 | 45.7623 | 0 / 45 |  |
| 2459943.16759 | 10258 | 11177 | 57.1573 | 0 / 57 |  |
| 2459943.24190 | 10119 | 11177 | 57.2316 | 1 / 57 | 57.2316 |
| 2459948.84804 | 5871 | 11177 | 62.8377 | 1 / 62 | 62.8377 |
| 2459948.92096 | 10635 | 11177 | 62.9106 | 0 / 62 |  |
| 2459960.34777 | 11219 | 11177 | 74.3374 | 0 / 74 |  |
| 2460291.84611 | 10677 | 11177 | 405.8358 | 4 / 405 | 405.836, 202.918, 101.459, 5.716 |
| 2460297.55995 | 11067 | 11177 | 411.5496 | 10 / 411 | 411.55, 205.775, 137.183, 102.887, 68.5916, 51.4437, 45.7277, 34.2958, 22.8639, 17.1479 |
| 2460308.99172 | 11240 | 11177 | 422.9814 | 4 / 422 | 422.981, 211.491, 105.745, 84.5963 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2031.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): 1 match(es) in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:32:26Z: TOI-2031 A b (host TOI-2031 A)
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:32:28Z: TOI-2031.01 (TIC 470127886, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:32:29Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:32:29Z: TOI-2031b (Pl); TOI-2031 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459886.0463: recovered, depth 11177 ± 139 ppm (catalogue 12241 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, 3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 40%, 20%, 10%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 24 repeat-candidate event(s); first at BJD 2459891.7642, ΔT = 5.754 d, 0 of 5 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2031.01: Gaia DR3 2299101254886404608 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2031.01: Teff 6286 K, R* 1.23 ± 0.10, M* 1.18 ± 0.12, ρ* 0.64 ± 0.17 ρ☉ (dwarf sequence, M_G 3.88, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-2031.01: 11 Gaia neighbour(s) within 52.5", contamination 1.89%; depth 11177 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 29 persistent event(s), 15 clean; BJD 2459897.4761 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR2 z=+8.1, POS_CORR2 z=+10.0, SAP_BKG z=+59.6; BJD 2459903.1921 suspect: POS_CORR1 z=-6.5, SAP_BKG z=+6.1; BJD 2459720.2966 suspect: manual exclude (within ±0.25 d), SAP_BKG z=-15.6; BJD 2459726.0139 suspect: SAP_BKG z=+6.0 |
| Moving objects at screen-event epochs | inconclusive | 29 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 4 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-2031.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2031.01: TOI-2031 otype * (star_or_other) at 0.4" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2031-01.yaml
python -m cygnus.multi report campaigns/toi-2031-01.yaml
```
