# Known-object test, TOI-6980.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

## Escalation (2026-09-25)

The covered positive control formally failed at BJD 2459463.7006 (86 usable cadences), but measured depth 384 ± 43 ppm matches the catalogue's 409 ppm. At k* = 3 the 90%-completeness floor is 2000 ppm at the tabulated durations, roughly five times the transit depth. The failure is sensitivity-limited on the current reduction; no threshold or state was changed. Next: check the catalogued epoch in SPOC DV and an independent reduction.


- Campaign spec: `campaigns/toi-6980-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #454, fetch_products #453, known_signal_recovery #455, period_aliases #457, prior_art #458, residual_screen #456
- Runner finished (UTC): 2026-09-25T05:45:06Z

## Bottom line

Positive control **failed**: BJD 2459463.7006: not recovered, depth 384 ± 43 ppm (catalogue 409 ppm).
Outside the catalogued epoch the screen left 211 threshold entries forming **90 distinct event(s)**, **0 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

Positive control **failed formally** with the epoch covered in sector 42 (86 usable in-transit cadences; QUALITY=0, max gap 2 min): measured 384 ± 43 ppm vs catalogue 409 ppm (ratio 0.94). At k* = 3 the 90%-completeness depth is 2000 ppm for the tabulated 1–8-h durations; the 409-ppm, 2.86-h transit is well below that sensitivity. The measured depth is concordant, but the screen's formal failure is expected at this floor.

There are **0 persistent** events among 211 crossings / 90 groups; visible entries are brief single-flux events only. No repeat candidate. The cross-match answered at all four services; no VSX variable match, SIMBAD returned HD 15819. Pixel/difference-image, pointing and alternate-reduction tests remain untested.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6980.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 422912527 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 38.206634 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 5.209801 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459463.700632 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 409.3413481 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 2.85547 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 7.9859 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2024-09-20 12:02:42 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2021232031932-s0042-0000000422912527-0213-s_lc.fits` | 42 | True | `7dbf1d02d4fb9b69` | True |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 4 | False | `2aa8d7dad24bf2b0` | True |
| `tess2021258175143-s0043-0000000422912527-0214-s_lc.fits` | 43 | False | `856d1405c8ee6d6b` | True |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 71 | False | `816a5ccb4a548523` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021232031932-s0042-0000000422912527-0213-s_lc.fits` | 2459463.70063 | not_recovered | 86 | 384 ± 43 | 409 | — |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | — | epoch not in this light curve | — | — | 409 | — |
| `tess2021258175143-s0043-0000000422912527-0214-s_lc.fits` | — | epoch not in this light curve | — | — | 409 | — |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | — | epoch not in this light curve | — | — | 409 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021232031932-s0042-0000000422912527-0213-s_lc.fits` | 3 | False | 1h: 5000, 2h: 2000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2021258175143-s0043-0000000422912527-0214-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2 | True | 1h: 2000, 2h: 2000, 4h: 5000, 8h: 5000 | 1h: 1000, 2h: 1000, 4h: 1000, 8h: 1000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.15255 | -0.00381 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.09630 | -0.00364 | 8 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.02547 | -0.00353 | 11 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.15741 | -0.00339 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.05672 | -0.00302 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.98172 | -0.00299 | 6 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.08172 | -0.00290 | 6 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.17339 | -0.00284 | 8 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.06922 | -0.00282 | 4 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.18172 | -0.00277 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.11922 | -0.00271 | 4 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.91158 | -0.00271 | 7 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.07547 | -0.00262 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.06089 | -0.00250 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.97478 | -0.00238 | 3 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 2458425.16177 | -0.00234 | 2 | SAP | 1, 3 | no |
| `tess2021258175143-s0043-0000000422912527-0214-s_lc.fits` | 2459482.20887 | -0.00233 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.01505 | -0.00233 | 6 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.13311 | -0.00232 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.92131 | -0.00230 | 5 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.12686 | -0.00230 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.78728 | -0.00228 | 12 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.04005 | -0.00227 | 4 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.98936 | -0.00225 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.14422 | -0.00223 | 4 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.93589 | -0.00219 | 8 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.11228 | -0.00217 | 6 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 2458411.30614 | -0.00213 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.89978 | -0.00208 | 8 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.20186 | -0.00208 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.94908 | -0.00204 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.04561 | -0.00203 | 6 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.84769 | -0.00201 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.96228 | -0.00199 | 12 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 2458411.03669 | -0.00193 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.50534 | -0.00189 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.80603 | -0.00188 | 5 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 2458411.47142 | -0.00185 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.92964 | -0.00184 | 3 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 2458410.99780 | -0.00183 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.77478 | -0.00183 | 4 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.76783 | -0.00180 | 4 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.85742 | -0.00179 | 8 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 2458433.51444 | -0.00176 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.49978 | -0.00174 | 4 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.88381 | -0.00171 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.75395 | -0.00170 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.18936 | -0.00169 | 5 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.81853 | -0.00168 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460240.19280 | -0.00167 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460240.29558 | -0.00166 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000422912527-0124-s_lc.fits` | 2458433.19222 | -0.00163 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.16297 | -0.00159 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.72756 | -0.00157 | 4 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460240.27753 | -0.00156 | 8 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.55186 | -0.00156 | 3 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.87756 | -0.00155 | 4 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.73381 | -0.00155 | 3 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.43173 | -0.00154 | 4 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460240.13447 | -0.00153 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.49353 | -0.00151 | 3 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460246.08867 | -0.00150 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.86922 | -0.00149 | 6 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.89006 | -0.00148 | 4 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.71922 | -0.00148 | 6 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460239.78030 | -0.00146 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.81228 | -0.00146 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.82825 | -0.00144 | 5 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460240.07058 | -0.00143 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.99561 | -0.00141 | 4 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.67478 | -0.00138 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.83450 | -0.00134 | 2 | SAP | 3 | no |
| `tess2021258175143-s0043-0000000422912527-0214-s_lc.fits` | 2459487.20774 | -0.00133 | 2 | PDCSAP | 1 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460240.26711 | -0.00132 | 5 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460240.08586 | -0.00131 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.65186 | -0.00130 | 3 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460245.95811 | -0.00129 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.56367 | -0.00128 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460236.59691 | -0.00128 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.83936 | -0.00126 | 3 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460245.26923 | -0.00125 | 2 | SAP | 1 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460259.30384 | -0.00125 | 2 | PDCSAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460240.25044 | -0.00124 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460240.19697 | -0.00123 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.61228 | -0.00122 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460252.38173 | -0.00118 | 4 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460253.20811 | -0.00116 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460259.33023 | -0.00111 | 2 | PDCSAP | 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460259.32051 | -0.00106 | 2 | PDCSAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000422912527-0266-s_lc.fits` | 2460259.31495 | -0.00095 | 4 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-6980.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:45:00Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:45:02Z: TOI-6980.01 (TIC 422912527, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:45:04Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T05:45:05Z: HD  15819 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | failed | BJD 2459463.7006: not recovered, depth 384 ± 43 ppm (catalogue 409 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100%, 100%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | catalogued transit not recovered; no reference depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-6980-01.yaml
python -m cygnus.campaign report campaigns/toi-6980-01.yaml
```
