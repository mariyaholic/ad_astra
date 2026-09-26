<!-- [private Drive store] -->
# Known-object test, TOI-585.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-585-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #185, calibrate_screen #129, event_census #136, fetch_products #128, known_signal_recovery #131, moving_objects #184, period_aliases #138, prior_art #187, residual_screen #135, stellar_context #132, variability_guard #186
- Runner finished (UTC): 2026-09-26T09:56:29Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-585.01 (BJD 2460009.6171: recovered, depth 15225 ± 55 ppm (catalogue 11569 ppm)).
Outside the catalogued epoch the screen left 117 threshold entries forming **37 distinct event(s)**, **12 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459992.9755 matches the catalogued transit's depth (15669 vs 15225 ppm), 16.641 d later; 2 of 16 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-585.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 190990336 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 134.373008 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -39.778423 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460009.617078 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 11569.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.835 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 8.9544 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-04-12 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | lightcurve | 62 | True | `fa98b4681b7efd71` | True |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | lightcurve | 9 | False | `ffb5a3926f25f9a8` | True |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | lightcurve | 89 | False | `36e989ef5509b32c` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460009.61708 | recovered | 145 | 15225 ± 55 | 11569 | -0.02 |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | — | epoch not in this light curve | — | — | 11569 | — |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | — | epoch not in this light curve | — | — | 11569 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 5000, 4h: 2000, 8h: 5000 |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2459992.97547 | -0.01581 | 141 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460004.06993 | -0.01569 | 140 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460741.85934 | -0.01557 | 140 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2459998.52133 | -0.01541 | 140 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460730.76496 | -0.01541 | 141 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460736.31217 | -0.01534 | 142 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460719.66906 | -0.01509 | 140 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460725.21703 | -0.01509 | 141 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | 2458550.67954 | -0.01475 | 141 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | 2458545.13235 | -0.01452 | 141 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | 2458561.77517 | -0.01439 | 139 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | 2458567.32156 | -0.01429 | 140 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | 2458553.17117 | -0.00272 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460007.01020 | -0.00270 | 2 | SAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460745.86345 | -0.00266 | 2 | SAP | 1, 2, 3 | no |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460007.20811 | -0.00259 | 3 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460006.89492 | -0.00259 | 2 | SAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460006.71575 | -0.00256 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460006.77270 | -0.00255 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | 2458560.23979 | -0.00255 | 2 | SAP | 1, 2, 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460718.22321 | -0.00249 | 3 | PDCSAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460718.23085 | -0.00243 | 3 | PDCSAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460718.21488 | -0.00242 | 6 | PDCSAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460725.50939 | -0.00237 | 2 | SAP | 1, 2 | no |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460007.04353 | -0.00234 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460007.14978 | -0.00231 | 3 | SAP | 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460718.24127 | -0.00230 | 2 | PDCSAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460739.63020 | -0.00229 | 2 | SAP | 1, 2, 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460718.39405 | -0.00228 | 2 | PDCSAP | 3 | no |
| `tess2019058134432-s0009-0000000190990336-0139-s_lc.fits` | 2458559.83424 | -0.00227 | 2 | PDCSAP | 2, 3 | no |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2460006.75325 | -0.00223 | 2 | SAP | 3 | no |
| `tess2023043185947-s0062-0000000190990336-0254-s_lc.fits` | 2459989.50738 | -0.00221 | 2 | PDCSAP | 1 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460718.19127 | -0.00218 | 4 | PDCSAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460739.11909 | -0.00210 | 2 | PDCSAP | 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460718.26349 | -0.00207 | 2 | PDCSAP | 2, 3 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460732.80107 | -0.00203 | 2 | SAP | 1 | no |
| `tess2025042113628-s0089-0000000190990336-0286-s_lc.fits` | 2460725.41773 | -0.00202 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459992.97547 | 15669 | 15225 | 16.6410 | 2 / 16 | 16.641, 5.547 |
| 2459998.52133 | 15310 | 15225 | 11.0951 | 2 / 11 | 11.0951, 5.5475 |
| 2460004.06993 | 15505 | 15225 | 5.5465 | 0 / 5 |  |
| 2458545.13235 | 14471 | 15225 | 1464.4841 | 51 / 1464 | 1464.48, 732.242, 488.161, 366.121, 292.897, 244.081, 209.212, 183.06, 162.72, 146.448, 133.135, 122.04, 112.653, 104.606, 97.6323, 91.5303, 86.1461, 81.3602, 77.0781, 73.2242 |
| 2458550.67954 | 14398 | 15225 | 1458.9369 | 18 / 1458 | 1458.94, 486.312, 291.787, 208.42, 162.104, 132.631, 112.226, 97.2625, 85.8198, 76.7862, 69.4732, 63.432, 58.3575, 54.0347, 50.3082, 47.0625, 44.2102, 5.5473 |
| 2458561.77517 | 14283 | 15225 | 1447.8413 | 26 / 1447 | 1447.84, 482.614, 289.568, 206.834, 160.871, 131.622, 111.372, 96.5228, 85.1671, 76.2022, 68.9448, 62.9496, 57.9137, 53.6238, 49.9256, 46.7046, 43.874, 41.3669, 39.1308, 37.1241 |
| 2458567.32156 | 14173 | 15225 | 1442.2949 | 55 / 1442 | 1442.29, 721.147, 480.765, 360.574, 288.459, 240.382, 206.042, 180.287, 160.255, 144.23, 131.118, 120.191, 110.946, 103.021, 96.153, 90.1434, 84.8409, 80.1275, 75.9103, 72.1147 |
| 2460719.66906 | 14998 | 15225 | 710.0526 | 20 / 710 | 710.053, 355.026, 236.684, 177.513, 142.011, 118.342, 101.436, 88.7566, 78.8947, 71.0053, 64.5502, 59.1711, 54.6194, 50.718, 47.3368, 44.3783, 33.812, 22.1891, 11.0946, 5.5473 |
| 2460725.21703 | 14977 | 15225 | 715.6006 | 23 / 715 | 715.601, 357.8, 238.534, 178.9, 143.12, 119.267, 102.229, 89.4501, 79.5112, 71.5601, 65.0546, 59.6334, 55.0462, 51.1143, 47.7067, 44.725, 42.0942, 39.7556, 37.6632, 35.78 |
| 2460730.76496 | 15235 | 15225 | 721.1485 | 32 / 721 | 721.149, 360.574, 240.383, 180.287, 144.23, 120.191, 103.021, 90.1436, 80.1276, 72.1149, 65.559, 60.0957, 55.473, 51.5106, 48.0766, 45.0718, 42.4205, 40.0638, 37.9552, 36.0574 |
| 2460736.31217 | 15185 | 15225 | 726.6957 | 39 / 726 | 726.696, 363.348, 242.232, 181.674, 145.339, 121.116, 103.814, 90.837, 80.744, 72.6696, 66.0632, 60.558, 55.8997, 51.9068, 48.4464, 45.4185, 42.7468, 40.372, 38.2471, 36.3348 |
| 2460741.85934 | 15493 | 15225 | 732.2429 | 34 / 732 | 732.243, 366.122, 244.081, 183.061, 146.449, 122.04, 104.606, 91.5304, 81.3603, 73.2243, 66.5675, 61.0202, 56.3264, 52.3031, 48.8162, 45.7652, 43.0731, 40.6802, 38.5391, 36.6121 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-585.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:56:26Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:56:27Z: TOI-585.01 (TIC 190990336, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:56:28Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T09:56:28Z: TOI-585.01 (err); HD  76859 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460009.6171: recovered, depth 15225 ± 55 ppm (catalogue 11569 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 90%, 90%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 12 repeat-candidate event(s); first at BJD 2459992.9755, ΔT = 16.641 d, 2 of 16 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (16.641, 5.547 d); duration likelihood under Gaia priors (circular orbits) peaks at 5.55 d (weight 0.64) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-585.01: Gaia DR3 5620894588719423616 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-585.01: Teff 6277 K, R* 1.45 ± 0.12, M* 1.31 ± 0.13, ρ* 0.43 ± 0.11 ρ☉ (dwarf sequence, M_G 3.33, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-585.01: 48 Gaia neighbour(s) within 52.5", contamination 1.08%; depth 15225 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 12 persistent event(s), 6 clean; BJD 2458545.1324 suspect: SAP_BKG z=+26.7; BJD 2458561.7752 suspect: SAP_BKG z=-7.8; BJD 2458567.3216 suspect: SAP_BKG z=-8.3; BJD 2460725.2170 suspect: MOM_CENTR1 z=-6.1, SAP_BKG z=-7.0 |
| Moving objects at screen-event epochs | inconclusive | 12 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-585.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-585.01: HD  76859 otype * (star_or_other) at 0.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-585-01.yaml
python -m cygnus.multi report campaigns/toi-585-01.yaml
```
