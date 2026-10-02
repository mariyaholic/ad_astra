<!-- cygnus:generated-draft -->
# Known-object test, TOI-3246.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3246-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4138, calibrate_screen #4126, event_census #4130, fetch_independent #4133, fetch_products #4123, known_signal_recovery #4127, moving_objects #4132, period_aliases #4131, prior_art #4140, residual_screen #4129, stellar_context #4128, variability_guard #4139
- Runner finished (UTC): 2026-09-30T21:39:44Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3246.01 (BJD 2461127.3185: gap (catalogue 10910 ppm); BJD 2461131.6382: not recovered, depth 8187 ± 421 ppm (catalogue 10910 ppm); BJD 2461135.9580: recovered, depth 8697 ± 427 ppm (catalogue 10910 ppm); BJD 2461140.2777: gap (catalogue 10910 ppm); BJD 2461144.5975: not recovered, depth 8284 ± 443 ppm (catalogue 10910 ppm); BJD 2461148.9172: partial, depth 8777 ± 419 ppm (catalogue 10910 ppm)).
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3246.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 179715231 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 213.538657 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -37.558384 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459351.899577 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.319754 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10910.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.78 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.2936 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000179715231-0304-s_lc.fits` | lightcurve | 102 | False | `68272538553038b6` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2026086090000-s0102-0000000179715231-0304-s_lc.fits` | 2461127.31847 | gap | 0 | — | 10910 | — |
| `tess2026086090000-s0102-0000000179715231-0304-s_lc.fits` | 2461131.63823 | not_recovered | 84 | 8187 ± 421 | 10910 | — |
| `tess2026086090000-s0102-0000000179715231-0304-s_lc.fits` | 2461135.95798 | recovered | 84 | 8697 ± 427 | 10910 | 0.61 |
| `tess2026086090000-s0102-0000000179715231-0304-s_lc.fits` | 2461140.27773 | gap | 0 | — | 10910 | — |
| `tess2026086090000-s0102-0000000179715231-0304-s_lc.fits` | 2461144.59749 | not_recovered | 83 | 8284 ± 443 | 10910 | — |
| `tess2026086090000-s0102-0000000179715231-0304-s_lc.fits` | 2461148.91724 | partial | 83 | 8777 ± 419 | 10910 | -0.42 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2026086090000-s0102-0000000179715231-0304-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

None at the threshold used.

## Catalogue cross-match

**TOI-3246.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:39:35Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:39:38Z: TOI-3246.01 (TIC 179715231, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:39:40Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:39:42Z: TOI-3246.01 (Pl?); TOI-3246 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2461127.3185: gap (catalogue 10910 ppm); BJD 2461131.6382: not recovered, depth 8187 ± 421 ppm (catalogue 10910 ppm); BJD 2461135.9580: recovered, depth 8697 ± 427 ppm (catalogue 10910 ppm); BJD 2461140.2777: gap (catalogue 10910 ppm); BJD 2461144.5975: not recovered, depth 8284 ± 443 ppm (catalogue 10910 ppm); BJD 2461148.9172: partial, depth 8777 ± 419 ppm (catalogue 10910 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3246.01: Gaia DR3 6117705344316886016 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3246.01: Teff 5610 K, R* 1.11 ± 0.09, M* 1.06 ± 0.11, ρ* 0.78 ± 0.20 ρ☉ (dwarf sequence, M_G 4.30, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3246.01: 12 Gaia neighbour(s) within 52.5", contamination 21.26%; depth 8697 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 6117705344316885888, 11.8", ΔG 1.71); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3246.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3246.01: TOI-3246 otype * (star_or_other) at 0.3" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3246-01.yaml
python -m cygnus.multi report campaigns/toi-3246-01.yaml
```
