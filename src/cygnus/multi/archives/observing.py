"""Steerable-observing adapters (DATA_SOURCES.md section 3).

These routes request *new* observations rather than retrieving archived
products, so ``fetch`` is not meaningful. They are registered so a campaign can
declare follow-up intent and so ``summary()`` covers the full source list;
``discover`` performs a reachability check and returns a status product, and
``fetch`` raises :class:`AdapterUnavailable` because there is no data to fetch
until a request is made and fulfilled (which is a user decision).
"""

from __future__ import annotations

from .base import AdapterUnavailable, ProductRef, Target, as_products, register
from .solar_system import _ContextAdapter


@register
class MicroObservatoryAdapter(_ContextAdapter):
    name = "microobservatory"
    description = "CfA MicroObservatory / Observing With NASA (free, fixed target list, no account)"
    formats = ("text",)
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        try:
            r = self.http_get("https://mo-www.cfa.harvard.edu/cgi-bin/OWN/Own.pl", timeout=30.0)
            r.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"MicroObservatory control endpoint unreachable: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": "microobservatory_control.txt", "format": "text", "url": None,
                             "description": "MicroObservatory control endpoint reachable; image arrives next day",
                             "text": "MicroObservatory reachable", "inline": True}], self.name, "text")

    def fetch(self, ref: ProductRef, dest, *, timeout_s: float = 120.0):
        raise AdapterUnavailable("MicroObservatory returns a next-day image after a manual request; nothing to fetch yet")


@register
class SkynetAdapter(_ContextAdapter):
    name = "skynet"
    description = "Skynet Robotic Telescope Network (free sign-up; custom RA/Dec, filters, queue)"
    formats = ("text",)
    verified = "[V]"

    def discover(self, target: Target, *, limit: int = 1, **opts) -> list[ProductRef]:
        try:
            r = self.http_get("https://skynet.unc.edu/", timeout=30.0)
            r.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            raise AdapterUnavailable(f"Skynet unreachable: {type(exc).__name__}: {exc}") from exc
        return as_products([{"product_id": "skynet_status.txt", "format": "text", "url": None,
                             "description": "Skynet reachable; requires a free account to submit a queue request",
                             "text": "Skynet reachable (login required to observe)", "inline": True}], self.name, "text")

    def fetch(self, ref: ProductRef, dest, *, timeout_s: float = 120.0):
        raise AdapterUnavailable("Skynet is a request queue; observations must be submitted with an account")


# observing routes submit new work; they never yield an archived product to screen
for _cls in (MicroObservatoryAdapter, SkynetAdapter):
    _cls.capabilities = ("observing",)