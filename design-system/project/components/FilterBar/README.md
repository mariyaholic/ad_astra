# FilterBar

Search field plus type chips above a listing; filters rows client-side and mirrors the state into `?q=&type=`.

- Consumer provides: the rows (`data-filter-row`, `data-type`, lowercase `data-search`), the type list with counts, a `[data-result-count]` live region and a `[data-filter-empty]` state.
- The bar ships `hidden` and is revealed by script, so the listing is complete without JavaScript.
- Chips are toggle buttons (`aria-pressed`); the pressed chip inverts to `ink` fill on `bg` text. Always keep an "All" chip first.
- Result count reads "N of M entries shown".
