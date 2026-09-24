# SiteHeader

The one header on every page: Northern Cross mark and wordmark, the five primary routes, and the theme toggle.

- Consumer provides: nothing beyond the page path — the current route gets `aria-current="page"` (ink text, 2px `accent` underline).
- Order is fixed: Repository, Campaigns, Candidates, Search log, Methods. Do not add routes for things that are not published.
- The brand mark is inline SVG in `currentColor` (ink); squares are stars (Deneb, Sadr, Albireo, the wings), not decoration.
- The theme toggle is rendered `hidden` and revealed by script; it cycles system → light → dark and states its current value in words ("Theme: system").
- Under 640px the nav becomes a horizontally scrolling row beneath the brand; never a hamburger menu.
- Ground: `surface`, bottom hairline `rule`.
