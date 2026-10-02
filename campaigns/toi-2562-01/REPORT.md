<!-- cygnus:generated-draft -->
# Known-object test, TOI-2562.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2562-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4614, calibrate_screen #4588, event_census #4603, fetch_independent #4607, fetch_products #4577, known_signal_recovery #4591, moving_objects #4605, period_aliases #4604, prior_art #4616, residual_screen #4602, stellar_context #4596, variability_guard #4615
- Runner finished (UTC): 2026-09-30T22:04:44Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2562.01 (BJD 2459770.7387: recovered, depth 10046 ± 487 ppm (catalogue 12060 ppm); BJD 2459774.7871: recovered, depth 7524 ± 597 ppm (catalogue 12060 ppm); BJD 2459778.8355: recovered, depth 9793 ± 619 ppm (catalogue 12060 ppm); BJD 2459782.8838: gap (catalogue 12060 ppm); BJD 2459786.9322: recovered, depth 10483 ± 575 ppm (catalogue 12060 ppm); BJD 2459790.9806: recovered, depth 10042 ± 582 ppm (catalogue 12060 ppm); BJD 2459795.0289: recovered, depth 9513 ± 563 ppm (catalogue 12060 ppm); BJD 2459394.2404: recovered, depth 10617 ± 556 ppm (catalogue 12060 ppm); BJD 2459398.2887: recovered, depth 8987 ± 499 ppm (catalogue 12060 ppm); BJD 2459402.3371: recovered, depth 10789 ± 472 ppm (catalogue 12060 ppm); BJD 2459406.3855: gap (catalogue 12060 ppm); BJD 2459410.4338: recovered, depth 9378 ± 534 ppm (catalogue 12060 ppm); BJD 2459414.4822: recovered, depth 10272 ± 493 ppm (catalogue 12060 ppm); BJD 2459418.5306: recovered, depth 6323 ± 488 ppm (catalogue 12060 ppm); BJD 2459422.5789: recovered, depth 10249 ± 595 ppm (catalogue 12060 ppm); BJD 2459426.6273: recovered, depth 8997 ± 554 ppm (catalogue 12060 ppm); BJD 2459430.6757: recovered, depth 9971 ± 489 ppm (catalogue 12060 ppm); BJD 2459434.7240: recovered, depth 8474 ± 573 ppm (catalogue 12060 ppm); BJD 2459438.7724: recovered, depth 8925 ± 574 ppm (catalogue 12060 ppm); BJD 2459442.8208: recovered, depth 9308 ± 498 ppm (catalogue 12060 ppm); BJD 2459580.4654: gap (catalogue 12060 ppm); BJD 2459584.5137: recovered, depth 9322 ± 435 ppm (catalogue 12060 ppm); BJD 2459588.5621: recovered, depth 7372 ± 454 ppm (catalogue 12060 ppm); BJD 2459592.6105: recovered, depth 9812 ± 440 ppm (catalogue 12060 ppm); BJD 2459596.6588: recovered, depth 10972 ± 498 ppm (catalogue 12060 ppm); BJD 2459600.7072: recovered, depth 9954 ± 434 ppm (catalogue 12060 ppm); BJD 2459604.7556: recovered, depth 9661 ± 449 ppm (catalogue 12060 ppm); BJD 2459665.4811: recovered, depth 9091 ± 797 ppm (catalogue 12060 ppm); BJD 2459669.5295: recovered, depth 5540 ± 662 ppm (catalogue 12060 ppm); BJD 2459673.5778: recovered, depth 9729 ± 522 ppm (catalogue 12060 ppm); BJD 2459677.6262: recovered, depth 9560 ± 516 ppm (catalogue 12060 ppm); BJD 2459681.6746: gap (catalogue 12060 ppm); BJD 2459685.7230: recovered, depth 9801 ± 586 ppm (catalogue 12060 ppm); BJD 2459689.7713: recovered, depth 9770 ± 466 ppm (catalogue 12060 ppm); BJD 2459693.8197: gap (catalogue 12060 ppm); BJD 2459697.8681: recovered, depth 10290 ± 610 ppm (catalogue 12060 ppm); BJD 2459701.9164: partial, depth 9259 ± 494 ppm (catalogue 12060 ppm); BJD 2459705.9648: not recovered, depth 4530 ± 613 ppm (catalogue 12060 ppm); BJD 2459710.0132: recovered, depth 9598 ± 826 ppm (catalogue 12060 ppm); BJD 2459714.0615: recovered, depth 9859 ± 544 ppm (catalogue 12060 ppm)).
Outside the catalogued epoch the screen left 16 threshold entries forming **5 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459665.2814 matches the catalogued transit's depth (6249 vs 10046 ppm), 105.448 d later; 1 of 105 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2562.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 420177051 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 292.018975 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 77.378608 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459770.738717 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.0483695 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 12060.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.896 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.5945 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-09-09 12:04:04 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | lightcurve | 54 | True | `3ea262ca75f5e4de` | True |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | lightcurve | 40 | False | `c1ad95aec4ab23d8` | True |
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | lightcurve | 41 | False | `c810c4461dbb13c3` | True |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | lightcurve | 47 | False | `f132cbfc0a0d7abd` | True |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | lightcurve | 50 | False | `c098e4cdf0177db2` | True |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | lightcurve | 51 | False | `1ee9952dc9874033` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 2459770.73872 | recovered | 87 | 10046 ± 487 | 12060 | -0.22 |
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 2459774.78709 | recovered | 87 | 7524 ± 597 | 12060 | 0.29 |
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 2459778.83546 | recovered | 87 | 9793 ± 619 | 12060 | 0.16 |
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 2459782.88383 | gap | 0 | — | 12060 | — |
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 2459786.93219 | recovered | 87 | 10483 ± 575 | 12060 | -0.12 |
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 2459790.98056 | recovered | 87 | 10042 ± 582 | 12060 | 0.01 |
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 2459795.02893 | recovered | 87 | 9513 ± 563 | 12060 | -0.51 |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | 2459394.24035 | recovered | 87 | 10617 ± 556 | 12060 | -0.41 |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | 2459398.28872 | recovered | 87 | 8987 ± 499 | 12060 | -0.52 |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | 2459402.33709 | recovered | 87 | 10789 ± 472 | 12060 | -0.35 |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | 2459406.38546 | gap | 0 | — | 12060 | — |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | 2459410.43383 | recovered | 87 | 9378 ± 534 | 12060 | -0.18 |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | 2459414.48220 | recovered | 87 | 10272 ± 493 | 12060 | 0.36 |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | 2459418.53057 | recovered | 87 | 6323 ± 488 | 12060 | 0.08 |
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | 2459422.57894 | recovered | 87 | 10249 ± 595 | 12060 | -0.19 |
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | 2459426.62731 | recovered | 86 | 8997 ± 554 | 12060 | -0.43 |
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | 2459430.67568 | recovered | 87 | 9971 ± 489 | 12060 | -0.43 |
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | 2459434.72405 | recovered | 87 | 8474 ± 573 | 12060 | -0.17 |
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | 2459438.77242 | recovered | 87 | 8925 ± 574 | 12060 | 0.45 |
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | 2459442.82079 | recovered | 87 | 9308 ± 498 | 12060 | 0.16 |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 2459580.46535 | gap | 0 | — | 12060 | — |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 2459584.51372 | recovered | 87 | 9322 ± 435 | 12060 | 0.11 |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 2459588.56209 | recovered | 86 | 7372 ± 454 | 12060 | -0.10 |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 2459592.61046 | recovered | 87 | 9812 ± 440 | 12060 | -0.15 |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 2459596.65883 | recovered | 87 | 10972 ± 498 | 12060 | -0.01 |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 2459600.70720 | recovered | 87 | 9954 ± 434 | 12060 | -0.24 |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 2459604.75557 | recovered | 87 | 9661 ± 449 | 12060 | -0.07 |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 2459665.48111 | recovered | 87 | 9091 ± 797 | 12060 | 0.01 |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 2459669.52948 | recovered | 86 | 5540 ± 662 | 12060 | 0.04 |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 2459673.57785 | recovered | 87 | 9729 ± 522 | 12060 | -0.52 |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 2459677.62622 | recovered | 87 | 9560 ± 516 | 12060 | 0.07 |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 2459681.67459 | gap | 0 | — | 12060 | — |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 2459685.72296 | recovered | 87 | 9801 ± 586 | 12060 | 0.34 |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 2459689.77133 | recovered | 87 | 9770 ± 466 | 12060 | 0.13 |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | 2459693.81970 | gap | 0 | — | 12060 | — |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | 2459697.86807 | recovered | 87 | 10290 ± 610 | 12060 | 0.67 |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | 2459701.91644 | partial | 87 | 9259 ± 494 | 12060 | 0.34 |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | 2459705.96480 | not_recovered | 87 | 4530 ± 613 | 12060 | — |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | 2459710.01317 | recovered | 67 | 9598 ± 826 | 12060 | -0.18 |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | 2459714.06154 | recovered | 87 | 9859 ± 544 | 12060 | -0.27 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 10000, 8h: 20000 |
| `tess2021175071901-s0040-0000000420177051-0211-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 10000, 2h: 20000, 4h: 10000, 8h: 20000 |
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021204101404-s0041-0000000420177051-0212-s_lc.fits` | 2459423.62441 | -0.01578 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022085151738-s0050-0000000420177051-0222-s_lc.fits` | 2459665.28136 | -0.01489 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022112184951-s0051-0000000420177051-0223-s_lc.fits` | 2459693.63367 | -0.01701 | 2 | PDCSAP | 2 | no |
| `tess2022190063128-s0054-0000000420177051-0227-s_lc.fits` | 2459779.88522 | -0.01488 | 2 | SAP | 1, 2 | no |
| `tess2021364111932-s0047-0000000420177051-0218-s_lc.fits` | 2459600.14385 | -0.01180 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459665.28136 | 6249 | 10046 | 105.4482 | 1 / 105 | 105.448 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2562.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:04:33Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:04:36Z: TOI-2562.01 (TIC 420177051, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:04:39Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:04:41Z: UCAC4 837-016278 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459770.7387: recovered, depth 10046 ± 487 ppm (catalogue 12060 ppm); BJD 2459774.7871: recovered, depth 7524 ± 597 ppm (catalogue 12060 ppm); BJD 2459778.8355: recovered, depth 9793 ± 619 ppm (catalogue 12060 ppm); BJD 2459782.8838: gap (catalogue 12060 ppm); BJD 2459786.9322: recovered, depth 10483 ± 575 ppm (catalogue 12060 ppm); BJD 2459790.9806: recovered, depth 10042 ± 582 ppm (catalogue 12060 ppm); BJD 2459795.0289: recovered, depth 9513 ± 563 ppm (catalogue 12060 ppm); BJD 2459394.2404: recovered, depth 10617 ± 556 ppm (catalogue 12060 ppm); BJD 2459398.2887: recovered, depth 8987 ± 499 ppm (catalogue 12060 ppm); BJD 2459402.3371: recovered, depth 10789 ± 472 ppm (catalogue 12060 ppm); BJD 2459406.3855: gap (catalogue 12060 ppm); BJD 2459410.4338: recovered, depth 9378 ± 534 ppm (catalogue 12060 ppm); BJD 2459414.4822: recovered, depth 10272 ± 493 ppm (catalogue 12060 ppm); BJD 2459418.5306: recovered, depth 6323 ± 488 ppm (catalogue 12060 ppm); BJD 2459422.5789: recovered, depth 10249 ± 595 ppm (catalogue 12060 ppm); BJD 2459426.6273: recovered, depth 8997 ± 554 ppm (catalogue 12060 ppm); BJD 2459430.6757: recovered, depth 9971 ± 489 ppm (catalogue 12060 ppm); BJD 2459434.7240: recovered, depth 8474 ± 573 ppm (catalogue 12060 ppm); BJD 2459438.7724: recovered, depth 8925 ± 574 ppm (catalogue 12060 ppm); BJD 2459442.8208: recovered, depth 9308 ± 498 ppm (catalogue 12060 ppm); BJD 2459580.4654: gap (catalogue 12060 ppm); BJD 2459584.5137: recovered, depth 9322 ± 435 ppm (catalogue 12060 ppm); BJD 2459588.5621: recovered, depth 7372 ± 454 ppm (catalogue 12060 ppm); BJD 2459592.6105: recovered, depth 9812 ± 440 ppm (catalogue 12060 ppm); BJD 2459596.6588: recovered, depth 10972 ± 498 ppm (catalogue 12060 ppm); BJD 2459600.7072: recovered, depth 9954 ± 434 ppm (catalogue 12060 ppm); BJD 2459604.7556: recovered, depth 9661 ± 449 ppm (catalogue 12060 ppm); BJD 2459665.4811: recovered, depth 9091 ± 797 ppm (catalogue 12060 ppm); BJD 2459669.5295: recovered, depth 5540 ± 662 ppm (catalogue 12060 ppm); BJD 2459673.5778: recovered, depth 9729 ± 522 ppm (catalogue 12060 ppm); BJD 2459677.6262: recovered, depth 9560 ± 516 ppm (catalogue 12060 ppm); BJD 2459681.6746: gap (catalogue 12060 ppm); BJD 2459685.7230: recovered, depth 9801 ± 586 ppm (catalogue 12060 ppm); BJD 2459689.7713: recovered, depth 9770 ± 466 ppm (catalogue 12060 ppm); BJD 2459693.8197: gap (catalogue 12060 ppm); BJD 2459697.8681: recovered, depth 10290 ± 610 ppm (catalogue 12060 ppm); BJD 2459701.9164: partial, depth 9259 ± 494 ppm (catalogue 12060 ppm); BJD 2459705.9648: not recovered, depth 4530 ± 613 ppm (catalogue 12060 ppm); BJD 2459710.0132: recovered, depth 9598 ± 826 ppm (catalogue 12060 ppm); BJD 2459714.0615: recovered, depth 9859 ± 544 ppm (catalogue 12060 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5, ≤2.5, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2459665.2814, ΔT = 105.448 d, 1 of 105 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (105.448 d); duration likelihood under Gaia priors (circular orbits) peaks at 105 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2562.01: Gaia DR3 2289934042329666688 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2562.01: Teff 5777 K, R* 1.15 ± 0.09, M* 1.10 ± 0.11, ρ* 0.72 ± 0.19 ρ☉ (dwarf sequence, M_G 4.16, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-2562.01: 6 Gaia neighbour(s) within 52.5", contamination 1.09%; depth 10046 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 2 persistent event(s), 1 clean; BJD 2459665.2814 suspect: earth point (in event), momentum dump (in event), MOM_CENTR1 z=+9.5, MOM_CENTR2 z=-5.4, POS_CORR1 z=+12.5, POS_CORR2 z=-7.8, SAP_BKG z=-10.7 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 7 light curve × candidate pair(s); aliases supported: none; excluded: none; 7 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-2562.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2562.01: UCAC4 837-016278 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 1 possible published-ephemeris overlap(s) within 1 d (TOI-2562.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2562-01.yaml
python -m cygnus.multi report campaigns/toi-2562-01.yaml
```
