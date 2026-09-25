# Known-object test, TOI-285.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

- Campaign spec: `campaigns/toi-285-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #460, fetch_products #459, known_signal_recovery #461, period_aliases #463, prior_art #464, residual_screen #462
- Runner finished (UTC): 2026-09-25T05:45:45Z

## Bottom line

Positive control **inconclusive**: BJD 2458393.9965: partial, depth 2459 ± 310 ppm (catalogue 2426 ppm).
Outside the catalogued epoch the screen left 35 threshold entries forming **17 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control is **inconclusive/partial** at BJD 2458393.9965 in sector 3: measured 2459 ± 310 ppm vs catalogue 2426 ppm (102 usable cadences; entry offset −1.54 h). The data suggest a depth-consistent depression, but the runner's partial state is retained. At k* = 2 the 90%-completeness depths are 10000 ppm across the tabulated durations and 2000-ppm/4-h injection recovery is only 10%; the catalogue signal is below tested sensitivity.

The one persistent row is BJD 2458476.31253 in sector 6 (2 cadences, −1.02%). The ±0.15-d SAP/PDCSAP profiles show a broad low-frequency offset (roughly −1.5…−2.5 ppt) rather than a localized transit; QUALITY=0, max gap 2 min, centroid residuals are <1σ. This is a baseline feature, not a repeat candidate. Other listed events are largely short SAP-only excursions. Cross-match answered at all four services; no VSX variable match. Pixel and alternate-reduction checks remain untested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-285.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 220459976 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 74.697171 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -56.393814 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2458393.996453 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 2425.505189 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 3.459632 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 12.1677 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2026-02-02 16:00:02 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 3 | True | `10ff00cfcc2a06fe` | True |
| `tess2018234235059-s0002-0000000220459976-0121-s_lc.fits` | 2 | False | `198de9208550dce8` | True |
| `tess2018292075959-s0004-0000000220459976-0124-s_lc.fits` | 4 | False | `0cacaee1be59a054` | True |
| `tess2018319095959-s0005-0000000220459976-0125-s_lc.fits` | 5 | False | `90aca4425d59e889` | True |
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | 6 | False | `5e0ffcea78d7dcde` | True |
| `tess2019006130736-s0007-0000000220459976-0131-s_lc.fits` | 7 | False | `c5d04694bf8dd44a` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 2458393.99645 | partial | 102 | 2459 ± 310 | 2426 | -1.54 |
| `tess2018234235059-s0002-0000000220459976-0121-s_lc.fits` | — | epoch not in this light curve | — | — | 2426 | — |
| `tess2018292075959-s0004-0000000220459976-0124-s_lc.fits` | — | epoch not in this light curve | — | — | 2426 | — |
| `tess2018319095959-s0005-0000000220459976-0125-s_lc.fits` | — | epoch not in this light curve | — | — | 2426 | — |
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | — | epoch not in this light curve | — | — | 2426 | — |
| `tess2019006130736-s0007-0000000220459976-0131-s_lc.fits` | — | epoch not in this light curve | — | — | 2426 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2018234235059-s0002-0000000220459976-0121-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2018292075959-s0004-0000000220459976-0124-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — |
| `tess2018319095959-s0005-0000000220459976-0125-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2019006130736-s0007-0000000220459976-0131-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | 2458476.31253 | -0.01022 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018292075959-s0004-0000000220459976-0124-s_lc.fits` | 2458421.23927 | -0.03485 | 36 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000220459976-0124-s_lc.fits` | 2458421.26844 | -0.03215 | 4 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000220459976-0124-s_lc.fits` | 2458421.31427 | -0.02436 | 60 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000220459976-0124-s_lc.fits` | 2458421.36844 | -0.01938 | 2 | SAP | 3 | no |
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 2458386.00839 | -0.01018 | 2 | SAP | 2, 3 | no |
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | 2458476.95974 | -0.01001 | 2 | PDCSAP | 1, 2 | no |
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | 2458478.44999 | -0.00980 | 2 | SAP | 1, 2, 3 | no |
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 2458405.90585 | -0.00920 | 2 | PDCSAP | 3 | no |
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 2458386.04866 | -0.00913 | 2 | SAP | 3 | no |
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 2458386.08478 | -0.00887 | 2 | SAP | 3 | no |
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | 2458476.70696 | -0.00874 | 2 | PDCSAP | 2 | no |
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 2458386.03894 | -0.00871 | 2 | SAP | 2, 3 | no |
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 2458405.75585 | -0.00868 | 2 | PDCSAP | 3 | no |
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | 2458469.03763 | -0.00862 | 2 | PDCSAP+SAP | 3 | no |
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | 2458478.46665 | -0.00849 | 2 | SAP | 3 | no |
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 2458386.24033 | -0.00816 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-285.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:45:39Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:45:41Z: TOI-285.01 (TIC 220459976, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:45:42Z
- SIMBAD (done, 2026-09-25): 2 match(es) in SIMBAD within 30" as of 2026-09-25T05:45:44Z: TOI-285 (PM*); TOI-285.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | inconclusive | BJD 2458393.9965: partial, depth 2459 ± 310 ppm (catalogue 2426 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 4, 3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-285-01.yaml
python -m cygnus.campaign report campaigns/toi-285-01.yaml
```
