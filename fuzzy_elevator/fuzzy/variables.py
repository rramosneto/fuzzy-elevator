import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# -- RMS Antecedents
RMS_Z_SCORE = ctrl.Antecedent(np.arange(0.0, 6.0, 0.25), "rms_z_score")
RMS_Z_SCORE["low"] = fuzz.trapmf(RMS_Z_SCORE.universe, [0.0, 0.0, 1.5, 2.0])
RMS_Z_SCORE["medium"] = fuzz.trapmf(RMS_Z_SCORE.universe, [1.5, 2.0, 3.0, 3.5])
RMS_Z_SCORE["high"] = fuzz.trapmf(RMS_Z_SCORE.universe, [3.0, 3.5, 6.0, 6.0])

RMS_P95_RUPTURE = ctrl.Antecedent(np.arange(0.0, 3.0, 0.1), "rms_p95_rupture")
RMS_P95_RUPTURE["low"] = fuzz.trapmf(RMS_P95_RUPTURE.universe, [0.0, 0.0, 1.2, 1.5])
RMS_P95_RUPTURE["medium"] = fuzz.trapmf(RMS_P95_RUPTURE.universe, [1.4, 1.5, 1.7, 2.0])
RMS_P95_RUPTURE["high"] = fuzz.trapmf(RMS_P95_RUPTURE.universe, [1.8, 2.0, 3.0, 3.0])

# -- Spectrum Antecedents
MIN_RUPTURE_DB = -1
MAX_RUPTURE_DB = 15

PEAK_RUPTURE_DB = ctrl.Antecedent(
    np.arange(MIN_RUPTURE_DB, MAX_RUPTURE_DB, 0.01), "peak_rupture_db"
)
PEAK_RUPTURE_DB["very_low"] = fuzz.trapmf(
    PEAK_RUPTURE_DB.universe, [MIN_RUPTURE_DB, MIN_RUPTURE_DB, 0, 1]
)
PEAK_RUPTURE_DB["low"] = fuzz.trapmf(PEAK_RUPTURE_DB.universe, [0, 1, 2, 3])
PEAK_RUPTURE_DB["medium"] = fuzz.trapmf(PEAK_RUPTURE_DB.universe, [2, 3, 4, 5])
PEAK_RUPTURE_DB["high"] = fuzz.trapmf(
    PEAK_RUPTURE_DB.universe, [4, 5, MAX_RUPTURE_DB, MAX_RUPTURE_DB]
)

PEAK_IMPORTANCE = ctrl.Antecedent(np.arange(0, 1.0, 0.01), "peak_importance")
PEAK_IMPORTANCE["low"] = fuzz.trapmf(PEAK_IMPORTANCE.universe, [0, 0, 0.1, 0.2])
PEAK_IMPORTANCE["medium"] = fuzz.trapmf(PEAK_IMPORTANCE.universe, [0.1, 0.2, 0.5, 0.6])
PEAK_IMPORTANCE["high"] = fuzz.trapmf(PEAK_IMPORTANCE.universe, [0.5, 0.6, 1, 1])

# -- Consequent
# universe limits were chosen such that the outputs are between 0.03, 0.97
HEALTH_STATUS = ctrl.Consequent(np.arange(-0.1, 1.2, 0.01), "health_status")
HEALTH_STATUS["healthy"] = fuzz.trapmf(HEALTH_STATUS.universe, [-0.1, -0.1, 0.1, 0.2])
HEALTH_STATUS["poor"] = fuzz.trapmf(HEALTH_STATUS.universe, [0.1, 0.2, 0.4, 0.5])
HEALTH_STATUS["bad"] = fuzz.trapmf(HEALTH_STATUS.universe, [0.4, 0.5, 0.7, 0.8])
HEALTH_STATUS["critical"] = fuzz.trapmf(HEALTH_STATUS.universe, [0.7, 0.8, 1.2, 1.2])
