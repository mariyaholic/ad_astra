# Position-epoch audit of campaign target coordinates

> Audit run 2026-09-25 (UTC) against the ESA Gaia TAP service. Pipeline check on catalogue
> metadata; no light curve, no discovery claim.

## Bottom line

The `ra_deg`/`dec_deg` values copied into the campaign specs from the NASA Exoplanet Archive
TOI table are **not at epoch J2000.0**, as every spec said. For **77 of 78** spec targets they
are Gaia DR2 positions at **epoch J2015.5**. One target (**TOI-6663.01**) carries a Gaia DR1
position at **epoch J2015.0**. **No** target is at J2000.0, and none is undetermined. The specs,
both scaffolds and both runner fallbacks now say so (`frame: ICRS` is unchanged).

Consequences: no campaign step propagates target positions (`priorart.catalogue_audit` and the
Gaia cone match use them as given), so nothing was computed from the wrong label. Offsets
against Gaia (epoch 2016.0) are only 0.5 yr × PM (at most 0.19″, TOI-6653.01 at 383 mas/yr).
Against epoch-2000 catalogues (SIMBAD, VSX `RAJ2000`) they are 15.5 yr × PM, up to 5.9″ for
TOI-6653.01. That is inside the 30″ prior-art radii used, but it is large enough to matter for any
arcsecond-level comparison. The 1.05″ and 0.57″ SIMBAD offsets for TOI-2666.01 and TOI-6666.01
are this effect.

## Method

1. **Targets.** Every `campaigns/*.yaml` target with `ra_deg`/`dec_deg`, parsed with PyYAML:
   78 targets in 78 specs, 76 unique positions (`toi-2666-01-nss` and `toi-6666-01-nss` reuse
   their parents' positions). The other 3 specs (`tess-mono-01`, `tess-wasp12-residual-01`,
   `wasp12-sector20-recovery`) have no explicit position.
2. **Query.** One ADQL cone per unique position, serialised with a 1.5 s pause, sync TAP (CSV):
   `SELECT source_id, ra, dec, pmra, pmdec, parallax, phot_g_mean_mag FROM gaiadr3.gaia_source
   WHERE 1=CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', <ra>, <dec>, 10/3600))`
   on `https://gea.esac.esa.int/tap-server/tap`, 2026-09-25T21:18:52Z to 21:36:23Z. Every query
   answered. Raw rows, ADQL and per-query UTC times: `gaia_rows.json`.
3. **Propagation.** The DR3 position (epoch 2016.0) is moved linearly in the tangent plane by
   (pmra, pmdec) × Δt to 2015.5 and to 2000.0. The residual is spec minus propagated position,
   in mas (RA·cos δ, Dec). Parallax and radial-velocity (perspective) terms are neglected.
   They are ≪ 1 mas over 16 yr for these stars.
4. **Match.** The source with the smallest residual at either epoch. In all 78 cases that is also
   the brightest DR3 source in the cone. 20 cones contain more than one source.
5. **Class.** J2015.5 if r(2015.5) ≤ 5 mas and r(2000.0) − r(2015.5) ≥ 5 mas. J2000.0 if the
   reverse. Undetermined if 16 yr × |PM| < 10 mas or there is no match. "Inconsistent" otherwise.
   5 mas allows for the TOI table's 1e-6 deg quantisation (≤ 1.8 mas per axis) plus DR2-to-DR3
   position differences.
6. **Second stage for "inconsistent" targets.** The spec position is compared directly (no
   propagation) with 10″ cones in `gaiadr2.gaia_source` (ref_epoch 2015.5) and
   `gaiadr1.gaia_source` (ref_epoch 2015.0), 2026-09-25 (UTC; per-query times in
   `gaia_dr2_check.json`). A match ≤ 2.5 mas assigns that release's epoch (`finalize.py`).
   TOI-2666.01 and TOI-6666.01 were included as controls.

## Results

| Class | DR3 stage | Final |
|---|---|---|
| J2015.5 | 75 | **77** |
| J2015.0 | — | **1** |
| J2000.0 | 0 | **0** |
| undetermined | 0 | **0** |
| inconsistent | 3 | 0 |

- For the 75 DR3-stage J2015.5 targets: median r(2015.5) is 1.1 mas, max 2.7 mas. Min r(2000.0)
  is 49 mas. The smallest 16 yr × |PM| in the whole set is 51 mas, so every target discriminates.
- **Worked examples.** TOI-2666.01: TOI − Gaia DR3 = (−11.2, +31.7) mas = −0.5 yr × PM
  (−11.6, +31.9) mas, residual 0.5 mas. TOI-6666.01: (+0.8, −19.1) mas vs (+0.8, −18.5) mas,
  residual 0.6 mas. Both match their DR2 positions directly to 0.23 and 0.75 mas.

### The three DR3-"inconsistent" targets (resolved, not guessed)

| Target | DR3 r(2015.5) / r(2000.0) (mas) | Direct match | Resolution |
|---|---|---|---|
| TOI-2318.01 | 18.5 / 939 | Gaia DR2 1346780595884995968 at **1.43 mas** | J2015.5 (DR2 position). DR2 has a two-parameter solution here (no PM), so its position differs from the propagated DR3 one by ~18 mas. |
| TOI-4319.01 | 13.9 / 1246 | Gaia DR2 5556279417085330816 at **0.83 mas** | J2015.5 (DR2 position). The DR2 and DR3 proper motions differ, (−27.0, 69.6) vs (−29.3, 75.8) mas/yr. |
| TOI-6663.01 | 7.7 / 237 | Gaia **DR1** 1132006663145960960 at **0.45 mas**; DR2 at 7.8 mas | **J2015.0** (Gaia DR1 epoch). A DR3 best-fit epoch of 2015.01 agrees. |

TOI-6663.01's cone has three DR3 sources. The match (G 11.23) is the brightest and agrees with the spec's Tmag 10.59.

### All targets

| Spec | Target | Gaia DR3 source | G | 16 yr × PM (mas) | r(2015.5) (mas) | r(2000.0) (mas) | DR3 class | Final epoch |
|---|---|---|---|---|---|---|---|---|
| `toi-125-04.yaml` | TOI-125.04 | 4698692748651744128 | 10.72 | 2745 | 1.8 | 2658 | J2015.5 | **J2015.5** |
| `toi-1301-02.yaml` | TOI-1301.02 | 2266490873877571712 | 11.14 | 1537 | 0.6 | 1490 | J2015.5 | **J2015.5** |
| `toi-1772-02.yaml` | TOI-1772.02 | 749676822006222464 | 9.80 | 699 | 0.8 | 677 | J2015.5 | **J2015.5** |
| `toi-1812-01.yaml` | TOI-1812.01 | 1623130061703102592 | 12.20 | 330 | 0.9 | 320 | J2015.5 | **J2015.5** |
| `toi-1835-02.yaml` | TOI-1835.02 | 3948424496764080640 | 8.18 | 2123 | 1.4 | 2056 | J2015.5 | **J2015.5** |
| `toi-1893-01.yaml` | TOI-1893.01 | 2285334677815121152 | 8.70 | 476 | 1.4 | 460 | J2015.5 | **J2015.5** |
| `toi-1896-01.yaml` | TOI-1896.01 | 1938752502320406400 | 9.19 | 911 | 1.3 | 883 | J2015.5 | **J2015.5** |
| `toi-2003-01.yaml` | TOI-2003.01 | 6189286849812601216 | 9.91 | 268 | 1.6 | 261 | J2015.5 | **J2015.5** |
| `toi-2007-01.yaml` | TOI-2007.01 | 1711633081221292800 | 10.72 | 1445 | 0.3 | 1400 | J2015.5 | **J2015.5** |
| `toi-2065-01.yaml` | TOI-2065.01 | 3961485079994112896 | 9.44 | 206 | 0.7 | 199 | J2015.5 | **J2015.5** |
| `toi-2085-01.yaml` | TOI-2085.01 | 1070704702302592512 | 10.40 | 836 | 0.3 | 810 | J2015.5 | **J2015.5** |
| `toi-2087-01.yaml` | TOI-2087.01 | 1712288703684932992 | 10.51 | 257 | 1.7 | 250 | J2015.5 | **J2015.5** |
| `toi-2098-01.yaml` | TOI-2098.01 | 1648927593788025984 | 8.37 | 397 | 1.2 | 386 | J2015.5 | **J2015.5** |
| `toi-2102-02.yaml` | TOI-2102.02 | 1635066737891844864 | 11.92 | 607 | 1.1 | 587 | J2015.5 | **J2015.5** |
| `toi-225-01.yaml` | TOI-225.01 | 2383924277704397056 | 11.62 | 2287 | 1.5 | 2215 | J2015.5 | **J2015.5** |
| `toi-2263-01.yaml` | TOI-2263.01 | 1723038457072262144 | 10.17 | 2709 | 1.0 | 2624 | J2015.5 | **J2015.5** |
| `toi-2270-01.yaml` | TOI-2270.01 | 1628115694100538624 | 8.07 | 2217 | 0.7 | 2148 | J2015.5 | **J2015.5** |
| `toi-2277-01.yaml` | TOI-2277.01 | 2294551716287593344 | 8.35 | 815 | 0.2 | 790 | J2015.5 | **J2015.5** |
| `toi-2298-01.yaml` | TOI-2298.01 | 2267279837892767488 | 11.94 | 1112 | 1.4 | 1078 | J2015.5 | **J2015.5** |
| `toi-2300-03.yaml` | TOI-2300.03 | 2250961264271388672 | 12.35 | 284 | 1.6 | 275 | J2015.5 | **J2015.5** |
| `toi-2318-01.yaml` | TOI-2318.01 | 1346780595884995968 | 9.47 | 961 | 18.5 | 939 | inconsistent | **J2015.5** |
| `toi-2423-01.yaml` | TOI-2423.01 | 4729324799004633472 | 9.91 | 226 | 0.8 | 218 | J2015.5 | **J2015.5** |
| `toi-2433-01.yaml` | TOI-2433.01 | 2234652178234899712 | 13.29 | 3054 | 1.7 | 2959 | J2015.5 | **J2015.5** |
| `toi-2435-01.yaml` | TOI-2435.01 | 1610656720761692928 | 10.98 | 563 | 0.9 | 546 | J2015.5 | **J2015.5** |
| `toi-2436-01.yaml` | TOI-2436.01 | 1689544206152233472 | 8.92 | 1087 | 1.4 | 1053 | J2015.5 | **J2015.5** |
| `toi-2456-01.yaml` | TOI-2456.01 | 3339208743313866368 | 10.17 | 1214 | 1.9 | 1178 | J2015.5 | **J2015.5** |
| `toi-2472-01.yaml` | TOI-2472.01 | 3204809355377070336 | 9.38 | 378 | 1.0 | 366 | J2015.5 | **J2015.5** |
| `toi-2490-01.yaml` | TOI-2490.01 | 4818818585874648320 | 11.76 | 371 | 1.3 | 358 | J2015.5 | **J2015.5** |
| `toi-2493-01.yaml` | TOI-2493.01 | 2917842382508546560 | 12.18 | 1887 | 1.5 | 1828 | J2015.5 | **J2015.5** |
| `toi-2530-01.yaml` | TOI-2530.01 | 4692151513459769088 | 13.41 | 363 | 0.5 | 351 | J2015.5 | **J2015.5** |
| `toi-2534-01.yaml` | TOI-2534.01 | 6504497488964997632 | 11.14 | 51 | 1.2 | 49 | J2015.5 | **J2015.5** |
| `toi-2634-01.yaml` | TOI-2634.01 | 5642251292706560 | 11.50 | 603 | 2.7 | 586 | J2015.5 | **J2015.5** |
| `toi-2666-01-nss.yaml` | TOI-2666.01 | 3837451574150437120 | 7.54 | 1088 | 0.5 | 1054 | J2015.5 | **J2015.5** |
| `toi-2666-01.yaml` | TOI-2666.01 | 3837451574150437120 | 7.54 | 1088 | 0.5 | 1054 | J2015.5 | **J2015.5** |
| `toi-285-01.yaml` | TOI-285.01 | 4764216563561182336 | 13.07 | 903 | 1.1 | 876 | J2015.5 | **J2015.5** |
| `toi-289-01.yaml` | TOI-289.01 | 4919562197762515456 | 11.88 | 409 | 0.9 | 395 | J2015.5 | **J2015.5** |
| `toi-3500-02.yaml` | TOI-3500.02 | 3471495415361216512 | 11.35 | 1119 | 0.7 | 1084 | J2015.5 | **J2015.5** |
| `toi-3724-01.yaml` | TOI-3724.01 | 183985232046648576 | 12.14 | 312 | 1.1 | 301 | J2015.5 | **J2015.5** |
| `toi-4187-02.yaml` | TOI-4187.02 | 5048187328587727744 | 8.71 | 1492 | 1.0 | 1445 | J2015.5 | **J2015.5** |
| `toi-429-01.yaml` | TOI-429.01 | 4777069717050967040 | 10.70 | 3666 | 2.0 | 3550 | J2015.5 | **J2015.5** |
| `toi-4309-01.yaml` | TOI-4309.01 | 3762126059756436480 | 9.99 | 3233 | 0.3 | 3131 | J2015.5 | **J2015.5** |
| `toi-4319-01.yaml` | TOI-4319.01 | 5556279417085330816 | 11.58 | 1300 | 13.9 | 1246 | inconsistent | **J2015.5** |
| `toi-4321-01.yaml` | TOI-4321.01 | 6395607011309867520 | 7.68 | 904 | 1.4 | 877 | J2015.5 | **J2015.5** |
| `toi-4355-01.yaml` | TOI-4355.01 | 5497773372578215296 | 7.73 | 2299 | 1.0 | 2228 | J2015.5 | **J2015.5** |
| `toi-4509-01.yaml` | TOI-4509.01 | 5501711995027853568 | 11.68 | 94 | 0.6 | 91 | J2015.5 | **J2015.5** |
| `toi-4585-01.yaml` | TOI-4585.01 | 2157077647164391296 | 10.08 | 454 | 0.7 | 439 | J2015.5 | **J2015.5** |
| `toi-5523-01.yaml` | TOI-5523.01 | 3789847707126025600 | 14.80 | 466 | 1.8 | 452 | J2015.5 | **J2015.5** |
| `toi-5563-01.yaml` | TOI-5563.01 | 643250349909794816 | 11.25 | 988 | 0.1 | 958 | J2015.5 | **J2015.5** |
| `toi-5696-03.yaml` | TOI-5696.03 | 3859284748342110208 | 9.65 | 1006 | 0.8 | 975 | J2015.5 | **J2015.5** |
| `toi-5719-01.yaml` | TOI-5719.01 | 744610375504790912 | 10.03 | 241 | 2.1 | 232 | J2015.5 | **J2015.5** |
| `toi-5745-01.yaml` | TOI-5745.01 | 761081437645780864 | 10.38 | 2787 | 1.8 | 2701 | J2015.5 | **J2015.5** |
| `toi-5812-02.yaml` | TOI-5812.02 | 2696613294311603584 | 10.88 | 426 | 1.7 | 411 | J2015.5 | **J2015.5** |
| `toi-5870-01.yaml` | TOI-5870.01 | 1742536509083998208 | 11.17 | 282 | 2.0 | 274 | J2015.5 | **J2015.5** |
| `toi-5893-01.yaml` | TOI-5893.01 | 1743373271792149760 | 11.92 | 197 | 0.5 | 191 | J2015.5 | **J2015.5** |
| `toi-6085-01.yaml` | TOI-6085.01 | 1723715034679751168 | 9.30 | 763 | 0.7 | 739 | J2015.5 | **J2015.5** |
| `toi-6650-04.yaml` | TOI-6650.04 | 2003378188041736320 | 10.36 | 195 | 1.9 | 190 | J2015.5 | **J2015.5** |
| `toi-6653-01.yaml` | TOI-6653.01 | 2800115065478177408 | 9.72 | 6133 | 1.5 | 5941 | J2015.5 | **J2015.5** |
| `toi-6663-01.yaml` | TOI-6663.01 | 1132006667438853760 | 11.23 | 252 | 7.7 | 237 | inconsistent | **J2015.0** |
| `toi-6664-01.yaml` | TOI-6664.01 | 1071126158853591424 | 8.37 | 827 | 0.4 | 802 | J2015.5 | **J2015.5** |
| `toi-6666-01-nss.yaml` | TOI-6666.01 | 2223770483452673408 | 8.78 | 591 | 0.6 | 572 | J2015.5 | **J2015.5** |
| `toi-6666-01.yaml` | TOI-6666.01 | 2223770483452673408 | 8.78 | 591 | 0.6 | 572 | J2015.5 | **J2015.5** |
| `toi-6667-01.yaml` | TOI-6667.01 | 6507438682567821568 | 12.52 | 1516 | 1.2 | 1468 | J2015.5 | **J2015.5** |
| `toi-6670-01.yaml` | TOI-6670.01 | 5324281398476375424 | 9.20 | 442 | 0.9 | 429 | J2015.5 | **J2015.5** |
| `toi-6671-01.yaml` | TOI-6671.01 | 6810533734371193216 | 11.02 | 262 | 0.9 | 255 | J2015.5 | **J2015.5** |
| `toi-6672-01.yaml` | TOI-6672.01 | 1975275839061373312 | 9.73 | 84 | 1.2 | 82 | J2015.5 | **J2015.5** |
| `toi-6674-01.yaml` | TOI-6674.01 | 428410038458702720 | 13.63 | 448 | 1.3 | 435 | J2015.5 | **J2015.5** |
| `toi-6675-01.yaml` | TOI-6675.01 | 1140358282886912256 | 9.73 | 200 | 1.3 | 195 | J2015.5 | **J2015.5** |
| `toi-6691-01.yaml` | TOI-6691.01 | 4767020077694168576 | 8.95 | 508 | 0.4 | 492 | J2015.5 | **J2015.5** |
| `toi-6692-01.yaml` | TOI-6692.01 | 6349145498210403840 | 11.58 | 720 | 0.9 | 697 | J2015.5 | **J2015.5** |
| `toi-6695-01.yaml` | TOI-6695.01 | 5701679002245319296 | 10.75 | 77 | 0.3 | 74 | J2015.5 | **J2015.5** |
| `toi-6698-01.yaml` | TOI-6698.01 | 3499124806833300736 | 11.12 | 1467 | 1.2 | 1421 | J2015.5 | **J2015.5** |
| `toi-6890-01.yaml` | TOI-6890.01 | 5679602531040786816 | 11.51 | 257 | 0.8 | 249 | J2015.5 | **J2015.5** |
| `toi-6893-01.yaml` | TOI-6893.01 | 2741377642494388864 | 8.59 | 662 | 1.0 | 641 | J2015.5 | **J2015.5** |
| `toi-6980-01.yaml` | TOI-6980.01 | 2516286274890560000 | 8.36 | 1491 | 1.2 | 1446 | J2015.5 | **J2015.5** |
| `toi-7399-01.yaml` | TOI-7399.01 | 1633938329724999680 | 9.04 | 411 | 1.6 | 397 | J2015.5 | **J2015.5** |
| `toi-7857-01.yaml` | TOI-7857.01 | 1730371439418183680 | 12.09 | 522 | 2.4 | 505 | J2015.5 | **J2015.5** |
| `toi-790-03.yaml` | TOI-790.03 | 5277235112690260864 | 9.28 | 866 | 1.8 | 837 | J2015.5 | **J2015.5** |
| `toi-941-02.yaml` | TOI-941.02 | 3240852617846876416 | 11.43 | 578 | 1.2 | 559 | J2015.5 | **J2015.5** |


r = residual of the spec position against the DR3 position propagated to that epoch. Full
numbers, including per-axis residuals, parallax and PM: `audit_results.csv`. Final labels and
basis: `final_labels.csv`.

## Checks

| Check | State | Note |
|---|---|---|
| Every query answered | passed | 76/76 DR3 cones plus 10 DR2/DR1 cones returned HTTP 200 |
| Unique Gaia match per target | passed | nearest = brightest in 78/78 |
| Proper motion large enough to discriminate | passed | min 16 yr × PM = 51 mas vs 10 mas threshold |
| Epoch of the TOI-table positions | passed | 77 J2015.5, 1 J2015.0, 0 J2000.0 |
| Positions from non-TOI sources | not_tested | 3 specs use `NAME_RESOLUTIONS.json` (CDS Sesame, labelled "resolver epoch default J2000"); pscomppars (`--planet`) and `--manual` positions are not audited, and the scaffolds now label them `unverified` |
| Perspective acceleration / parallax in propagation | not_tested | neglected; ≪ 1 mas at these distances over 16 yr |

## Changes made from this audit

- `src/cygnus/campaign/scaffold.py`, `src/cygnus/multi/scaffold.py`: `position_epoch()`. TOI-table
  sources give `J2015.5`, other sources give `unverified` unless an explicit epoch is supplied.
- `src/cygnus/campaign/__main__.py`, `src/cygnus/multi/__main__.py`: the TOI-table
  `position_source` names the epoch and this audit.
- `src/cygnus/campaign/runner.py`, `src/cygnus/multi/runner.py`: the queue-target fallback now
  says `J2015.5`, replacing `J2000.0 (TIC)`.
- 78 specs: `epoch:` and `position_source:` per `final_labels.csv`.
- NSS vetting of TOI-2666.01 and TOI-6666.01: the proper-motion check note is corrected and the
  check is marked passed. The SIMBAD-offset and neighbour text in the reports is corrected.

Existing sky records keep the old label until the records are regenerated.

## Reproduction

Environment: Python 3.13.3, astropy 8.0.1, requests 2.34.2, PyYAML 6.0.3; TAP client
`cygnus.ingest.tap.TapDirect`.

```bash
python reports/position-epoch-audit-01/audit_position_epochs.py            # DR3 queries -> gaia_rows.json, audit_results.{csv,json}
python reports/position-epoch-audit-01/audit_position_epochs.py --offline  # reclassify from gaia_rows.json
python reports/position-epoch-audit-01/check_outliers.py                   # DR2/DR1 cones -> gaia_dr2_check.json
python reports/position-epoch-audit-01/finalize.py                         # -> final_labels.csv
```

Output SHA-256 (first 16): `gaia_rows.json` 0ae13350326260d9, `audit_results.json`
bd1be3297bc694bd, `audit_results.csv` 9e4c4e3f780ec66c, `gaia_dr2_check.json` c592998f0e817089,
`final_labels.csv` 6f1957bde7f62ecd.
