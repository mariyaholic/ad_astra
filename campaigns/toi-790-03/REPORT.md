# Known-object test, TOI-790.03

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The reviewer notes below were added by hand; every other number is the runner's.

> **Reviewer flag (2026-09-25):** the screen did **not** set a repeat candidate, but the 19 persistent
> events are all one extended ~9 h depression in sector 9 (see *Reviewer notes*). It falls below the
> repeat-candidate depth test only because that test measures depth over the catalogued 17.4 h window.
> It is recorded here for a reviewer; the record's outcome is unchanged.

- Campaign spec: `campaigns/toi-790-03.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #597, fetch_products #596, known_signal_recovery #598, period_aliases #600, prior_art #601, residual_screen #599
- Runner finished (UTC): 2026-09-25T11:10:11Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-790.03 (BJD 2460203.6215: recovered, depth 1998 ± 26 ppm (catalogue 1628 ppm)).
Outside the catalogued epoch the screen left 219 threshold entries forming **83 distinct event(s)**, **19 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.

This is a pipeline check on a known object, not a discovery claim. No period is implied by a single transit.

## Reviewer notes (2026-09-25)

The positive control passed (catalogued transit recovered in sector 69, depth 1998 ± 26 ppm vs 1628 ppm
catalogue, 521 in-transit cadences). **No repeat candidate was set.** Six sectors were retrieved; all 19
persistent events are in sector 9 and 18 of them fall inside a single 0.36 d window (BJD 2458551.878 –
2458552.236), i.e. one extended episode rather than 18 transits.

| Test | Result | State |
|---|---|---|
| Quality flags and gaps | all cadences within ±0.15 d of the episode have QUALITY = 0; largest gap 2.0 min | passed |
| SAP vs PDCSAP | the ~9 h depression is present in both, agreeing to ~100 ppm | passed |
| Shape vs the catalogued transit | catalogued transit is a ~15 h, ≈ −2.2 ppt plateau; the sector 9 episode is a ~9 h, ≈ −1.4 ppt plateau — similar *kind* but shorter and shallower | inconclusive |
| Flux-weighted centroid (MOM_CENTR1/2) | episode residual within the excursion scatter (+0.0013/−0.0002 px vs sd 0.0020/0.0061 px) | inconclusive (no help) |
| Repeat-candidate depth test | not triggered: the depth is measured over the catalogued ±8.7 h window, diluting the shorter episode below the 0.5× threshold | noted (not a pass) |
| Difference-image centroids / blend audit | not done | not tested |
| TOI table / literature | TOI table (row updated 2024-03-15) lists no period; ADS and ExoFOP not searched | inconclusive |

Persistent events, one line each (all `tess2019058134432-s0009-…-s_lc.fits`, all PDCSAP+SAP at baselines 1/2/3):

- 2458551.87821 (−0.00187), 2458551.90669 (−0.00208), 2458551.93099 (−0.00214), 2458551.95807 (−0.00199),
  2458551.96294 (−0.00220), 2458551.97544 (−0.00219), 2458551.97960 (−0.00200), 2458551.98794 (−0.00201),
  2458552.01155 (−0.00204), 2458552.02266 (−0.00218), 2458552.11849 (−0.00216), 2458552.13516 (−0.00207),
  2458552.15321 (−0.00216), 2458552.16294 (−0.00218), 2458552.16988 (−0.00267), 2458552.19349 (−0.00192),
  2458552.21572 (−0.00224), 2458552.23585 (−0.00233) — one ~9 h depression, split by the grouping; likely a
  single astrophysical or systematic episode, not 18 separate events.
- 2458568.42549 (−0.00197) — a separate, shorter event near the end of sector 9; the profile is a broad
  shallow negative trend, similar in character to the sector-edge events seen in other targets.

What this supports: the catalogued transit of TOI-790.03 is recovered where the catalogue puts it. What it
does not: a period, or a confirmed second transit. The sector 9 depression is the most interesting residual
in this target — it is broad (~9 h), present in SAP and PDCSAP, clean in quality and centroid — but a
single sector cannot distinguish it from scattered-light or pointing systematics. Next test: a
difference-image / background check for the sector 9 episode and a targeted re-run with the repeat-candidate
depth window set from the *event* duration rather than the catalogued one.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-790.03 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 308994098 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 123.39778 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -64.090901 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2460203.621473 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 1628.2500301 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 17.3550472 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 8.9914 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2024-03-15 12:03:14 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 69 | True | `24c770869eb7cd29` | False |
| `tess2018206045859-s0001-0000000308994098-0120-s_lc.fits` | 1 | False | `5aebc6d52b55575e` | False |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 4 | False | `100cbf98a015bbae` | False |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 8 | False | `aa702ec1ec187688` | False |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 9 | False | `870a35460122e57d` | False |
| `tess2019085135100-s0010-0000000308994098-0140-s_lc.fits` | 10 | False | `6c0ab7221be273b7` | False |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460203.62147 | recovered | 521 | 1998 ± 26 | 1628 | 0.28 |
| `tess2018206045859-s0001-0000000308994098-0120-s_lc.fits` | — | epoch not in this light curve | — | — | 1628 | — |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | — | epoch not in this light curve | — | — | 1628 | — |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | — | epoch not in this light curve | — | — | 1628 | — |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | — | epoch not in this light curve | — | — | 1628 | — |
| `tess2019085135100-s0010-0000000308994098-0140-s_lc.fits` | — | epoch not in this light curve | — | — | 1628 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2018206045859-s0001-0000000308994098-0120-s_lc.fits` | 4 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 5000, 2h: 2000, 4h: 2000, 8h: 5000 |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2 | True | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2019085135100-s0010-0000000308994098-0140-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.16988 | -0.00267 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.23585 | -0.00233 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.21572 | -0.00224 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.96294 | -0.00220 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.97544 | -0.00219 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.02266 | -0.00218 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.16294 | -0.00218 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.15321 | -0.00216 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.11849 | -0.00216 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.93099 | -0.00214 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.90669 | -0.00208 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.13516 | -0.00207 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.01155 | -0.00204 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.98794 | -0.00201 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.97960 | -0.00200 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.95807 | -0.00199 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458568.42549 | -0.00197 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.19349 | -0.00192 | 6 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.87821 | -0.00187 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458421.23686 | -0.00539 | 36 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458421.26603 | -0.00510 | 4 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458421.29103 | -0.00461 | 30 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000308994098-0120-s_lc.fits` | 2458348.48146 | -0.00433 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458425.15496 | -0.00372 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458421.31464 | -0.00361 | 2 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000308994098-0120-s_lc.fits` | 2458349.21478 | -0.00352 | 2 | SAP | 3 | no |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 2458535.05026 | -0.00335 | 10 | SAP | 1, 2, 3 | no |
| `tess2018206045859-s0001-0000000308994098-0120-s_lc.fits` | 2458347.51342 | -0.00328 | 2 | SAP | 1 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458424.63134 | -0.00327 | 2 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000308994098-0120-s_lc.fits` | 2458348.10925 | -0.00324 | 2 | SAP | 3 | no |
| `tess2018206045859-s0001-0000000308994098-0120-s_lc.fits` | 2458348.43007 | -0.00319 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458424.67023 | -0.00317 | 2 | SAP | 2, 3 | no |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 2458535.06901 | -0.00311 | 5 | SAP | 1, 2, 3 | no |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 2458535.07526 | -0.00310 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460201.26925 | -0.00309 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458412.68121 | -0.00306 | 2 | SAP | 1, 2, 3 | no |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 2458535.08082 | -0.00293 | 4 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458421.32784 | -0.00277 | 3 | SAP | 3 | no |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 2458535.02665 | -0.00272 | 18 | SAP | 2, 3 | no |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 2458535.05999 | -0.00272 | 2 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458411.22564 | -0.00271 | 2 | SAP | 1, 2, 3 | no |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 2458535.00790 | -0.00264 | 7 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458412.26037 | -0.00264 | 2 | SAP | 1 | no |
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460201.32828 | -0.00260 | 3 | SAP | 1, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.92613 | -0.00259 | 3 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458563.49077 | -0.00255 | 2 | SAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458421.32089 | -0.00255 | 5 | SAP | 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458417.40904 | -0.00250 | 2 | SAP | 2 | no |
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460201.25814 | -0.00247 | 2 | SAP | 1, 2, 3 | no |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 2458535.08637 | -0.00245 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460201.11926 | -0.00244 | 2 | SAP | 2, 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458415.25485 | -0.00243 | 2 | SAP | 1 | no |
| `tess2019085135100-s0010-0000000308994098-0140-s_lc.fits` | 2458585.96571 | -0.00238 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.92127 | -0.00235 | 2 | PDCSAP | 2, 3 | no |
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460200.71509 | -0.00228 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.96988 | -0.00226 | 2 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.21016 | -0.00224 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2018292075959-s0004-0000000308994098-0124-s_lc.fits` | 2458413.25066 | -0.00223 | 2 | SAP | 1 | no |
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460201.32064 | -0.00220 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460201.26370 | -0.00218 | 2 | SAP | 1, 2, 3 | no |
| `tess2019032160000-s0008-0000000308994098-0136-s_lc.fits` | 2458535.13776 | -0.00217 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460201.02620 | -0.00212 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.10738 | -0.00211 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000308994098-0264-s_lc.fits` | 2460201.15259 | -0.00209 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.91710 | -0.00205 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.08516 | -0.00195 | 4 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.99905 | -0.00192 | 2 | PDCSAP | 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458560.10603 | -0.00191 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.03377 | -0.00190 | 2 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.09349 | -0.00188 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458560.23798 | -0.00185 | 2 | SAP | 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.24905 | -0.00183 | 2 | PDCSAP | 2, 3 | no |
| `tess2019085135100-s0010-0000000308994098-0140-s_lc.fits` | 2458581.77963 | -0.00183 | 2 | PDCSAP | 1 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.89280 | -0.00181 | 3 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.07891 | -0.00180 | 3 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.17405 | -0.00179 | 2 | PDCSAP | 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458568.31924 | -0.00175 | 3 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.15738 | -0.00173 | 2 | PDCSAP | 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458551.85738 | -0.00172 | 3 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.18099 | -0.00172 | 2 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.00738 | -0.00168 | 2 | PDCSAP | 2, 3 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458565.89216 | -0.00166 | 2 | PDCSAP | 2 | no |
| `tess2019058134432-s0009-0000000308994098-0139-s_lc.fits` | 2458552.13933 | -0.00157 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Catalogue cross-match

**TOI-790.03**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T11:10:04Z
- TESS_TOI (done, 2026-09-25): 3 match(es) in TESS_TOI within 30" as of 2026-09-25T11:10:06Z: TOI-790.01 (TIC 308994098, disposition PC); TOI-790.02 (TIC 308994098, disposition PC); TOI-790.03 (TIC 308994098, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T11:10:08Z
- SIMBAD (done, 2026-09-25): 4 match(es) in SIMBAD within 30" as of 2026-09-25T11:10:09Z: TOI-790.03 (Pl?); CD-63   391 (PM*); TOI-790.01 (Pl?); TOI-790.02 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460203.6215: recovered, depth 1998 ± 26 ppm (catalogue 1628 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 4, 3, 3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 10%, 80%, 100%, 100%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | not_tested | no persistent screen event matches the catalogued depth |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-790-03.yaml
python -m cygnus.campaign report campaigns/toi-790-03.yaml
```
