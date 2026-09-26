<!-- [private Drive store] -->
# Known-object test, TOI-3972.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3972-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #809, calibrate_screen #793, event_census #797, fetch_products #792, known_signal_recovery #794, moving_objects #803, period_aliases #798, prior_art #811, residual_screen #796, stellar_context #795, variability_guard #810
- Runner finished (UTC): 2026-09-26T10:19:55Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3972.01 (BJD 2459903.2388: recovered, depth 14179 ± 166 ppm (catalogue 16120 ppm)).
Outside the catalogued epoch the screen left 48 threshold entries forming **12 distinct event(s)**, **6 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459892.7292 matches the catalogued transit's depth (13680 vs 14179 ppm), 10.510 d later; 0 of 10 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3972.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 284206913 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 9.305074 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 61.205097 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459903.238824 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 16120.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.112 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.7486 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-09-08 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000284206913-0247-s_lc.fits` | lightcurve | 58 | True | `194972ab2b35621a` | True |
| `tess2024114025118-s0078-0000000284206913-0273-s_lc.fits` | lightcurve | 78 | False | `665c0512c017447f` | True |
| `tess2024300212641-s0085-0000000284206913-0282-s_lc.fits` | lightcurve | 85 | False | `ab3d384af2c545bb` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000284206913-0247-s_lc.fits` | 2459903.23882 | recovered | 93 | 14179 ± 166 | 16120 | -0.00 |
| `tess2024114025118-s0078-0000000284206913-0273-s_lc.fits` | — | epoch not in this light curve | — | — | 16120 | — |
| `tess2024300212641-s0085-0000000284206913-0282-s_lc.fits` | — | epoch not in this light curve | — | — | 16120 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022302161335-s0058-0000000284206913-0247-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2024114025118-s0078-0000000284206913-0273-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 10000, 8h: 10000 |
| `tess2024300212641-s0085-0000000284206913-0282-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024114025118-s0078-0000000284206913-0273-s_lc.fits` | 2460439.31910 | -0.01457 | 84 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000284206913-0282-s_lc.fits` | 2460618.01245 | -0.01432 | 84 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000284206913-0247-s_lc.fits` | 2459892.72920 | -0.01387 | 86 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000284206913-0273-s_lc.fits` | 2460449.82896 | -0.01374 | 82 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000284206913-0273-s_lc.fits` | 2460449.88868 | -0.00685 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000284206913-0273-s_lc.fits` | 2460439.38022 | -0.00651 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000284206913-0273-s_lc.fits` | 2460445.51222 | -0.00734 | 2 | SAP | 1, 2, 3 | no |
| `tess2024114025118-s0078-0000000284206913-0273-s_lc.fits` | 2460445.49555 | -0.00635 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000284206913-0282-s_lc.fits` | 2460616.54161 | -0.00558 | 2 | SAP | 1, 2, 3 | no |
| `tess2024300212641-s0085-0000000284206913-0282-s_lc.fits` | 2460616.05411 | -0.00523 | 2 | SAP | 2, 3 | no |
| `tess2024300212641-s0085-0000000284206913-0282-s_lc.fits` | 2460623.01243 | -0.00480 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000284206913-0282-s_lc.fits` | 2460622.91938 | -0.00467 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459892.72920 | 13680 | 14179 | 10.5096 | 0 / 10 |  |
| 2460439.31910 | 13961 | 14179 | 536.0803 | 23 / 536 | 536.08, 268.04, 178.693, 134.02, 107.216, 89.3467, 76.5829, 67.01, 59.5645, 53.608, 44.6734, 41.2369, 35.7387, 33.505, 31.5341, 29.7822, 28.2148, 26.804, 25.5276, 23.3078 |
| 2460449.82896 | 13259 | 14179 | 546.5902 | 12 / 546 | 546.59, 273.295, 136.648, 109.318, 78.0843, 68.3238, 49.69, 42.0454, 39.0422, 21.8636, 21.0227, 10.5113 |
| 2460618.01245 | 13866 | 14179 | 714.7737 | 32 / 714 | 714.774, 357.387, 238.258, 178.693, 142.955, 119.129, 102.111, 89.3467, 79.4193, 71.4774, 64.9794, 59.5645, 54.9826, 51.0553, 47.6516, 44.6734, 42.0455, 39.7096, 37.6197, 35.7387 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3972.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:19:52Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:19:53Z: TOI-3972.01 (TIC 284206913, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:19:54Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:19:55Z: Wolf    7b (Pl); Wolf    7 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459903.2388: recovered, depth 14179 ± 166 ppm (catalogue 16120 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 30% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 4 repeat-candidate event(s); first at BJD 2459892.7292, ΔT = 10.510 d, 0 of 10 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3972.01: Gaia DR3 427232186629403264 at 0.00" (propagated 2016.0 → J2015.5; 0.07" unpropagated, proper-motion shift 0.07") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3972.01: Teff 5256 K, R* 0.89 ± 0.07, M* 0.92 ± 0.09, ρ* 1.31 ± 0.34 ρ☉ (dwarf sequence, M_G 5.19, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3972.01: 63 Gaia neighbour(s) within 52.5", contamination 26.29%; depth 14179 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 427232186631110400, 46.2", ΔG 1.50); a centroid test is needed |
| Pointing and quality census per event | passed | 6 persistent event(s), 6 clean; no artifact quality bit within ±0.25 d and no centroid, pointing or background shift beyond 5σ |
| Moving objects at screen-event epochs | passed | 6 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-3972.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3972.01: Wolf    7 otype PM* (star_or_other) at 2.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3972-01.yaml
python -m cygnus.multi report campaigns/toi-3972-01.yaml
```
