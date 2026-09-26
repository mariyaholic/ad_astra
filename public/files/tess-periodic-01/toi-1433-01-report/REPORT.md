<!-- [private Drive store] -->
# Known-object test, TOI-1433.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1433-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #212, calibrate_screen #101, event_census #112, fetch_products #94, known_signal_recovery #104, moving_objects #195, period_aliases #114, prior_art #214, residual_screen #109, stellar_context #105, variability_guard #213
- Runner finished (UTC): 2026-09-26T09:57:03Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1433.01 (BJD 2458695.0109: recovered, depth 57850 ± 1349 ppm (catalogue 107230 ppm)).
Outside the catalogued epoch the screen left 71 threshold entries forming **11 distinct event(s)**, **11 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2458719.8830 matches the catalogued transit's depth (64284 vs 57850 ppm), 24.871 d later; 0 of 24 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1433.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 13684720 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 305.538257 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 36.064784 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458695.010937 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 107230.4220068 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.710953 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.4647 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-09-18 16:00:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019198215352-s0014-0000000013684720-0150-s_lc.fits` | lightcurve | 14 | True | `02c6c36ad641591e` | True |
| `tess2019226182529-s0015-0000000013684720-0151-s_lc.fits` | lightcurve | 15 | False | `5876c453b890fb54` | True |
| `tess2021204101404-s0041-0000000013684720-0212-s_lc.fits` | lightcurve | 41 | False | `e1d0cac5580bb427` | True |
| `tess2022217014003-s0055-0000000013684720-0242-s_lc.fits` | lightcurve | 55 | False | `94cfe22a4c69a92a` | True |
| `tess2024030031500-s0075-0000000013684720-0270-s_lc.fits` | lightcurve | 75 | False | `366834220f8ffe8f` | True |
| `tess2024196212429-s0081-0000000013684720-0276-s_lc.fits` | lightcurve | 81 | False | `4ac175b9569bcd9b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019198215352-s0014-0000000013684720-0150-s_lc.fits` | 2458695.01094 | recovered | 52 | 57850 ± 1349 | 107230 | 0.04 |
| `tess2019226182529-s0015-0000000013684720-0151-s_lc.fits` | — | epoch not in this light curve | — | — | 107230 | — |
| `tess2021204101404-s0041-0000000013684720-0212-s_lc.fits` | — | epoch not in this light curve | — | — | 107230 | — |
| `tess2022217014003-s0055-0000000013684720-0242-s_lc.fits` | — | epoch not in this light curve | — | — | 107230 | — |
| `tess2024030031500-s0075-0000000013684720-0270-s_lc.fits` | — | epoch not in this light curve | — | — | 107230 | — |
| `tess2024196212429-s0081-0000000013684720-0276-s_lc.fits` | — | epoch not in this light curve | — | — | 107230 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019198215352-s0014-0000000013684720-0150-s_lc.fits` | — | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2019226182529-s0015-0000000013684720-0151-s_lc.fits` | 6 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2021204101404-s0041-0000000013684720-0212-s_lc.fits` | — | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2022217014003-s0055-0000000013684720-0242-s_lc.fits` | 6 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024030031500-s0075-0000000013684720-0270-s_lc.fits` | 8 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2024196212429-s0081-0000000013684720-0276-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000013684720-0276-s_lc.fits` | 2460523.39146 | -0.09939 | 30 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000013684720-0270-s_lc.fits` | 2460361.69978 | -0.09662 | 19 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021204101404-s0041-0000000013684720-0212-s_lc.fits` | 2459441.28758 | -0.09637 | 31 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019226182529-s0015-0000000013684720-0151-s_lc.fits` | 2458719.88299 | -0.09573 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000013684720-0270-s_lc.fits` | 2460349.26225 | -0.09432 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021204101404-s0041-0000000013684720-0212-s_lc.fits` | 2459428.85210 | -0.09204 | 32 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024196212429-s0081-0000000013684720-0276-s_lc.fits` | 2460510.95512 | -0.09139 | 28 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019226182529-s0015-0000000013684720-0151-s_lc.fits` | 2458732.32515 | -0.09019 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000013684720-0242-s_lc.fits` | 2459801.98952 | -0.08842 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000013684720-0242-s_lc.fits` | 2459814.42976 | -0.08034 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000013684720-0242-s_lc.fits` | 2459802.00896 | -0.06826 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2458719.88299 | 64284 | 57850 | 24.8705 | 0 / 24 |  |
| 2458732.32515 | 65153 | 57850 | 37.3127 | 0 / 37 |  |
| 2459428.85210 | 72325 | 57850 | 733.8396 | 7 / 733 | 733.84, 244.613, 146.768, 104.834, 81.5377, 29.3536, 12.438 |
| 2459441.28758 | 64422 | 57850 | 746.2751 | 13 / 746 | 746.275, 373.138, 248.758, 186.569, 149.255, 124.379, 93.2844, 74.6275, 62.1896, 49.7517, 37.3138, 24.8758, 12.4379 |
| 2459801.98952 | 57072 | 57850 | 1106.9771 | 23 / 1106 | 1106.98, 553.489, 368.992, 276.744, 221.395, 184.496, 158.14, 138.372, 122.998, 110.698, 100.634, 92.2481, 85.1521, 73.7985, 69.1861, 65.1163, 61.4987, 58.262, 52.7132, 50.3171 |
| 2459802.00896 | 55702 | 57850 | 1106.9965 | 23 / 1106 | 1107, 553.498, 368.999, 276.749, 221.399, 184.499, 158.142, 138.375, 123, 110.7, 100.636, 92.2497, 85.1536, 73.7998, 69.1873, 65.1174, 61.4998, 58.263, 52.7141, 50.318 |
| 2459814.42976 | 52202 | 57850 | 1119.4173 | 19 / 1119 | 1119.42, 559.709, 373.139, 279.854, 223.883, 186.57, 159.917, 124.38, 111.942, 93.2848, 86.109, 79.9584, 74.6278, 65.8481, 62.1899, 39.9792, 37.3139, 24.8759, 12.438 |
| 2460349.26225 | 62046 | 57850 | 1654.2498 | 19 / 1654 | 1654.25, 827.125, 413.562, 330.85, 236.321, 206.781, 165.425, 150.386, 127.25, 118.161, 103.391, 97.3088, 87.0658, 75.1932, 71.9239, 63.625, 51.6953, 47.2643, 12.438 |
| 2460361.69978 | 57986 | 57850 | 1666.6873 | 16 / 1666 | 1666.69, 833.344, 416.672, 333.337, 238.098, 208.336, 128.207, 119.049, 98.0404, 87.7204, 64.1034, 59.5245, 47.6196, 45.0456, 24.8759, 12.438 |
| 2460510.95512 | 61923 | 57850 | 1815.9427 | 16 / 1815 | 1815.94, 907.971, 605.314, 453.986, 302.657, 259.42, 226.993, 201.771, 129.71, 113.496, 95.5759, 58.5788, 47.788, 42.2312, 24.8759, 12.438 |
| 2460523.39146 | 68313 | 57850 | 1828.3790 | 19 / 1828 | 1828.38, 914.189, 609.46, 457.095, 304.73, 261.197, 228.547, 203.153, 166.216, 152.365, 130.599, 114.274, 107.552, 96.2305, 87.0657, 76.1825, 63.0476, 37.3139, 12.438 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1433.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:56:59Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:57:01Z: TOI-1433.01 (TIC 13684720, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:57:02Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T09:57:02Z: TOI-1433 (PM*); TOI-1433.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458695.0109: recovered, depth 57850 ± 1349 ppm (catalogue 107230 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | inconclusive | screen run at each light curve's own k* (none, 6, none, 5.5, 8, 4.5; ≤ 0 persistent null events outside the veto); 2 light curve(s) reached no k* on the grid and used the declared k, uncalibrated |
| Synthetic signal injection–recovery | inconclusive | completeness for 2000 ppm, 4.0 h boxes at the declared threshold: 0%, 0%, 0%, 0%, 10%, 0% per light curve (pass mark 90%) |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 11 repeat-candidate event(s); first at BJD 2458719.8830, ΔT = 24.871 d, 0 of 24 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1433.01: Gaia DR3 2057288892412649472 at 0.00" (propagated 2016.0 → J2015.5; 0.03" unpropagated, proper-motion shift 0.03") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1433.01: dwarf priors not applied — 1.33 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1433.01: 52 Gaia neighbour(s) within 52.5", contamination 47.73%; depth 57850 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 2057288823693170176, 22.6", ΔG 1.30); a centroid test is needed |
| Pointing and quality census per event | failed | 11 persistent event(s), 3 clean; BJD 2458719.8830 suspect: coarse point (in event), manual exclude (in event), momentum dump (in event), MOM_CENTR2 z=+6.5, SAP_BKG z=+18.6; BJD 2458732.3252 suspect: MOM_CENTR2 z=+5.2; BJD 2459428.8521 suspect: MOM_CENTR2 z=+10.9; BJD 2459441.2876 suspect: manual exclude (within ±0.25 d), MOM_CENTR2 z=+10.3, SAP_BKG z=-6.1 |
| Moving objects at screen-event epochs | inconclusive | 11 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 3 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1433.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1433.01: TOI-1433 otype PM* (star_or_other) at 1.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1433-01.yaml
python -m cygnus.multi report campaigns/toi-1433-01.yaml
```
