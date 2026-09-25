# Known-object test, TOI-2493.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

## Escalation (2026-09-25)

The covered positive control formally failed at BJD 2459225.8233 (62 usable cadences), although the measured depth 1871 ± 272 ppm is consistent with the catalogue's 1704 ppm. At k* = 3 the 90%-completeness depth is 10000 ppm for the tabulated durations, so this 2.09-h transit lies well below tested sensitivity. Record the failure as sensitivity-limited; no thresholds or states were changed. Next: check SPOC DV/TOI timing and compare a reduction capable of recovering ~1700-ppm events.


- Campaign spec: `campaigns/toi-2493-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #526, fetch_products #525, known_signal_recovery #527, period_aliases #529, prior_art #530, residual_screen #528
- Runner finished (UTC): 2026-09-25T05:58:16Z

## Bottom line

Positive control **failed**: BJD 2459225.8233: not recovered, depth 1871 ± 272 ppm (catalogue 1704 ppm).
Outside the catalogued epoch the screen left 23 threshold entries forming **13 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **failed formally** at the covered sector-33 epoch (62 usable cadences; QUALITY=0, max gap 2 min): measured 1871 ± 272 ppm vs catalogue 1704 ppm (ratio 1.10). However, k* = 3 has a 90%-completeness floor of 10000 ppm for the tabulated 1–8-h durations; the 2.09-h catalogue transit is below that sensitivity. The depth is consistent, but the screen gate could not validate it; no threshold was changed.

There are **0 persistent** events among 23 entries / 13 groups; all report rows are short single-flux features. No repeat candidate. All four prior-art services answered, no VSX variable match. Pixel, pointing and alternate-reduction checks remain untested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2493.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 123664207 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 89.746248 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -21.575094 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459225.823327 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 1704.3313705 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 2.0935301 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 11.433 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2021-12-19 12:02:11 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2020351194500-s0033-0000000123664207-0203-s_lc.fits` | 33 | True | `986d0856f0093dc9` | True |
| `tess2024353092137-s0087-0000000123664207-0284-s_lc.fits` | 87 | False | `949563d7d960e78d` | True |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 98 | False | `824bb5c01c6bea21` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020351194500-s0033-0000000123664207-0203-s_lc.fits` | 2459225.82333 | not_recovered | 62 | 1871 ± 272 | 1704 | — |
| `tess2024353092137-s0087-0000000123664207-0284-s_lc.fits` | — | epoch not in this light curve | — | — | 1704 | — |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | — | epoch not in this light curve | — | — | 1704 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020351194500-s0033-0000000123664207-0203-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024353092137-s0087-0000000123664207-0284-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461037.05150 | -0.00875 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461045.77708 | -0.00796 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461037.37233 | -0.00729 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461045.55556 | -0.00724 | 2 | PDCSAP | 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461045.83055 | -0.00705 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461024.13761 | -0.00693 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461024.21261 | -0.00677 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461045.68195 | -0.00671 | 2 | PDCSAP | 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461036.99178 | -0.00660 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461017.72226 | -0.00646 | 2 | PDCSAP+SAP | 1 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461017.60976 | -0.00644 | 2 | SAP | 1, 2 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461045.21390 | -0.00633 | 2 | PDCSAP | 3 | no |
| `tess2025312202959-s0098-0000000123664207-0298-s_lc.fits` | 2461038.03344 | -0.00629 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-2493.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:58:10Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:58:12Z: TOI-2493.01 (TIC 123664207, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:58:14Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T05:58:15Z: UCAC4 343-010274 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2459225.8233: not recovered, depth 1871 ± 272 ppm (catalogue 1704 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-2493-01.yaml
python -m cygnus.campaign report campaigns/toi-2493-01.yaml
```
