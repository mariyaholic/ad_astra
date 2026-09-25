"""Archive adapters for the experimental multi-archive pipeline.

Importing this package registers every adapter. Use::

    from cygnus_multi.archives import base
    base.summary()          # every registered archive
    base.get("gaia")        # one adapter

Only astronomy archives that serve retrievable *products* are wired into campaign
steps; catalogue/context services return tables, and observing-only routes raise
``AdapterUnavailable`` for discovery (they cannot be fetched, only requested).
"""

from . import base  # noqa: F401
from . import astronomy  # noqa: F401  (registers MAST, Gaia, SkyView, CDS, NED, ESO, IRSA, Legacy, ExoArchive)
from . import solar_system  # noqa: F401  (registers Horizons, SBDB, MPC, AstDyS, SkyBoT)
from . import earth_obs  # noqa: F401  (registers Earthdata, CDSE, ASF, USGS, FIRMS)
from . import observing  # noqa: F401  (registers MicroObservatory, Skynet)

__all__ = ["base", "astronomy", "solar_system", "earth_obs", "observing"]