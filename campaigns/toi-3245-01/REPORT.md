<!-- cygnus:generated-draft -->
# Known-object test, TOI-3245.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3245-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4976, calibrate_screen #4967, event_census #4971, fetch_independent #4974, fetch_products #4963, known_signal_recovery #4968, moving_objects #4973, period_aliases #4972, prior_art #4978, residual_screen #4970, stellar_context #4969, variability_guard #4977
- Runner finished (UTC): 2026-09-30T22:45:59Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3245.01 (BJD 2460777.5384: recovered, depth 9887 ± 459 ppm (catalogue 10130 ppm); BJD 2460780.4361: recovered, depth 11287 ± 510 ppm (catalogue 10130 ppm); BJD 2460783.3338: gap (catalogue 10130 ppm); BJD 2460786.2315: gap (catalogue 10130 ppm); BJD 2460789.1292: recovered, depth 7952 ± 508 ppm (catalogue 10130 ppm); BJD 2460792.0269: recovered, depth 9340 ± 435 ppm (catalogue 10130 ppm); BJD 2460794.9246: recovered, depth 9640 ± 497 ppm (catalogue 10130 ppm); BJD 2460797.8223: not recovered, depth -491 ± 952 ppm (catalogue 10130 ppm); BJD 2460800.7200: gap (catalogue 10130 ppm)).
Outside the catalogued epoch the screen left 9 threshold entries forming **2 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3245.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 203476998 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 217.801851 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -23.054805 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459354.766143 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 2.8977031 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10130.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.148 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.6561 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | lightcurve | 91 | False | `0ab3073df722ef5b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460777.53837 | recovered | 125 | 9887 ± 459 | 10130 | -0.05 |
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460780.43607 | recovered | 125 | 11287 ± 510 | 10130 | 0.48 |
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460783.33377 | gap | 0 | — | 10130 | — |
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460786.23147 | gap | 0 | — | 10130 | — |
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460789.12918 | recovered | 125 | 7952 ± 508 | 10130 | -0.42 |
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460792.02688 | recovered | 124 | 9340 ± 435 | 10130 | 0.85 |
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460794.92458 | recovered | 124 | 9640 ± 497 | 10130 | -1.11 |
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460797.82229 | not_recovered | 46 | -491 ± 952 | 10130 | — |
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460800.71999 | gap | 0 | — | 10130 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460780.95873 | -0.01880 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025099153000-s0091-0000000203476998-0288-s_lc.fits` | 2460780.87956 | -0.01553 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-3245.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:45:48Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:45:51Z: TOI-3245.01 (TIC 203476998, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:45:53Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:45:55Z: TOI-3245 (*); TOI-3245.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460777.5384: recovered, depth 9887 ± 459 ppm (catalogue 10130 ppm); BJD 2460780.4361: recovered, depth 11287 ± 510 ppm (catalogue 10130 ppm); BJD 2460783.3338: gap (catalogue 10130 ppm); BJD 2460786.2315: gap (catalogue 10130 ppm); BJD 2460789.1292: recovered, depth 7952 ± 508 ppm (catalogue 10130 ppm); BJD 2460792.0269: recovered, depth 9340 ± 435 ppm (catalogue 10130 ppm); BJD 2460794.9246: recovered, depth 9640 ± 497 ppm (catalogue 10130 ppm); BJD 2460797.8223: not recovered, depth -491 ± 952 ppm (catalogue 10130 ppm); BJD 2460800.7200: gap (catalogue 10130 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3245.01: Gaia DR3 6279163060571364224 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3245.01: dwarf priors not applied — RUWE 1.4671751 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3245.01: 11 Gaia neighbour(s) within 52.5", contamination 9.80%; depth 9887 ppm (measured depth of the recovered catalogued transit); 3 could produce it if fully eclipsed (brightest 6279163060570823040, 36.2", ΔG 3.17); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2460780.9587 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR2 z=+6.1, POS_CORR1 z=+5.5, POS_CORR2 z=+11.4, SAP_BKG z=+56.5 |
| Moving objects at screen-event epochs | passed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-3245.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3245.01: TOI-3245 otype * (star_or_other) at 0.1" |
| Event-time prior art | not_tested | no repeat events to compare |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3245-01.yaml
python -m cygnus.multi report campaigns/toi-3245-01.yaml
```
