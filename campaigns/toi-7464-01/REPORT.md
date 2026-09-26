<!-- cygnus:generated-draft -->
# Known-object test, TOI-7464.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-7464-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #701, calibrate_screen #683, event_census #690, fetch_products #680, known_signal_recovery #686, moving_objects #696, period_aliases #691, prior_art #703, residual_screen #689, stellar_context #687, variability_guard #702
- Runner finished (UTC): 2026-09-26T10:13:57Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-7464.01 (BJD 2459580.8683: recovered, depth 39342 ± 682 ppm (catalogue 45279 ppm)).
Outside the catalogued epoch the screen left 30 threshold entries forming **5 distinct event(s)**, **5 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459600.8470 matches the catalogued transit's depth (24346 vs 39342 ppm), 20.032 d later; 0 of 20 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-7464.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 251090642 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 139.793743 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 53.594557 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459580.868263 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 45278.8810079 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.8624508 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.0912 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-07-17 12:03:25 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000251090642-0218-s_lc.fits` | lightcurve | 47 | True | `b807f26d1b7c7778` | True |
| `tess2024003055635-s0074-0000000251090642-0269-s_lc.fits` | lightcurve | 74 | False | `78b0cc44648eb576` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000251090642-0218-s_lc.fits` | 2459580.86826 | recovered | 116 | 39342 ± 682 | 45279 | -1.27 |
| `tess2024003055635-s0074-0000000251090642-0269-s_lc.fits` | — | epoch not in this light curve | — | — | 45279 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021364111932-s0047-0000000251090642-0218-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2024003055635-s0074-0000000251090642-0269-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000251090642-0269-s_lc.fits` | 2460322.41532 | -0.04417 | 78 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000251090642-0218-s_lc.fits` | 2459600.91093 | -0.04055 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000251090642-0269-s_lc.fits` | 2460322.35699 | -0.03739 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000251090642-0218-s_lc.fits` | 2459600.84704 | -0.03364 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000251090642-0269-s_lc.fits` | 2460322.35143 | -0.03314 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459600.84704 | 24346 | 39342 | 20.0316 | 0 / 20 |  |
| 2459600.91093 | 37480 | 39342 | 20.0955 | 0 / 20 |  |
| 2460322.35143 | 25506 | 39342 | 741.5360 | 29 / 741 | 741.536, 370.768, 247.179, 185.384, 148.307, 123.589, 105.934, 92.692, 82.3929, 74.1536, 67.4124, 61.7947, 57.0412, 52.9669, 49.4357, 46.346, 43.6198, 41.1964, 39.0282, 37.0768 |
| 2460322.35699 | 32825 | 39342 | 741.5416 | 29 / 741 | 741.542, 370.771, 247.18, 185.385, 148.308, 123.59, 105.934, 92.6927, 82.3935, 74.1542, 67.4129, 61.7951, 57.0417, 52.9673, 49.4361, 46.3463, 43.6201, 41.1968, 39.0285, 37.0771 |
| 2460322.41532 | 39306 | 39342 | 741.5999 | 29 / 741 | 741.6, 370.8, 247.2, 185.4, 148.32, 123.6, 105.943, 92.7, 82.4, 74.16, 67.4182, 61.8, 57.0461, 52.9714, 49.44, 46.35, 43.6235, 41.2, 39.0316, 37.08 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-7464.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:13:53Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:13:55Z: TOI-7464.01 (TIC 251090642, disposition PC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:13:56Z: Gaia DR3 1022973218913663488 (type ROT, P — d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:13:56Z: TIC 251090642 (*); CTOI 251090642.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459580.8683: recovered, depth 39342 ± 682 ppm (catalogue 45279 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 5 repeat-candidate event(s); first at BJD 2459600.8470, ΔT = 20.032 d, 0 of 20 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-7464.01: Gaia DR3 1022973218913663488 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-7464.01: Teff 3530 K, R* 0.49 ± 0.04, M* 0.49 ± 0.05, ρ* 4.08 ± 1.06 ρ☉ (dwarf sequence, M_G 8.90, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-7464.01: 6 Gaia neighbour(s) within 52.5", contamination 38.25%; depth 39342 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 1022974696382412928, 38.5", ΔG 0.61); a centroid test is needed |
| Pointing and quality census per event | passed | 5 persistent event(s), 5 clean; no artifact quality bit within ±0.25 d and no centroid, pointing or background shift beyond 5σ |
| Moving objects at screen-event epochs | inconclusive | 5 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-7464.01: Gaia DR3 1022973218913663488   ROT                            P=None at 0.6" |
| Object-class guard (SIMBAD) | passed | TOI-7464.01: CTOI 251090642.01 otype Pl? (star_or_other) at 0.6" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-7464-01.yaml
python -m cygnus.multi report campaigns/toi-7464-01.yaml
```
