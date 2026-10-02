<!-- cygnus:generated-draft -->
# Known-object test, TOI-4238.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4238-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4234, calibrate_screen #4210, event_census #4219, fetch_independent #4222, fetch_products #4203, known_signal_recovery #4211, moving_objects #4221, period_aliases #4220, prior_art #4237, residual_screen #4218, stellar_context #4212, variability_guard #4235
- Runner finished (UTC): 2026-09-30T21:43:09Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4238.01 (BJD 2461046.1460: recovered, depth 20576 ± 1386 ppm (catalogue 23100 ppm); BJD 2461047.4192: recovered, depth 20832 ± 1312 ppm (catalogue 23100 ppm); BJD 2461048.6925: recovered, depth 16995 ± 1328 ppm (catalogue 23100 ppm); BJD 2461049.9657: recovered, depth 19366 ± 1298 ppm (catalogue 23100 ppm); BJD 2461051.2389: recovered, depth 18214 ± 1269 ppm (catalogue 23100 ppm); BJD 2461052.5121: recovered, depth 20596 ± 1364 ppm (catalogue 23100 ppm); BJD 2461053.7854: recovered, depth 20788 ± 1271 ppm (catalogue 23100 ppm); BJD 2461055.0586: recovered, depth 14170 ± 1306 ppm (catalogue 23100 ppm); BJD 2461056.3318: gap (catalogue 23100 ppm); BJD 2461057.6050: gap (catalogue 23100 ppm); BJD 2461058.8783: gap (catalogue 23100 ppm); BJD 2461060.1515: gap (catalogue 23100 ppm); BJD 2461061.4247: gap (catalogue 23100 ppm); BJD 2461062.6979: gap (catalogue 23100 ppm); BJD 2461063.9712: recovered, depth 16422 ± 1287 ppm (catalogue 23100 ppm); BJD 2461065.2444: recovered, depth 18925 ± 1284 ppm (catalogue 23100 ppm); BJD 2461066.5176: recovered, depth 17001 ± 1260 ppm (catalogue 23100 ppm); BJD 2461067.7908: recovered, depth 16909 ± 1241 ppm (catalogue 23100 ppm); BJD 2461069.0641: recovered, depth 22215 ± 1283 ppm (catalogue 23100 ppm); BJD 2461070.3373: recovered, depth 17925 ± 1374 ppm (catalogue 23100 ppm); BJD 2461071.6105: gap (catalogue 23100 ppm); BJD 2461072.8837: gap (catalogue 23100 ppm)).
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4238.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 24615998 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 141.395946 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -33.229454 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459277.637194 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 1.2732245 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 23100.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.634 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.3502 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | lightcurve | 99 | False | `072512d8c4e7ddb6` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461046.14602 | recovered | 46 | 20576 ± 1386 | 23100 | 0.36 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461047.41925 | recovered | 49 | 20832 ± 1312 | 23100 | 0.05 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461048.69247 | recovered | 49 | 16995 ± 1328 | 23100 | 0.35 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461049.96570 | recovered | 49 | 19366 ± 1298 | 23100 | 0.04 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461051.23892 | recovered | 49 | 18214 ± 1269 | 23100 | 0.36 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461052.51215 | recovered | 49 | 20596 ± 1364 | 23100 | 0.21 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461053.78537 | recovered | 49 | 20788 ± 1271 | 23100 | 0.14 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461055.05860 | recovered | 49 | 14170 ± 1306 | 23100 | 0.22 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461056.33182 | gap | 0 | — | 23100 | — |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461057.60505 | gap | 0 | — | 23100 | — |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461058.87827 | gap | 0 | — | 23100 | — |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461060.15149 | gap | 0 | — | 23100 | — |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461061.42472 | gap | 0 | — | 23100 | — |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461062.69794 | gap | 0 | — | 23100 | — |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461063.97117 | recovered | 49 | 16422 ± 1287 | 23100 | 0.49 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461065.24439 | recovered | 49 | 18925 ± 1284 | 23100 | 0.37 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461066.51762 | recovered | 49 | 17001 ± 1260 | 23100 | 0.15 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461067.79084 | recovered | 49 | 16909 ± 1241 | 23100 | 0.18 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461069.06407 | recovered | 49 | 22215 ± 1283 | 23100 | 0.23 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461070.33729 | recovered | 49 | 17925 ± 1374 | 23100 | 0.33 |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461071.61051 | gap | 0 | — | 23100 | — |
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2461072.88374 | gap | 0 | — | 23100 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2026005125623-s0099-0000000024615998-0300-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: 20000, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

None at the threshold used.

## Catalogue cross-match

**TOI-4238.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:43:03Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:43:05Z: TOI-4238.01 (TIC 24615998, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:43:07Z: Gaia DR3 5630351350788316672 (type ROT, P 11.5891 d)
- SIMBAD (done, 2026-09-30): 3 match(es) in SIMBAD within 30" as of 2026-09-30T21:43:08Z: UCAC4 284-051487 (*); TOI-4238 (*); TOI-4238.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2461046.1460: recovered, depth 20576 ± 1386 ppm (catalogue 23100 ppm); BJD 2461047.4192: recovered, depth 20832 ± 1312 ppm (catalogue 23100 ppm); BJD 2461048.6925: recovered, depth 16995 ± 1328 ppm (catalogue 23100 ppm); BJD 2461049.9657: recovered, depth 19366 ± 1298 ppm (catalogue 23100 ppm); BJD 2461051.2389: recovered, depth 18214 ± 1269 ppm (catalogue 23100 ppm); BJD 2461052.5121: recovered, depth 20596 ± 1364 ppm (catalogue 23100 ppm); BJD 2461053.7854: recovered, depth 20788 ± 1271 ppm (catalogue 23100 ppm); BJD 2461055.0586: recovered, depth 14170 ± 1306 ppm (catalogue 23100 ppm); BJD 2461056.3318: gap (catalogue 23100 ppm); BJD 2461057.6050: gap (catalogue 23100 ppm); BJD 2461058.8783: gap (catalogue 23100 ppm); BJD 2461060.1515: gap (catalogue 23100 ppm); BJD 2461061.4247: gap (catalogue 23100 ppm); BJD 2461062.6979: gap (catalogue 23100 ppm); BJD 2461063.9712: recovered, depth 16422 ± 1287 ppm (catalogue 23100 ppm); BJD 2461065.2444: recovered, depth 18925 ± 1284 ppm (catalogue 23100 ppm); BJD 2461066.5176: recovered, depth 17001 ± 1260 ppm (catalogue 23100 ppm); BJD 2461067.7908: recovered, depth 16909 ± 1241 ppm (catalogue 23100 ppm); BJD 2461069.0641: recovered, depth 22215 ± 1283 ppm (catalogue 23100 ppm); BJD 2461070.3373: recovered, depth 17925 ± 1374 ppm (catalogue 23100 ppm); BJD 2461071.6105: gap (catalogue 23100 ppm); BJD 2461072.8837: gap (catalogue 23100 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4238.01: Gaia DR3 5630351350788316672 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-4238.01: dwarf priors not applied — RUWE 2.4106998 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4238.01: 25 Gaia neighbour(s) within 52.5", contamination 55.30%; depth 20576 ppm (measured depth of the recovered catalogued transit); 5 could produce it if fully eclipsed (brightest 5630351350788319360, 10.1", ΔG 0.76); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-4238.01: Gaia DR3 5630351350788316672   ROT                            P=11.5891 at 0.2" |
| Object-class guard (SIMBAD) | passed | TOI-4238.01: TOI-4238 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4238-01.yaml
python -m cygnus.multi report campaigns/toi-4238-01.yaml
```
