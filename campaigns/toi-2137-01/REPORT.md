<!-- cygnus:generated-draft -->
# Known-object test, TOI-2137.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2137-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #340, calibrate_screen #310, event_census #314, fetch_products #309, known_signal_recovery #311, moving_objects #334, period_aliases #315, prior_art #345, residual_screen #313, stellar_context #312, variability_guard #341
- Runner finished (UTC): 2026-09-26T10:03:24Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2137.01 (BJD 2459011.0279: recovered, depth 29935 ± 513 ppm (catalogue 40979 ppm)).
Outside the catalogued epoch the screen left 132 threshold entries forming **30 distinct event(s)**, **19 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459025.1798 matches the catalogued transit's depth (32049 vs 29935 ppm), 14.152 d later; 0 of 14 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2137.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 23059280 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 274.143956 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 34.173012 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459011.027941 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 40979.435014 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.8543682 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.2186 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-09-18 16:00:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | lightcurve | 26 | True | `053a5e1030eadd00` | True |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | lightcurve | 40 | False | `fd29cdb64f397ef7` | True |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | lightcurve | 53 | False | `96cea10acb10763d` | True |
| `tess2024003055635-s0074-0000000023059280-0269-s_lc.fits` | lightcurve | 74 | False | `6e83b9d7557b9bc0` | True |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | lightcurve | 80 | False | `e30e66e10e8c5f85` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | 2459011.02794 | recovered | 116 | 29935 ± 513 | 40979 | 0.01 |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | — | epoch not in this light curve | — | — | 40979 | — |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | — | epoch not in this light curve | — | — | 40979 | — |
| `tess2024003055635-s0074-0000000023059280-0269-s_lc.fits` | — | epoch not in this light curve | — | — | 40979 | — |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | — | epoch not in this light curve | — | — | 40979 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | 3 | False | 1h: —, 2h: 20000, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024003055635-s0074-0000000023059280-0269-s_lc.fits` | 3 | False | 1h: —, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000023059280-0269-s_lc.fits` | 2460327.00102 | -0.03865 | 92 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 2459407.23441 | -0.03811 | 87 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | 2459025.17979 | -0.03745 | 82 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 2459393.08033 | -0.03723 | 87 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | 2460482.65370 | -0.03721 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | 2460496.80300 | -0.03638 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | 2459760.99406 | -0.03585 | 79 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | 2459746.84122 | -0.03496 | 83 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | 2459760.93364 | -0.02133 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | 2459746.78011 | -0.01988 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 2459407.29830 | -0.01774 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | 2459746.90164 | -0.01765 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | 2459761.05308 | -0.01730 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 2459393.14769 | -0.01689 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | 2460490.27455 | -0.01514 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | 2460506.30637 | -0.01429 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 2459399.56295 | -0.01368 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 2459400.07961 | -0.01335 | 2 | PDCSAP+SAP | 1, 2 | yes |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 2459414.22666 | -0.01280 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | 2459026.46034 | -0.01949 | 4 | SAP | 1, 2 | no |
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | 2459026.08951 | -0.01895 | 2 | PDCSAP | 1 | no |
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | 2459014.52137 | -0.01754 | 2 | SAP | 1, 2, 3 | no |
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | 2459016.48806 | -0.01753 | 2 | SAP | 1 | no |
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | 2459028.44923 | -0.01715 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000023059280-0269-s_lc.fits` | 2460327.06769 | -0.01351 | 2 | SAP | 1 | no |
| `tess2024003055635-s0074-0000000023059280-0269-s_lc.fits` | 2460312.88974 | -0.01299 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | 2460506.24526 | -0.01290 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | 2460490.46482 | -0.01281 | 2 | PDCSAP+SAP | 1 | no |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | 2460506.23831 | -0.01259 | 2 | PDCSAP | 2 | no |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 2459414.73499 | -0.00984 | 2 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459025.17979 | 32049 | 29935 | 14.1515 | 0 / 14 |  |
| 2459393.08033 | 33427 | 29935 | 382.0521 | 9 / 382 | 382.052, 191.026, 127.351, 95.513, 76.4104, 63.6753, 47.7565, 42.4502, 14.1501 |
| 2459407.23441 | 33320 | 29935 | 396.2061 | 7 / 396 | 396.206, 198.103, 99.0515, 79.2412, 56.6009, 28.3004, 14.1502 |
| 2459407.29830 | 15025 | 29935 | 396.2700 | 3 / 396 | 396.27, 198.135, 79.254 |
| 2459746.84122 | 29958 | 29935 | 735.8129 | 13 / 735 | 735.813, 367.906, 245.271, 183.953, 122.635, 105.116, 91.9766, 61.3177, 56.601, 45.9883, 38.727, 28.3005, 14.1502 |
| 2459760.93364 | 17525 | 29935 | 749.9054 | 12 / 749 | 749.905, 374.953, 249.969, 149.981, 124.984, 107.129, 83.3228, 74.9905, 68.1732, 53.5647, 41.6614, 34.0866 |
| 2459760.99406 | 30643 | 29935 | 749.9658 | 13 / 749 | 749.966, 374.983, 249.989, 149.993, 124.994, 107.138, 83.3295, 74.9966, 68.1787, 53.569, 41.6648, 34.0894, 14.1503 |
| 2459761.05308 | 30191 | 29935 | 750.0248 | 12 / 750 | 750.025, 375.012, 250.008, 150.005, 125.004, 107.146, 83.3361, 75.0025, 68.1841, 53.5732, 41.668, 34.092 |
| 2460327.00102 | 31921 | 29935 | 1315.9727 | 23 / 1315 | 1315.97, 657.986, 438.658, 328.993, 263.195, 219.329, 187.996, 164.497, 146.219, 119.634, 109.664, 93.9981, 82.2483, 73.1096, 69.2617, 62.6654, 59.8169, 46.999, 45.3784, 42.4507 |
| 2460482.65370 | 34895 | 29935 | 1471.6254 | 23 / 1471 | 1471.63, 735.813, 490.542, 367.906, 294.325, 245.271, 210.232, 183.953, 122.635, 113.202, 105.116, 91.9766, 86.5662, 77.454, 70.0774, 61.3177, 58.865, 56.601, 45.9883, 38.727 |
| 2460496.80300 | 33761 | 29935 | 1485.7747 | 11 / 1485 | 1485.77, 495.258, 297.155, 212.254, 114.29, 99.0516, 70.7512, 64.5989, 51.2336, 42.4507, 14.1502 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2137.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:03:20Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:03:21Z: TOI-2137.01 (TIC 23059280, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:03:23Z
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T10:03:23Z: Gaia DR3 4605117746420595712 (*); TOI-2137.01 (Pl?); TOI-2137 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459011.0279: recovered, depth 29935 ± 513 ppm (catalogue 40979 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 11 repeat-candidate event(s); first at BJD 2459025.1798, ΔT = 14.152 d, 0 of 14 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2137.01: Gaia DR3 4605117677701118208 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2137.01: Teff 4949 K, R* 0.78 ± 0.06, M* 0.82 ± 0.08, ρ* 1.72 ± 0.45 ρ☉ (dwarf sequence, M_G 5.87, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2137.01: 15 Gaia neighbour(s) within 52.5", contamination 14.48%; depth 29935 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 4605117746420595712, 29.7", ΔG 2.41); a centroid test is needed |
| Pointing and quality census per event | failed | 19 persistent event(s), 4 clean; BJD 2459025.1798 caution: manual exclude (within ±0.25 d); BJD 2459399.5629 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+5.1; BJD 2459400.0796 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+14.3; BJD 2459407.2344 suspect: SAP_BKG z=-11.0 |
| Moving objects at screen-event epochs | inconclusive | 19 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-2137.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-2137.01: TOI-2137 otype SB* (multiple) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2137-01.yaml
python -m cygnus.multi report campaigns/toi-2137-01.yaml
```
