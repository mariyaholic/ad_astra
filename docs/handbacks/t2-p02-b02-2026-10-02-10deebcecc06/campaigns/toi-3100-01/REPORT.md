# T2 follow-up: toi-3100-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 3 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460014.5588: gap (catalogue 15760 ppm); BJD 2460017.8495: recovered, depth 12418 ± 832 ppm (catalogue 15760 ppm); BJD 2460021.1403: recovered, depth 11027 ± 852 ppm (catalogue 15760 ppm); BJD 2460024.4310: recovered, depth 12508 ± 880 ppm (catalogue 15760 ppm); BJD 2460027.7218: gap (catalogue 15760 ppm); BJD 2460031.0125: recovered, depth 16300 ± 892 ppm (catalogue 15760 ppm); BJD 2460034.3033: partial, depth 8884 ± 1335 ppm (catalogue 15760 ppm); BJD 2460037.5940: recovered, depth 15423 ± 888 ppm (catalogue 15760 ppm); BJD 2460040.8848: not recovered, depth -12644 ± 1275 ppm (catalogue 15760 ppm); BJD 2461047.8533: recovered, depth 13459 ± 850 ppm (catalogue 15760 ppm); BJD 2461051.1440: recovered, depth 12092 ± 897 ppm (catalogue 15760 ppm); BJD 2461054.4348: recovered, depth 15540 ± 858 ppm (catalogue 15760 ppm); BJD 2461057.7255: gap (catalogue 15760 ppm); BJD 2461061.0163: gap (catalogue 15760 ppm); BJD 2461064.3070: recovered, depth 14220 ± 919 ppm (catalogue 15760 ppm); BJD 2461067.5978: recovered, depth 15922 ± 863 ppm (catalogue 15760 ppm); BJD 2461070.8885: recovered, depth 16009 ± 914 ppm (catalogue 15760 ppm); BJD 2461074.1793: recovered, depth 15323 ± 898 ppm (catalogue 15760 ppm); BJD 2461077.4700: recovered, depth 14954 ± 948 ppm (catalogue 15760 ppm); BJD 2461080.7608: gap (catalogue 15760 ppm); BJD 2461084.0515: recovered, depth 14747 ± 871 ppm (catalogue 15760 ppm); BJD 2461087.3423: gap (catalogue 15760 ppm); BJD 2461090.6330: recovered, depth 14072 ± 853 ppm (catalogue 15760 ppm); BJD 2461093.9238: recovered, depth 7840 ± 1292 ppm (catalogue 15760 ppm); BJD 2461097.2145: recovered, depth 12640 ± 919 ppm (catalogue 15760 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460015.7218, ΔT = 2.118 d, 0 of 2 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested | Worst defining-event pixel localization: no pixel localization was produced; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3100.01: Gaia DR3 5376814998897274240 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3100.01: Teff 6005 K, R* 1.10 ± 0.09, M* 1.06 ± 0.11, ρ* 0.79 ± 0.21 ρ☉ (dwarf sequence, M_G 4.32, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3100.01: 17 Gaia neighbour(s) within 52.5", contamination 78.68%; depth 12418 ppm (measured depth of the recovered catalogued transit); 6 could produce it if fully eclipsed (brightest 5376814685361468416, 50.1", ΔG -0.92); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 2 clean; BJD 2460015.7218 suspect: scattered light 2 (within ±0.25 d), POS_CORR1 z=-5.3, POS_CORR2 z=-10.3, SAP_BKG z=+388.9 |
| Moving objects at screen-event epochs | inconclusive | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3100.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3100.01: TOI-3100 otype * (star_or_other) at 0.4" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | not_tested | no pixel localization was produced |
| Event-epoch null exceedance (k/N) | inconclusive | BJD 2460015.722: 16/62 event-free windows at least as deep; resolution 1/62, not a probability of zero |
| Event-depth injection-recovery | failed | BJD 2460015.722: 38/62 recovered |
