<!-- cygnus:generated-draft -->
# Known-object test, TOI-7119.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-7119-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4669, calibrate_screen #4651, event_census #4655, fetch_independent #4659, fetch_products #4644, known_signal_recovery #4652, moving_objects #4657, period_aliases #4656, prior_art #4671, residual_screen #4654, stellar_context #4653, variability_guard #4670
- Runner finished (UTC): 2026-09-30T22:09:48Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-7119.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 420383981 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 344.8819 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 54.888207 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460422.161169 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.5933417 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 9482.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.253 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.2118 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-09-01 12:03:47 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

None at the threshold used.

## Catalogue cross-match

**TOI-7119.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:09:34Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:09:37Z: TOI-7119.01 (TIC 420383981, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:09:40Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:09:43Z: UCAC4 725-099344 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | not_tested | no products to analyse: none pinned and none found for the requested targets (TOI-7119.01: no SPOC 120-s light curve found at MAST for TIC 420383981.) |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | not_tested | no products to analyse: none pinned and none found for the requested targets (TOI-7119.01: no SPOC 120-s light curve found at MAST for TIC 420383981.) |
| Synthetic signal injection–recovery | not_tested | no products to analyse: none pinned and none found for the requested targets (TOI-7119.01: no SPOC 120-s light curve found at MAST for TIC 420383981.) |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-7119.01: Gaia DR3 2008680651581632128 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-7119.01: dwarf priors not applied — RUWE 9.983156 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-7119.01: 61 Gaia neighbour(s) within 52.5", contamination 44.31%; depth 9482 ppm (catalogue depth); 9 could produce it if fully eclipsed (brightest 2008680651581630976, 31.4", ΔG 1.49); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-7119.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-7119.01: UCAC4 725-099344 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-7119-01.yaml
python -m cygnus.multi report campaigns/toi-7119-01.yaml
```
