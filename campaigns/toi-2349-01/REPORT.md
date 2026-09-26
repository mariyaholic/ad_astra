<!-- cygnus:generated-draft -->
# Known-object test, TOI-2349.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2349-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #824, calibrate_screen #769, event_census #773, fetch_products #767, known_signal_recovery #770, moving_objects #812, period_aliases #774, prior_art #826, residual_screen #772, stellar_context #771, variability_guard #825
- Runner finished (UTC): 2026-09-26T10:20:48Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2349.01 (BJD 2459997.9134: recovered, depth 15222 ± 206 ppm (catalogue 18730 ppm)).
Outside the catalogued epoch the screen left 153 threshold entries forming **20 distinct event(s)**, **19 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460009.3791 matches the catalogued transit's depth (10924 vs 15222 ppm), 11.465 d later; 0 of 11 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2349.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 405452527 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 143.259339 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -13.830634 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459997.913355 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 18730.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 6.656 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.8929 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-10-17 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | lightcurve | 62 | True | `f000fc1274eaab79` | True |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | lightcurve | 89 | False | `c9de97530e9925f3` | True |
| `tess2026005125623-s0099-0000000405452527-0300-s_lc.fits` | lightcurve | 99 | False | `4a378a73fc62adfa` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | 2459997.91335 | recovered | 200 | 15222 ± 206 | 18730 | 0.02 |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | — | epoch not in this light curve | — | — | 18730 | — |
| `tess2026005125623-s0099-0000000405452527-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 18730 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2026005125623-s0099-0000000405452527-0300-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000405452527-0300-s_lc.fits` | 2461051.22775 | -0.01885 | 149 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000405452527-0300-s_lc.fits` | 2461051.23608 | -0.01805 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460738.62904 | -0.01748 | 136 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460727.05693 | -0.01718 | 136 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | 2460009.55206 | -0.01689 | 76 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | 2460009.44512 | -0.01681 | 76 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460738.73737 | -0.01674 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460727.16040 | -0.01565 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460738.75403 | -0.01523 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460726.95693 | -0.01495 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460727.17568 | -0.01443 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460727.18610 | -0.01401 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460738.52904 | -0.01381 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | 2460009.37915 | -0.01318 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000405452527-0300-s_lc.fits` | 2461051.24372 | -0.01256 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000405452527-0300-s_lc.fits` | 2461051.01940 | -0.01227 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000405452527-0286-s_lc.fits` | 2460726.94999 | -0.01132 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | 2460009.35901 | -0.00911 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | 2460009.60762 | -0.00828 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023043185947-s0062-0000000405452527-0254-s_lc.fits` | 2460007.30071 | -0.00830 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460009.37915 | 10924 | 15222 | 11.4651 | 0 / 11 |  |
| 2460009.44512 | 15253 | 15222 | 11.5311 | 0 / 11 |  |
| 2460009.55206 | 14591 | 15222 | 11.6380 | 0 / 11 |  |
| 2460726.94999 | 10112 | 15222 | 729.0360 | 22 / 729 | 729.036, 364.518, 243.012, 182.259, 145.807, 121.506, 104.148, 91.1295, 72.9036, 66.276, 60.753, 52.074, 45.5647, 34.716, 33.138, 31.6972, 30.3765, 29.1614, 23.5173, 22.092 |
| 2460726.95693 | 11438 | 15222 | 729.0429 | 22 / 729 | 729.043, 364.522, 243.014, 182.261, 145.809, 121.507, 104.149, 91.1304, 72.9043, 66.2766, 60.7536, 52.0745, 45.5652, 34.7163, 33.1383, 31.6975, 30.3768, 29.1617, 23.5175, 22.0922 |
| 2460727.05693 | 15736 | 15222 | 729.1429 | 28 / 729 | 729.143, 364.572, 243.048, 182.286, 145.829, 121.524, 104.163, 91.1429, 81.0159, 72.9143, 66.2857, 60.7619, 52.0816, 48.6095, 45.5714, 40.5079, 34.7211, 33.1429, 31.7019, 30.381 |
| 2460727.16040 | 13964 | 15222 | 729.2464 | 22 / 729 | 729.246, 364.623, 243.082, 182.312, 145.849, 121.541, 104.178, 91.1558, 72.9246, 66.2951, 60.7705, 52.089, 45.5779, 34.726, 33.1476, 31.7064, 30.3853, 29.1699, 23.5241, 22.0984 |
| 2460727.17568 | 10747 | 15222 | 729.2617 | 22 / 729 | 729.262, 364.631, 243.087, 182.315, 145.852, 121.544, 104.18, 91.1577, 72.9262, 66.2965, 60.7718, 52.0901, 45.5789, 34.7267, 33.1483, 31.707, 30.3859, 29.1705, 23.5246, 22.0988 |
| 2460727.18610 | 8048 | 15222 | 729.2721 | 22 / 729 | 729.272, 364.636, 243.091, 182.318, 145.854, 121.545, 104.182, 91.159, 72.9272, 66.2975, 60.7727, 52.0909, 45.5795, 34.7272, 33.1487, 31.7075, 30.3863, 29.1709, 23.5249, 22.0992 |
| 2460738.52904 | 8973 | 15222 | 740.6150 | 25 / 740 | 740.615, 370.308, 246.872, 185.154, 148.123, 123.436, 105.802, 92.5769, 74.0615, 67.3286, 61.7179, 56.9704, 52.9011, 49.3743, 46.2884, 43.5656, 35.2674, 33.6643, 32.2007, 30.859 |
| 2460738.62904 | 14751 | 15222 | 740.7150 | 25 / 740 | 740.715, 370.358, 246.905, 185.179, 148.143, 123.453, 105.816, 92.5894, 74.0715, 67.3377, 61.7263, 56.9781, 52.9082, 49.381, 46.2947, 43.5715, 35.2721, 33.6689, 32.205, 30.8631 |
| 2460738.73737 | 11949 | 15222 | 740.8234 | 24 / 740 | 740.823, 370.412, 246.941, 185.206, 148.165, 123.471, 105.832, 92.6029, 74.0823, 67.3476, 61.7353, 56.9864, 52.916, 49.3882, 46.3015, 43.5778, 35.2773, 33.6738, 32.2097, 30.8676 |
| 2460738.75403 | 9545 | 15222 | 740.8400 | 24 / 740 | 740.84, 370.42, 246.947, 185.21, 148.168, 123.473, 105.834, 92.605, 74.084, 67.3491, 61.7367, 56.9877, 52.9171, 49.3893, 46.3025, 43.5788, 35.2781, 33.6745, 32.2104, 30.8683 |
| 2461051.01940 | 11092 | 15222 | 1053.1054 | 23 / 1053 | 1053.11, 526.553, 351.035, 263.276, 210.621, 175.518, 150.444, 131.638, 117.012, 95.7369, 87.7588, 81.0081, 75.2218, 70.207, 58.5059, 50.1479, 47.8684, 42.1242, 40.5041, 37.6109 |
| 2461051.22775 | 12837 | 15222 | 1053.3137 | 22 / 1053 | 1053.31, 526.657, 351.105, 263.328, 210.663, 175.552, 150.473, 131.664, 117.035, 95.7558, 87.7761, 81.0241, 75.2367, 70.2209, 58.5174, 50.1578, 47.8779, 42.1325, 40.5121, 37.6183 |
| 2461051.23608 | 12274 | 15222 | 1053.3221 | 22 / 1053 | 1053.32, 526.661, 351.107, 263.33, 210.664, 175.554, 150.475, 131.665, 117.036, 95.7566, 87.7768, 81.0248, 75.2373, 70.2215, 58.5179, 50.1582, 47.8783, 42.1329, 40.5124, 37.6186 |
| 2461051.24372 | 10277 | 15222 | 1053.3297 | 22 / 1053 | 1053.33, 526.665, 351.11, 263.332, 210.666, 175.555, 150.476, 131.666, 117.037, 95.7572, 87.7775, 81.0254, 75.2378, 70.222, 58.5183, 50.1586, 47.8786, 42.1332, 40.5127, 37.6189 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2349.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:20:45Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:20:46Z: TOI-2349.01 (TIC 405452527, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:20:47Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:20:47Z: UCAC4 381-056230 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459997.9134: recovered, depth 15222 ± 206 ppm (catalogue 18730 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 17 repeat-candidate event(s); first at BJD 2460009.3791, ΔT = 11.465 d, 0 of 11 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2349.01: Gaia DR3 5689821044216119296 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-2349.01: dwarf priors not applied — 1.04 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2349.01: 4 Gaia neighbour(s) within 52.5", contamination 4.44%; depth 15222 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 5689821048511400832, 29.5", ΔG 4.10); a centroid test is needed |
| Pointing and quality census per event | failed | 19 persistent event(s), 14 clean; BJD 2460009.3590 caution: argabrightening (within ±0.25 d); BJD 2460009.3791 suspect: argabrightening (in event); BJD 2460009.4451 caution: argabrightening (within ±0.25 d); BJD 2460009.5521 caution: argabrightening (within ±0.25 d), manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 19 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-2349.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-2349.01: UCAC4 381-056230 otype SB* (multiple) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2349-01.yaml
python -m cygnus.multi report campaigns/toi-2349-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead event is the target's own catalogued ephemeris transit** (one period after the reference). No new signal.

Source: `campaigns/toi-2349-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
