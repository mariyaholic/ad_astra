# Redesign mockups and the sky explorer (prototype)

Status (2026-09-24): **prototype for review, not the published site.** The user has approved the direction (an interactive night-sky explorer) but not yet the conversion of the real site in `src/cygnus/publish/`. Do not replace the published templates with this code without that approval. See `docs/STATUS.md`.

Everything here follows AGENTS.md "verifiable telemetry only": every position, footprint, star and image comes from a recorded file or a fetch logged in `data/PROVENANCE.json`. Renditions are labelled as generated from catalogue values and say which parts are illustrative.

## Contents

| Path | What | Committed? |
|---|---|---|
| `explorer/index.html`, `explorer.js`, `explorer.css`, `favicon.svg` | the sky explorer (canvas; no external scripts or fonts) | yes |
| `explorer/data/`, `explorer/img/` | generated bundle | no — rebuilt by `build_explorer.py` |
| `data/` | fetched public catalogue extracts, survey cutouts, `PROVENANCE.json` | yes (so builds are offline and reproducible) |
| `fetch_sky_data.py` | fetches `data/` from public archives (network) | yes |
| `build_explorer.py` | builds the explorer bundle from `data/` and the worktree records (offline) | yes |
| `build_mockups.py`, `index.html`, `target-wasp-12.html`, `log.html`, `mockup.css` | earlier static mockups (sky map, target page, observing log) | yes |

## Run it

From the repository root (Python 3.10+, `numpy`, `requests`; `pip install -e ".[analysis]" requests`):

```bash
python design-system/mockups/build_explorer.py          # offline; writes explorer/data and explorer/img
python -m http.server 8768 --bind 127.0.0.1 --directory design-system/mockups
# open http://127.0.0.1:8768/explorer/   (deep link a target: /explorer/#wasp-12)
```

The page must be served over HTTP (it fetches `data/sky.json`); opening the file directly will not work.

## Inputs

| Layer | Source |
|---|---|
| target positions | `docs/tier1_pack/NAME_RESOLUTIONS.json` (CDS Sesame), plus explicit positions in sky records |
| query footprints ("patches") | parsed from each row of `docs/tier1_pack/MASTER_MANIFEST.csv`; rows whose query records no size are listed, not drawn |
| analyses, plots, checks | every `sky_record.json` via `cygnus.skyrecord.collect` (see `docs/SKY_RECORDS.md`) |
| bright stars | Yale Bright Star Catalogue (VizieR V/50), V ≤ 6.5 |
| Milky Way glow | Gaia DR3 source counts, G < 11, per HEALPix level-5 cell |
| zoomed star fields | Gaia DR3 cones around each target (J2016.0 positions) |
| planet systems | NASA Exoplanet Archive `pscomppars` |
| survey images | CDS hips2fits: Pan-STARRS1 DR1 colour (Dec > −29°), else 2MASS colour |

## Common tasks

- **A new analysis finished:** write its `sky_record.json` (required by AGENTS.md, enforced by `tests/test_skyrecord.py`), then run `build_explorer.py`. No explorer code changes are needed.
- **A new target with explicit coordinates:** `python design-system/mockups/fetch_sky_data.py --missing` fetches its Gaia field and survey image and records provenance; then rebuild.
- **Refresh all catalogue data:** `python design-system/mockups/fetch_sky_data.py` (network, a few minutes). Commit `data/` with its updated `PROVENANCE.json`.

## Rules for changing the explorer

- Never draw a position, footprint or value that is not in an input above. If a query's footprint cannot be parsed, list it without a shape.
- Renditions (system views, transit discs, generated fields, colour–magnitude diagrams) must say what they are generated from and which parts are illustrative (enlarged planets, unmeasured orbital phases, generic limb darkening).
- Check states are shown exactly as recorded: passed, failed, inconclusive, not tested.
- Third-party terms: Gaia (CC BY-SA 3.0 IGO), Pan-STARRS1, 2MASS and CDS/VizieR need the acknowledgements already present in the captions and `data/PROVENANCE.json`.
- Keep it self-contained: no CDN scripts or web fonts (the published site's CSP is `default-src 'self'`).

## Checked so far

Checked in a browser: whole sky, WASP-12, TRAPPIST-1, Pleiades and M44 views, renditions, the comparison viewer, the tour and night vision, at narrow and ~800 px widths. **Not yet checked:** full-width desktop, keyboard-only use, screen readers.
