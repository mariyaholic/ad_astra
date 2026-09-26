<!-- [private Drive store] -->
# Known-object test, TOI-4427.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4427-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #993, calibrate_screen #954, event_census #963, fetch_products #952, known_signal_recovery #957, moving_objects #982, period_aliases #964, prior_art #1001, residual_screen #959, stellar_context #958, variability_guard #994
- Runner finished (UTC): 2026-09-26T10:27:55Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4427.01 (BJD 2459940.4642: recovered, depth 17619 ± 238 ppm (catalogue 20288 ppm)).
Outside the catalogued epoch the screen left 164 threshold entries forming **37 distinct event(s)**, **22 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459945.0832 matches the catalogued transit's depth (16909 vs 17619 ppm), 4.597 d later; 0 of 4 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4427.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 207339000 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 135.049261 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 72.147747 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459940.464211 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 20287.618268 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.7008637 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.3427 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-12-09 12:03:42 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000207339000-0249-s_lc.fits` | lightcurve | 60 | True | `66bc625a5ba07ae6` | True |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | lightcurve | 40 | False | `2ae2e0c9bc1af81d` | True |
| `tess2021364111932-s0047-0000000207339000-0218-s_lc.fits` | lightcurve | 47 | False | `2fc93435e69286f0` | True |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | lightcurve | 53 | False | `d7a6ea51c5317948` | True |
| `tess2024003055635-s0074-0000000207339000-0269-s_lc.fits` | lightcurve | 74 | False | `56b90af97a87cbfa` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022357055054-s0060-0000000207339000-0249-s_lc.fits` | 2459940.46421 | recovered | 81 | 17619 ± 238 | 20288 | 0.54 |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | — | epoch not in this light curve | — | — | 20288 | — |
| `tess2021364111932-s0047-0000000207339000-0218-s_lc.fits` | — | epoch not in this light curve | — | — | 20288 | — |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | — | epoch not in this light curve | — | — | 20288 | — |
| `tess2024003055635-s0074-0000000207339000-0269-s_lc.fits` | — | epoch not in this light curve | — | — | 20288 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022357055054-s0060-0000000207339000-0249-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 5000 |
| `tess2021364111932-s0047-0000000207339000-0218-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2024003055635-s0074-0000000207339000-0269-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 2459751.11676 | -0.01919 | 67 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000207339000-0218-s_lc.fits` | 2459603.33126 | -0.01916 | 64 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000207339000-0269-s_lc.fits` | 2460319.16430 | -0.01897 | 64 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000207339000-0249-s_lc.fits` | 2459958.93951 | -0.01886 | 66 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 2459746.49396 | -0.01882 | 64 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459390.89183 | -0.01877 | 67 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459395.50843 | -0.01871 | 67 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000207339000-0269-s_lc.fits` | 2460337.63361 | -0.01870 | 64 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 2459755.73472 | -0.01866 | 63 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000207339000-0249-s_lc.fits` | 2459949.70268 | -0.01860 | 63 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000207339000-0218-s_lc.fits` | 2459598.71117 | -0.01860 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 2459760.35270 | -0.01849 | 65 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000207339000-0269-s_lc.fits` | 2460323.77820 | -0.01841 | 63 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000207339000-0218-s_lc.fits` | 2459589.47719 | -0.01823 | 64 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022357055054-s0060-0000000207339000-0249-s_lc.fits` | 2459945.08320 | -0.01777 | 67 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021364111932-s0047-0000000207339000-0218-s_lc.fits` | 2459584.85842 | -0.01774 | 69 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459409.36528 | -0.01761 | 65 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 2459764.97140 | -0.01760 | 64 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459418.60074 | -0.01752 | 65 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 2459755.69098 | -0.01103 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459401.70628 | -0.00921 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459400.59518 | -0.00746 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024003055635-s0074-0000000207339000-0269-s_lc.fits` | 2460318.71430 | -0.00894 | 2 | SAP | 3 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459400.31324 | -0.00851 | 2 | SAP | 1 | no |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 2459765.01862 | -0.00844 | 2 | SAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459400.57851 | -0.00843 | 2 | PDCSAP | 2 | no |
| `tess2022164095748-s0053-0000000207339000-0226-s_lc.fits` | 2459760.30478 | -0.00759 | 2 | SAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459401.80489 | -0.00750 | 2 | SAP | 2, 3 | no |
| `tess2022357055054-s0060-0000000207339000-0249-s_lc.fits` | 2459949.65338 | -0.00744 | 2 | SAP | 2, 3 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459400.69796 | -0.00731 | 2 | SAP | 2 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459413.18543 | -0.00730 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459401.80906 | -0.00729 | 2 | SAP | 2, 3 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459400.42990 | -0.00715 | 2 | PDCSAP | 1, 2 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459400.49101 | -0.00707 | 2 | PDCSAP | 2 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459396.64522 | -0.00700 | 2 | SAP | 1, 2 | no |
| `tess2021175071901-s0040-0000000207339000-0211-s_lc.fits` | 2459391.15780 | -0.00666 | 2 | PDCSAP | 3 | no |
| `tess2022357055054-s0060-0000000207339000-0249-s_lc.fits` | 2459962.37143 | -0.00594 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459945.08320 | 16909 | 17619 | 4.5966 | 0 / 4 |  |
| 2459949.70268 | 16909 | 17619 | 9.2161 | 0 / 9 |  |
| 2459958.93951 | 17418 | 17619 | 18.4529 | 0 / 18 |  |
| 2459390.89183 | 18013 | 17619 | 549.5948 | 7 / 549 | 549.595, 274.797, 137.399, 109.919, 78.5135, 32.3291, 4.6184 |
| 2459395.50843 | 16835 | 17619 | 544.9782 | 7 / 544 | 544.978, 272.489, 136.244, 108.996, 77.854, 9.2369, 4.6185 |
| 2459409.36528 | 16864 | 17619 | 531.1213 | 7 / 531 | 531.121, 265.561, 106.224, 53.1121, 40.8555, 23.0922, 4.6184 |
| 2459418.60074 | 16137 | 17619 | 521.8859 | 7 / 521 | 521.886, 260.943, 130.471, 104.377, 52.1886, 40.1451, 4.6185 |
| 2459584.85842 | 16804 | 17619 | 355.6282 | 6 / 355 | 355.628, 118.543, 71.1256, 50.804, 32.3298, 4.6185 |
| 2459589.47719 | 17140 | 17619 | 351.0094 | 11 / 351 | 351.009, 175.505, 117.003, 87.7524, 70.2019, 58.5016, 50.1442, 25.0721, 18.4742, 9.2371, 4.6185 |
| 2459598.71117 | 18163 | 17619 | 341.7754 | 4 / 341 | 341.775, 170.888, 113.925, 85.4439 |
| 2459603.33126 | 17174 | 17619 | 337.1553 | 4 / 337 | 337.155, 168.578, 112.385, 84.2888 |
| 2459746.49396 | 17471 | 17619 | 193.9926 | 5 / 193 | 193.993, 96.9963, 64.6642, 27.7132, 13.8566 |
| 2459751.11676 | 17783 | 17619 | 189.3698 | 0 / 189 |  |
| 2459755.69098 | 9690 | 17619 | 184.7956 | 5 / 184 | 184.796, 92.3978, 61.5985, 46.1989, 36.9591 |
| 2459755.73472 | 17764 | 17619 | 184.7519 | 7 / 184 | 184.752, 92.3759, 61.584, 46.188, 36.9504, 23.094, 18.4752 |
| 2459760.35270 | 17301 | 17619 | 180.1339 | 6 / 180 | 180.134, 90.067, 60.0446, 45.0335, 30.0223, 13.8565 |
| 2459764.97140 | 16507 | 17619 | 175.5152 | 4 / 175 | 175.515, 87.7576, 58.5051, 25.0736 |
| 2460319.16430 | 17023 | 17619 | 378.6777 | 7 / 378 | 378.678, 189.339, 126.226, 94.6694, 63.113, 54.0968, 47.3347 |
| 2460323.77820 | 17573 | 17619 | 383.2916 | 2 / 383 | 383.292, 127.764 |
| 2460337.63361 | 17771 | 17619 | 397.1470 | 4 / 397 | 397.147, 198.573, 99.2868, 79.4294 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4427.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): 1 match(es) in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:27:51Z: TOI-4427 b (host TOI-4427)
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:27:53Z: TOI-4427.01 (TIC 207339000, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:27:54Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:27:54Z: TOI-4427b (Pl); UCAC4 811-018805 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459940.4642: recovered, depth 17619 ± 238 ppm (catalogue 20288 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 20%, 10%, 0%, 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 20 repeat-candidate event(s); first at BJD 2459945.0832, ΔT = 4.597 d, 0 of 4 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4427.01: Gaia DR3 1119137502311125248 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4427.01: Teff 5292 K, R* 0.86 ± 0.07, M* 0.90 ± 0.09, ρ* 1.44 ± 0.37 ρ☉ (dwarf sequence, M_G 5.33, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-4427.01: 1 Gaia neighbour(s) within 52.5", contamination 0.23%; depth 17619 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 22 persistent event(s), 11 clean; BJD 2459949.7027 suspect: argabrightening (within ±0.25 d), coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=+6.8, POS_CORR1 z=+6.6, SAP_BKG z=+36.8; BJD 2459390.8918 suspect: earth point (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR2 z=-6.1, POS_CORR2 z=-7.6, SAP_BKG z=-49.0; BJD 2459409.3653 suspect: SAP_BKG z=-10.1; BJD 2459418.6007 suspect: SAP_BKG z=-13.3 |
| Moving objects at screen-event epochs | passed | 22 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-4427.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4427.01: TOI-4427b otype Pl (star_or_other) at 0.7" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4427-01.yaml
python -m cygnus.multi report campaigns/toi-4427-01.yaml
```
