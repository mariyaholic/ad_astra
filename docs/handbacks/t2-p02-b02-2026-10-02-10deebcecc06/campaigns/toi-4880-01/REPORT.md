# T2 follow-up: toi-4880-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 3 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460041.3092: not recovered, depth -5400 ± 718 ppm (catalogue 11480 ppm); BJD 2460044.7810: recovered, depth 15949 ± 959 ppm (catalogue 11480 ppm); BJD 2460048.2527: gap (catalogue 11480 ppm); BJD 2460051.7245: not recovered, depth 1211 ± 1087 ppm (catalogue 11480 ppm); BJD 2460055.1962: gap (catalogue 11480 ppm); BJD 2460058.6680: not recovered, depth -3930 ± 844 ppm (catalogue 11480 ppm); BJD 2460062.1397: recovered, depth 2288 ± 876 ppm (catalogue 11480 ppm); BJD 2460065.6115: partial, depth 2725 ± 781 ppm (catalogue 11480 ppm); BJD 2461048.1191: not recovered, depth 979 ± 720 ppm (catalogue 11480 ppm); BJD 2461051.5909: not recovered, depth 2304 ± 731 ppm (catalogue 11480 ppm); BJD 2461055.0626: not recovered, depth -2106 ± 728 ppm (catalogue 11480 ppm); BJD 2461058.5344: gap (catalogue 11480 ppm); BJD 2461062.0061: gap (catalogue 11480 ppm); BJD 2461065.4779: not recovered, depth -1591 ± 748 ppm (catalogue 11480 ppm); BJD 2461068.9496: not recovered, depth 3662 ± 800 ppm (catalogue 11480 ppm); BJD 2461072.4214: not recovered, depth 7512 ± 841 ppm (catalogue 11480 ppm); BJD 2461075.8932: not recovered, depth 1193 ± 895 ppm (catalogue 11480 ppm); BJD 2461079.3649: not recovered, depth -4477 ± 824 ppm (catalogue 11480 ppm); BJD 2461082.8367: not recovered, depth -8104 ± 776 ppm (catalogue 11480 ppm); BJD 2461086.3084: not recovered, depth -9644 ± 684 ppm (catalogue 11480 ppm); BJD 2461089.7802: not recovered, depth 4960 ± 839 ppm (catalogue 11480 ppm); BJD 2461093.2520: not recovered, depth 1916 ± 947 ppm (catalogue 11480 ppm); BJD 2461096.7237: not recovered, depth -2553 ± 852 ppm (catalogue 11480 ppm); BJD 2461100.1955: gap (catalogue 11480 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 22 repeat-candidate event(s); first at BJD 2461048.3972, ΔT = 1003.521 d, 25 of 1003 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1003.52, 501.761, 334.507, 250.88, 200.704, 167.254, 143.36, 125.44, 111.502, 100.352, 91.2292, 83.6268 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | inconclusive | Worst defining-event pixel localization: difference-image centroid 99.9″ from the out-of-transit centroid (2.2σ bootstrap); 3.6″ from the catalogue position; 37% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4880.01: Gaia DR3 6067960071023963392 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-4880.01: dwarf priors not applied — 1.20 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4880.01: 61 Gaia neighbour(s) within 52.5", contamination 40.27%; depth 15949 ppm (measured depth of the recovered catalogued transit); 6 could produce it if fully eclipsed (brightest 6067960139743443072, 29.1", ΔG 2.27); a centroid test is needed |
| Pointing and quality census per event | failed | 24 persistent event(s), 16 clean; BJD 2461055.3811 suspect: MOM_CENTR1 z=-6.6, POS_CORR2 z=+6.2, SAP_BKG z=-6.9; BJD 2461055.4255 suspect: MOM_CENTR1 z=-5.2, POS_CORR2 z=+6.6, SAP_BKG z=-8.6; BJD 2461072.6990 suspect: manual exclude (in event), SAP_BKG z=+8.6; BJD 2461072.7087 suspect: manual exclude (in event), SAP_BKG z=+9.3 |
| Moving objects at screen-event epochs | inconclusive | 24 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-4880.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4880.01: UCAC4 183-096100 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | 22 possible published-ephemeris overlap(s) within 1 d (TOI-4880.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |
| Vetting difference-image localization (E1) | inconclusive | difference-image centroid 99.9″ from the out-of-transit centroid (2.2σ bootstrap); 3.6″ from the catalogue position; 37% of the deficit in the optimal aperture |
| Event-time comparison vs published ephemerides | failed | E8: TOI-4880.01 (PC, P 3.4718 d, 11480 ppm) predicted +8.12 h ± 11.51 h; primary-literature/TTV review still required |
| Vetting difference-image localization (E2) | inconclusive | difference-image centroid 98.4″ from the out-of-transit centroid (2.0σ bootstrap); 2.5″ from the catalogue position; 45% of the deficit in the optimal aperture |
| Vetting difference-image localization (E3) | inconclusive | difference-image centroid 97.8″ from the out-of-transit centroid (2.0σ bootstrap); 2.1″ from the catalogue position; 31% of the deficit in the optimal aperture |
| Vetting difference-image localization (E4) | inconclusive | difference-image centroid 97.5″ from the out-of-transit centroid (2.5σ bootstrap); 1.5″ from the catalogue position; 34% of the deficit in the optimal aperture |
| Vetting difference-image localization (E5) | passed | difference-image centroid 2.1″ from the out-of-transit centroid (0.3σ bootstrap); 99.1″ from the catalogue position; 15% of the deficit in the optimal aperture |
| Vetting difference-image localization (E6) | inconclusive | difference-image centroid 86.6″ from the out-of-transit centroid (2.0σ bootstrap); 1.5″ from the catalogue position; 34% of the deficit in the optimal aperture |
| Vetting difference-image localization (E7) | inconclusive | difference-image centroid 86.6″ from the out-of-transit centroid (2.2σ bootstrap); 0.7″ from the catalogue position; 51% of the deficit in the optimal aperture |
| Vetting difference-image localization (E8) | inconclusive | difference-image centroid 86.1″ from the out-of-transit centroid (2.5σ bootstrap); 3.4″ from the catalogue position; 45% of the deficit in the optimal aperture |
| Event-epoch null exceedance (k/N) | not_tested | not run: current vetting closed the tool route; event-identity review is required |
| Event-depth injection-recovery | not_tested | not run: current vetting closed the tool route; event-identity review is required |
