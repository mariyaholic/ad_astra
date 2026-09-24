# DataTable

Tables inside `.table-wrap` (its own horizontal scroll, keyboard focusable, labelled region) so the page never scrolls sideways.

- Heads: mono uppercase `fs-xs` on `surface-sunk`, sticky. Numbers right-aligned `.num` with tabular figures. IDs `td.id` mono, min 26ch, wrap anywhere.
- Every value that can be missing uses `.unset`. Units get their own column; uncertainties are never dropped.
- Row hover `accent-wash`. Captions sit below the table in `ink-3`.
