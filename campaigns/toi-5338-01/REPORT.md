<!-- cygnus:generated-draft -->
# Known-object test, TOI-5338.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5338-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4722, calibrate_screen #4710, event_census #4717, fetch_independent #4720, fetch_products #4709, known_signal_recovery #4711, moving_objects #4719, period_aliases #4718, prior_art #4724, residual_screen #4716, stellar_context #4713, variability_guard #4723
- Runner finished (UTC): 2026-09-30T22:13:42Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the completeness below.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5338.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 467615239 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 78.172728 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 22.505924 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459522.34129 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.6429687 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 17800.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.184 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.1504 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-11-26 12:03:11 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

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

**TOI-5338.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:13:30Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:13:33Z: TOI-5338.01 (TIC 467615239, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:13:36Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:13:37Z: UCAC4 563-015155 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | not_tested | no products to analyse: none pinned and none found for the requested targets (TOI-5338.01: no SPOC 120-s light curve found at MAST for TIC 467615239.) |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | not_tested | no products to analyse: none pinned and none found for the requested targets (TOI-5338.01: no SPOC 120-s light curve found at MAST for TIC 467615239.) |
| Synthetic signal injection–recovery | not_tested | no products to analyse: none pinned and none found for the requested targets (TOI-5338.01: no SPOC 120-s light curve found at MAST for TIC 467615239.) |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5338.01: Gaia DR3 3415130158651368320 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5338.01: Teff 4765 K, R* 0.80 ± 0.06, M* 0.86 ± 0.09, ρ* 1.69 ± 0.44 ρ☉ (dwarf sequence, M_G 5.64, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5338.01: 21 Gaia neighbour(s) within 52.5", contamination 34.14%; depth 17800 ppm (catalogue depth); 4 could produce it if fully eclipsed (brightest 3415129948199684096, 35.3", ΔG 1.78); a centroid test is needed |
| Pointing and quality census per event | not_tested | no persistent screen event outside the veto |
| Moving objects at screen-event epochs | not_tested | no persistent screen event outside the veto |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-5338.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5338.01: UCAC4 563-015155 otype * (star_or_other) at 0.3" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5338-01.yaml
python -m cygnus.multi report campaigns/toi-5338-01.yaml
```
