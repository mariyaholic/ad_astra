# PageHead

Top of every page: breadcrumbs, a mono kicker, one serif `h1`, an optional lede and badges, closed by the coordinate-ruler hairline.

- Consumer provides: kicker text (what kind of page · a count or qualifier), the title, optional lede (≤ 2 sentences, `lede` style, `ink-2`), optional badges.
- The ruler (`.page-head::after`) is the system's signature motif: minor ticks every 12px, major every 60px in `rule-strong`. Use it only here.
- Exactly one `h1` per page. When the title is an identifier, use `h1.id` (mono `id-title`).
- Kicker format: `TYPE · qualifier` — e.g. "Collection · dataset", "Candidate dossiers · 0 published".
