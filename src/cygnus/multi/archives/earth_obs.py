"""Earth-observation adapters (DATA_SOURCES.md section 2).

These serve satellite imagery rather than astrophysical products. They are
registered so the framework covers the full source list, but their ``discover``
returns no automatic product for a sky target and is marked ``context``: EO
fetches are only made against explicit areas, never a sky coordinate. Downloads
that need an Earthdata/Copernicus login raise :class:`AdapterUnavailable` when
credentials are absent, rather than silently returning nothing.
"""

from __future__ import annotations

from .base import AdapterUnavailable, ProductRef, Target, as_products, register
from .solar_system import _ContextAdapter


@register
class EarthdataAdapter(_ContextAdapter):
    name = "earthdata"
    description = "NASA Earthdata (MODIS, VIIRS, GPM, Landsat, ICESat-2, HLS); download needs Earthdata login"
    formats = ("text",)
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        try:
            r = self.http_get("https://www.earthdata.nasa.gov/", timeout=30.0)
            r.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"Earthdata unreachable: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": "earthdata_status.txt", "format": "text", "url": None,
                             "description": "Earthdata reachable; cursored product search needs search.earthdata.nasa.gov",
                             "text": "Earthdata reachable", "inline": True}], self.name, "text")


@register
class CopernicusAdapter(_ContextAdapter):
    name = "copernicus"
    description = "Copernicus Data Space Ecosystem (Sentinel-1/2/3/5P; anonymous browse, account for download)"
    formats = ("text",)
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        try:
            r = self.http_get("https://dataspace.copernicus.eu/", timeout=30.0)
            r.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"CDSE unreachable: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": "cdse_status.txt", "format": "text", "url": None,
                             "description": "CDSE reachable; STAC/openEO search needs a free account",
                             "text": "CDSE reachable", "inline": True}], self.name, "text")


@register
class AsfAdapter(_ContextAdapter):
    name = "asf"
    description = "Alaska Satellite Facility DAAC (Sentinel-1, ALOS, RCM, SMAP); free Earthdata login"
    formats = ("text",)
    verified = "[K]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        raise AdapterUnavailable("ASF Vertex search uses an authenticated session; not wired for anonymous discovery")


@register
class UsgsAdapter(_ContextAdapter):
    name = "usgs"
    description = "USGS EarthExplorer (full Landsat history); free USGS account"
    formats = ("text",)
    verified = "[K]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        raise AdapterUnavailable("USGS EarthExplorer needs an account session; not wired for anonymous discovery")


@register
class FirmsAdapter(_ContextAdapter):
    name = "firms"
    description = "NASA FIRMS active-fire detections (browse anonymous, download needs Earthdata login)"
    formats = ("text",)
    verified = "[K]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        raise AdapterUnavailable("FIRMS download requires an Earthdata login; browsing is interactive only")


@register
class WorldviewAdapter(_ContextAdapter):
    name = "worldview"
    description = "NASA Worldview / GIBS near-real-time imagery (anonymous browsing)"
    formats = ("text",)
    verified = "[K]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        raise AdapterUnavailable("Worldview is a browser viewer; use GIBS WMTS for programmatic tiles")


# EO services are none of them a sky-object product: label them uniformly so a
# campaign summary cannot mistake an Earth-observation fetch for an astronomy one.
for _cls in (EarthdataAdapter, CopernicusAdapter, AsfAdapter, UsgsAdapter, FirmsAdapter, WorldviewAdapter):
    _cls.capabilities = ("earth_observation", "context")