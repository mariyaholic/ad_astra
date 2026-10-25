# T2 follow-up: toi-5937-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 4 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460324.2468: not recovered, depth 12952 ± 1321 ppm (catalogue 15800 ppm); BJD 2460345.3153: partial, depth 14594 ± 1206 ppm (catalogue 15800 ppm); BJD 2460366.3838: partial, depth 14085 ± 1211 ppm (catalogue 15800 ppm); BJD 2460492.7950: not recovered, depth 11427 ± 1339 ppm (catalogue 15800 ppm); BJD 2460513.8635: recovered, depth 14176 ± 1394 ppm (catalogue 15800 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 2 repeat-candidate event(s); first at BJD 2460312.9154, ΔT = 200.961 d, 3 of 200 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (200.961, 100.481, 66.9871 d); duration likelihood under Gaia priors (circular orbits) peaks at 67 d (weight 0.97) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | inconclusive | Worst defining-event pixel localization: difference-image centroid 103.3″ from the out-of-transit centroid (2.0σ bootstrap); 117.5″ from the catalogue position; 1% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5937.01: Gaia DR3 2102562864229866240 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5937.01: Teff 5310 K, R* 0.95 ± 0.08, M* 0.97 ± 0.10, ρ* 1.14 ± 0.30 ρ☉ (dwarf sequence, M_G 4.91, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5937.01: 17 Gaia neighbour(s) within 52.5", contamination 83.11%; depth 14176 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 2102562859929080832, 18.1", ΔG -1.63); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2460312.9154 suspect: coarse point (within ±0.25 d), earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=-10.2, MOM_CENTR2 z=-7.1, POS_CORR1 z=-23.5, POS_CORR2 z=-8.5; BJD 2460519.9128 suspect: manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=-11.0, POS_CORR1 z=-15.2, POS_CORR2 z=-14.2 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 4 light curve × candidate pair(s); aliases supported: none; excluded: none; 12 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-5937.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5937.01: UCAC4 664-071776 otype * (star_or_other) at 0.4" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | inconclusive | difference-image centroid 103.3″ from the out-of-transit centroid (2.0σ bootstrap); 117.5″ from the catalogue position; 1% of the deficit in the optimal aperture |
| Vetting difference-image localization (E2) | inconclusive | difference-image centroid 16.0″ from the out-of-transit centroid (0.5σ bootstrap); 22.0″ from the catalogue position; -2% of the deficit in the optimal aperture |
| Event-epoch null exceedance (k/N) | not_tested | BJD 2460519.913: 2/266 event-free windows at least as deep; resolution 1/266, not a probability of zero |
| Event-depth injection-recovery | failed | BJD 2460519.913: 75/89 recovered |
