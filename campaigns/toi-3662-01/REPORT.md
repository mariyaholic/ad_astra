<!-- cygnus:generated-draft -->
# Known-object test, TOI-3662.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3662-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4240, calibrate_screen #4224, event_census #4228, fetch_independent #4236, fetch_products #4217, known_signal_recovery #4225, moving_objects #4230, period_aliases #4229, prior_art #4243, residual_screen #4227, stellar_context #4226, variability_guard #4241
- Runner finished (UTC): 2026-09-30T21:43:38Z

## Bottom line

Positive control **failed**: BJD 2460642.0321: not recovered, depth 552 ± 450 ppm (catalogue 4620 ppm); BJD 2460652.0229: gap (catalogue 4620 ppm); BJD 2460662.0137: not recovered, depth -196 ± 157 ppm (catalogue 4620 ppm).
Outside the catalogued epoch the screen left 64 threshold entries forming **18 distinct event(s)**, **7 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3662.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 65446983 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 54.405622 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 46.84287 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458813.713584 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 9.9908116 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 4620.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.566 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.7043 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | lightcurve | 86 | False | `2627fa531a218097` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460642.03211 | not_recovered | 14 | 552 ± 450 | 4620 | — |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460652.02292 | gap | 0 | — | 4620 | — |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460662.01373 | not_recovered | 107 | -196 ± 157 | 4620 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460661.22670 | -0.00627 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460661.18017 | -0.00590 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460661.16629 | -0.00545 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460661.14337 | -0.00539 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460661.15795 | -0.00538 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460661.14962 | -0.00532 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460661.13434 | -0.00523 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460641.15345 | -0.00859 | 3 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460641.21109 | -0.00636 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460649.08325 | -0.00612 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460641.23470 | -0.00607 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460649.36519 | -0.00593 | 2 | SAP | 1, 2, 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460649.35130 | -0.00583 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460649.42074 | -0.00551 | 2 | SAP | 2, 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460641.22775 | -0.00540 | 4 | PDCSAP | 1, 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460641.55414 | -0.00528 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460649.14436 | -0.00507 | 2 | SAP | 3 | no |
| `tess2024326142117-s0086-0000000065446983-0283-s_lc.fits` | 2460641.26109 | -0.00502 | 2 | PDCSAP | 1, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3662.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:43:31Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:43:33Z: TOI-3662.01 (TIC 65446983, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:43:35Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:43:36Z: TOI-3662.01 (Pl?); Cl Melotte   20  1237 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2460642.0321: not recovered, depth 552 ± 450 ppm (catalogue 4620 ppm); BJD 2460652.0229: gap (catalogue 4620 ppm); BJD 2460662.0137: not recovered, depth -196 ± 157 ppm (catalogue 4620 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3662.01: Gaia DR3 248127411812876160 at 0.02" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3662.01: dwarf priors not applied — parallax/error 4.2 < 5; RUWE 25.239485 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3662.01: 27 Gaia neighbour(s) within 52.5", contamination 8.60%; depth 4620 ppm (catalogue depth); 4 could produce it if fully eclipsed (brightest 248127446175392128, 33.5", ΔG 3.51); a centroid test is needed |
| Pointing and quality census per event | passed | 7 persistent event(s), 7 clean; no artifact quality bit within ±0.25 d and no centroid, pointing or background shift beyond 5σ |
| Moving objects at screen-event epochs | inconclusive | 7 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3662.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3662.01: Cl Melotte   20  1237 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3662-01.yaml
python -m cygnus.multi report campaigns/toi-3662-01.yaml
```
