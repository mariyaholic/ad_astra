<!-- cygnus:generated-draft -->
# Known-object test, TOI-4776.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4776-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4743, calibrate_screen #4725, event_census #4731, fetch_independent #4734, fetch_products #4721, known_signal_recovery #4727, moving_objects #4733, period_aliases #4732, prior_art #4748, residual_screen #4730, stellar_context #4729, variability_guard #4746
- Runner finished (UTC): 2026-09-30T22:15:35Z

## Bottom line

Positive control **failed**: BJD 2459964.5232: not recovered, depth 5570 ± 712 ppm (catalogue 6720 ppm); BJD 2459974.9370: not recovered, depth 4446 ± 686 ppm (catalogue 6720 ppm); BJD 2459985.3508: not recovered, depth 7559 ± 652 ppm (catalogue 6720 ppm).
Outside the catalogued epoch the screen left 16 threshold entries forming **7 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4776.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 196286578 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 125.554446 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -25.067535 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459245.97102 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 10.4137997 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6720.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.774 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.6309 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | lightcurve | 61 | False | `a7ac5de32510cdf5` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459964.52320 | not_recovered | 114 | 5570 ± 712 | 6720 | — |
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459974.93700 | not_recovered | 113 | 4446 ± 686 | 6720 | — |
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459985.35080 | not_recovered | 113 | 7559 ± 652 | 6720 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459963.94831 | -0.04028 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459963.96706 | -0.03413 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459963.97193 | -0.03404 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459963.98165 | -0.03111 | 2 | PDCSAP | 3 | no |
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459963.96220 | -0.02943 | 2 | PDCSAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459963.98581 | -0.02934 | 3 | PDCSAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 2459963.95526 | -0.02882 | 2 | PDCSAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-4776.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:15:20Z
- TESS_TOI (done, 2026-09-30): 2 match(es) in TESS_TOI within 30" as of 2026-09-30T22:15:24Z: TOI-592.01 (TIC 196286587, disposition FP); TOI-4776.01 (TIC 196286578, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:15:28Z
- SIMBAD (done, 2026-09-30): 7 match(es) in SIMBAD within 30" as of 2026-09-30T22:15:30Z: TOI-592.01 (err); Gaia DR3 5695996352497665024 (*); 2MASS J08221320-2503557 (*); ** TOI 4776B (BD*); PSO J125.5533-25.0675 (*); TOI-4776 (*); TOI-592 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2459964.5232: not recovered, depth 5570 ± 712 ppm (catalogue 6720 ppm); BJD 2459974.9370: not recovered, depth 4446 ± 686 ppm (catalogue 6720 ppm); BJD 2459985.3508: not recovered, depth 7559 ± 652 ppm (catalogue 6720 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4776.01: Gaia DR3 5695996348197148032 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4776.01: Teff 6018 K, R* 1.15 ± 0.09, M* 1.10 ± 0.11, ρ* 0.72 ± 0.19 ρ☉ (dwarf sequence, M_G 4.15, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4776.01: 35 Gaia neighbour(s) within 52.5", contamination 80.48%; depth 6720 ppm (catalogue depth); 2 could produce it if fully eclipsed (brightest 5695996352497664512, 11.3", ΔG -1.48); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-4776.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4776.01: TOI-4776 otype * (star_or_other) at 0.5" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4776-01.yaml
python -m cygnus.multi report campaigns/toi-4776-01.yaml
```
