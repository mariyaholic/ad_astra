"""Experimental multi-archive campaign pipeline (isolated copy of ``cygnus.campaign``).

This package is a *safe working copy*: the production runner in ``cygnus.campaign``
is not modified. Here the product discovery/fetch/read path is generalised through
archive adapters (``cygnus_multi.archives``) so a campaign can be run against any
archive listed in ``DATA_SOURCES.md``, not only MAST.

Entry point (run from the repository root, or use ``experimental/run.cmd``/``run.sh``)::

    python -m experimental.cygnus_multi run experimental/campaigns/<id>.yaml

Writes are confined to the sandbox root (``CYGNUS_MULTI_ROOT``, default
``experimental/``) and runs are ledgered under the ``cygnus_multi:`` namespace. The
package shares the core ``cygnus`` ledger *class*, config and sky-record schema, but
never the production output directories or script namespace.
"""

__all__ = ["archives", "readers", "runner", "steps", "lightcurve", "targets", "priorart", "scaffold", "vet",
           "source_checks", "systematics", "nss"]