<!-- cygnus:generated-draft -->
# Known-object test, TOI-4218.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4218-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4492, calibrate_screen #4476, event_census #4482, fetch_independent #4486, fetch_products #4471, known_signal_recovery #4478, moving_objects #4485, period_aliases #4483, prior_art #4494, residual_screen #4481, stellar_context #4480, variability_guard #4493
- Runner finished (UTC): 2026-09-30T21:56:18Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4218.01 (BJD 2459964.7114: partial, depth 1975 ± 656 ppm (catalogue 12010 ppm); BJD 2459967.3383: partial, depth 4140 ± 626 ppm (catalogue 12010 ppm); BJD 2459969.9653: not recovered, depth 3413 ± 609 ppm (catalogue 12010 ppm); BJD 2459972.5923: partial, depth 2273 ± 568 ppm (catalogue 12010 ppm); BJD 2459975.2192: not recovered, depth 2147 ± 986 ppm (catalogue 12010 ppm); BJD 2459977.8462: not recovered, depth 3762 ± 602 ppm (catalogue 12010 ppm); BJD 2459980.4731: not recovered, depth 3122 ± 628 ppm (catalogue 12010 ppm); BJD 2459983.1001: not recovered, depth 6097 ± 583 ppm (catalogue 12010 ppm); BJD 2459985.7270: not recovered, depth 2288 ± 593 ppm (catalogue 12010 ppm); BJD 2460692.3771: recovered, depth -1002 ± 668 ppm (catalogue 12010 ppm); BJD 2460695.0041: recovered, depth -1257 ± 694 ppm (catalogue 12010 ppm); BJD 2460697.6310: recovered, depth 2799 ± 687 ppm (catalogue 12010 ppm); BJD 2460700.2580: not recovered, depth 835 ± 654 ppm (catalogue 12010 ppm); BJD 2460702.8849: recovered, depth -77 ± 682 ppm (catalogue 12010 ppm); BJD 2460705.5119: recovered, depth 708 ± 710 ppm (catalogue 12010 ppm); BJD 2460708.1388: recovered, depth -470 ± 689 ppm (catalogue 12010 ppm); BJD 2460710.7658: partial, depth 1040 ± 694 ppm (catalogue 12010 ppm); BJD 2460713.3927: recovered, depth 577 ± 664 ppm (catalogue 12010 ppm); BJD 2460716.0197: partial, depth -2421 ± 710 ppm (catalogue 12010 ppm)).
Outside the catalogued epoch the screen left 2 threshold entries forming **1 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4218.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 142628514 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 118.791369 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -22.611009 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458514.633837 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.6269521 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 12010.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.503 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.7868 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | lightcurve | 61 | False | `eb37fb1d459f880c` | True |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | lightcurve | 88 | False | `8c1b957002ab6691` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 2459964.71140 | partial | 105 | 1975 ± 656 | 12010 | 1.22 |
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 2459967.33835 | partial | 105 | 4140 ± 626 | 12010 | 2.14 |
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 2459969.96530 | not_recovered | 105 | 3413 ± 609 | 12010 | — |
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 2459972.59225 | partial | 105 | 2273 ± 568 | 12010 | 2.28 |
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 2459975.21920 | not_recovered | 41 | 2147 ± 986 | 12010 | — |
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 2459977.84616 | not_recovered | 105 | 3762 ± 602 | 12010 | — |
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 2459980.47311 | not_recovered | 105 | 3122 ± 628 | 12010 | — |
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 2459983.10006 | not_recovered | 105 | 6097 ± 583 | 12010 | — |
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 2459985.72701 | not_recovered | 105 | 2288 ± 593 | 12010 | — |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460692.37713 | recovered | 105 | -1002 ± 668 | 12010 | 3.09 |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460695.00408 | recovered | 105 | -1257 ± 694 | 12010 | 2.81 |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460697.63103 | recovered | 106 | 2799 ± 687 | 12010 | 2.97 |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460700.25798 | not_recovered | 105 | 835 ± 654 | 12010 | — |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460702.88494 | recovered | 105 | -77 ± 682 | 12010 | 2.94 |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460705.51189 | recovered | 105 | 708 ± 710 | 12010 | 2.39 |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460708.13884 | recovered | 105 | -470 ± 689 | 12010 | 2.50 |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460710.76579 | partial | 105 | 1040 ± 694 | 12010 | 2.60 |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460713.39274 | recovered | 105 | 577 ± 664 | 12010 | 2.98 |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460716.01970 | partial | 105 | -2421 ± 710 | 12010 | 2.47 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023018032328-s0061-0000000142628514-0250-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025014115807-s0088-0000000142628514-0285-s_lc.fits` | 2460699.02688 | -0.01975 | 2 | PDCSAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-4218.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:56:07Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:56:10Z: TOI-4218.01 (TIC 142628514, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:56:12Z: Gaia DR3 5711409890611873408 (type ROT, P 5.3099 d)
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T21:56:14Z: TOI-4218.01 (Pl?); TOI-4218 (*); Gaia DR3 5711409890611873408 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459964.7114: partial, depth 1975 ± 656 ppm (catalogue 12010 ppm); BJD 2459967.3383: partial, depth 4140 ± 626 ppm (catalogue 12010 ppm); BJD 2459969.9653: not recovered, depth 3413 ± 609 ppm (catalogue 12010 ppm); BJD 2459972.5923: partial, depth 2273 ± 568 ppm (catalogue 12010 ppm); BJD 2459975.2192: not recovered, depth 2147 ± 986 ppm (catalogue 12010 ppm); BJD 2459977.8462: not recovered, depth 3762 ± 602 ppm (catalogue 12010 ppm); BJD 2459980.4731: not recovered, depth 3122 ± 628 ppm (catalogue 12010 ppm); BJD 2459983.1001: not recovered, depth 6097 ± 583 ppm (catalogue 12010 ppm); BJD 2459985.7270: not recovered, depth 2288 ± 593 ppm (catalogue 12010 ppm); BJD 2460692.3771: recovered, depth -1002 ± 668 ppm (catalogue 12010 ppm); BJD 2460695.0041: recovered, depth -1257 ± 694 ppm (catalogue 12010 ppm); BJD 2460697.6310: recovered, depth 2799 ± 687 ppm (catalogue 12010 ppm); BJD 2460700.2580: not recovered, depth 835 ± 654 ppm (catalogue 12010 ppm); BJD 2460702.8849: recovered, depth -77 ± 682 ppm (catalogue 12010 ppm); BJD 2460705.5119: recovered, depth 708 ± 710 ppm (catalogue 12010 ppm); BJD 2460708.1388: recovered, depth -470 ± 689 ppm (catalogue 12010 ppm); BJD 2460710.7658: partial, depth 1040 ± 694 ppm (catalogue 12010 ppm); BJD 2460713.3927: recovered, depth 577 ± 664 ppm (catalogue 12010 ppm); BJD 2460716.0197: partial, depth -2421 ± 710 ppm (catalogue 12010 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4218.01: Gaia DR3 5711409886308248320 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4218.01: Teff 6600 K, R* 1.61 ± 0.13, M* 1.46 ± 0.15, ρ* 0.35 ± 0.09 ρ☉ (dwarf sequence, M_G 2.91, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4218.01: 73 Gaia neighbour(s) within 52.5", contamination 72.53%; depth -1002 ppm (measured depth of the recovered catalogued transit); 25 could produce it if fully eclipsed (brightest 5711409890611883904, 21.2", ΔG 0.10); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-4218.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4218.01: TOI-4218 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4218-01.yaml
python -m cygnus.multi report campaigns/toi-4218-01.yaml
```
