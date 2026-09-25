# Known-object test, TOI-5893.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-5893-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #182, fetch_products #181, known_signal_recovery #183, period_aliases #185, prior_art #186, residual_screen #184
- Runner finished (UTC): 2026-09-25T02:58:16Z

## Bottom line

Positive control **not tested**: no retrieved light curve covers a catalogued transit epoch.
Outside the catalogued epoch the screen left 20 threshold entries forming **10 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

**Positive control not tested.** Only one SPOC light curve was available (sector 82, `tess2024223182411-s0082-…-s_lc.fits`)
and it does not cover the catalogued epoch (BJD 2460536.083 is not in the retrieved sector's window; the
target's single retrieved sector is sector 82). Per the runbook this is recorded and the target skipped —
it is not a positive-control failure. Injection–recovery completeness at the reference box is 20 %, so the
screen is only weakly sensitive here.

No persistent screen events and no repeat candidate were found, so there are no events to review
individually. The 10 distinct events outside the veto are all non-persistent (single flux type or a single
baseline), which the runbook treats as systematics.

What this supports: nothing beyond a null screen of a single, weakly sensitive sector. What it does not: any
statement about the catalogued transit (not covered) or a second transit (none persistent). Next test:
none proposed; the target is not informative until a light curve covering the catalogue epoch exists.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5893.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 321790238 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 317.926468 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 8.980673 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459817.171119 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 7997.0 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 5.718 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 11.4879 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 82 | False | `04270c33ff960ac1` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | — | epoch not in this light curve | — | — | 7997 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460545.26275 | -0.00791 | 2 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460545.04887 | -0.00754 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460545.15303 | -0.00724 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460538.45169 | -0.00662 | 2 | SAP | 1, 2, 3 | no |
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460545.03984 | -0.00638 | 3 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460545.18359 | -0.00628 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460545.38914 | -0.00611 | 2 | SAP | 3 | no |
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460544.77248 | -0.00607 | 2 | SAP | 1, 2 | no |
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460545.22525 | -0.00582 | 2 | SAP | 2, 3 | no |
| `tess2024223182411-s0082-0000000321790238-0278-s_lc.fits` | 2460545.03081 | -0.00573 | 2 | SAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-5893.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T02:57:58Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T02:58:01Z: TOI-5893.01 (TIC 321790238, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T02:58:04Z
- SIMBAD (error, 2026-09-25): inconclusive (SIMBAD query failed as of 2026-09-25T02:58:05Z: ProxyError: HTTPSConnectionPool(host='simbad.cds.unistra.fr', port=443): Max retries exceeded with url: /simbad/sim-tap/sync (Caused by ProxyError('Unable to connect to proxy', OSError('Tunnel connection failed: )

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | not_tested | no retrieved light curve covers a catalogued transit epoch |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 20% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | inconclusive | 1 target(s) × 4 services, radius 30″; 3 answered, 1 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-5893-01.yaml
python -m cygnus.campaign report campaigns/toi-5893-01.yaml
```
