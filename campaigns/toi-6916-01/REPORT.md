<!-- cygnus:generated-draft -->
# Known-object test, TOI-6916.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6916-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4464, calibrate_screen #4449, event_census #4455, fetch_independent #4458, fetch_products #4443, known_signal_recovery #4450, moving_objects #4457, period_aliases #4456, prior_art #4469, residual_screen #4454, stellar_context #4451, variability_guard #4467
- Runner finished (UTC): 2026-09-30T21:54:19Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6916.01 (BJD 2460663.2082: gap (catalogue 12003 ppm); BJD 2460667.1237: recovered, depth 12228 ± 651 ppm (catalogue 12003 ppm); BJD 2460671.0393: not recovered, depth 9088 ± 593 ppm (catalogue 12003 ppm); BJD 2460674.9548: recovered, depth 11627 ± 599 ppm (catalogue 12003 ppm); BJD 2460678.8704: gap (catalogue 12003 ppm); BJD 2460682.7859: not recovered, depth 10808 ± 625 ppm (catalogue 12003 ppm); BJD 2460686.7015: recovered, depth 10637 ± 613 ppm (catalogue 12003 ppm)).
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6916.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 264159776 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 108.382077 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 9.639457 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459222.28434 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 3.9155539 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 12003.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.72 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8463 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-02-02 12:03:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | lightcurve | 87 | False | `4b5634fe4df22007` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | 2460663.20818 | gap | 0 | — | 12003 | — |
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | 2460667.12373 | recovered | 112 | 12228 ± 651 | 12003 | -0.03 |
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | 2460671.03928 | not_recovered | 112 | 9088 ± 593 | 12003 | — |
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | 2460674.95484 | recovered | 112 | 11627 ± 599 | 12003 | -0.44 |
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | 2460678.87039 | gap | 0 | — | 12003 | — |
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | 2460682.78594 | not_recovered | 110 | 10808 ± 625 | 12003 | — |
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | 2460686.70150 | recovered | 112 | 10637 ± 613 | 12003 | 0.24 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024353092137-s0087-0000000264159776-0284-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

None at the threshold used.

## Catalogue cross-match

**TOI-6916.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:54:09Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:54:12Z: TOI-6916.01 (TIC 264159776, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:54:15Z: Gaia DR3 3156132395070341632 (type DSCT|GDOR|SXPHE, P — d)
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T21:54:17Z: UCAC4 499-040295 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460663.2082: gap (catalogue 12003 ppm); BJD 2460667.1237: recovered, depth 12228 ± 651 ppm (catalogue 12003 ppm); BJD 2460671.0393: not recovered, depth 9088 ± 593 ppm (catalogue 12003 ppm); BJD 2460674.9548: recovered, depth 11627 ± 599 ppm (catalogue 12003 ppm); BJD 2460678.8704: gap (catalogue 12003 ppm); BJD 2460682.7859: not recovered, depth 10808 ± 625 ppm (catalogue 12003 ppm); BJD 2460686.7015: recovered, depth 10637 ± 613 ppm (catalogue 12003 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6916.01: Gaia DR3 3156132395070341632 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6916.01: Teff 6156 K, R* 1.45 ± 0.12, M* 1.32 ± 0.13, ρ* 0.43 ± 0.11 ρ☉ (dwarf sequence, M_G 3.31, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6916.01: 25 Gaia neighbour(s) within 52.5", contamination 45.21%; depth 12228 ppm (measured depth of the recovered catalogued transit); 5 could produce it if fully eclipsed (brightest 3156132635588509568, 39.5", ΔG 1.13); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6916.01: Gaia DR3 3156132395070341632   DSCT/GDOR/SXPHE                P=None at 0.3" |
| Object-class guard (SIMBAD) | passed | TOI-6916.01: UCAC4 499-040295 otype * (star_or_other) at 0.2" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6916-01.yaml
python -m cygnus.multi report campaigns/toi-6916-01.yaml
```
