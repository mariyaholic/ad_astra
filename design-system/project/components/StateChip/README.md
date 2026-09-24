# StateChip

Outcome of a test, run, retrieval or module: glyph + word + reserved colour, so it reads without colour.

- Audit states (exactly four, never merged): `passed` ✓ `pass`, `failed` ✕ `fail`, `inconclusive` ~ `warn`, `not_tested` ○ `none` with a dashed border. "Not tested" is never styled like "passed".
- Retrieval: `held` ■ neutral, `excluded` – dashed, `failed` ✕. Runs: `completed` ✓, `open` … dashed warn ("no close recorded"), `aborted` ■.
- Module status: `verified` ✓, `implemented` ■, `planned` ○ dashed, `unknown` dotted.
- Consumer provides the state key and, optionally, a more specific word ("drive only", "unresolved"). Never invent a new colour for a new state; map it to one of these.
