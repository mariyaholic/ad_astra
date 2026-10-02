<!-- cygnus:generated-draft -->
# Known-object test, TOI-5832.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5832-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5165, calibrate_screen #5143, event_census #5149, fetch_independent #5152, fetch_products #5136, known_signal_recovery #5144, moving_objects #5151, period_aliases #5150, prior_art #5175, residual_screen #5148, stellar_context #5145, variability_guard #5169
- Runner finished (UTC): 2026-09-30T23:05:17Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5832.01 (BJD 2460509.3477: not recovered, depth 10825 ± 601 ppm (catalogue 11560 ppm); BJD 2460514.4834: gap (catalogue 11560 ppm); BJD 2460519.6192: gap (catalogue 11560 ppm); BJD 2460524.7549: recovered, depth 11036 ± 583 ppm (catalogue 11560 ppm); BJD 2460529.8907: recovered, depth 9234 ± 616 ppm (catalogue 11560 ppm)).
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5832.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 287934343 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 300.997003 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 21.216507 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459795.478353 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.1357505 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 11560.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.504 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.776 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-09-03 12:05:55 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000287934343-0276-s_lc.fits` | lightcurve | 81 | False | `7b275028cc6a539e` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000287934343-0276-s_lc.fits` | 2460509.34767 | not_recovered | 105 | 10825 ± 601 | 11560 | — |
| `tess2024196212429-s0081-0000000287934343-0276-s_lc.fits` | 2460514.48342 | gap | 0 | — | 11560 | — |
| `tess2024196212429-s0081-0000000287934343-0276-s_lc.fits` | 2460519.61917 | gap | 0 | — | 11560 | — |
| `tess2024196212429-s0081-0000000287934343-0276-s_lc.fits` | 2460524.75492 | recovered | 106 | 11036 ± 583 | 11560 | -1.33 |
| `tess2024196212429-s0081-0000000287934343-0276-s_lc.fits` | 2460529.89067 | recovered | 105 | 9234 ± 616 | 11560 | 0.31 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024196212429-s0081-0000000287934343-0276-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

None at the threshold used.

## Catalogue cross-match

**TOI-5832.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T23:05:07Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T23:05:10Z: TOI-5832.01 (TIC 287934343, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T23:05:13Z: ZTF J200400.70+211248.2 (type RS, P 0.2530545 d)
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T23:05:15Z: UCAC4 557-105354 (*); ZTF J200400.70+211248.2 (RS*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460509.3477: not recovered, depth 10825 ± 601 ppm (catalogue 11560 ppm); BJD 2460514.4834: gap (catalogue 11560 ppm); BJD 2460519.6192: gap (catalogue 11560 ppm); BJD 2460524.7549: recovered, depth 11036 ± 583 ppm (catalogue 11560 ppm); BJD 2460529.8907: recovered, depth 9234 ± 616 ppm (catalogue 11560 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5832.01: Gaia DR3 1823847008894119680 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5832.01: Teff 5865 K, R* 1.19 ± 0.10, M* 1.15 ± 0.11, ρ* 0.69 ± 0.18 ρ☉ (dwarf sequence, M_G 4.03, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5832.01: 163 Gaia neighbour(s) within 52.5", contamination 69.87%; depth 11036 ppm (measured depth of the recovered catalogued transit); 12 could produce it if fully eclipsed (brightest 1823846940174633472, 26.3", ΔG 1.62); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5832.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5832.01: UCAC4 557-105354 otype * (star_or_other) at 0.2" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5832-01.yaml
python -m cygnus.multi report campaigns/toi-5832-01.yaml
```
