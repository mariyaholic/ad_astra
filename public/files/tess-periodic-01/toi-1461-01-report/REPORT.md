<!-- [private Drive store] -->
# Known-object test, TOI-1461.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1461-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #1087, calibrate_screen #1056, event_census #1060, fetch_products #1055, known_signal_recovery #1057, moving_objects #1070, period_aliases #1061, prior_art #1089, residual_screen #1059, stellar_context #1058, variability_guard #1088
- Runner finished (UTC): 2026-09-26T10:33:29Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1461.01 (BJD 2458767.3175: recovered, depth 14247 ± 285 ppm (catalogue 20261 ppm)).
Outside the catalogued epoch the screen left 131 threshold entries forming **35 distinct event(s)**, **16 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2458770.8840 matches the catalogued transit's depth (15641 vs 14247 ppm), 3.567 d later; 0 of 3 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1461.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 44631965 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 22.236394 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 35.864854 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458767.31752 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 20260.8743805 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.6185972 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.3805 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-09-18 16:00:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | lightcurve | 17 | True | `a5399f0fce6964ae` | True |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | lightcurve | 85 | False | `4caf5b31d76fb66f` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458767.31752 | recovered | 79 | 14247 ± 285 | 20261 | -0.01 |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | — | epoch not in this light curve | — | — | 20261 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458778.02087 | -0.02274 | 20 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458778.04587 | -0.02201 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458778.00421 | -0.02154 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460615.85912 | -0.02111 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460622.98888 | -0.02070 | 62 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458770.88396 | -0.01854 | 61 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460633.69066 | -0.01784 | 58 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460615.82995 | -0.01735 | 23 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460619.41811 | -0.01734 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458781.59103 | -0.01712 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458785.15909 | -0.01704 | 59 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460630.12480 | -0.01639 | 55 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458777.98893 | -0.01552 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460615.88065 | -0.01488 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458778.05837 | -0.01356 | 12 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460615.81120 | -0.00826 | 4 | PDCSAP+SAP | 1, 2 | yes |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460622.94235 | -0.00973 | 3 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458768.79989 | -0.00966 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460631.64420 | -0.00951 | 2 | PDCSAP+SAP | 3 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460622.77638 | -0.00926 | 2 | SAP | 3 | no |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458782.65840 | -0.00916 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458768.20543 | -0.00912 | 2 | SAP | 1, 2, 3 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460631.66920 | -0.00903 | 2 | PDCSAP+SAP | 3 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460622.76249 | -0.00895 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460631.72614 | -0.00886 | 2 | PDCSAP | 3 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460631.76225 | -0.00886 | 2 | PDCSAP | 3 | no |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458769.31240 | -0.00867 | 2 | SAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458782.17923 | -0.00761 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458782.22923 | -0.00723 | 2 | PDCSAP | 3 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460633.73580 | -0.00688 | 2 | SAP | 1 | no |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458787.18755 | -0.00681 | 2 | PDCSAP | 1, 2 | no |
| `tess2019279210107-s0017-0000000044631965-0161-s_lc.fits` | 2458781.63340 | -0.00658 | 2 | PDCSAP | 1 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460615.89315 | -0.00641 | 2 | SAP | 1 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460619.45978 | -0.00638 | 2 | SAP | 1 | no |
| `tess2024300212641-s0085-0000000044631965-0282-s_lc.fits` | 2460630.08314 | -0.00628 | 4 | SAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2458770.88396 | 15641 | 14247 | 3.5667 | 0 / 3 |  |
| 2458777.98893 | 12315 | 14247 | 10.6717 | 0 / 10 |  |
| 2458778.00421 | 15710 | 14247 | 10.6870 | 0 / 10 |  |
| 2458778.02087 | 15428 | 14247 | 10.7037 | 0 / 10 |  |
| 2458778.04587 | 14146 | 14247 | 10.7287 | 0 / 10 |  |
| 2458778.05837 | 8909 | 14247 | 10.7412 | 0 / 10 |  |
| 2458781.59103 | 13802 | 14247 | 14.2738 | 0 / 14 |  |
| 2458785.15909 | 15295 | 14247 | 17.8419 | 0 / 17 |  |
| 2460615.81120 | 8260 | 14247 | 1848.4940 | 102 / 1848 | 1848.49, 924.247, 616.165, 462.123, 369.699, 308.082, 264.071, 231.062, 205.388, 184.849, 168.045, 154.041, 142.192, 132.035, 123.233, 115.531, 108.735, 102.694, 97.2892, 92.4247 |
| 2460615.82995 | 14644 | 14247 | 1848.5127 | 102 / 1848 | 1848.51, 924.256, 616.171, 462.128, 369.702, 308.086, 264.073, 231.064, 205.39, 184.851, 168.047, 154.043, 142.193, 132.037, 123.234, 115.532, 108.736, 102.695, 97.2901, 92.4256 |
| 2460615.85912 | 14564 | 14247 | 1848.5419 | 104 / 1848 | 1848.54, 924.271, 616.181, 462.135, 369.708, 308.09, 264.077, 231.068, 205.393, 184.854, 168.049, 154.045, 142.196, 132.039, 123.236, 115.534, 108.738, 102.697, 97.2917, 92.4271 |
| 2460615.88065 | 14694 | 14247 | 1848.5634 | 102 / 1848 | 1848.56, 924.282, 616.188, 462.141, 369.713, 308.094, 264.08, 231.07, 205.396, 184.856, 168.051, 154.047, 142.197, 132.04, 123.238, 115.535, 108.739, 102.698, 97.2928, 92.4282 |
| 2460619.41811 | 14236 | 14247 | 1852.1009 | 103 / 1852 | 1852.1, 926.05, 617.367, 463.025, 370.42, 308.683, 264.586, 231.513, 205.789, 185.21, 168.373, 154.342, 142.469, 132.293, 123.473, 115.756, 108.947, 102.894, 97.479, 92.605 |
| 2460622.98888 | 13833 | 14247 | 1855.6717 | 100 / 1855 | 1855.67, 927.836, 618.557, 463.918, 371.134, 309.279, 265.096, 231.959, 206.186, 185.567, 168.697, 154.639, 142.744, 132.548, 123.711, 115.98, 109.157, 103.093, 97.6669, 92.7836 |
| 2460630.12480 | 12266 | 14247 | 1862.8076 | 97 / 1862 | 1862.81, 931.404, 620.936, 465.702, 372.562, 310.468, 266.115, 232.851, 206.979, 186.281, 169.346, 155.234, 143.293, 133.058, 124.187, 116.425, 109.577, 103.489, 98.0425, 93.1404 |
| 2460633.69066 | 14459 | 14247 | 1866.3734 | 101 / 1866 | 1866.37, 933.187, 622.125, 466.593, 373.275, 311.062, 266.625, 233.297, 207.375, 186.637, 169.67, 155.531, 143.567, 133.312, 124.425, 116.648, 109.787, 103.687, 98.2302, 93.3187 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1461.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:33:26Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:33:27Z: TOI-1461.01 (TIC 44631965, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:33:29Z: KELT KC02C16040 (type EA, P 3.5684647 d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:33:29Z: TOI-1461.01 (err); TOI-1461 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458767.3175: recovered, depth 14247 ± 285 ppm (catalogue 20261 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 16 repeat-candidate event(s); first at BJD 2458770.8840, ΔT = 3.567 d, 0 of 3 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1461.01: Gaia DR3 320523552351605632 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-1461.01: Teff 5975 K, R* 1.20 ± 0.10, M* 1.16 ± 0.12, ρ* 0.68 ± 0.18 ρ☉ (dwarf sequence, M_G 3.99, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-1461.01: 6 Gaia neighbour(s) within 52.5", contamination 1.41%; depth 14247 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 16 persistent event(s), 3 clean; BJD 2458770.8840 caution: manual exclude (within ±0.25 d); BJD 2458777.9889 suspect: manual exclude (in event), coarse point (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR2 z=-14.0, POS_CORR2 z=-16.3; BJD 2458778.0042 suspect: manual exclude (in event), momentum dump (within ±0.25 d), MOM_CENTR2 z=-13.7, POS_CORR2 z=-14.6; BJD 2458778.0209 suspect: manual exclude (in event), MOM_CENTR2 z=-12.3, POS_CORR2 z=-13.7 |
| Moving objects at screen-event epochs | inconclusive | 16 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 3 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1461.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-1461.01: TOI-1461 otype SB* (multiple) at 0.5" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1461-01.yaml
python -m cygnus.multi report campaigns/toi-1461-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits** (one period after the reference for E1, on-ephemeris for the rest). No new signal.

Source: `campaigns/toi-1461-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
