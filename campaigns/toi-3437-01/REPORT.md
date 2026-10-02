<!-- cygnus:generated-draft -->
# Known-object test, TOI-3437.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3437-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4262, calibrate_screen #4242, event_census #4249, fetch_independent #4254, fetch_products #4238, known_signal_recovery #4244, moving_objects #4253, period_aliases #4250, prior_art #4265, residual_screen #4246, stellar_context #4245, variability_guard #4263
- Runner finished (UTC): 2026-09-30T21:44:27Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3437.01 (BJD 2459967.0782: not recovered, depth 12280 ± 1514 ppm (catalogue 16931 ppm); BJD 2459972.0655: not recovered, depth 12783 ± 1589 ppm (catalogue 16931 ppm); BJD 2459977.0528: not recovered, depth 3830 ± 1597 ppm (catalogue 16931 ppm); BJD 2459982.0402: not recovered, depth 10994 ± 1481 ppm (catalogue 16931 ppm); BJD 2459987.0275: not recovered, depth 14480 ± 1561 ppm (catalogue 16931 ppm); BJD 2459992.0148: partial, depth 10471 ± 1418 ppm (catalogue 16931 ppm); BJD 2459997.0021: partial, depth 13130 ± 1566 ppm (catalogue 16931 ppm); BJD 2460001.9894: gap (catalogue 16931 ppm); BJD 2460006.9767: recovered, depth 10414 ± 1525 ppm (catalogue 16931 ppm); BJD 2460011.9640: partial, depth 10310 ± 1510 ppm (catalogue 16931 ppm); BJD 2460690.2388: gap (catalogue 16931 ppm); BJD 2460695.2261: not recovered, depth 8107 ± 1740 ppm (catalogue 16931 ppm); BJD 2460700.2134: not recovered, depth 16438 ± 1610 ppm (catalogue 16931 ppm); BJD 2460705.2008: not recovered, depth 7974 ± 1804 ppm (catalogue 16931 ppm); BJD 2460710.1881: not recovered, depth 8317 ± 1665 ppm (catalogue 16931 ppm); BJD 2460715.1754: not recovered, depth 15401 ± 1698 ppm (catalogue 16931 ppm); BJD 2460720.1627: not recovered, depth 11417 ± 1524 ppm (catalogue 16931 ppm); BJD 2460725.1500: not recovered, depth 10533 ± 1437 ppm (catalogue 16931 ppm); BJD 2460730.1373: not recovered, depth 11345 ± 1568 ppm (catalogue 16931 ppm); BJD 2460735.1247: not recovered, depth 12403 ± 1449 ppm (catalogue 16931 ppm); BJD 2460740.1120: not recovered, depth 17450 ± 1469 ppm (catalogue 16931 ppm); BJD 2460745.0993: not recovered, depth 14325 ± 1499 ppm (catalogue 16931 ppm)).
Outside the catalogued epoch the screen left 31 threshold entries forming **14 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460691.1920 matches the catalogued transit's depth (15388 vs 10414 ppm), 684.220 d later; 13 of 684 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3437.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 132313173 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 119.412446 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -41.241508 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459967.078218 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.9873145 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 16931.1672966 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.3425677 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.0707 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-10 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000132313173-0250-s_lc.fits` | lightcurve | 61 | True | `ab8548b2d66a5df7` | True |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | lightcurve | 62 | False | `05bc4ca7a3f35bc2` | True |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | lightcurve | 88 | False | `6cf3568833fa298b` | True |
| `tess2025042113628-s0089-0000000132313173-0286-s_lc.fits` | lightcurve | 89 | False | `f7e0145bc62b1108` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000132313173-0250-s_lc.fits` | 2459967.07822 | not_recovered | 71 | 12280 ± 1514 | 16931 | — |
| `tess2023018032328-s0061-0000000132313173-0250-s_lc.fits` | 2459972.06553 | not_recovered | 70 | 12783 ± 1589 | 16931 | — |
| `tess2023018032328-s0061-0000000132313173-0250-s_lc.fits` | 2459977.05285 | not_recovered | 70 | 3830 ± 1597 | 16931 | — |
| `tess2023018032328-s0061-0000000132313173-0250-s_lc.fits` | 2459982.04016 | not_recovered | 69 | 10994 ± 1481 | 16931 | — |
| `tess2023018032328-s0061-0000000132313173-0250-s_lc.fits` | 2459987.02748 | not_recovered | 70 | 14480 ± 1561 | 16931 | — |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2459992.01479 | partial | 70 | 10471 ± 1418 | 16931 | -0.32 |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2459997.00210 | partial | 71 | 13130 ± 1566 | 16931 | -0.49 |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460001.98942 | gap | 0 | — | 16931 | — |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460006.97673 | recovered | 71 | 10414 ± 1525 | 16931 | -0.12 |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460011.96405 | partial | 71 | 10310 ± 1510 | 16931 | -0.35 |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460690.23882 | gap | 0 | — | 16931 | — |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460695.22614 | not_recovered | 71 | 8107 ± 1740 | 16931 | — |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460700.21345 | not_recovered | 70 | 16438 ± 1610 | 16931 | — |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460705.20076 | not_recovered | 70 | 7974 ± 1804 | 16931 | — |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460710.18808 | not_recovered | 70 | 8317 ± 1665 | 16931 | — |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460715.17539 | not_recovered | 70 | 15401 ± 1698 | 16931 | — |
| `tess2025042113628-s0089-0000000132313173-0286-s_lc.fits` | 2460720.16271 | not_recovered | 70 | 11417 ± 1524 | 16931 | — |
| `tess2025042113628-s0089-0000000132313173-0286-s_lc.fits` | 2460725.15002 | not_recovered | 70 | 10533 ± 1437 | 16931 | — |
| `tess2025042113628-s0089-0000000132313173-0286-s_lc.fits` | 2460730.13734 | not_recovered | 71 | 11345 ± 1568 | 16931 | — |
| `tess2025042113628-s0089-0000000132313173-0286-s_lc.fits` | 2460735.12465 | not_recovered | 71 | 12403 ± 1449 | 16931 | — |
| `tess2025042113628-s0089-0000000132313173-0286-s_lc.fits` | 2460740.11197 | not_recovered | 71 | 17450 ± 1469 | 16931 | — |
| `tess2025042113628-s0089-0000000132313173-0286-s_lc.fits` | 2460745.09928 | not_recovered | 71 | 14325 ± 1499 | 16931 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023018032328-s0061-0000000132313173-0250-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2025042113628-s0089-0000000132313173-0286-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460691.19199 | -0.04210 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460704.63522 | -0.01029 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460013.77730 | -0.00965 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460013.71481 | -0.00920 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460007.27608 | -0.00906 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460007.21080 | -0.00858 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460013.85925 | -0.00854 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460013.69119 | -0.00786 | 2 | SAP | 3 | no |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460691.42533 | -0.00746 | 2 | SAP | 2 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460013.96896 | -0.00743 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000132313173-0285-s_lc.fits` | 2460697.01292 | -0.00693 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460003.32476 | -0.00682 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2459998.64845 | -0.00674 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000132313173-0254-s_lc.fits` | 2460013.99119 | -0.00658 | 2 | SAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460691.19199 | 15388 | 10414 | 684.2201 | 13 / 684 | 684.22, 342.11, 228.073, 171.055, 136.844, 114.037, 97.7457, 85.5275, 76.0245, 68.422, 62.2018, 57.0183, 48.8729 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3437.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:44:18Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:44:20Z: TOI-3437.01 (TIC 132313173, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:44:23Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:44:24Z: TOI-3437.01 (Pl?); TOI-3437 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459967.0782: not recovered, depth 12280 ± 1514 ppm (catalogue 16931 ppm); BJD 2459972.0655: not recovered, depth 12783 ± 1589 ppm (catalogue 16931 ppm); BJD 2459977.0528: not recovered, depth 3830 ± 1597 ppm (catalogue 16931 ppm); BJD 2459982.0402: not recovered, depth 10994 ± 1481 ppm (catalogue 16931 ppm); BJD 2459987.0275: not recovered, depth 14480 ± 1561 ppm (catalogue 16931 ppm); BJD 2459992.0148: partial, depth 10471 ± 1418 ppm (catalogue 16931 ppm); BJD 2459997.0021: partial, depth 13130 ± 1566 ppm (catalogue 16931 ppm); BJD 2460001.9894: gap (catalogue 16931 ppm); BJD 2460006.9767: recovered, depth 10414 ± 1525 ppm (catalogue 16931 ppm); BJD 2460011.9640: partial, depth 10310 ± 1510 ppm (catalogue 16931 ppm); BJD 2460690.2388: gap (catalogue 16931 ppm); BJD 2460695.2261: not recovered, depth 8107 ± 1740 ppm (catalogue 16931 ppm); BJD 2460700.2134: not recovered, depth 16438 ± 1610 ppm (catalogue 16931 ppm); BJD 2460705.2008: not recovered, depth 7974 ± 1804 ppm (catalogue 16931 ppm); BJD 2460710.1881: not recovered, depth 8317 ± 1665 ppm (catalogue 16931 ppm); BJD 2460715.1754: not recovered, depth 15401 ± 1698 ppm (catalogue 16931 ppm); BJD 2460720.1627: not recovered, depth 11417 ± 1524 ppm (catalogue 16931 ppm); BJD 2460725.1500: not recovered, depth 10533 ± 1437 ppm (catalogue 16931 ppm); BJD 2460730.1373: not recovered, depth 11345 ± 1568 ppm (catalogue 16931 ppm); BJD 2460735.1247: not recovered, depth 12403 ± 1449 ppm (catalogue 16931 ppm); BJD 2460740.1120: not recovered, depth 17450 ± 1469 ppm (catalogue 16931 ppm); BJD 2460745.0993: not recovered, depth 14325 ± 1499 ppm (catalogue 16931 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (4, ≤2.5, ≤2.5, 4; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460691.1920, ΔT = 684.220 d, 13 of 684 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (684.22, 342.11, 228.073, 171.055, 136.844, 114.037, 97.7457, 85.5275, 76.0245, 68.422, 62.2018, 57.0183 … d); duration likelihood under Gaia priors (circular orbits) peaks at 48.9 d (weight 0.80) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3437.01: Gaia DR3 5534252179097911936 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3437.01: Teff 5297 K, R* 0.88 ± 0.07, M* 0.92 ± 0.09, ρ* 1.36 ± 0.35 ρ☉ (dwarf sequence, M_G 5.24, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3437.01: 63 Gaia neighbour(s) within 52.5", contamination 80.07%; depth 10414 ppm (measured depth of the recovered catalogued transit); 7 could produce it if fully eclipsed (brightest 5534252174798034048, 4.8", ΔG -0.85); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2460691.1920 suspect: argabrightening (in event), scattered light 2 (in event), MOM_CENTR1 z=-5.2, POS_CORR2 z=+5.4, SAP_BKG z=+15.9 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3437.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3437.01: TOI-3437 otype * (star_or_other) at 0.4" |
| Event-time prior art | inconclusive | 1 possible published-ephemeris overlap(s) within 1 d (TOI-3437.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3437-01.yaml
python -m cygnus.multi report campaigns/toi-3437-01.yaml
```
