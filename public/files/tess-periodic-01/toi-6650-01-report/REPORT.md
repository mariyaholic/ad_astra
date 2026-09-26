<!-- [private Drive store] -->
# Known-object test, TOI-6650.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6650-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #383, calibrate_screen #361, event_census #376, fetch_products #355, known_signal_recovery #364, moving_objects #381, period_aliases #377, prior_art #385, residual_screen #373, stellar_context #365, variability_guard #384
- Runner finished (UTC): 2026-09-26T10:05:09Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6650.01 (BJD 2460582.7117: recovered, depth 9511 ± 78 ppm (catalogue 10524 ppm)).
Outside the catalogued epoch the screen left 134 threshold entries forming **37 distinct event(s)**, **13 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460562.3867 matches the catalogued transit's depth (7724 vs 9511 ppm), 20.330 d later; 1 of 20 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6650.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 64837857 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 338.805332 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 54.773557 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460582.711665 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10524.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 6.584 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.0252 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-01-09 16:02:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | lightcurve | 83 | True | `2ce9b5b429702c22` | True |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | lightcurve | 57 | False | `6aa4ca0c14bcf416` | True |
| `tess2024085201119-s0077-0000000064837857-0272-s_lc.fits` | lightcurve | 77 | False | `472fe0fb5951a760` | True |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | lightcurve | 84 | False | `a513194fd134cf25` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460582.71166 | recovered | 198 | 9511 ± 78 | 10524 | 0.12 |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | — | epoch not in this light curve | — | — | 10524 | — |
| `tess2024085201119-s0077-0000000064837857-0272-s_lc.fits` | — | epoch not in this light curve | — | — | 10524 | — |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | — | epoch not in this light curve | — | — | 10524 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | 6 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024085201119-s0077-0000000064837857-0272-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | 2459871.10023 | -0.00970 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460603.04803 | -0.00964 | 172 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | 2459871.24120 | -0.00950 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | 2459871.06273 | -0.00939 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | 2459871.16343 | -0.00928 | 87 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460562.38669 | -0.00906 | 174 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000064837857-0272-s_lc.fits` | 2460399.74229 | -0.00884 | 164 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000064837857-0272-s_lc.fits` | 2460420.07109 | -0.00828 | 164 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | 2459871.07037 | -0.00811 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | 2459871.26967 | -0.00743 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024085201119-s0077-0000000064837857-0272-s_lc.fits` | 2460399.62562 | -0.00632 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460609.10905 | -0.00425 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460609.02572 | -0.00370 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | 2459871.05857 | -0.00728 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024085201119-s0077-0000000064837857-0272-s_lc.fits` | 2460420.18776 | -0.00611 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460572.19869 | -0.00453 | 3 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460572.15077 | -0.00437 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460570.43894 | -0.00392 | 3 | SAP | 1, 2, 3 | no |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460590.65924 | -0.00390 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460572.15494 | -0.00389 | 2 | SAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460590.10090 | -0.00375 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460564.61452 | -0.00369 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460572.10563 | -0.00366 | 3 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460584.23423 | -0.00354 | 2 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460564.74646 | -0.00352 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460578.47030 | -0.00348 | 2 | PDCSAP | 2, 3 | no |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460590.13632 | -0.00348 | 3 | SAP | 1, 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460564.73257 | -0.00341 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460568.61738 | -0.00331 | 2 | PDCSAP | 2 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460564.53257 | -0.00324 | 2 | SAP | 2, 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460572.08133 | -0.00322 | 2 | SAP | 3 | no |
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 2460572.13133 | -0.00312 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460600.86751 | -0.00306 | 2 | PDCSAP | 2 | no |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460590.03702 | -0.00301 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460590.57868 | -0.00298 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460590.69535 | -0.00292 | 2 | SAP | 3 | no |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 2460609.08822 | -0.00281 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460562.38669 | 7724 | 9511 | 20.3302 | 1 / 20 | 20.3302 |
| 2459871.06273 | 7090 | 9511 | 711.6541 | 17 / 711 | 711.654, 355.827, 237.218, 142.331, 118.609, 101.665, 79.0727, 71.1654, 64.6958, 50.8324, 47.4436, 41.862, 39.5363, 37.4555, 33.8883, 28.4662, 20.333 |
| 2459871.07037 | 7618 | 9511 | 711.6465 | 17 / 711 | 711.646, 355.823, 237.215, 142.329, 118.608, 101.664, 79.0718, 71.1646, 64.6951, 50.8319, 47.4431, 41.8616, 39.5359, 37.4551, 33.8879, 28.4659, 20.3328 |
| 2459871.10023 | 8363 | 9511 | 711.6166 | 17 / 711 | 711.617, 355.808, 237.206, 142.323, 118.603, 101.659, 79.0685, 71.1617, 64.6924, 50.8298, 47.4411, 41.8598, 39.5343, 37.4535, 33.8865, 28.4647, 20.3319 |
| 2459871.16343 | 8594 | 9511 | 711.5534 | 17 / 711 | 711.553, 355.777, 237.185, 142.311, 118.592, 101.65, 79.0615, 71.1553, 64.6867, 50.8252, 47.4369, 41.8561, 39.5307, 37.4502, 33.8835, 28.4621, 20.3301 |
| 2459871.24120 | 8343 | 9511 | 711.4757 | 16 / 711 | 711.476, 355.738, 237.159, 142.295, 118.579, 101.639, 79.0529, 71.1476, 64.6796, 50.8197, 47.4317, 41.8515, 39.5264, 33.8798, 28.459, 20.3279 |
| 2459871.26967 | 7076 | 9511 | 711.4472 | 16 / 711 | 711.447, 355.724, 237.149, 142.289, 118.575, 101.635, 79.0497, 71.1447, 64.677, 50.8177, 47.4298, 41.8498, 39.5248, 33.8784, 28.4579, 20.3271 |
| 2460399.74229 | 8482 | 9511 | 182.9746 | 6 / 182 | 182.975, 91.4873, 60.9915, 45.7436, 36.5949, 20.3305 |
| 2460420.07109 | 7915 | 9511 | 162.6458 | 4 / 162 | 162.646, 81.3229, 40.6614, 20.3307 |
| 2460603.04803 | 9224 | 9511 | 20.3312 | 1 / 20 | 20.3312 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6650.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:05:05Z
- TESS_TOI (done, 2026-09-26): 4 match(es) in TESS_TOI within 30" as of 2026-09-26T10:05:07Z: TOI-6650.01 (TIC 64837857, disposition PC); TOI-6650.02 (TIC 64837857, disposition PC); TOI-6650.03 (TIC 64837857, disposition FP); TOI-6650.04 (TIC 64837857, disposition PC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:05:08Z: Gaia DR3 2003378084962524032 (type DSCT|GDOR|SXPHE, P — d)
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:05:08Z: BD+54  2812 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460582.7117: recovered, depth 9511 ± 78 ppm (catalogue 10524 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 6, 3.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 40%, 0%, 10%, 40% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 10 repeat-candidate event(s); first at BJD 2460562.3867, ΔT = 20.330 d, 1 of 20 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (20.3302 d); duration likelihood under Gaia priors (circular orbits) peaks at 20.3 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6650.01: Gaia DR3 2003378188041736320 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6650.01: Teff 6427 K, R* 1.39 ± 0.11, M* 1.27 ± 0.13, ρ* 0.48 ± 0.12 ρ☉ (dwarf sequence, M_G 3.49, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6650.01: 65 Gaia neighbour(s) within 52.5", contamination 12.51%; depth 9511 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 2003378084962524032, 28.3", ΔG 2.80); a centroid test is needed |
| Pointing and quality census per event | failed | 13 persistent event(s), 8 clean; BJD 2460562.3867 suspect: argabrightening (within ±0.25 d), coarse point (within ±0.25 d), manual exclude (within ±0.25 d), MOM_CENTR2 z=-11.3, POS_CORR2 z=-10.6, SAP_BKG z=-5.3; BJD 2460399.6256 suspect: SAP_BKG z=-5.4; BJD 2460399.7423 suspect: SAP_BKG z=-9.4; BJD 2460420.0711 suspect: SAP_BKG z=+7.7 |
| Moving objects at screen-event epochs | inconclusive | 13 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-6650.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6650.01: BD+54  2812 otype * (star_or_other) at 0.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6650-01.yaml
python -m cygnus.multi report campaigns/toi-6650-01.yaml
```
