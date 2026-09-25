# Experimental multi-archive pipeline

A **safe working copy** of the campaign pipeline that can analyse products from
any archive in `DATA_SOURCES.md`, not only MAST SPOC light curves. The production
runner in `src/cygnus/campaign/` is **not modified** and keeps running exactly as
before; this tree imports it only for shared, read-only pieces (ledger, config,
sky-record schema, resumable downloader).

## Why a copy

The production `fetch_products` step is hardcoded to MAST TESS SPOC 120-s light
curves (`_discover_spoc_lcs`, `MAST_DOWNLOAD`) and the screen's reader requires
the SPOC column set. Adding archives there would have meant changing the runner
that produced the committed 76-target queue and its sky records. Instead the
pipeline is duplicated here and generalised through an adapter layer, so the two
can be compared and the proven parts promoted later.

## Layout

```
experimental/
  __init__.py          makes `python -m experimental.cygnus_multi` runnable from the repo root
  cygnus_multi/
    __init__.py        package doc
    __main__.py        CLI: run/check/new/report/vet/queue/archives
    runner.py          ledgered, resumable step runner (archive-aware records)
    steps.py           screen/calibration/known-signal/aliases/prior-art steps
    lightcurve.py      screen primitives + read_campaign_lc (any archive)
    readers.py         format dispatch: LightCurve / Image / Table
    systematics.py     red-noise model + event significance (single-channel)
    source_checks.py   per-source integrity/context check helpers
    nss.py             Gaia NSS two-body cross-match and mass function
    targets.py         ranked TOI target queue
    priorart.py        Known-Object Gate catalogue adapters
    scaffold.py        spec/report/queue generation (per-archive aware)
    vet.py             lead vetting (MAST SPOC products only)
    archives/
      base.py          ArchiveAdapter contract, ProductRef/Target, registry
      astronomy.py     MAST, Gaia, SkyView, VizieR, SIMBAD, NED, ESO, IRSA,
                       Legacy Survey, Exoplanet Archive
      solar_system.py  Horizons, SBDB, MPC, AstDyS, SkyBoT
      earth_obs.py     Earthdata, Copernicus, ASF, USGS, FIRMS, Worldview
      observing.py     MicroObservatory, Skynet
  tests/               offline tests (no network); run explicitly
  promote.py           promote a completed sandbox campaign into campaigns/ (draft collection)
  VERIFICATION_REQUEST.md  independent-verification request and promotion contract
  campaigns/           specs written by `new` live here (sandbox)
  state/               sandbox ledger (gitignored)
  run.cmd / run.sh     launchers that cd to the repo root and set PYTHONPATH
```

## Usage

Run from the repository root (the launchers `cd` there for you and set
`PYTHONPATH`):

```bash
experimental/run.sh archives          # Windows: experimental\run.cmd archives
# or, from the repository root:
python -m experimental.cygnus_multi archives

# live-probe one adapter's discovery path
experimental/run.sh archives --check gaia --ra 139.48 --dec -3.39

# generate a campaign that fetches from several archives
experimental/run.sh new --manual "TOI-2666.01" --tic 170889511 --ra 139.480865 \
    --dec -3.387525 --t0 2459259.1414 --archives mast,gaia,skyview

experimental/run.sh run    experimental/campaigns/<slug>.yaml
experimental/run.sh report experimental/campaigns/<slug>.yaml
experimental/run.sh queue  # what is free/claimed/run in the sandbox
```

When `--archives` is omitted, the generated spec uses the original MAST SPOC
discovery path, so behaviour matches the production runner for existing targets.

### Sandbox confinement

Everything an agent does stays under the sandbox root: specs and outputs under
`<root>/campaigns/`, the ledger under `<root>/state/ledger.sqlite`. The root is
`CYGNUS_MULTI_ROOT` when set, else `experimental/`. The production
`campaigns/`, `reports/` and `state/` are never written by this CLI, and the
ledger records runs under the `cygnus_multi:` script namespace, so experimental
provenance cannot be confused with, or reused by, the production
`cygnus.campaign:` runs. `--ledger` or `CYGNUS_LEDGER` overrides the ledger path
explicitly.

`experimental/tests/` is separate from the production suite (`pytest tests`):
run it with `python -m pytest experimental/tests -q`.

## Running agents on the pipeline

* **One campaign per agent.** `new` refuses to overwrite an existing
  `campaigns/<slug>.yaml`, so claiming a target is collision-safe; `queue` shows
  what is free, claimed, run and reviewed.
* **Do not run two agents on the same campaign at once.** Step outputs
  (`runner/<step>.json`) and the ledger are not file-locked; parallel writers can
  interleave. Split work by target, not by step.
* **Steps are resumable.** Re-running skips a step whose config hash (params,
  shared spec blocks, upstream outputs, code fingerprint) matches a completed
  run; `--force` recomputes, `--until <step>` stops early.
* **Failure is explicit.** A step that cannot fetch or read raises and is
  recorded `failed` in the ledger with the reason; an unavailable archive is a
  note and a `not_tested` check, never an empty success. CLI exit codes:
  `0` success, `1` run/new/queue error, `2` spec missing or invalid.
* **Check the record.** Every campaign writes `sky_record.json`; promotion
  validates it against `cygnus.skyrecord`, and the production gate fails if a
  spec or report lacks one. (The sandbox tests do not yet schema-check records —
  that gap is listed in `VERIFICATION_REQUEST.md`.) Read
  `runner/RUN_SUMMARY.json` and the checks before treating any event as a lead.

## Promotion and independent verification

Sandbox results stay private until promoted. The promotion path is
`experimental/promote.py` (no production code change):

```bash
python -m experimental.promote --campaign <sandbox-id> --as <production-id> --dry-run
python -m experimental.promote --campaign <sandbox-id> --as <production-id> --note "..."
```

It validates the sandbox record with `cygnus.skyrecord.validate`, refuses to
overwrite existing production content, copies the spec/report/search log/record
and runner outputs into `campaigns/<production-id>/`, writes `PROMOTED.md` with
the sandbox ledger run ids, and creates a **draft**
`publish/collections/<production-id>.json`. It never publishes or deploys —
that remains the user's decision (`docs/PUBLISHING.md`).

The pipeline itself must be **independently verified before any of it is merged
into `src/cygnus/`**. The request, acceptance criteria and claim-by-claim test
plan are in `experimental/VERIFICATION_REQUEST.md`; the verifier writes their
verdict as a normal analysis under `reports/<verification-id>/`. A promoted
result is not an endorsement: `PROMOTED.md` and the report record the provenance
and any withdrawn or corrected claims.

## The adapter contract

Every adapter subclasses `archives.base.ArchiveAdapter` and implements
`discover(target, **opts) -> list[ProductRef]`. `fetch` and `read` are provided:
download is resumable and bounded (`cygnus.ingest.netio`), and `read` dispatches
on the product `format` through `readers.py`:

* `LightCurve` — `spoc_lc`, `tess_lc`, `kepler_lc`, `csv_lc`: one time axis and
  named flux channels. `read_campaign_lc` maps the available channels onto the
  screen's `SAP`/`PDCSAP` pair and records the mapping in `primary['_channels']`,
  so a single-channel product is visible as non-independent rather than hidden.
* `Image` — `fits_image`, `fits_cube`, `coadd_image`.
* `Table` — `csv`, `votable`, `table`, `json`.

**Unavailable is never "no match."** An adapter that cannot be queried raises
`AdapterUnavailable`; the runner records a note (state *not tested*) and the
ledger record shows it. Archives that only request new observations (MicroObservatory,
Skynet) or need an authenticated session (ASF, USGS, FIRMS) raise
`AdapterUnavailable` from `discover`/`fetch` rather than returning an empty list.

**Product kinds keep the screen honest.** Every product carries a `kind`
(`lightcurve`, `image`, `table`, `text`). The screen, calibration and recovery
steps iterate only light-curve products; other products are read and summarised
by the `context_products` step into `context.json` with their row counts, image
shapes and byte sizes. A campaign that retrieves only images/tables reports no
light curve rather than feeding an image into the transit screen.

## Coverage

Section 1 (deep-sky) adapters retrieve analysable products. Section 5
(solar-system) return context tables. Sections 2–3 are registered for coverage:
EO services need area inputs/accounts, and observing routes request new data.
Per-service quirks and verification dates are in `DATA_SOURCES.md`; each adapter
carries a `verified` tag (`[V]` live, `[K]` knowledge-based).

## Per-source checks

Every adapter runs its own checks on its fetched products via the
`source_checks` step (written to `source_checks.json`, one aggregate check per
archive in the sky record):

| Source | Check |
|---|---|
| MAST | cadence, baseline, time standard, and the SPOC `QUALITY != 0` census |
| Gaia | table rows, nearest match, RUWE > 1.4 count, `non_single_star` flags, parallax range |
| VizieR / SIMBAD / NED / Exo Archive | row count and nearest-match separation |
| SkyView / Legacy Survey | image shape, finite-pixel fraction, robust background |
| IRSA | ZTF magnitude light-curve cadence/baseline, or AllWISE table rows/nearest match |
| ESO | readable product of its kind with finite pixels/rows |
| Horizons / SBDB | payload parses; object text present |
| MPC | observations returned by the `data.minorplanetcenter.net` API, with a record count |
| SkyBoT | known-object rows at a required observation epoch |
| Earth-observation, observing | reachability / account requirement; a campaign summary cannot mistake one for a sky product |

An archive-level state is the worst of its checks: `failed` > `inconclusive` >
`not_tested` > `passed`. A CSV with no `TIMESYS`, for example, is honestly
`not_tested` on the time standard even when its other checks pass.

## Single-channel products

A product with one flux channel (a CSV, a ZTF magnitude series) is read with
`sap == pdc` and `independent=False`. The screen then runs *once* per baseline,
persistence means repeatability across baselines only, and the record says
`channel_mode: "single"` with a persistence basis of
`"baseline repeatability (single channel; not independent)"`. It never claims a
SAP-versus-PDCSAP comparison it does not have.

### Red-noise systematics model (`systematics.py`)

Because a single-channel product has no second reduction to compare against, the
pipeline builds a noise model from the light curve itself:

* the residual autocorrelation gives the red-noise correlation timescale `tau`;
* a box statistic at the event is measured against the same light curve at random
  epochs (empirical per-epoch p-value);
* a parametric p-value comes from the robust z **inflated by** `sqrt(tau / cadence)`,
  then corrected for the number of independent resolution elements
  (`span / max(duration, tau)`) — a look-elsewhere correction;
* both are written to `screen.json` under `systematics_model`, and the strongest
  event sets the check `Single-channel event significance (red noise)`
  (`passed` FAP ≤ 0.01, `inconclusive` ≤ 0.1, `failed` otherwise; `not_tested`
  when the veto leaves no event to assess).

The caveat is recorded: a correlated systematic repeating on the event timescale
can still mimic a dip. The model constrains noise; it does not prove origin. The
empirical p-value is floor-limited by the number of random epochs, so the
parametric, tau-inflated value drives the state and both are reported.

## Astrometric vetting (Gaia NSS)

`astrometric_vetting` cross-matches each target against Gaia DR3
`nss_two_body_orbit` (verified live schema). For a solution it records the type,
period, eccentricity, significance, goodness of fit, flags, astrometric jitter,
and — where the primary RV amplitude is present — the spectroscopic mass function

    f(M) = P K1^3 (1 - e^2)^(3/2) / (2 pi G)

Interpretation follows the audit discipline: a solution at or above
`significance_min` means the companion is **already known to Gaia**, so the
new-unseen-companion hypothesis is refuted (`failed`); no solution is
`inconclusive` — Gaia's sensitivity is incomplete, so absence is not proof of a
single star; an unmatched target or unavailable service is `not_tested`. A
minimum companion mass would need an adopted primary mass and inclination and is
not claimed. Written to `nss.json`; generated specs include the step when `gaia`
is among the archives.

## Tests

```bash
python -m pytest experimental/tests -q
```

Offline and synthetic: registry coverage, the adapter contract (including
"unavailable is not empty"), readers (FITS, CSV, ZTF VOTable), per-source checks
(Gaia flags, NaN image, MPC data API, malformed product), the red-noise model
(deep dip significant, shallow dip in red noise not), Gaia NSS vetting (known
companion, no solution, unmatched target, low significance), single-channel
screening end to end, an end-to-end multi-archive run, a mixed light-curve + table
campaign that screens only the curve, a pinned MAST path, and an unavailable-archive
failure that records why rather than returning nothing.

## Known limits

* The red-noise model is a per-light-curve noise model, not a physical
  systematic model: it cannot exclude a correlated instrumental signal that
  repeats on the event timescale.
* Gaia NSS vetting uses the published two-body solution; the pipeline does not
  fit an orbit itself and does not derive a companion mass (that needs an adopted
  primary mass and inclination).
* Earth-observation and observing routes need credentials or manual requests by
  design; they are registered for coverage and honest reporting, not automation.