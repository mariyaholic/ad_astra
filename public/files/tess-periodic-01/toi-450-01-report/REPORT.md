<!-- [private Drive store] -->
# Known-object test, TOI-450.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-450-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #457, calibrate_screen #358, event_census #378, fetch_products #354, known_signal_recovery #366, moving_objects #446, period_aliases #379, prior_art #461, residual_screen #372, stellar_context #367, variability_guard #458
- Runner finished (UTC): 2026-09-26T10:08:40Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-450.01 (BJD 2459182.4874: recovered, depth 35519 ± 550 ppm (catalogue 56326 ppm)).
Outside the catalogued epoch the screen left 147 threshold entries forming **38 distinct event(s)**, **17 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459193.2015 matches the catalogued transit's depth (34618 vs 35519 ppm), 10.683 d later; 0 of 10 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-450.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 77951245 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 79.005088 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -31.412694 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459182.487384 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 56325.9173745 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.1121584 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.4258 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2021-10-29 12:59:15 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | lightcurve | 32 | True | `bb2f5128e31dbaf9` | True |
| `tess2018319095959-s0005-0000000077951245-0125-s_lc.fits` | lightcurve | 5 | False | `3f2c0c200085bb77` | True |
| `tess2018349182500-s0006-0000000077951245-0126-s_lc.fits` | lightcurve | 6 | False | `ec937220aa123fcf` | True |
| `tess2025312202959-s0098-0000000077951245-0298-s_lc.fits` | lightcurve | 98 | False | `565ae25d11daa2c8` | True |
| `tess2026192185000-s0106-0000000077951245-0308-s_lc.fits` | lightcurve | 106 | False | `bd8c440b4f612c00` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459182.48738 | recovered | 63 | 35519 ± 550 | 56326 | 0.75 |
| `tess2018319095959-s0005-0000000077951245-0125-s_lc.fits` | — | epoch not in this light curve | — | — | 56326 | — |
| `tess2018349182500-s0006-0000000077951245-0126-s_lc.fits` | — | epoch not in this light curve | — | — | 56326 | — |
| `tess2025312202959-s0098-0000000077951245-0298-s_lc.fits` | — | epoch not in this light curve | — | — | 56326 | — |
| `tess2026192185000-s0106-0000000077951245-0308-s_lc.fits` | — | epoch not in this light curve | — | — | 56326 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2018319095959-s0005-0000000077951245-0125-s_lc.fits` | — | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2018349182500-s0006-0000000077951245-0126-s_lc.fits` | 5 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2025312202959-s0098-0000000077951245-0298-s_lc.fits` | 7 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026192185000-s0106-0000000077951245-0308-s_lc.fits` | — | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000077951245-0298-s_lc.fits` | 2461036.14365 | -0.05574 | 32 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000077951245-0308-s_lc.fits` | 2461239.71428 | -0.05327 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000077951245-0298-s_lc.fits` | 2461025.42508 | -0.05279 | 32 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000077951245-0298-s_lc.fits` | 2460993.28116 | -0.05187 | 32 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000077951245-0298-s_lc.fits` | 2461014.71057 | -0.05178 | 32 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000077951245-0126-s_lc.fits` | 2458475.30651 | -0.05174 | 28 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000077951245-0126-s_lc.fits` | 2458486.02849 | -0.04897 | 34 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018319095959-s0005-0000000077951245-0125-s_lc.fits` | 2458443.17045 | -0.04737 | 39 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018319095959-s0005-0000000077951245-0125-s_lc.fits` | 2458453.88305 | -0.04555 | 40 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000077951245-0308-s_lc.fits` | 2461239.73512 | -0.04403 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459193.20147 | -0.04331 | 53 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000077951245-0126-s_lc.fits` | 2458475.32873 | -0.04116 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000077951245-0126-s_lc.fits` | 2458475.33429 | -0.03491 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000077951245-0308-s_lc.fits` | 2461239.69761 | -0.03030 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2018349182500-s0006-0000000077951245-0126-s_lc.fits` | 2458486.00141 | -0.02599 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459199.63960 | -0.01529 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459187.51328 | -0.01450 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459200.03473 | -0.01842 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459200.04515 | -0.01815 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459200.05070 | -0.01808 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459200.07293 | -0.01667 | 2 | PDCSAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459200.05765 | -0.01588 | 4 | PDCSAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459174.30971 | -0.01548 | 11 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459199.42988 | -0.01473 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459199.97987 | -0.01462 | 2 | PDCSAP | 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459199.53960 | -0.01450 | 2 | PDCSAP+SAP | 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459200.01321 | -0.01443 | 2 | PDCSAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459174.37151 | -0.01402 | 2 | PDCSAP | 1 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459195.80770 | -0.01356 | 2 | PDCSAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459199.88404 | -0.01352 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459199.79724 | -0.01338 | 3 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459199.91598 | -0.01334 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459199.90904 | -0.01329 | 2 | PDCSAP+SAP | 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459174.31526 | -0.01319 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459199.41738 | -0.01314 | 2 | SAP | 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459200.06390 | -0.01305 | 3 | PDCSAP | 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459192.96883 | -0.01267 | 2 | PDCSAP | 2, 3 | no |
| `tess2020324010417-s0032-0000000077951245-0200-s_lc.fits` | 2459174.36179 | -0.01230 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459193.20147 | 34618 | 35519 | 10.6826 | 0 / 10 |  |
| 2458443.17045 | 30371 | 35519 | 739.3484 | 5 / 739 | 739.348, 246.45, 147.87, 105.621, 49.2899 |
| 2458453.88305 | 32425 | 35519 | 728.6358 | 10 / 728 | 728.636, 364.318, 242.879, 182.159, 145.727, 104.091, 91.0795, 72.8636, 52.0454, 45.5397 |
| 2458475.30651 | 32093 | 35519 | 707.2123 | 8 / 707 | 707.212, 353.606, 235.737, 176.803, 141.442, 117.869, 78.5791, 70.7212 |
| 2458475.32873 | 32093 | 35519 | 707.1901 | 8 / 707 | 707.19, 353.595, 235.73, 176.798, 141.438, 117.865, 78.5767, 70.719 |
| 2458475.33429 | 32093 | 35519 | 707.1845 | 8 / 707 | 707.184, 353.592, 235.728, 176.796, 141.437, 117.864, 78.5761, 70.7185 |
| 2458486.00141 | 24414 | 35519 | 696.5174 | 6 / 696 | 696.517, 348.259, 174.129, 99.5025, 63.3198, 53.5783 |
| 2458486.02849 | 32105 | 35519 | 696.4903 | 6 / 696 | 696.49, 348.245, 174.123, 99.4986, 63.3173, 53.5762 |
| 2460993.28116 | 32028 | 35519 | 1810.7623 | 14 / 1810 | 1810.76, 905.381, 603.587, 452.691, 301.794, 226.345, 201.196, 164.615, 150.897, 113.173, 106.515, 100.598, 95.3033, 75.4484 |
| 2461014.71057 | 32757 | 35519 | 1832.1917 | 20 / 1832 | 1832.19, 916.096, 610.731, 458.048, 305.365, 261.742, 203.577, 166.563, 152.683, 140.938, 130.871, 107.776, 96.4311, 83.2814, 79.6605, 70.4689, 67.859, 46.9793, 39.8303, 35.9253 |
| 2461025.42508 | 34298 | 35519 | 1842.9063 | 16 / 1842 | 1842.91, 921.453, 614.302, 460.727, 307.151, 263.272, 204.767, 167.537, 153.576, 131.636, 102.384, 96.9951, 83.7685, 68.2558, 51.1918, 34.1279 |
| 2461036.14365 | 35435 | 35519 | 1853.6248 | 15 / 1853 | 1853.62, 926.812, 617.875, 463.406, 308.938, 264.803, 168.511, 154.469, 132.402, 109.037, 97.5592, 84.2557, 59.7943, 48.7796, 32.5197 |
| 2461239.69761 | 28734 | 35519 | 2057.1788 | 20 / 2057 | 2057.18, 1028.59, 685.726, 514.295, 411.436, 342.863, 293.883, 257.147, 205.718, 187.016, 171.432, 158.244, 137.145, 128.574, 93.5081, 89.4426, 85.7158, 68.5726, 62.3388, 58.7765 |
| 2461239.71428 | 28938 | 35519 | 2057.1955 | 20 / 2057 | 2057.2, 1028.6, 685.732, 514.299, 411.439, 342.866, 293.885, 257.149, 205.72, 187.018, 171.433, 158.246, 137.146, 128.575, 93.5089, 89.4433, 85.7165, 68.5732, 62.3393, 58.777 |
| 2461239.73512 | 28938 | 35519 | 2057.2163 | 20 / 2057 | 2057.22, 1028.61, 685.739, 514.304, 411.443, 342.869, 293.888, 257.152, 205.722, 187.02, 171.435, 158.247, 137.148, 128.576, 93.5098, 89.4442, 85.7173, 68.5739, 62.3399, 58.7776 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-450.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:08:37Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:08:39Z: TOI-450.01 (TIC 77951245, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:08:40Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:08:40Z: TOI-450 (*); TOI-450.01 (err)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459182.4874: recovered, depth 35519 ± 550 ppm (catalogue 56326 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | inconclusive | screen run at each light curve's own k* (≤2.5, none, 5, 7, none; ≤ 0 persistent null events outside the veto); 2 light curve(s) reached no k* on the grid and used the declared k, uncalibrated |
| Synthetic signal injection–recovery | inconclusive | completeness for 2000 ppm, 4.0 h boxes at the declared threshold: 0%, 0%, 0%, 0%, 0% per light curve (pass mark 90%) |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 15 repeat-candidate event(s); first at BJD 2459193.2015, ΔT = 10.683 d, 0 of 10 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-450.01: Gaia DR3 4827527233363019776 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-450.01: dwarf priors not applied — 1.49 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-450.01: 5 Gaia neighbour(s) within 52.5", contamination 5.66%; depth 35519 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 17 persistent event(s), 9 clean; BJD 2459187.5133 suspect: MOM_CENTR1 z=+7.8, MOM_CENTR2 z=-13.8, POS_CORR1 z=+12.7, POS_CORR2 z=-14.8; BJD 2459193.2015 caution: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2458475.3065 suspect: manual exclude (in event); BJD 2458475.3287 suspect: manual exclude (in event) |
| Moving objects at screen-event epochs | inconclusive | 17 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 5 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-450.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-450.01: TOI-450 otype * (star_or_other) at 0.5" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-450-01.yaml
python -m cygnus.multi report campaigns/toi-450-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** No new signal.

Source: `campaigns/toi-450-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.
