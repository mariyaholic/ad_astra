Ad Astra is the visual and verbal system of the Project Cygnus / Astraea public repository: a field notebook kept on an instrument console. It exists to make research records legible and to make their status impossible to misread. Every rule below serves one principle: **the design must never claim more than the evidence does.**

The reference implementation is the static site in `src/cygnus/publish/` (stylesheet `static/site.css`, macros `templates/_macros.html.j2`). Token names here are the site's CSS custom property names, so `var(--ink)` means the same thing in both.

## Content fundamentals

**Voice.** Plain, measured, specific. Write like a careful lab notebook read by a stranger: what was done, what was found, what was not tested. Active voice, sentence case, no exclamation marks, no emoji, no superlatives.

- Say what a thing is before what it could be: "Engineering baseline · not a scientific result", "Draft · not executed".
- Missing is missing. Render absent values as `not recorded`, `not specified by the project`, `none selected yet` — in the `.unset` style — never as a blank, a zero or a plausible guess.
- Counts are dated: "Status at build time · read 2026-09-24T00:46:08Z". Never "live", never animated tickers.
- Negative results are content. "Retrieval failed", "zero SPOC timeseries observations matched", "no close recorded" appear in tables, not footnotes.
- A missing catalog match is "not found in the services searched as of <date>", never "uncatalogued" or "new".
- Identifiers beginning `CYG-` are working IDs. Wherever one is the subject, the page also says "not an official designation".

**Banned words and moves** (unless quoting a source): discovery (as a claim), breakthrough, confirmed (for anything below *established*), mysterious, groundbreaking, "we found" before an artifact audit, rounding "not tested" up to "passed", dramatic calls to action.

**Real examples from the site.**

> No candidate dossier has been published, and the provenance ledger holds 0 candidate records. What is here today is infrastructure: specifications, a draft campaign plan, archive-access tests, and their provenance.

> “Not tested” means the test was unavailable or not run. It never counts toward a higher evidence level.

> The measurements cite their input product by an ID that does not exactly match the product row in the ledger. The site shows the link as **unresolved** instead of guessing it.

**Units and time.** Keep units in their own column or directly after the value (`1289 cadences`, `±150 ppm`). Timestamps are ISO-8601 UTC with `Z` in `mono`. Dates alone are `YYYY-MM-DD`. Sizes use decimal units (`27.4 KB`).

## Visual foundations

**Colour.** Two themes built from the same roles: *Paper* (light, default) and *Console* (dark). Grounds are `bg` (page), `surface` (raised: header, panels, tables) and `surface-sunk` (recessed: table heads, code). Text is `ink`, `ink-2`, `ink-3` in descending emphasis; every text token clears 4.5:1 on all three grounds in both themes (lowest pair: `ink-3` on `surface-sunk`, 4.89:1 light / 5.76:1 dark).

- One accent: `accent` (plotting-ink blue) for the current-page underline, solid buttons, focus ring and route arrows; `accent-ink` for link text; `accent-wash` for hover. Nothing else is blue.
- State colours are reserved and never decorative: `pass`, `fail`, `warn`, `none`, each with its `-wash` ground. They always travel with a glyph and a word (see StateChip), so no state depends on hue. `draft` marks drafts and nothing else.
- Neutrals are warm-grey paper and cool-grey console, chosen, not defaulted. No gradients anywhere.

**Type.** Three roles, all system-installed faces with named preferred families first; the site loads no web fonts and makes no third-party requests.

- `serif` (`page-title`, `display-hero`): the one `h1` per page. Archival, quiet, 600 weight.
- `ui` (`heading-2`, `heading-3`, `lede`, `body`, `small`): everything read.
- `mono` (`kicker`, `stat`, `id-title`, `data`, `chip-label`): everything *recorded* — identifiers, hashes, timestamps, labels, figures. If a string could be pasted into a query, it is mono.
- Tabular figures everywhere (`font-feature-settings: "tnum"`). Prose max `measure` (72ch).

**Space and layout.** A 4px scale `s1`–`s8`. Pages sit in `page` (1180px) with `s5` gutters (`s4` under 640px). Detail pages use `.grid-2`: main column 2fr, facts sidebar 1fr, stacked below 900px. Long documents use `.doc`: a 230px sticky table of contents beside the text. Sections are separated by `s7` and a heading row with a `rule` hairline, not by boxes.

**Lines, not shadows.** Structure is drawn with hairlines: `rule` between regions, `grid` inside tables, `rule-strong` for outlines and the ruler. Corners are nearly square — `radius` (3px) on panels and controls, `radius-tight` (2px) on badges and chips. The only shadow is `focus`.

**Motifs** — each has exactly one meaning:

- *Coordinate ruler* under every page head (ticks every 12px, major every 60px): this is an instrument record.
- *Diagonal hatch* on the draft callout's rail: not executed, no results.
- *Graph-paper grid* behind empty states: nothing recorded here yet.
- *Dashed outline*: not tested, excluded, planned, open, restricted — absence or incompleteness.

**Data display.** Tables live in `.table-wrap` so they scroll inside themselves and the page never scrolls sideways. The one chart form is the StateBar (stacked outcome counts) with a legend and the underlying table nearby. Segment order and colours are fixed (`seg-held`, `none-wash` dashed, `fail`), validated for colour-vision deficiency.

**Motion.** Only 120ms colour transitions on hover and press. No entrance animations, parallax, particles or glow. `prefers-reduced-motion: reduce` removes all transitions.

**States and focus.** Hover: `accent-wash` ground or a thicker underline. Pressed chip: `ink` fill with `bg` text. Keyboard focus: the `focus` ring (2px `surface` gap + 2px `accent`) on every interactive element. First tab stop on every page is "Skip to content".

**Theming mechanics.** Light tokens on `:root`; dark under `@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])`, and again under `:root[data-theme="dark"]`. The theme toggle writes `data-theme` and remembers it per browser.

## Iconography

There is no icon font and no icon set. The system uses a small fixed set of Unicode glyphs, always beside a word:

| Glyph | Meaning |
| --- | --- |
| ✓ | passed · completed · verified |
| ✕ | failed |
| ~ | inconclusive · unresolved |
| ○ | not tested · planned |
| ■ | held · implemented · aborted |
| – | excluded |
| … | open (no close recorded) |
| ↗ | external link (after the link text) |
| → | route or "go to" link |

The brand mark is the Northern Cross (see Logos): five square stars on two hairline strokes. Draw it only from the asset files or the site's inline SVG; do not redraw, animate or add stars.

## Accessibility floor

- Text ≥ 4.5:1 on its grounds in both themes (verified for every token pair above); marks and borders that carry meaning ≥ 3:1.
- No state by colour alone; no information only in hover.
- One `h1`, `lang="en"`, a `main` landmark and a skip link on every page; tables have `scope`d headers and labelled scroll regions.
- Layouts work at 375px with no horizontal page scroll.
- No inline styles or scripts (the site's Content-Security-Policy is `self`-only); pages remain complete without JavaScript.

## Composing a page

1. SiteHeader, then PageHead (crumbs → kicker → serif `h1` → lede → badges → ruler).
2. If the subject is a draft, restricted, withdrawn or a candidate, the matching Callout comes next — before any data.
3. Main column: sections with `heading-2` rows; DataTables, MetaLists, Steps, StateBars.
4. Sidebar Panels: record facts, citation, files, RelatedList, EvidenceLadder.
5. EmptyState wherever a section has nothing — with the real count and the condition under which it fills.
