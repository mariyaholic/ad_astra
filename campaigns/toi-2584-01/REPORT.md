<!-- cygnus:generated-draft -->
# Known-object test, TOI-2584.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2584-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4754, calibrate_screen #4737, event_census #4749, fetch_independent #4752, fetch_products #4728, known_signal_recovery #4739, moving_objects #4751, period_aliases #4750, prior_art #4759, residual_screen #4745, stellar_context #4740, variability_guard #4756
- Runner finished (UTC): 2026-09-30T22:17:06Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2584.01 (BJD 2459963.8691: gap (catalogue 12380 ppm); BJD 2459968.5656: partial, depth 8250 ± 533 ppm (catalogue 12380 ppm); BJD 2459973.2622: not recovered, depth 8798 ± 536 ppm (catalogue 12380 ppm); BJD 2459977.9588: partial, depth 9902 ± 599 ppm (catalogue 12380 ppm); BJD 2459982.6553: partial, depth 9905 ± 514 ppm (catalogue 12380 ppm); BJD 2459987.3519: not recovered, depth 7391 ± 597 ppm (catalogue 12380 ppm); BJD 2460236.2698: not recovered, depth 8056 ± 701 ppm (catalogue 12380 ppm); BJD 2460240.9663: not recovered, depth 9412 ± 594 ppm (catalogue 12380 ppm); BJD 2460245.6629: not recovered, depth 10039 ± 608 ppm (catalogue 12380 ppm); BJD 2460250.3595: not recovered, depth 10639 ± 617 ppm (catalogue 12380 ppm); BJD 2460255.0560: not recovered, depth 9975 ± 625 ppm (catalogue 12380 ppm); BJD 2460259.7526: gap (catalogue 12380 ppm); BJD 2460264.4491: not recovered, depth 10175 ± 612 ppm (catalogue 12380 ppm); BJD 2460269.1457: not recovered, depth 10710 ± 580 ppm (catalogue 12380 ppm); BJD 2460273.8423: gap (catalogue 12380 ppm); BJD 2460278.5388: not recovered, depth 9594 ± 570 ppm (catalogue 12380 ppm); BJD 2460283.2354: recovered, depth 9896 ± 584 ppm (catalogue 12380 ppm); BJD 2460691.8365: gap (catalogue 12380 ppm); BJD 2460696.5330: not recovered, depth 9398 ± 530 ppm (catalogue 12380 ppm); BJD 2460701.2296: not recovered, depth 9827 ± 526 ppm (catalogue 12380 ppm); BJD 2460705.9261: recovered, depth 9280 ± 577 ppm (catalogue 12380 ppm); BJD 2460710.6227: recovered, depth 10235 ± 519 ppm (catalogue 12380 ppm); BJD 2460715.3193: recovered, depth 8954 ± 503 ppm (catalogue 12380 ppm)).
Outside the catalogued epoch the screen left 3 threshold entries forming **2 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2584.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 458641144 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 125.108796 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 7.588913 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459245.2948 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.6965638 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 12380.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.056 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.731 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-01-23 12:02:45 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000458641144-0250-s_lc.fits` | lightcurve | 61 | False | `f628863d060965ef` | True |
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | lightcurve | 71 | False | `cf499be6e5546b79` | True |
| `tess2023315124025-s0072-0000000458641144-0267-s_lc.fits` | lightcurve | 72 | False | `42e939247d0b0fea` | True |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | lightcurve | 88 | False | `677f8a4ae87ec110` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000458641144-0250-s_lc.fits` | 2459963.86906 | gap | 0 | — | 12380 | — |
| `tess2023018032328-s0061-0000000458641144-0250-s_lc.fits` | 2459968.56563 | partial | 92 | 8250 ± 533 | 12380 | 0.66 |
| `tess2023018032328-s0061-0000000458641144-0250-s_lc.fits` | 2459973.26219 | not_recovered | 92 | 8798 ± 536 | 12380 | — |
| `tess2023018032328-s0061-0000000458641144-0250-s_lc.fits` | 2459977.95875 | partial | 91 | 9902 ± 599 | 12380 | -0.18 |
| `tess2023018032328-s0061-0000000458641144-0250-s_lc.fits` | 2459982.65532 | partial | 92 | 9905 ± 514 | 12380 | 0.30 |
| `tess2023018032328-s0061-0000000458641144-0250-s_lc.fits` | 2459987.35188 | not_recovered | 91 | 7391 ± 597 | 12380 | — |
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | 2460236.26976 | not_recovered | 92 | 8056 ± 701 | 12380 | — |
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | 2460240.96633 | not_recovered | 91 | 9412 ± 594 | 12380 | — |
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | 2460245.66289 | not_recovered | 91 | 10039 ± 608 | 12380 | — |
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | 2460250.35945 | not_recovered | 92 | 10639 ± 617 | 12380 | — |
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | 2460255.05602 | not_recovered | 92 | 9975 ± 625 | 12380 | — |
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | 2460259.75258 | gap | 0 | — | 12380 | — |
| `tess2023315124025-s0072-0000000458641144-0267-s_lc.fits` | 2460264.44914 | not_recovered | 91 | 10175 ± 612 | 12380 | — |
| `tess2023315124025-s0072-0000000458641144-0267-s_lc.fits` | 2460269.14571 | not_recovered | 91 | 10710 ± 580 | 12380 | — |
| `tess2023315124025-s0072-0000000458641144-0267-s_lc.fits` | 2460273.84227 | gap | 0 | — | 12380 | — |
| `tess2023315124025-s0072-0000000458641144-0267-s_lc.fits` | 2460278.53884 | not_recovered | 92 | 9594 ± 570 | 12380 | — |
| `tess2023315124025-s0072-0000000458641144-0267-s_lc.fits` | 2460283.23540 | recovered | 92 | 9896 ± 584 | 12380 | 0.06 |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | 2460691.83645 | gap | 0 | — | 12380 | — |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | 2460696.53301 | not_recovered | 91 | 9398 ± 530 | 12380 | — |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | 2460701.22958 | not_recovered | 92 | 9827 ± 526 | 12380 | — |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | 2460705.92614 | recovered | 91 | 9280 ± 577 | 12380 | 0.48 |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | 2460710.62271 | recovered | 92 | 10235 ± 519 | 12380 | 0.26 |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | 2460715.31927 | recovered | 92 | 8954 ± 503 | 12380 | 1.11 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023018032328-s0061-0000000458641144-0250-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023315124025-s0072-0000000458641144-0267-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000458641144-0266-s_lc.fits` | 2460253.07673 | -0.02679 | 2 | SAP | 2, 3 | no |
| `tess2025014115807-s0088-0000000458641144-0285-s_lc.fits` | 2460703.79768 | -0.01882 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2584.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:16:42Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:16:49Z: TOI-2584.01 (TIC 458641144, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:16:54Z
- SIMBAD (done, 2026-09-30): 4 match(es) in SIMBAD within 30" as of 2026-09-30T22:16:57Z: DES J082026.55+073538.5 (GiC); UCAC4 488-047656 (*); DES J082026.36+073456.6 (GiC); [SPD2011] 130 (ClG)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459963.8691: gap (catalogue 12380 ppm); BJD 2459968.5656: partial, depth 8250 ± 533 ppm (catalogue 12380 ppm); BJD 2459973.2622: not recovered, depth 8798 ± 536 ppm (catalogue 12380 ppm); BJD 2459977.9588: partial, depth 9902 ± 599 ppm (catalogue 12380 ppm); BJD 2459982.6553: partial, depth 9905 ± 514 ppm (catalogue 12380 ppm); BJD 2459987.3519: not recovered, depth 7391 ± 597 ppm (catalogue 12380 ppm); BJD 2460236.2698: not recovered, depth 8056 ± 701 ppm (catalogue 12380 ppm); BJD 2460240.9663: not recovered, depth 9412 ± 594 ppm (catalogue 12380 ppm); BJD 2460245.6629: not recovered, depth 10039 ± 608 ppm (catalogue 12380 ppm); BJD 2460250.3595: not recovered, depth 10639 ± 617 ppm (catalogue 12380 ppm); BJD 2460255.0560: not recovered, depth 9975 ± 625 ppm (catalogue 12380 ppm); BJD 2460259.7526: gap (catalogue 12380 ppm); BJD 2460264.4491: not recovered, depth 10175 ± 612 ppm (catalogue 12380 ppm); BJD 2460269.1457: not recovered, depth 10710 ± 580 ppm (catalogue 12380 ppm); BJD 2460273.8423: gap (catalogue 12380 ppm); BJD 2460278.5388: not recovered, depth 9594 ± 570 ppm (catalogue 12380 ppm); BJD 2460283.2354: recovered, depth 9896 ± 584 ppm (catalogue 12380 ppm); BJD 2460691.8365: gap (catalogue 12380 ppm); BJD 2460696.5330: not recovered, depth 9398 ± 530 ppm (catalogue 12380 ppm); BJD 2460701.2296: not recovered, depth 9827 ± 526 ppm (catalogue 12380 ppm); BJD 2460705.9261: recovered, depth 9280 ± 577 ppm (catalogue 12380 ppm); BJD 2460710.6227: recovered, depth 10235 ± 519 ppm (catalogue 12380 ppm); BJD 2460715.3193: recovered, depth 8954 ± 503 ppm (catalogue 12380 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 4, 3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2584.01: Gaia DR3 3097237913719100672 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2584.01: Teff 6441 K, R* 1.38 ± 0.11, M* 1.27 ± 0.13, ρ* 0.48 ± 0.12 ρ☉ (dwarf sequence, M_G 3.50, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2584.01: 6 Gaia neighbour(s) within 52.5", contamination 8.01%; depth 9896 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 3097238291676221440, 26.3", ΔG 2.89); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2584.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2584.01: UCAC4 488-047656 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2584-01.yaml
python -m cygnus.multi report campaigns/toi-2584-01.yaml
```
