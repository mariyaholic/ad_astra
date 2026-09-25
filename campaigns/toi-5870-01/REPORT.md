# Known-object test, TOI-5870.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-5870-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #297, fetch_products #296, known_signal_recovery #298, period_aliases #300, prior_art #301, residual_screen #299
- Runner finished (UTC): 2026-09-25T04:27:54Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 6 threshold entries forming **2 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **not run** (not the same as passed): the catalogue epoch (BJD 2459817.7994, updated 2024-08-22) is ~716 d before the only retrieved light curve (sector 82: 2460533.40–2460559.25), so nothing checked the transit at its epoch; the null below is a coverage null, not a data null. Not run deeper into the MAST pool per runbook (fetch covers standard 120-s SPOC already).

Hand checks on the two screen events, from files already on disk:

| Event (BJD) | Shape | Quality/gaps | Centroid | Verdict |
|---|---|---|---|---|
| 2460538.35999 (−0.51 %, 2 cadences) | 20-min binned PDCSAP ±0.15 d: scatter ±~0.001 only, no coherent dip | 0 flags/212, max gap 4 min | MOM_CENTR values present (1983.011, 1395.373) but only 6 entries exist, all at two times — drift-corrected scatter unusable | two 2-cadence deep-noise spikes; the "persistent" flag comes from the two overlapping baselines sharing the same pair of cadences |
| 2460538.52943 (−0.46 %, 2 cadences) | same: no coherent dip | 0 flags/211 | as above | noise |

NOTES: also the sector-82 screen result is consistent with a quiet light curve at the calibrated k* = 2.5 (null: 0 persistent null events). Sensitivity: 90 %-complete depths are 5000 ppm at k* — the catalogue 3736 ppm/3.52 h signal is below it regardless of epoch, so even a covered epoch could have failed; the recovery gate here is coverage-limited, not sensitivity-limited.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5870.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 305375697 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 324.59941 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 11.006898 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459817.799423 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 3736.0 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 3.516 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 10.7974 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2024223182411-s0082-0000000305375697-0278-s_lc.fits` | 82 | False | `f023ef21b7b0a03b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000305375697-0278-s_lc.fits` | — | epoch not in this light curve | — | — | 3736 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024223182411-s0082-0000000305375697-0278-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000305375697-0278-s_lc.fits` | 2460538.35999 | -0.00512 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000305375697-0278-s_lc.fits` | 2460538.52943 | -0.00455 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5870.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T04:27:45Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T04:27:48Z: TOI-5870.01 (TIC 305375697, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T04:27:51Z
- SIMBAD (done, 2026-09-25): 2 match(es) in SIMBAD within 30" as of 2026-09-25T04:27:52Z: TYC 1124-343-1 (*); SDSS J213825.40+110032.6 (BiC)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 30% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-5870-01.yaml
python -m cygnus.campaign report campaigns/toi-5870-01.yaml
```
