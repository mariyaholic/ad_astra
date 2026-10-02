<!-- cygnus:generated-draft -->
# Known-object test, TOI-1527.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1527-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4049, calibrate_screen #4034, event_census #4040, fetch_independent #4043, fetch_products #4025, known_signal_recovery #4037, moving_objects #4042, period_aliases #4041, prior_art #4052, residual_screen #4039, stellar_context #4038, variability_guard #4051
- Runner finished (UTC): 2026-09-30T21:35:15Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1527.01 (BJD 2460585.7015: recovered, depth 2077 ± 92 ppm (catalogue 2884 ppm); BJD 2460590.7641: recovered, depth 2559 ± 99 ppm (catalogue 2884 ppm); BJD 2460595.8267: gap (catalogue 2884 ppm); BJD 2460600.8893: partial, depth 2388 ± 87 ppm (catalogue 2884 ppm); BJD 2460605.9519: partial, depth 2423 ± 78 ppm (catalogue 2884 ppm); BJD 2459856.6899: recovered, depth 2556 ± 78 ppm (catalogue 2884 ppm); BJD 2459861.7525: recovered, depth 2395 ± 85 ppm (catalogue 2884 ppm); BJD 2459866.8151: recovered, depth 2363 ± 83 ppm (catalogue 2884 ppm); BJD 2459871.8776: recovered, depth 2730 ± 78 ppm (catalogue 2884 ppm); BJD 2459876.9402: recovered, depth 2582 ± 77 ppm (catalogue 2884 ppm); BJD 2459882.0028: recovered, depth 2889 ± 82 ppm (catalogue 2884 ppm); BJD 2460611.0144: not recovered, depth 1048 ± 127 ppm (catalogue 2884 ppm); BJD 2460616.0770: recovered, depth 2559 ± 92 ppm (catalogue 2884 ppm); BJD 2460621.1396: recovered, depth 2667 ± 81 ppm (catalogue 2884 ppm); BJD 2460626.2022: gap (catalogue 2884 ppm); BJD 2460631.2648: recovered, depth 2547 ± 83 ppm (catalogue 2884 ppm)).
Outside the catalogued epoch the screen left 30 threshold entries forming **16 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1527.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 202375913 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 5.965461 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 51.468293 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460600.889284 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.0625809 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 2884.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.69 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.6968 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-05-02 16:23:22 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024274222008-s0084-0000000202375913-0281-s_lc.fits` | lightcurve | 84 | True | `735259caa26dc8f2` | True |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | lightcurve | 57 | False | `82c0521eba6bd65c` | True |
| `tess2024300212641-s0085-0000000202375913-0282-s_lc.fits` | lightcurve | 85 | False | `aba85d21f4dc152f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024274222008-s0084-0000000202375913-0281-s_lc.fits` | 2460585.70154 | recovered | 110 | 2077 ± 92 | 2884 | -0.43 |
| `tess2024274222008-s0084-0000000202375913-0281-s_lc.fits` | 2460590.76412 | recovered | 73 | 2559 ± 99 | 2884 | -0.20 |
| `tess2024274222008-s0084-0000000202375913-0281-s_lc.fits` | 2460595.82670 | gap | 0 | — | 2884 | — |
| `tess2024274222008-s0084-0000000202375913-0281-s_lc.fits` | 2460600.88928 | partial | 110 | 2388 ± 87 | 2884 | 0.34 |
| `tess2024274222008-s0084-0000000202375913-0281-s_lc.fits` | 2460605.95186 | partial | 110 | 2423 ± 78 | 2884 | 0.57 |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459856.68989 | recovered | 109 | 2556 ± 78 | 2884 | 0.17 |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459861.75247 | recovered | 110 | 2395 ± 85 | 2884 | 0.34 |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459866.81505 | recovered | 108 | 2363 ± 83 | 2884 | 0.25 |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459871.87763 | recovered | 110 | 2730 ± 78 | 2884 | -0.43 |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459876.94022 | recovered | 110 | 2582 ± 77 | 2884 | -0.04 |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459882.00280 | recovered | 110 | 2889 ± 82 | 2884 | -0.40 |
| `tess2024300212641-s0085-0000000202375913-0282-s_lc.fits` | 2460611.01445 | not_recovered | 55 | 1048 ± 127 | 2884 | — |
| `tess2024300212641-s0085-0000000202375913-0282-s_lc.fits` | 2460616.07703 | recovered | 99 | 2559 ± 92 | 2884 | 0.08 |
| `tess2024300212641-s0085-0000000202375913-0282-s_lc.fits` | 2460621.13961 | recovered | 111 | 2667 ± 81 | 2884 | -0.09 |
| `tess2024300212641-s0085-0000000202375913-0282-s_lc.fits` | 2460626.20219 | gap | 0 | — | 2884 | — |
| `tess2024300212641-s0085-0000000202375913-0282-s_lc.fits` | 2460631.26477 | recovered | 111 | 2547 ± 83 | 2884 | 0.01 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024274222008-s0084-0000000202375913-0281-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 2000, 2h: 2000, 4h: 5000, 8h: 5000 |
| `tess2024300212641-s0085-0000000202375913-0282-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459863.21227 | -0.00270 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459863.25810 | -0.00262 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459866.56509 | -0.00336 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459867.11162 | -0.00303 | 3 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459867.18454 | -0.00297 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459867.19704 | -0.00295 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459863.19699 | -0.00286 | 2 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459867.21232 | -0.00283 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459867.17065 | -0.00280 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459867.18940 | -0.00279 | 3 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459863.17616 | -0.00265 | 2 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459863.07407 | -0.00264 | 3 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459867.05815 | -0.00262 | 2 | SAP | 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459880.35958 | -0.00260 | 2 | SAP | 2, 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459860.30805 | -0.00247 | 2 | SAP | 1, 2, 3 | no |
| `tess2022273165103-s0057-0000000202375913-0245-s_lc.fits` | 2459858.14690 | -0.00238 | 2 | PDCSAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-1527.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:35:08Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:35:10Z: TOI-1527.01 (TIC 202375913, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:35:12Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:35:14Z: TOI-1527.01 (Pl?); BD+50    62 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460585.7015: recovered, depth 2077 ± 92 ppm (catalogue 2884 ppm); BJD 2460590.7641: recovered, depth 2559 ± 99 ppm (catalogue 2884 ppm); BJD 2460595.8267: gap (catalogue 2884 ppm); BJD 2460600.8893: partial, depth 2388 ± 87 ppm (catalogue 2884 ppm); BJD 2460605.9519: partial, depth 2423 ± 78 ppm (catalogue 2884 ppm); BJD 2459856.6899: recovered, depth 2556 ± 78 ppm (catalogue 2884 ppm); BJD 2459861.7525: recovered, depth 2395 ± 85 ppm (catalogue 2884 ppm); BJD 2459866.8151: recovered, depth 2363 ± 83 ppm (catalogue 2884 ppm); BJD 2459871.8776: recovered, depth 2730 ± 78 ppm (catalogue 2884 ppm); BJD 2459876.9402: recovered, depth 2582 ± 77 ppm (catalogue 2884 ppm); BJD 2459882.0028: recovered, depth 2889 ± 82 ppm (catalogue 2884 ppm); BJD 2460611.0144: not recovered, depth 1048 ± 127 ppm (catalogue 2884 ppm); BJD 2460616.0770: recovered, depth 2559 ± 92 ppm (catalogue 2884 ppm); BJD 2460621.1396: recovered, depth 2667 ± 81 ppm (catalogue 2884 ppm); BJD 2460626.2022: gap (catalogue 2884 ppm); BJD 2460631.2648: recovered, depth 2547 ± 83 ppm (catalogue 2884 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (4, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 80%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1527.01: Gaia DR3 394878060542362112 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1527.01: dwarf priors not applied — 1.21 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1527.01: 19 Gaia neighbour(s) within 52.5", contamination 1.12%; depth 2077 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 394878060542363008, 18.5", ΔG 6.36); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2459863.2123 suspect: SAP_BKG z=+10.7; BJD 2459863.2581 suspect: SAP_BKG z=+10.5 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-1527.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1527.01: BD+50    62 otype * (star_or_other) at 0.0" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1527-01.yaml
python -m cygnus.multi report campaigns/toi-1527-01.yaml
```
