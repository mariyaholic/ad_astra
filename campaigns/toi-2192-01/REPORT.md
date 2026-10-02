<!-- cygnus:generated-draft -->
# Known-object test, TOI-2192.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2192-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4110, calibrate_screen #4082, event_census #4088, fetch_independent #4105, fetch_products #4077, known_signal_recovery #4084, moving_objects #4101, period_aliases #4089, prior_art #4116, residual_screen #4086, stellar_context #4085, variability_guard #4112
- Runner finished (UTC): 2026-09-30T21:38:33Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2192.01 (BJD 2459039.4623: recovered, depth 8030 ± 393 ppm (catalogue 10552 ppm); BJD 2459045.7266: recovered, depth 7847 ± 436 ppm (catalogue 10552 ppm); BJD 2459051.9910: recovered, depth 8419 ± 400 ppm (catalogue 10552 ppm); BJD 2459058.2553: recovered, depth 7434 ± 426 ppm (catalogue 10552 ppm); BJD 2459064.5197: recovered, depth 7619 ± 438 ppm (catalogue 10552 ppm); BJD 2459070.7840: recovered, depth 9049 ± 448 ppm (catalogue 10552 ppm); BJD 2459077.0483: recovered, depth 9579 ± 444 ppm (catalogue 10552 ppm); BJD 2459083.3127: recovered, depth 9185 ± 447 ppm (catalogue 10552 ppm); BJD 2460129.4582: recovered, depth 9010 ± 447 ppm (catalogue 10552 ppm); BJD 2460135.7225: recovered, depth 8113 ± 459 ppm (catalogue 10552 ppm); BJD 2460141.9869: recovered, depth 10196 ± 407 ppm (catalogue 10552 ppm); BJD 2460148.2512: recovered, depth 8725 ± 425 ppm (catalogue 10552 ppm); BJD 2460160.7799: recovered, depth 8474 ± 436 ppm (catalogue 10552 ppm); BJD 2460167.0442: gap (catalogue 10552 ppm); BJD 2460173.3086: partial, depth 7936 ± 448 ppm (catalogue 10552 ppm); BJD 2460179.5729: gap (catalogue 10552 ppm); BJD 2460862.3864: not recovered, depth 5172 ± 1336 ppm (catalogue 10552 ppm); BJD 2460868.6508: gap (catalogue 10552 ppm); BJD 2460874.9151: recovered, depth 8770 ± 522 ppm (catalogue 10552 ppm); BJD 2460881.1795: recovered, depth 3337 ± 1808 ppm (catalogue 10552 ppm); BJD 2460887.4438: recovered, depth 8363 ± 429 ppm (catalogue 10552 ppm); BJD 2460893.7082: not recovered, depth 6780 ± 445 ppm (catalogue 10552 ppm); BJD 2460899.9725: recovered, depth 8458 ± 417 ppm (catalogue 10552 ppm); BJD 2460906.2368: recovered, depth 9549 ± 429 ppm (catalogue 10552 ppm)).
Outside the catalogued epoch the screen left 52 threshold entries forming **14 distinct event(s)**, **7 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460168.6496 matches the catalogued transit's depth (4101 vs 8030 ppm), 1129.167 d later; 13 of 1129 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2192.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 277890574 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 353.281713 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -76.819155 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459039.462278 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 6.2643442 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10552.2490654 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.8202596 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.5625 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-12-05 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2020186164531-s0027-0000000277890574-0189-s_lc.fits` | lightcurve | 27 | True | `ec4797a7331b14db` | True |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | lightcurve | 28 | False | `a81d745dcf491eea` | True |
| `tess2023181235917-s0067-0000000277890574-0261-s_lc.fits` | lightcurve | 67 | False | `0a4642f6c549bd9c` | True |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | lightcurve | 68 | False | `a4871a6db9aaddb6` | True |
| `tess2025180145000-s0094-0000000277890574-0291-s_lc.fits` | lightcurve | 94 | False | `2efc35aa355ec220` | True |
| `tess2025206162959-s0095-0000000277890574-0292-s_lc.fits` | lightcurve | 95 | False | `7d502b116ad94eb0` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020186164531-s0027-0000000277890574-0189-s_lc.fits` | 2459039.46228 | recovered | 115 | 8030 ± 393 | 10552 | 0.49 |
| `tess2020186164531-s0027-0000000277890574-0189-s_lc.fits` | 2459045.72662 | recovered | 114 | 7847 ± 436 | 10552 | 0.12 |
| `tess2020186164531-s0027-0000000277890574-0189-s_lc.fits` | 2459051.99097 | recovered | 115 | 8419 ± 400 | 10552 | 0.26 |
| `tess2020186164531-s0027-0000000277890574-0189-s_lc.fits` | 2459058.25531 | recovered | 115 | 7434 ± 426 | 10552 | -0.66 |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459064.51965 | recovered | 114 | 7619 ± 438 | 10552 | -0.03 |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459070.78400 | recovered | 115 | 9049 ± 448 | 10552 | -0.51 |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459077.04834 | recovered | 114 | 9579 ± 444 | 10552 | -0.51 |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459083.31269 | recovered | 115 | 9185 ± 447 | 10552 | -0.24 |
| `tess2023181235917-s0067-0000000277890574-0261-s_lc.fits` | 2460129.45817 | recovered | 114 | 9010 ± 447 | 10552 | -0.17 |
| `tess2023181235917-s0067-0000000277890574-0261-s_lc.fits` | 2460135.72251 | recovered | 115 | 8113 ± 459 | 10552 | -0.55 |
| `tess2023181235917-s0067-0000000277890574-0261-s_lc.fits` | 2460141.98686 | recovered | 115 | 10196 ± 407 | 10552 | -0.12 |
| `tess2023181235917-s0067-0000000277890574-0261-s_lc.fits` | 2460148.25120 | recovered | 114 | 8725 ± 425 | 10552 | 0.30 |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460160.77989 | recovered | 115 | 8474 ± 436 | 10552 | -0.39 |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460167.04423 | gap | 0 | — | 10552 | — |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460173.30858 | partial | 115 | 7936 ± 448 | 10552 | -0.88 |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460179.57292 | gap | 0 | — | 10552 | — |
| `tess2025180145000-s0094-0000000277890574-0291-s_lc.fits` | 2460862.38644 | not_recovered | 11 | 5172 ± 1336 | 10552 | — |
| `tess2025180145000-s0094-0000000277890574-0291-s_lc.fits` | 2460868.65078 | gap | 0 | — | 10552 | — |
| `tess2025180145000-s0094-0000000277890574-0291-s_lc.fits` | 2460874.91513 | recovered | 79 | 8770 ± 522 | 10552 | 0.15 |
| `tess2025180145000-s0094-0000000277890574-0291-s_lc.fits` | 2460881.17947 | recovered | 8 | 3337 ± 1808 | 10552 | -1.60 |
| `tess2025206162959-s0095-0000000277890574-0292-s_lc.fits` | 2460887.44382 | recovered | 115 | 8363 ± 429 | 10552 | -0.41 |
| `tess2025206162959-s0095-0000000277890574-0292-s_lc.fits` | 2460893.70816 | not_recovered | 115 | 6780 ± 445 | 10552 | — |
| `tess2025206162959-s0095-0000000277890574-0292-s_lc.fits` | 2460899.97251 | recovered | 114 | 8458 ± 417 | 10552 | -0.37 |
| `tess2025206162959-s0095-0000000277890574-0292-s_lc.fits` | 2460906.23685 | recovered | 115 | 9549 ± 429 | 10552 | -0.58 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020186164531-s0027-0000000277890574-0189-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2023181235917-s0067-0000000277890574-0261-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2025180145000-s0094-0000000277890574-0291-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025206162959-s0095-0000000277890574-0292-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460165.22739 | -0.01812 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460179.26462 | -0.01800 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459084.92201 | -0.01596 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460155.02889 | -0.01528 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460168.64957 | -0.01499 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459062.22310 | -0.01396 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2020186164531-s0027-0000000277890574-0189-s_lc.fits` | 2459053.94050 | -0.01263 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459061.90782 | -0.01436 | 3 | PDCSAP | 2, 3 | no |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460164.95934 | -0.01388 | 2 | PDCSAP | 3 | no |
| `tess2025180145000-s0094-0000000277890574-0291-s_lc.fits` | 2460867.72532 | -0.01332 | 2 | SAP | 2 | no |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459085.53033 | -0.01249 | 2 | SAP | 2, 3 | no |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459084.98312 | -0.01224 | 2 | SAP | 2, 3 | no |
| `tess2020212050318-s0028-0000000277890574-0190-s_lc.fits` | 2459085.55533 | -0.01102 | 2 | SAP | 2, 3 | no |
| `tess2023209231226-s0068-0000000277890574-0262-s_lc.fits` | 2460165.48850 | -0.01085 | 2 | SAP | 1, 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460168.64957 | 4101 | 8030 | 1129.1668 | 13 / 1129 | 1129.17, 564.583, 376.389, 282.292, 225.833, 188.195, 161.31, 125.463, 112.917, 94.0972, 80.6548, 75.2778, 59.4298 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2192.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:38:23Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:38:26Z: TOI-2192.01 (TIC 277890574, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:38:28Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T21:38:31Z: UCAC4 066-034136 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459039.4623: recovered, depth 8030 ± 393 ppm (catalogue 10552 ppm); BJD 2459045.7266: recovered, depth 7847 ± 436 ppm (catalogue 10552 ppm); BJD 2459051.9910: recovered, depth 8419 ± 400 ppm (catalogue 10552 ppm); BJD 2459058.2553: recovered, depth 7434 ± 426 ppm (catalogue 10552 ppm); BJD 2459064.5197: recovered, depth 7619 ± 438 ppm (catalogue 10552 ppm); BJD 2459070.7840: recovered, depth 9049 ± 448 ppm (catalogue 10552 ppm); BJD 2459077.0483: recovered, depth 9579 ± 444 ppm (catalogue 10552 ppm); BJD 2459083.3127: recovered, depth 9185 ± 447 ppm (catalogue 10552 ppm); BJD 2460129.4582: recovered, depth 9010 ± 447 ppm (catalogue 10552 ppm); BJD 2460135.7225: recovered, depth 8113 ± 459 ppm (catalogue 10552 ppm); BJD 2460141.9869: recovered, depth 10196 ± 407 ppm (catalogue 10552 ppm); BJD 2460148.2512: recovered, depth 8725 ± 425 ppm (catalogue 10552 ppm); BJD 2460160.7799: recovered, depth 8474 ± 436 ppm (catalogue 10552 ppm); BJD 2460167.0442: gap (catalogue 10552 ppm); BJD 2460173.3086: partial, depth 7936 ± 448 ppm (catalogue 10552 ppm); BJD 2460179.5729: gap (catalogue 10552 ppm); BJD 2460862.3864: not recovered, depth 5172 ± 1336 ppm (catalogue 10552 ppm); BJD 2460868.6508: gap (catalogue 10552 ppm); BJD 2460874.9151: recovered, depth 8770 ± 522 ppm (catalogue 10552 ppm); BJD 2460881.1795: recovered, depth 3337 ± 1808 ppm (catalogue 10552 ppm); BJD 2460887.4438: recovered, depth 8363 ± 429 ppm (catalogue 10552 ppm); BJD 2460893.7082: not recovered, depth 6780 ± 445 ppm (catalogue 10552 ppm); BJD 2460899.9725: recovered, depth 8458 ± 417 ppm (catalogue 10552 ppm); BJD 2460906.2368: recovered, depth 9549 ± 429 ppm (catalogue 10552 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460168.6496, ΔT = 1129.167 d, 13 of 1129 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1129.17, 564.583, 376.389, 282.292, 225.833, 188.195, 161.31, 125.463, 112.917, 94.0972, 80.6548, 75.2778 … d); duration likelihood under Gaia priors (circular orbits) peaks at 59.4 d (weight 0.29) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2192.01: Gaia DR3 6377434729802003072 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2192.01: Teff 5228 K, R* 0.95 ± 0.08, M* 0.97 ± 0.10, ρ* 1.12 ± 0.29 ρ☉ (dwarf sequence, M_G 4.89, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2192.01: 6 Gaia neighbour(s) within 52.5", contamination 34.47%; depth 8030 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 6377434901600696704, 43.1", ΔG 0.98); a centroid test is needed |
| Pointing and quality census per event | failed | 7 persistent event(s), 0 clean; BJD 2459053.9405 suspect: SAP_BKG z=+5.2; BJD 2459062.2231 suspect: POS_CORR1 z=-8.2, POS_CORR2 z=-8.9; BJD 2459084.9220 suspect: SAP_BKG z=+19.5; BJD 2460155.0289 suspect: scattered light 2 (in event), MOM_CENTR1 z=-6.0, POS_CORR1 z=-7.8, POS_CORR2 z=-11.4, SAP_BKG z=+158.6 |
| Moving objects at screen-event epochs | passed | 7 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-2192.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2192.01: UCAC4 066-034136 otype * (star_or_other) at 0.4" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2192-01.yaml
python -m cygnus.multi report campaigns/toi-2192-01.yaml
```
