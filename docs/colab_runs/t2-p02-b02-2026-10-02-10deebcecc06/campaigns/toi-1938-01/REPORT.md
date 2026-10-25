# T2 follow-up: toi-1938-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 4 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2459346.0735: recovered, depth 5656 ± 250 ppm (catalogue 5160 ppm); BJD 2459358.7796: not recovered, depth 1694 ± 245 ppm (catalogue 5160 ppm); BJD 2460070.3204: recovered, depth 4918 ± 242 ppm (catalogue 5160 ppm); BJD 2460083.0265: partial, depth 367 ± 320 ppm (catalogue 5160 ppm); BJD 2460095.7326: gap (catalogue 5160 ppm); BJD 2461137.6317: recovered, depth 3389 ± 260 ppm (catalogue 5160 ppm); BJD 2461150.3378: recovered, depth 4588 ± 315 ppm (catalogue 5160 ppm); BJD 2461163.0439: recovered, depth 2829 ± 240 ppm (catalogue 5160 ppm); BJD 2461175.7500: partial, depth 3468 ± 241 ppm (catalogue 5160 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2460075.1009, ΔT = 729.025 d, 7 of 729 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (729.025, 243.008, 145.805, 104.147, 34.7155, 31.6968, 19.7034 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | inconclusive | Worst defining-event pixel localization: difference-image centroid 6.5″ from the out-of-transit centroid (0.8σ bootstrap); 6.0″ from the catalogue position; 44% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-1938.01: Gaia DR3 6100120270737811072 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1938.01: dwarf priors not applied — RUWE 3.6803052 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1938.01: 32 Gaia neighbour(s) within 52.5", contamination 39.60%; depth 5656 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 6100120305097553536, 26.7", ΔG 0.75); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 1 clean; BJD 2460082.5023 suspect: SAP_BKG z=+161.4; BJD 2460082.5537 suspect: SAP_BKG z=+151.8 |
| Moving objects at screen-event epochs | passed | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-1938.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-1938.01: TOI-1938 otype * (star_or_other) at 0.3" |
| Event-time prior art | inconclusive | 2 possible published-ephemeris overlap(s) within 1 d (TOI-1938.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |
| Vetting difference-image localization (E1) | inconclusive | difference-image centroid 6.5″ from the out-of-transit centroid (0.8σ bootstrap); 6.0″ from the catalogue position; 44% of the deficit in the optimal aperture |
| Vetting difference-image localization (E2) | inconclusive | difference-image centroid 19.8″ from the out-of-transit centroid (0.6σ bootstrap); 12.3″ from the catalogue position; 24% of the deficit in the optimal aperture |
| Event-epoch null exceedance (k/N) | passed | BJD 2460075.101: 0/190 event-free windows at least as deep; resolution 1/190, not a probability of zero; BJD 2460082.502: 0/210 event-free windows at least as deep; resolution 1/210, not a probability of zero; BJD 2460082.554: 0/202 event-free windows at least as deep; resolution 1/202, not a probability of zero |
| Event-depth injection-recovery | failed | BJD 2460075.101: 54/62 recovered; BJD 2460082.502: 64/71 recovered; BJD 2460082.554: 58/69 recovered |
