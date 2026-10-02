<!-- cygnus:generated-draft -->
# Known-object test, TOI-2644.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2644-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4702, calibrate_screen #4678, event_census #4693, fetch_independent #4696, fetch_products #4672, known_signal_recovery #4681, moving_objects #4695, period_aliases #4694, prior_art #4706, residual_screen #4690, stellar_context #4683, variability_guard #4704
- Runner finished (UTC): 2026-09-30T22:11:51Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2644.01 (BJD 2459290.5731: recovered, depth 5272 ± 208 ppm (catalogue 6711 ppm); BJD 2459300.3171: recovered, depth 4667 ± 220 ppm (catalogue 6711 ppm); BJD 2460021.3712: not recovered, depth 251 ± 895 ppm (catalogue 6711 ppm); BJD 2460031.1152: recovered, depth 49 ± 217 ppm (catalogue 6711 ppm); BJD 2460040.8592: gap (catalogue 6711 ppm); BJD 2460752.1693: not recovered, depth -295 ± 223 ppm (catalogue 6711 ppm); BJD 2460761.9133: not recovered, depth -1157 ± 262 ppm (catalogue 6711 ppm); BJD 2460771.6572: not recovered, depth 261 ± 220 ppm (catalogue 6711 ppm)).
Outside the catalogued epoch the screen left 59 threshold entries forming **30 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2644.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 385332171 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 181.692982 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -16.510294 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459300.317115 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 9.7439744 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6711.0590566 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.9764395 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.9206 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | lightcurve | 36 | True | `725807a58a58e807` | True |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | lightcurve | 63 | False | `69fb436f4cb5cd55` | True |
| `tess2025071122000-s0090-0000000385332171-0287-s_lc.fits` | lightcurve | 90 | False | `9d773c5d7336a0a5` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459290.57314 | recovered | 59 | 5272 ± 208 | 6711 | -0.20 |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459300.31711 | recovered | 59 | 4667 ± 220 | 6711 | 0.08 |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460021.37122 | not_recovered | 3 | 251 ± 895 | 6711 | — |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460031.11520 | recovered | 60 | 49 ± 217 | 6711 | -1.53 |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460040.85917 | gap | 0 | — | 6711 | — |
| `tess2025071122000-s0090-0000000385332171-0287-s_lc.fits` | 2460752.16930 | not_recovered | 59 | -295 ± 223 | 6711 | — |
| `tess2025071122000-s0090-0000000385332171-0287-s_lc.fits` | 2460761.91328 | not_recovered | 59 | -1157 ± 262 | 6711 | — |
| `tess2025071122000-s0090-0000000385332171-0287-s_lc.fits` | 2460771.65725 | not_recovered | 60 | 261 ± 220 | 6711 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2025071122000-s0090-0000000385332171-0287-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.62375 | -0.00847 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459305.55508 | -0.00838 | 3 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459305.53078 | -0.00826 | 4 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.41958 | -0.00806 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459305.73286 | -0.00794 | 3 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.65152 | -0.00771 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.61125 | -0.00738 | 3 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459305.60717 | -0.00737 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.49597 | -0.00714 | 4 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459305.82244 | -0.00710 | 3 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.37791 | -0.00703 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460033.59087 | -0.00698 | 3 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.52999 | -0.00695 | 3 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.42444 | -0.00678 | 3 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460033.54573 | -0.00672 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460039.19849 | -0.00668 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459305.41272 | -0.00654 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459305.81828 | -0.00653 | 2 | SAP | 1, 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459305.66133 | -0.00651 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.54319 | -0.00644 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460033.48323 | -0.00642 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.31680 | -0.00639 | 2 | SAP | 2, 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459292.43485 | -0.00635 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459305.78217 | -0.00630 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460033.66518 | -0.00595 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460033.86795 | -0.00590 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460033.83323 | -0.00555 | 2 | SAP | 3 | no |
| `tess2021065132309-s0036-0000000385332171-0207-s_lc.fits` | 2459282.37902 | -0.00552 | 2 | PDCSAP | 3 | no |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460039.02905 | -0.00545 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000385332171-0255-s_lc.fits` | 2460039.57280 | -0.00537 | 3 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2644.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:11:38Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:11:41Z: TOI-2644.01 (TIC 385332171, disposition APC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:11:46Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:11:48Z: TYC 6095-201-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459290.5731: recovered, depth 5272 ± 208 ppm (catalogue 6711 ppm); BJD 2459300.3171: recovered, depth 4667 ± 220 ppm (catalogue 6711 ppm); BJD 2460021.3712: not recovered, depth 251 ± 895 ppm (catalogue 6711 ppm); BJD 2460031.1152: recovered, depth 49 ± 217 ppm (catalogue 6711 ppm); BJD 2460040.8592: gap (catalogue 6711 ppm); BJD 2460752.1693: not recovered, depth -295 ± 223 ppm (catalogue 6711 ppm); BJD 2460761.9133: not recovered, depth -1157 ± 262 ppm (catalogue 6711 ppm); BJD 2460771.6572: not recovered, depth 261 ± 220 ppm (catalogue 6711 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2644.01: Gaia DR3 3567876272486171904 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-2644.01: dwarf priors not applied — RUWE 7.2496696 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-2644.01: 3 Gaia neighbour(s) within 52.5", contamination 0.19%; depth 5272 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2644.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2644.01: TYC 6095-201-1 otype * (star_or_other) at 0.6" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2644-01.yaml
python -m cygnus.multi report campaigns/toi-2644-01.yaml
```
