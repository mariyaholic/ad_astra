# StateBar

Horizontal stacked bar of archive-manifest row outcomes (held / excluded / failed) with a legend and a row total.

- Fixed segment order: held (`seg-held`), excluded (`none-wash` fill, dashed `none` stroke), failed (`fail`). Never reorder or recolour per chart.
- Always with the legend above and the table of rows nearby; each segment has a `<title>` tooltip and the SVG an `aria-label` listing counts.
- Strokes use `vector-effect: non-scaling-stroke` because the SVG stretches.
