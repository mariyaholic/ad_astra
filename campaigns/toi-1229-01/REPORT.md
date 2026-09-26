<!-- cygnus:generated-draft -->
# Known-object test, TOI-1229.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1229-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #423, calibrate_screen #357, event_census #374, fetch_products #350, known_signal_recovery #362, moving_objects #417, period_aliases #375, prior_art #425, residual_screen #371, stellar_context #363, variability_guard #424
- Runner finished (UTC): 2026-09-26T10:07:11Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1229.01 (BJD 2459970.4916: recovered, depth 9984 ± 86 ppm (catalogue 11479 ppm)).
Outside the catalogued epoch the screen left 130 threshold entries forming **22 distinct event(s)**, **14 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2458602.5208 matches the catalogued transit's depth (9549 vs 9984 ppm), 1367.973 d later; 18 of 1367 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1229.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 140760434 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 74.130396 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -74.920333 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459970.491644 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 11479.375547 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 11.2567164 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.779 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-07-12 10:10:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000140760434-0250-s_lc.fits` | lightcurve | 61 | True | `7fc74300a7480752` | True |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | lightcurve | 11 | False | `55f9a5fb255098f2` | True |
| `tess2019140104343-s0012-0000000140760434-0144-s_lc.fits` | lightcurve | 12 | False | `dd0d769547022a5d` | True |
| `tess2019169103026-s0013-0000000140760434-0146-s_lc.fits` | lightcurve | 13 | False | `350cf1f3d91bae33` | True |
| `tess2020212050318-s0028-0000000140760434-0190-s_lc.fits` | lightcurve | 28 | False | `da389b4f0204ea59` | True |
| `tess2020238165205-s0029-0000000140760434-0193-s_lc.fits` | lightcurve | 29 | False | `6357d549f7ebb7b5` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000140760434-0250-s_lc.fits` | 2459970.49164 | recovered | 338 | 9984 ± 86 | 11479 | 0.06 |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | — | epoch not in this light curve | — | — | 11479 | — |
| `tess2019140104343-s0012-0000000140760434-0144-s_lc.fits` | — | epoch not in this light curve | — | — | 11479 | — |
| `tess2019169103026-s0013-0000000140760434-0146-s_lc.fits` | — | epoch not in this light curve | — | — | 11479 | — |
| `tess2020212050318-s0028-0000000140760434-0190-s_lc.fits` | — | epoch not in this light curve | — | — | 11479 | — |
| `tess2020238165205-s0029-0000000140760434-0193-s_lc.fits` | — | epoch not in this light curve | — | — | 11479 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023018032328-s0061-0000000140760434-0250-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019140104343-s0012-0000000140760434-0144-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2019169103026-s0013-0000000140760434-0146-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2020212050318-s0028-0000000140760434-0190-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020238165205-s0029-0000000140760434-0193-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 10000, 4h: 5000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019140104343-s0012-0000000140760434-0144-s_lc.fits` | 2458634.37060 | -0.01250 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000140760434-0193-s_lc.fits` | 2459111.41322 | -0.01060 | 90 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000140760434-0146-s_lc.fits` | 2458666.16043 | -0.01058 | 281 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000140760434-0193-s_lc.fits` | 2459111.60419 | -0.01053 | 195 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020212050318-s0028-0000000140760434-0190-s_lc.fits` | 2459079.72334 | -0.01047 | 288 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019140104343-s0012-0000000140760434-0144-s_lc.fits` | 2458634.24490 | -0.01020 | 161 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019140104343-s0012-0000000140760434-0144-s_lc.fits` | 2458634.46990 | -0.01017 | 111 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019140104343-s0012-0000000140760434-0144-s_lc.fits` | 2458634.38379 | -0.01002 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | 2458602.52084 | -0.00979 | 297 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000140760434-0146-s_lc.fits` | 2458665.95904 | -0.00831 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020212050318-s0028-0000000140760434-0190-s_lc.fits` | 2459079.92473 | -0.00770 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019169103026-s0013-0000000140760434-0146-s_lc.fits` | 2458665.94446 | -0.00656 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2020212050318-s0028-0000000140760434-0190-s_lc.fits` | 2459079.51640 | -0.00564 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | 2458602.73682 | -0.00429 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2020238165205-s0029-0000000140760434-0193-s_lc.fits` | 2459111.74377 | -0.00768 | 2 | SAP | 2, 3 | no |
| `tess2023018032328-s0061-0000000140760434-0250-s_lc.fits` | 2459981.81841 | -0.00651 | 2 | SAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000140760434-0193-s_lc.fits` | 2459088.35103 | -0.00649 | 2 | SAP | 1, 2, 3 | no |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | 2458623.86768 | -0.00518 | 2 | SAP | 2, 3 | no |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | 2458602.72987 | -0.00504 | 2 | SAP | 2, 3 | no |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | 2458623.82741 | -0.00487 | 2 | SAP | 2, 3 | no |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | 2458623.79407 | -0.00456 | 2 | SAP | 3 | no |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | 2458623.74129 | -0.00427 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2458602.52084 | 9549 | 9984 | 1367.9732 | 18 / 1367 | 1367.97, 683.987, 455.991, 341.993, 273.595, 227.995, 195.425, 170.997, 151.997, 136.797, 124.361, 113.998, 105.229, 91.1982, 85.4983, 80.469, 40.2345, 31.8133 |
| 2458634.24490 | 9316 | 9984 | 1336.2492 | 27 / 1336 | 1336.25, 668.125, 445.416, 334.062, 267.25, 222.708, 190.893, 167.031, 148.472, 133.625, 121.477, 111.354, 102.788, 95.4464, 89.0833, 83.5156, 74.2361, 70.3289, 66.8125, 63.6309 |
| 2458634.37060 | 9670 | 9984 | 1336.1235 | 25 / 1336 | 1336.12, 668.062, 445.375, 334.031, 267.225, 222.687, 190.875, 167.015, 148.458, 133.612, 121.466, 111.344, 102.779, 95.4374, 89.0749, 83.5077, 74.2291, 70.3223, 66.8062, 63.6249 |
| 2458634.38379 | 9676 | 9984 | 1336.1103 | 25 / 1336 | 1336.11, 668.055, 445.37, 334.028, 267.222, 222.685, 190.873, 167.014, 148.457, 133.611, 121.465, 111.343, 102.778, 95.4364, 89.074, 83.5069, 74.2283, 70.3216, 66.8055, 63.6243 |
| 2458634.46990 | 9046 | 9984 | 1336.0241 | 25 / 1336 | 1336.02, 668.012, 445.341, 334.006, 267.205, 222.671, 190.861, 167.003, 148.447, 133.602, 121.457, 111.335, 102.771, 95.4303, 89.0683, 83.5015, 74.2236, 70.3171, 66.8012, 63.6202 |
| 2458665.95904 | 6500 | 9984 | 1304.5350 | 23 / 1304 | 1304.54, 652.268, 434.845, 326.134, 260.907, 217.423, 186.362, 163.067, 144.948, 130.453, 118.594, 108.711, 93.1811, 86.969, 81.5334, 76.7374, 72.4742, 65.2268, 54.3556, 40.7667 |
| 2458666.16043 | 9795 | 9984 | 1304.3336 | 24 / 1304 | 1304.33, 652.167, 434.778, 326.083, 260.867, 217.389, 186.333, 163.042, 144.926, 130.433, 118.576, 108.695, 93.1667, 86.9556, 81.5209, 76.7255, 72.463, 65.2167, 54.3472, 42.0753 |
| 2459079.72334 | 9667 | 9984 | 890.7707 | 19 / 890 | 890.771, 445.385, 296.924, 222.693, 178.154, 148.462, 127.253, 111.346, 98.9745, 89.0771, 74.2309, 68.5208, 63.6265, 55.6732, 49.4873, 42.4177, 38.7292, 34.2604, 31.8132 |
| 2459079.92473 | 6401 | 9984 | 890.5693 | 7 / 890 | 890.569, 296.856, 178.114, 127.224, 98.9521, 42.4081, 38.7204 |
| 2459111.41322 | 9404 | 9984 | 859.0808 | 7 / 859 | 859.081, 286.36, 171.816, 95.4534, 78.0983, 57.2721, 31.8178 |
| 2459111.60419 | 9751 | 9984 | 858.8899 | 6 / 858 | 858.89, 286.297, 171.778, 95.4322, 57.2593, 31.8107 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1229.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:07:03Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:07:09Z: TOI-1229.01 (TIC 140760434, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:07:10Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:07:10Z: TOI-1229.01 (err); TOI-1229 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459970.4916: recovered, depth 9984 ± 86 ppm (catalogue 11479 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, 3.5, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 40%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 11 repeat-candidate event(s); first at BJD 2458602.5208, ΔT = 1367.973 d, 18 of 1367 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1367.97, 683.987, 455.991, 341.993, 273.595, 227.995, 195.425, 170.997, 151.997, 136.797, 124.361, 113.998 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1229.01: Gaia DR3 4649243686371932928 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1229.01: dwarf priors not applied — RUWE 3.6770322 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-1229.01: 48 Gaia neighbour(s) within 52.5", contamination 3.38%; depth 9984 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 14 persistent event(s), 6 clean; BJD 2458602.5208 suspect: SAP_BKG z=-14.8; BJD 2458634.2449 suspect: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), SAP_BKG z=-8.4; BJD 2458634.3706 suspect: coarse point (in event), manual exclude (in event), momentum dump (in event); BJD 2458634.3838 suspect: manual exclude (in event), momentum dump (in event), coarse point (within ±0.25 d) |
| Moving objects at screen-event epochs | passed | 14 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1229.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1229.01: TOI-1229.01 otype err (star_or_other) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1229-01.yaml
python -m cygnus.multi report campaigns/toi-1229-01.yaml
```
