<!-- cygnus:generated-draft -->
# Known-object test, TOI-6326.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6326-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4160, calibrate_screen #4145, event_census #4154, fetch_independent #4158, fetch_products #4143, known_signal_recovery #4148, moving_objects #4157, period_aliases #4156, prior_art #4164, residual_screen #4151, stellar_context #4149, variability_guard #4161
- Runner finished (UTC): 2026-09-30T21:40:43Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6326.01 (BJD 2460611.9086: gap (catalogue 9377 ppm); BJD 2460614.2643: gap (catalogue 9377 ppm); BJD 2460616.6200: recovered, depth 10028 ± 570 ppm (catalogue 9377 ppm); BJD 2460618.9756: recovered, depth 11124 ± 405 ppm (catalogue 9377 ppm); BJD 2460621.3313: partial, depth 9425 ± 384 ppm (catalogue 9377 ppm); BJD 2460623.6870: recovered, depth 7714 ± 384 ppm (catalogue 9377 ppm); BJD 2460626.0427: gap (catalogue 9377 ppm); BJD 2460628.3983: gap (catalogue 9377 ppm); BJD 2460630.7540: not recovered, depth 7971 ± 450 ppm (catalogue 9377 ppm); BJD 2460633.1097: recovered, depth 10673 ± 374 ppm (catalogue 9377 ppm); BJD 2460635.4654: recovered, depth 11584 ± 423 ppm (catalogue 9377 ppm)).
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6326.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 307201632 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 14.976875 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 49.034174 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459907.561815 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.3556749 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 9377.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.351 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.1684 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-09-19 12:04:41 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | lightcurve | 85 | False | `775f8228d0ec7fbc` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460611.90861 | gap | 0 | — | 9377 | — |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460614.26429 | gap | 0 | — | 9377 | — |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460616.61996 | recovered | 66 | 10028 ± 570 | 9377 | 0.41 |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460618.97563 | recovered | 100 | 11124 ± 405 | 9377 | 0.77 |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460621.33131 | partial | 100 | 9425 ± 384 | 9377 | 0.72 |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460623.68698 | recovered | 100 | 7714 ± 384 | 9377 | 0.36 |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460626.04266 | gap | 0 | — | 9377 | — |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460628.39833 | gap | 0 | — | 9377 | — |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460630.75401 | not_recovered | 101 | 7971 ± 450 | 9377 | — |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460633.10968 | recovered | 101 | 10673 ± 374 | 9377 | 0.88 |
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 2460635.46536 | recovered | 100 | 11584 ± 423 | 9377 | 0.62 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024300212641-s0085-0000000307201632-0282-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

None at the threshold used.

## Catalogue cross-match

**TOI-6326.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:40:36Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:40:38Z: TOI-6326.01 (TIC 307201632, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:40:40Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T21:40:41Z: TYC 3271-1102-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460611.9086: gap (catalogue 9377 ppm); BJD 2460614.2643: gap (catalogue 9377 ppm); BJD 2460616.6200: recovered, depth 10028 ± 570 ppm (catalogue 9377 ppm); BJD 2460618.9756: recovered, depth 11124 ± 405 ppm (catalogue 9377 ppm); BJD 2460621.3313: partial, depth 9425 ± 384 ppm (catalogue 9377 ppm); BJD 2460623.6870: recovered, depth 7714 ± 384 ppm (catalogue 9377 ppm); BJD 2460626.0427: gap (catalogue 9377 ppm); BJD 2460628.3983: gap (catalogue 9377 ppm); BJD 2460630.7540: not recovered, depth 7971 ± 450 ppm (catalogue 9377 ppm); BJD 2460633.1097: recovered, depth 10673 ± 374 ppm (catalogue 9377 ppm); BJD 2460635.4654: recovered, depth 11584 ± 423 ppm (catalogue 9377 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6326.01: Gaia DR3 402607451188257152 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6326.01: Teff 6339 K, R* 1.59 ± 0.13, M* 1.44 ± 0.14, ρ* 0.36 ± 0.09 ρ☉ (dwarf sequence, M_G 2.97, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6326.01: 14 Gaia neighbour(s) within 52.5", contamination 31.86%; depth 10028 ppm (measured depth of the recovered catalogued transit); 5 could produce it if fully eclipsed (brightest 402607451188487168, 17.2", ΔG 1.98); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-6326.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6326.01: TYC 3271-1102-1 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6326-01.yaml
python -m cygnus.multi report campaigns/toi-6326-01.yaml
```
