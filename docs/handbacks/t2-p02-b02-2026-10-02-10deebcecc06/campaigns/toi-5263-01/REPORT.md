# T2 follow-up: toi-5263-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 3 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460339.9791: not recovered, depth 8954 ± 1004 ppm (catalogue 16270 ppm); BJD 2460343.1292: recovered, depth 20622 ± 1324 ppm (catalogue 16270 ppm); BJD 2460346.2793: gap (catalogue 16270 ppm); BJD 2460349.4295: recovered, depth 15047 ± 974 ppm (catalogue 16270 ppm); BJD 2460352.5796: not recovered, depth 5806 ± 1065 ppm (catalogue 16270 ppm); BJD 2460355.7298: recovered, depth 10307 ± 1041 ppm (catalogue 16270 ppm); BJD 2460358.8799: recovered, depth 14490 ± 1079 ppm (catalogue 16270 ppm); BJD 2460362.0300: recovered, depth 14036 ± 993 ppm (catalogue 16270 ppm); BJD 2460365.1802: not recovered, depth 12276 ± 1028 ppm (catalogue 16270 ppm); BJD 2460506.9363: recovered, depth 16153 ± 1152 ppm (catalogue 16270 ppm); BJD 2460510.0864: recovered, depth 21282 ± 1193 ppm (catalogue 16270 ppm); BJD 2460513.2365: not recovered, depth 18100 ± 1276 ppm (catalogue 16270 ppm); BJD 2460516.3867: recovered, depth 18548 ± 1375 ppm (catalogue 16270 ppm); BJD 2460519.5368: gap (catalogue 16270 ppm); BJD 2460522.6869: recovered, depth 7424 ± 1224 ppm (catalogue 16270 ppm); BJD 2460525.8371: recovered, depth 8710 ± 1331 ppm (catalogue 16270 ppm); BJD 2460528.9872: not recovered, depth 7476 ± 1249 ppm (catalogue 16270 ppm); BJD 2460532.1373: recovered, depth 10180 ± 1277 ppm (catalogue 16270 ppm); BJD 2460535.2875: not recovered, depth 12304 ± 1103 ppm (catalogue 16270 ppm); BJD 2460538.4376: recovered, depth 19743 ± 1174 ppm (catalogue 16270 ppm); BJD 2460541.5878: recovered, depth 14187 ± 1072 ppm (catalogue 16270 ppm); BJD 2460544.7379: partial, depth 14896 ± 1269 ppm (catalogue 16270 ppm); BJD 2460547.8880: partial, depth 15939 ± 1090 ppm (catalogue 16270 ppm); BJD 2460551.0382: recovered, depth 18202 ± 1098 ppm (catalogue 16270 ppm); BJD 2460554.1883: not recovered, depth 15713 ± 1033 ppm (catalogue 16270 ppm); BJD 2460557.3384: not recovered, depth 17586 ± 1144 ppm (catalogue 16270 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 2 repeat-candidate event(s); first at BJD 2460530.0896, ΔT = 186.992 d, 6 of 186 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (186.992, 93.4961, 62.3307, 46.748, 37.3984, 31.1654 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested | Worst defining-event pixel localization: no pixel localization was produced; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5263.01: Gaia DR3 2068625819365716224 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-5263.01: dwarf priors not applied — 1.56 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5263.01: 19 Gaia neighbour(s) within 52.5", contamination 37.22%; depth 20622 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 2068625819365713408, 13.1", ΔG 1.34); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 2 clean; BJD 2460526.7181 suspect: manual exclude (within ±0.25 d), POS_CORR1 z=-8.1 |
| Moving objects at screen-event epochs | passed | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF failed: ) |
| Variable-catalogue collision (VSX) | passed | TOI-5263.01: Gaia DR3 2068625819365716224   RS                             P=None at 1.1" |
| Object-class guard (SIMBAD) | passed | TOI-5263.01: UCAC4 660-087192 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | not_tested | no pixel localization was produced |
| Event-epoch null exceedance (k/N) | inconclusive | BJD 2460530.090: 8/36 event-free windows at least as deep; resolution 1/36, not a probability of zero; BJD 2460530.155: 6/38 event-free windows at least as deep; resolution 1/38, not a probability of zero |
| Event-depth injection-recovery | inconclusive | BJD 2460530.090: 24/36 recovered; BJD 2460530.155: 27/38 recovered |
