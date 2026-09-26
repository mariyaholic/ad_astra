<!-- cygnus:generated-draft -->
# Known-object test, TOI-573.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-573-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #100, calibrate_screen #23, event_census #47, fetch_products #7, known_signal_recovery #27, moving_objects #79, period_aliases #48, prior_art #103, residual_screen #38, stellar_context #28, variability_guard #102
- Runner finished (UTC): 2026-09-26T09:54:30Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-573.01 (BJD 2458524.6324: recovered, depth 80629 ± 742 ppm (catalogue 156035 ppm)).
Outside the catalogued epoch the screen left 83 threshold entries forming **28 distinct event(s)**, **7 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2458538.2090 matches the catalogued transit's depth (93312 vs 80629 ppm), 13.576 d later; 0 of 13 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-573.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 296780789 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 142.346908 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -14.511711 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458524.632416 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 156034.718417 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.7245219 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.519 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-19 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019032160000-s0008-0000000296780789-0136-s_lc.fits` | lightcurve | 8 | True | `6084949eeaf31596` | True |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | lightcurve | 35 | False | `26a0fe05bb7ecf4e` | True |
| `tess2023043185947-s0062-0000000296780789-0254-s_lc.fits` | lightcurve | 62 | False | `6d725824c8c71304` | True |
| `tess2026005125623-s0099-0000000296780789-0300-s_lc.fits` | lightcurve | 99 | False | `6047698cc0c09c57` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019032160000-s0008-0000000296780789-0136-s_lc.fits` | 2458524.63242 | recovered | 51 | 80629 ± 742 | 156035 | 0.00 |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | — | epoch not in this light curve | — | — | 156035 | — |
| `tess2023043185947-s0062-0000000296780789-0254-s_lc.fits` | — | epoch not in this light curve | — | — | 156035 | — |
| `tess2026005125623-s0099-0000000296780789-0300-s_lc.fits` | — | epoch not in this light curve | — | — | 156035 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019032160000-s0008-0000000296780789-0136-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2023043185947-s0062-0000000296780789-0254-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026005125623-s0099-0000000296780789-0300-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019032160000-s0008-0000000296780789-0136-s_lc.fits` | 2458538.20904 | -0.11378 | 39 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000296780789-0300-s_lc.fits` | 2461050.01796 | -0.11066 | 42 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000296780789-0254-s_lc.fits` | 2460004.56250 | -0.10737 | 43 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000296780789-0254-s_lc.fits` | 2459990.98548 | -0.10681 | 46 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000296780789-0300-s_lc.fits` | 2461063.59503 | -0.10662 | 44 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459257.80871 | -0.10576 | 41 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000296780789-0300-s_lc.fits` | 2461048.49426 | -0.02179 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.48375 | -0.02808 | 9 | SAP | 1, 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.40806 | -0.02765 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.60528 | -0.02643 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.39417 | -0.02641 | 4 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.46847 | -0.02460 | 5 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.50181 | -0.02440 | 11 | SAP | 1, 2, 3 | no |
| `tess2019032160000-s0008-0000000296780789-0136-s_lc.fits` | 2458535.08475 | -0.02430 | 2 | SAP | 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.57542 | -0.02410 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.42958 | -0.02377 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.52056 | -0.02368 | 12 | SAP | 1, 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.45528 | -0.02365 | 10 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.57055 | -0.02364 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.41361 | -0.02357 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.47472 | -0.02270 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.43583 | -0.02234 | 2 | SAP | 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.38444 | -0.02228 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.40181 | -0.02196 | 3 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.54694 | -0.02158 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.44278 | -0.02118 | 6 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.42056 | -0.02014 | 2 | SAP | 2, 3 | no |
| `tess2021039152502-s0035-0000000296780789-0205-s_lc.fits` | 2459266.53444 | -0.02012 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2458538.20904 | 93312 | 80629 | 13.5764 | 0 / 13 |  |
| 2459257.80871 | 91631 | 80629 | 733.1761 | 25 / 733 | 733.176, 366.588, 244.392, 183.294, 146.635, 122.196, 104.739, 91.647, 81.464, 73.3176, 66.6524, 61.098, 56.3982, 52.3697, 45.8235, 40.732, 34.9131, 33.3262, 31.8772, 30.549 |
| 2459990.98548 | 87205 | 80629 | 1466.3529 | 43 / 1466 | 1466.35, 733.176, 488.784, 366.588, 293.271, 244.392, 209.479, 183.294, 162.928, 146.635, 133.305, 122.196, 112.796, 104.74, 91.6471, 86.2561, 81.464, 73.3176, 69.8263, 66.6524 |
| 2460004.56250 | 91492 | 80629 | 1479.9299 | 19 / 1479 | 1479.93, 493.31, 295.986, 211.419, 164.437, 134.539, 113.841, 98.662, 77.891, 70.4729, 64.3448, 54.8122, 51.0321, 44.8464, 42.2837, 39.9981, 32.8873, 31.4879, 13.5773 |
| 2461050.01796 | 90052 | 80629 | 2525.3854 | 48 / 2525 | 2525.39, 1262.69, 841.795, 631.346, 505.077, 420.898, 360.769, 315.673, 280.598, 252.538, 229.581, 194.26, 180.385, 168.359, 157.837, 140.299, 132.915, 126.269, 120.256, 114.79 |
| 2461063.59503 | 92254 | 80629 | 2538.9624 | 47 / 2538 | 2538.96, 1269.48, 846.321, 634.741, 507.793, 423.16, 362.709, 317.37, 282.107, 253.896, 230.815, 195.305, 181.355, 169.264, 158.685, 149.351, 141.054, 126.948, 120.903, 115.407 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-573.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:54:26Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:54:27Z: TOI-573.01 (TIC 296780789, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:54:28Z
- SIMBAD (done, 2026-09-26): 4 match(es) in SIMBAD within 30" as of 2026-09-26T09:54:29Z: TOI-573.01 (Pl?); ** TOI  573A (PM*); ** TOI  573B (PM*); TOI-573 (**)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458524.6324: recovered, depth 80629 ± 742 ppm (catalogue 156035 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (4.5, 4, 3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 6 repeat-candidate event(s); first at BJD 2458538.2090, ΔT = 13.576 d, 0 of 13 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | inconclusive | TOI-573.01: Gaia DR3 5689391929738059648 at 0.00" (propagated 2016.0 → J2015.5; 0.05" unpropagated, proper-motion shift 0.05"; another source 1.71" away, ΔG 0.8787669999999999) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-573.01: dwarf priors not applied — 1.10 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-573.01: 5 Gaia neighbour(s) within 52.5", contamination 37.90%; depth 80629 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 5689391929738875776, 1.7", ΔG 0.88); a centroid test is needed |
| Pointing and quality census per event | failed | 7 persistent event(s), 4 clean; BJD 2459257.8087 suspect: MOM_CENTR1 z=+5.0; BJD 2461048.4943 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR2 z=-7.7, POS_CORR1 z=+7.6, POS_CORR2 z=-11.9, SAP_BKG z=+15.9; BJD 2461063.5950 suspect: MOM_CENTR2 z=+10.5, POS_CORR1 z=-9.0, POS_CORR2 z=+12.6 |
| Moving objects at screen-event epochs | inconclusive | 7 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-573.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-573.01: ** TOI  573A otype PM* (star_or_other) at 1.6" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-573-01.yaml
python -m cygnus.multi report campaigns/toi-573-01.yaml
```
