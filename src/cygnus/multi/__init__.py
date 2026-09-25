"""Multi-archive campaign pipeline (``python -m cygnus.multi``).

Extends ``cygnus.campaign`` with archive adapters (``cygnus.multi.archives``) so a campaign can
discover, fetch and read products from any archive in ``DATA_SOURCES.md``, not only MAST SPOC
light curves. Shared pieces — the ledger, config, sky-record schema, SPOC reader and screen
primitives, catalogue cross-match and lead vetting — are the production modules; the MAST code
path is pinned unchanged by ``tests/test_multi_archive_runner.py`` (offline, on synthetic
products). Specs declare ``runner: cygnus.multi`` and ``python -m cygnus.campaign`` hands them
over. Runs are ledgered under the ``cygnus_multi:`` script namespace. See ``docs/CAMPAIGNS.md``
("Multi-archive campaigns").
"""

__all__ = ["archives", "readers", "runner", "steps", "lightcurve", "scaffold", "source_checks", "systematics",
           "nss", "promote"]
