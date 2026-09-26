<!-- cygnus:generated-draft -->
# Known-object test, TOI-1986.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1986-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #68, calibrate_screen #22, event_census #53, fetch_products #4, known_signal_recovery #24, moving_objects #55, period_aliases #54, prior_art #70, residual_screen #36, stellar_context #26, variability_guard #69
- Runner finished (UTC): 2026-09-26T09:54:06Z

## Bottom line

Positive control **failed**: BJD 2459256.9745: not recovered, depth 649 ± 488 ppm (catalogue 12480 ppm).
Outside the catalogued epoch the screen left 194 threshold entries forming **60 distinct event(s)**, **28 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1986.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 468997317 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 144.023758 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -51.744648 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459256.974533 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 12479.7176832 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.8967771 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.135 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021039152502-s0035-0000000468997317-0205-s_lc.fits` | lightcurve | 35 | True | `0cac12b06e7714a4` | True |
| `tess2019058134432-s0009-0000000468997317-0139-s_lc.fits` | lightcurve | 9 | False | `36f4dbc72df74db6` | True |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | lightcurve | 10 | False | `fd5d720f9049797c` | True |
| `tess2021065132309-s0036-0000000468997317-0207-s_lc.fits` | lightcurve | 36 | False | `20cc346d0c230394` | True |
| `tess2023043185947-s0062-0000000468997317-0254-s_lc.fits` | lightcurve | 62 | False | `dd91d55261d4dc4e` | True |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | lightcurve | 63 | False | `9ccc0741b44297bb` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021039152502-s0035-0000000468997317-0205-s_lc.fits` | 2459256.97453 | not_recovered | 147 | 649 ± 488 | 12480 | — |
| `tess2019058134432-s0009-0000000468997317-0139-s_lc.fits` | — | epoch not in this light curve | — | — | 12480 | — |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | — | epoch not in this light curve | — | — | 12480 | — |
| `tess2021065132309-s0036-0000000468997317-0207-s_lc.fits` | — | epoch not in this light curve | — | — | 12480 | — |
| `tess2023043185947-s0062-0000000468997317-0254-s_lc.fits` | — | epoch not in this light curve | — | — | 12480 | — |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | — | epoch not in this light curve | — | — | 12480 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021039152502-s0035-0000000468997317-0205-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2019058134432-s0009-0000000468997317-0139-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2021065132309-s0036-0000000468997317-0207-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023043185947-s0062-0000000468997317-0254-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019058134432-s0009-0000000468997317-0139-s_lc.fits` | 2458544.10324 | -0.02581 | 44 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458589.14195 | -0.02533 | 75 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460037.35821 | -0.02527 | 76 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021039152502-s0035-0000000468997317-0205-s_lc.fits` | 2459279.50509 | -0.02325 | 80 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.59913 | -0.02171 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.60400 | -0.02138 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.64427 | -0.02118 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.65330 | -0.02100 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.65816 | -0.02082 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.58038 | -0.02070 | 6 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.59427 | -0.02037 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2021039152502-s0035-0000000468997317-0205-s_lc.fits` | 2459266.78960 | -0.02034 | 113 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.57136 | -0.02019 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.68038 | -0.02018 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.67066 | -0.01979 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.66233 | -0.01959 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.56650 | -0.01940 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.55122 | -0.01937 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.68455 | -0.01935 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2021039152502-s0035-0000000468997317-0205-s_lc.fits` | 2459279.44884 | -0.01920 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.69010 | -0.01858 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.17953 | -0.01764 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.53039 | -0.01741 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460022.38400 | -0.01718 | 31 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.20036 | -0.01703 | 14 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.16981 | -0.01697 | 8 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.16008 | -0.01693 | 6 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.20661 | -0.01688 | 5 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019058134432-s0009-0000000468997317-0139-s_lc.fits` | 2458544.07477 | -0.02312 | 3 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000468997317-0139-s_lc.fits` | 2458544.06991 | -0.02293 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460039.97623 | -0.01770 | 4 | PDCSAP+SAP | 3 | no |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.86146 | -0.01742 | 86 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.70122 | -0.01732 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460039.93317 | -0.01728 | 8 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.69566 | -0.01723 | 2 | PDCSAP+SAP | 3 | no |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.21703 | -0.01713 | 2 | PDCSAP+SAP | 2 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460039.95817 | -0.01710 | 12 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460039.99289 | -0.01680 | 10 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460039.94220 | -0.01650 | 3 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460039.91373 | -0.01613 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460039.92276 | -0.01612 | 5 | PDCSAP+SAP | 3 | no |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.93299 | -0.01604 | 3 | PDCSAP+SAP | 3 | no |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.79896 | -0.01601 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.00331 | -0.01600 | 11 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.71858 | -0.01585 | 6 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.49497 | -0.01580 | 4 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.01373 | -0.01572 | 3 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.50191 | -0.01567 | 3 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460039.90470 | -0.01563 | 7 | PDCSAP+SAP | 3 | no |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.23786 | -0.01548 | 2 | SAP | 2 | no |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.23369 | -0.01546 | 2 | SAP | 2 | no |
| `tess2019085135100-s0010-0000000468997317-0140-s_lc.fits` | 2458585.22397 | -0.01541 | 2 | SAP | 2 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460022.40136 | -0.01532 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.02206 | -0.01526 | 6 | PDCSAP+SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460039.88595 | -0.01451 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.73733 | -0.01430 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.50677 | -0.01429 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.72899 | -0.01427 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.03595 | -0.01392 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000468997317-0255-s_lc.fits` | 2460040.03178 | -0.01391 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-1986.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:54:03Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:54:04Z: TOI-1986.01 (TIC 468997317, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T09:54:05Z: Gaia DR3 5312673922948554880 (type SPB, P — d)
- SIMBAD (done, 2026-09-26): 5 match(es) in SIMBAD within 30" as of 2026-09-26T09:54:05Z: HD  83358 (*); TOI-1986.01 (Pl?); 2MASS J09360298-5144381 (PM*); HD  83358B (*); Gaia DR3 5312673888594180608 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2459256.9745: not recovered, depth 649 ± 488 ppm (catalogue 12480 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 4, ≤2.5, 3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1986.01: Gaia DR3 5312673922948554880 at 0.01" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1986.01: dwarf priors not applied — RUWE 6.7684994 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1986.01: 90 Gaia neighbour(s) within 52.5", contamination 4.74%; depth 12480 ppm (catalogue depth); 1 could produce it if fully eclipsed (brightest 5312673922954351360, 2.3", ΔG 3.37); a centroid test is needed |
| Pointing and quality census per event | failed | 28 persistent event(s), 3 clean; BJD 2459266.7896 suspect: MOM_CENTR1 z=-256.1, MOM_CENTR2 z=-99.3, POS_CORR1 z=-259.9, POS_CORR2 z=-99.2, SAP_BKG z=-20.3; BJD 2459279.5051 suspect: MOM_CENTR2 z=+10.8, POS_CORR1 z=-5.9, POS_CORR2 z=+10.4, SAP_BKG z=-5.3; BJD 2458544.1032 suspect: manual exclude (within ±0.25 d), MOM_CENTR1 z=+10.1, MOM_CENTR2 z=-11.6, POS_CORR1 z=+8.9, POS_CORR2 z=-13.1, SAP_BKG z=+61.9; BJD 2458585.1601 suspect: MOM_CENTR1 z=+9.2, POS_CORR1 z=+8.1, SAP_BKG z=+22.9 |
| Moving objects at screen-event epochs | inconclusive | 28 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 3 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no repeat candidate with allowed period aliases |
| Independent-epoch confirmation (ZTF) | not_tested | no repeat candidate with allowed period aliases |
| Variable-catalogue collision (VSX) | passed | TOI-1986.01: Gaia DR3 5312673922948554880   SPB                            P=None at 0.6" |
| Object-class guard (SIMBAD) | passed | TOI-1986.01: HD  83358 otype * (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1986-01.yaml
python -m cygnus.multi report campaigns/toi-1986-01.yaml
```
