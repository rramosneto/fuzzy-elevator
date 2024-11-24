from .variables import (
    PEAK_IMPORTANCE,
    PEAK_RUPTURE_DB,
    HEALTH_STATUS,
    RMS_P95_RUPTURE,
    RMS_Z_SCORE,
)
from skfuzzy import control as ctrl

# -- Spectrum Fuzzy rules
# fmt: off
BAND_RULES: list[ctrl.Rule] = [
    ctrl.Rule(PEAK_RUPTURE_DB["very_low"], HEALTH_STATUS["healthy"]),
    ctrl.Rule(PEAK_RUPTURE_DB["low"] & (PEAK_IMPORTANCE["low"] | PEAK_IMPORTANCE["medium"]),HEALTH_STATUS["healthy"]),
    ctrl.Rule(PEAK_RUPTURE_DB["low"] & PEAK_IMPORTANCE["high"], HEALTH_STATUS["poor"]),
    ctrl.Rule(PEAK_RUPTURE_DB["medium"] & PEAK_IMPORTANCE["low"], HEALTH_STATUS["healthy"]),
    ctrl.Rule(PEAK_RUPTURE_DB["medium"] & PEAK_IMPORTANCE["medium"], HEALTH_STATUS["poor"]),
    ctrl.Rule(PEAK_RUPTURE_DB["medium"] & PEAK_IMPORTANCE["high"], HEALTH_STATUS["bad"]),
    ctrl.Rule(PEAK_RUPTURE_DB["high"] & PEAK_IMPORTANCE["medium"], HEALTH_STATUS["bad"]),
    ctrl.Rule(PEAK_RUPTURE_DB["high"] & PEAK_IMPORTANCE["high"], HEALTH_STATUS["critical"]),
    ctrl.Rule(PEAK_RUPTURE_DB["high"] & PEAK_IMPORTANCE["low"], HEALTH_STATUS["poor"]),
]

# -- RMS fuzzy rules
RMS_RULES: list[ctrl.Rule] = [
    ctrl.Rule(RMS_Z_SCORE["low"] | RMS_P95_RUPTURE["low"], HEALTH_STATUS["healthy"]),
    ctrl.Rule(RMS_Z_SCORE["low"] & RMS_P95_RUPTURE["medium"], HEALTH_STATUS["poor"]),
    ctrl.Rule(RMS_Z_SCORE["low"] & RMS_P95_RUPTURE["high"], HEALTH_STATUS["bad"]),
    ctrl.Rule(RMS_Z_SCORE["medium"] & RMS_P95_RUPTURE["low"], HEALTH_STATUS["poor"]),
    ctrl.Rule(RMS_Z_SCORE["medium"] & RMS_P95_RUPTURE["medium"], HEALTH_STATUS["poor"]),
    ctrl.Rule(RMS_Z_SCORE["medium"] & RMS_P95_RUPTURE["high"], HEALTH_STATUS["bad"]),
    ctrl.Rule(RMS_Z_SCORE["high"] & RMS_P95_RUPTURE["low"], HEALTH_STATUS["poor"]),
    ctrl.Rule(RMS_Z_SCORE["high"] & RMS_P95_RUPTURE["medium"], HEALTH_STATUS["bad"]),
    ctrl.Rule(RMS_Z_SCORE["high"] & RMS_P95_RUPTURE["high"], HEALTH_STATUS["critical"]),
]
# fmt: on
