<!-- cygnus:generated-draft -->
# Known-object test, TOI-2721.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2721-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4199, calibrate_screen #4176, event_census #4187, fetch_independent #4190, fetch_products #4171, known_signal_recovery #4179, moving_objects #4189, period_aliases #4188, prior_art #4201, residual_screen #4186, stellar_context #4180, variability_guard #4200
- Runner finished (UTC): 2026-09-30T21:42:11Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2721.01 (BJD 2460991.4832: gap (catalogue 12870 ppm); BJD 2460995.6460: not recovered, depth 8411 ± 1069 ppm (catalogue 12870 ppm); BJD 2460999.8087: recovered, depth 10627 ± 513 ppm (catalogue 12870 ppm); BJD 2461003.9714: gap (catalogue 12870 ppm); BJD 2461008.1342: recovered, depth 9298 ± 560 ppm (catalogue 12870 ppm); BJD 2461012.2969: recovered, depth 11097 ± 529 ppm (catalogue 12870 ppm); BJD 2461016.4596: recovered, depth 10723 ± 544 ppm (catalogue 12870 ppm); BJD 2461020.6224: gap (catalogue 12870 ppm); BJD 2461024.7851: recovered, depth 11646 ± 504 ppm (catalogue 12870 ppm); BJD 2461028.9478: recovered, depth 11333 ± 502 ppm (catalogue 12870 ppm); BJD 2461033.1106: gap (catalogue 12870 ppm); BJD 2461037.2733: recovered, depth 12301 ± 548 ppm (catalogue 12870 ppm); BJD 2461041.4360: recovered, depth 11936 ± 510 ppm (catalogue 12870 ppm); BJD 2461045.5988: recovered, depth 10776 ± 527 ppm (catalogue 12870 ppm)).
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2721.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 167714124 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 80.421253 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -38.656827 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459222.321706 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.162733 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 12870.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.319 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8482 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | lightcurve | 98 | False | `4930bce84b65ae74` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2460991.48323 | gap | 0 | — | 12870 | — |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2460995.64596 | not_recovered | 22 | 8411 ± 1069 | 12870 | — |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2460999.80870 | recovered | 100 | 10627 ± 513 | 12870 | -1.11 |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461003.97143 | gap | 0 | — | 12870 | — |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461008.13416 | recovered | 99 | 9298 ± 560 | 12870 | -0.62 |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461012.29690 | recovered | 99 | 11097 ± 529 | 12870 | 0.41 |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461016.45963 | recovered | 100 | 10723 ± 544 | 12870 | -0.19 |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461020.62236 | gap | 0 | — | 12870 | — |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461024.78509 | recovered | 100 | 11646 ± 504 | 12870 | -0.77 |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461028.94783 | recovered | 99 | 11333 ± 502 | 12870 | 0.31 |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461033.11056 | gap | 0 | — | 12870 | — |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461037.27329 | recovered | 97 | 12301 ± 548 | 12870 | -0.73 |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461041.43603 | recovered | 100 | 11936 ± 510 | 12870 | -0.52 |
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 2461045.59876 | recovered | 100 | 10776 ± 527 | 12870 | 0.48 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025312202959-s0098-0000000167714124-0298-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

None at the threshold used.

## Catalogue cross-match

**TOI-2721.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): 1 match(es) in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:42:04Z: NGTS-31 b (host NGTS-31)
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:42:06Z: TOI-2721.01 (TIC 167714124, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:42:08Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:42:10Z: NGTS-31 (*); NGTS-31b (Pl)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460991.4832: gap (catalogue 12870 ppm); BJD 2460995.6460: not recovered, depth 8411 ± 1069 ppm (catalogue 12870 ppm); BJD 2460999.8087: recovered, depth 10627 ± 513 ppm (catalogue 12870 ppm); BJD 2461003.9714: gap (catalogue 12870 ppm); BJD 2461008.1342: recovered, depth 9298 ± 560 ppm (catalogue 12870 ppm); BJD 2461012.2969: recovered, depth 11097 ± 529 ppm (catalogue 12870 ppm); BJD 2461016.4596: recovered, depth 10723 ± 544 ppm (catalogue 12870 ppm); BJD 2461020.6224: gap (catalogue 12870 ppm); BJD 2461024.7851: recovered, depth 11646 ± 504 ppm (catalogue 12870 ppm); BJD 2461028.9478: recovered, depth 11333 ± 502 ppm (catalogue 12870 ppm); BJD 2461033.1106: gap (catalogue 12870 ppm); BJD 2461037.2733: recovered, depth 12301 ± 548 ppm (catalogue 12870 ppm); BJD 2461041.4360: recovered, depth 11936 ± 510 ppm (catalogue 12870 ppm); BJD 2461045.5988: recovered, depth 10776 ± 527 ppm (catalogue 12870 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2721.01: Gaia DR3 4819647205326045824 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-2721.01: dwarf priors not applied — RUWE 6.8341603 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2721.01: 3 Gaia neighbour(s) within 52.5", contamination 2.44%; depth 10627 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 4819647170965723904, 46.0", ΔG 4.18); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-2721.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2721.01: NGTS-31 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2721-01.yaml
python -m cygnus.multi report campaigns/toi-2721-01.yaml
```
