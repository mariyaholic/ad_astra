# Known-object test, TOI-2490.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-2490-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #231, fetch_products #230, known_signal_recovery #232, period_aliases #234, prior_art #235, residual_screen #233
- Runner finished (UTC): 2026-09-25T03:57:56Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2490.01 (BJD 2459180.6915: recovered, depth 7064 ± 124 ppm (catalogue 4408 ppm)).
Outside the catalogued epoch the screen left 20 threshold entries forming **9 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **passed**: the calibrated screen recovered the catalogued transit (BJD 2459180.6915)
at 7064 ± 124 ppm against a catalogue depth of 4408 ppm. The screen left **no persistent events**
outside the veto, so there is nothing to review event by event and no repeat candidate
(`period_aliases` `not_tested`). Catalogue cross-match answered by all four services. A clean pipeline
pass; no lead and no escalation.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2490.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 77437543 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 73.124509 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -36.257098 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459180.691467 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 4407.5735305 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 7.474737 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 11.2759 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2024-03-26 12:03:01 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2020324010417-s0032-0000000077437543-0200-s_lc.fits` | 32 | True | `822bca7f5289219d` | True |
| `tess2020294194027-s0031-0000000077437543-0198-s_lc.fits` | 31 | False | `7ffeb2803de19a0a` | True |
| `tess2025312202959-s0098-0000000077437543-0298-s_lc.fits` | 98 | False | `3f8563f30b181952` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020324010417-s0032-0000000077437543-0200-s_lc.fits` | 2459180.69147 | recovered | 225 | 7064 ± 124 | 4408 | 0.91 |
| `tess2020294194027-s0031-0000000077437543-0198-s_lc.fits` | — | epoch not in this light curve | — | — | 4408 | — |
| `tess2025312202959-s0098-0000000077437543-0298-s_lc.fits` | — | epoch not in this light curve | — | — | 4408 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020324010417-s0032-0000000077437543-0200-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 5000, 8h: 10000 |
| `tess2020294194027-s0031-0000000077437543-0198-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025312202959-s0098-0000000077437543-0298-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000077437543-0298-s_lc.fits` | 2461024.20035 | -0.01003 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000077437543-0298-s_lc.fits` | 2461024.29618 | -0.00913 | 2 | SAP | 1, 2 | no |
| `tess2025312202959-s0098-0000000077437543-0298-s_lc.fits` | 2461024.28229 | -0.00849 | 4 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000077437543-0298-s_lc.fits` | 2461024.23784 | -0.00736 | 2 | SAP | 2 | no |
| `tess2025312202959-s0098-0000000077437543-0298-s_lc.fits` | 2461038.58194 | -0.00719 | 2 | SAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000077437543-0200-s_lc.fits` | 2459184.69349 | -0.00664 | 2 | SAP | 3 | no |
| `tess2020294194027-s0031-0000000077437543-0198-s_lc.fits` | 2459144.62635 | -0.00592 | 2 | SAP | 1, 2, 3 | no |
| `tess2020294194027-s0031-0000000077437543-0198-s_lc.fits` | 2459169.70459 | -0.00564 | 2 | SAP | 2, 3 | no |
| `tess2020294194027-s0031-0000000077437543-0198-s_lc.fits` | 2459162.11979 | -0.00553 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2490.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T03:57:48Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T03:57:50Z: TOI-2490.01 (TIC 77437543, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T03:57:52Z
- SIMBAD (done, 2026-09-25): 2 match(es) in SIMBAD within 30" as of 2026-09-25T03:57:54Z: ** TOI 2490B (BD*); TOI-2490 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459180.6915: recovered, depth 7064 ± 124 ppm (catalogue 4408 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2490-01.yaml
python -m cygnus.campaign report campaigns/toi-2490-01.yaml
```
