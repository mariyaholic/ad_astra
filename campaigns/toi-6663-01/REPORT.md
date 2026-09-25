# Known-object test, TOI-6663.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-6663-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #249, fetch_products #248, known_signal_recovery #250, period_aliases #252, prior_art #253, residual_screen #251
- Runner finished (UTC): 2026-09-25T04:05:10Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6663.01 (BJD 2459598.6538: recovered, depth 4441 ± 134 ppm (catalogue 3066 ppm)).
Outside the catalogued epoch the screen left 4 threshold entries forming **2 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **passed**: the calibrated screen recovered the catalogued transit (BJD 2459598.6538)
at 4441 ± 134 ppm against a catalogue depth of 3066 ppm. The screen left **no persistent events**
outside the veto (2 distinct events, both non-persistent), so there is nothing to review event by event
and no repeat candidate (`period_aliases` `not_tested`). Catalogue cross-match answered by all four
services. A clean pipeline pass; no lead and no escalation.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6663.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 415732733 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 142.031271 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 78.944752 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459598.653805 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 3065.8159708 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 7.1157207 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 10.594 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2025-07-22 12:04:25 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2021364111932-s0047-0000000415732733-0218-s_lc.fits` | 47 | True | `c87b322693e3f330` | True |
| `tess2022357055054-s0060-0000000415732733-0249-s_lc.fits` | 60 | False | `6e06cd7b067ed96d` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021364111932-s0047-0000000415732733-0218-s_lc.fits` | 2459598.65380 | recovered | 213 | 4441 ± 134 | 3066 | 1.18 |
| `tess2022357055054-s0060-0000000415732733-0249-s_lc.fits` | — | epoch not in this light curve | — | — | 3066 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021364111932-s0047-0000000415732733-0218-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 5000, 8h: 10000 |
| `tess2022357055054-s0060-0000000415732733-0249-s_lc.fits` | 3 | False | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000415732733-0249-s_lc.fits` | 2459944.03198 | -0.00740 | 2 | PDCSAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000415732733-0249-s_lc.fits` | 2459943.98267 | -0.00679 | 3 | PDCSAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6663.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T04:04:59Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T04:05:01Z: TOI-6663.01 (TIC 415732733, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T04:05:06Z
- SIMBAD (done, 2026-09-25): 3 match(es) in SIMBAD within 30" as of 2026-09-25T04:05:09Z: TYC 4544-1272-2 (*); GSC 04544-01272 (**); TYC 4544-1272-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459598.6538: recovered, depth 4441 ± 134 ppm (catalogue 3066 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-6663-01.yaml
python -m cygnus.campaign report campaigns/toi-6663-01.yaml
```
