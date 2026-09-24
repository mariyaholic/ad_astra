"""Bounded, offline research utilities—not a discovery or significance engine.

All functionality consumes in-memory inputs or reads a caller-selected,
checksum-verified local pack product. Heavy science dependencies are imported
on demand. See ``docs/ANALYSIS_SUITE.md`` for scientific limitations.
"""

from .crossmatch import Pair, Source, match_optical_infrared
from .imaging import Feature, ResidualResult, independent_band_consistency, triage_residual
from .io import (PackIntegrityError, PackProduct, checked_product_path,
                 read_manifest, read_spoc_lightcurve, read_tesscut_window)
from .ml import AnomalyRanking, rank_control_trained_anomalies
from .nss import (NEGATIVE_CONTROLS, MassConstraint, NSSTriage, SpectroscopicOrbit,
                  spectroscopic_mass_constraint, triage_nss)
from .pixels import ApertureSeries, CentroidTest, aperture_counterfactuals, event_control_centroid
from .timeseries import Disagreement, DisagreementResult, mine_reduction_disagreements

__all__ = [
    "AnomalyRanking", "ApertureSeries", "CentroidTest", "Disagreement", "DisagreementResult",
    "Feature", "MassConstraint", "NEGATIVE_CONTROLS", "NSSTriage", "PackIntegrityError",
    "PackProduct", "Pair", "ResidualResult", "Source", "SpectroscopicOrbit",
    "aperture_counterfactuals", "checked_product_path", "event_control_centroid",
    "independent_band_consistency", "match_optical_infrared", "mine_reduction_disagreements",
    "rank_control_trained_anomalies", "read_manifest", "read_spoc_lightcurve",
    "read_tesscut_window", "spectroscopic_mass_constraint", "triage_nss", "triage_residual",
]
