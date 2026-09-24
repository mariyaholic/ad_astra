"""Archive clients.

Heavy dependencies (astroquery/astropy/lightkurve/...) are imported lazily
inside function bodies so the package and its unit tests run without them;
install the corresponding extras (``pip install 'cygnus[mast]'``) when real
retrieval is needed.
"""

from .scratch import cleanup_scratch, resolve_scratch

__all__ = ["resolve_scratch", "cleanup_scratch"]
