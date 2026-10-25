# T2 follow-up: toi-6609-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 3 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2461054.3819: not recovered, depth 15167 ± 1338 ppm (catalogue 13164 ppm); BJD 2461067.3234: gap (catalogue 13164 ppm); BJD 2461106.1478: not recovered, depth 17439 ± 1604 ppm (catalogue 13164 ppm); BJD 2461119.0892: recovered, depth 15861 ± 1627 ppm (catalogue 13164 ppm); BJD 2461132.0307: not recovered, depth 16220 ± 1262 ppm (catalogue 13164 ppm); BJD 2461144.9722: not recovered, depth 14314 ± 1225 ppm (catalogue 13164 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 8 repeat-candidate event(s); first at BJD 2461046.1162, ΔT = 73.035 d, 2 of 73 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (73.0353, 36.5177 d); duration likelihood under Gaia priors (circular orbits) peaks at 36.5 d (weight 0.70) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | inconclusive | Worst defining-event pixel localization: difference-image centroid 41.9″ from the out-of-transit centroid (0.8σ bootstrap); 118.5″ from the catalogue position; 9% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6609.01: Gaia DR3 5894446244146213632 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6609.01: Teff 5112 K, R* 0.90 ± 0.07, M* 0.93 ± 0.09, ρ* 1.29 ± 0.33 ρ☉ (dwarf sequence, M_G 5.16, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6609.01: 158 Gaia neighbour(s) within 52.5", contamination 78.90%; depth 15861 ppm (measured depth of the recovered catalogued transit); 12 could produce it if fully eclipsed (brightest 5894445488231952000, 38.1", ΔG 0.62); a centroid test is needed |
| Pointing and quality census per event | failed | 10 persistent event(s), 3 clean; BJD 2461046.1162 suspect: earth point (in event), manual exclude (in event), momentum dump (in event), POS_CORR1 z=-14.6, POS_CORR2 z=+12.0, SAP_BKG z=+228.7; BJD 2461046.1280 suspect: momentum dump (in event), earth point (within ±0.25 d), manual exclude (within ±0.25 d), MOM_CENTR1 z=-5.6, POS_CORR1 z=-19.1, POS_CORR2 z=+15.7, SAP_BKG z=+270.4; BJD 2461046.1377 suspect: earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=-6.3, POS_CORR1 z=-21.0, POS_CORR2 z=+16.9, SAP_BKG z=+271.9; BJD 2461101.5849 suspect: SAP_BKG z=+38.7 |
| Moving objects at screen-event epochs | inconclusive | 10 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-6609.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6609.01: UCAC4 178-125008 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | not_tested | no pixel localization was produced |
| Vetting difference-image localization (E2) | not_tested | no pixel localization was produced |
| Vetting difference-image localization (E3) | inconclusive | difference-image centroid 41.9″ from the out-of-transit centroid (0.8σ bootstrap); 118.5″ from the catalogue position; 9% of the deficit in the optimal aperture |
| Vetting difference-image localization (E4) | not_tested | no pixel localization was produced |
| Event-epoch null exceedance (k/N) | not_tested | BJD 2461101.585: 260/281 event-free windows at least as deep; resolution 1/281, not a probability of zero; BJD 2461101.712: 193/265 event-free windows at least as deep; resolution 1/265, not a probability of zero; BJD 2461125.032: 42/265 event-free windows at least as deep; resolution 1/265, not a probability of zero |
| Event-depth injection-recovery | not_tested | BJD 2461101.585: 12/95 recovered; BJD 2461101.712: 32/88 recovered; BJD 2461125.032: 71/90 recovered |
