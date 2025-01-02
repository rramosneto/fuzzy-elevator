import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# -- Distance Antecedents
# DISTANCE = ctrl.Antecedent(np.arange(0.0, 15.0, 1), "distance")
# DISTANCE["S"] = fuzz.trimf(DISTANCE.universe, [0.0, 0.0, 0.0])
# DISTANCE["MP"] = fuzz.trimf(DISTANCE.universe, [0.0, 1.0, 2.0])
# DISTANCE["P"] = fuzz.trapmf(DISTANCE.universe, [1.0, 2.0, 3.0, 4.0])
# DISTANCE["D"] = fuzz.trapmf(DISTANCE.universe, [3.0, 5.0, 7.0, 9.0])
# DISTANCE["MD"] = fuzz.trimf(DISTANCE.universe, [8.0, 15.0, 15.0])

DISTANCE = ctrl.Antecedent(np.arange(0.0, 1.0, 0.0005), "distance")
DISTANCE["0"] = fuzz.trimf(DISTANCE.universe, [0.0, 0.0, 0.1])
DISTANCE["1"] = fuzz.trimf(DISTANCE.universe, [0.0, 0.1, 0.2])
DISTANCE["2"] = fuzz.trimf(DISTANCE.universe, [0.1, 0.2, 0.3])
DISTANCE["3"] = fuzz.trimf(DISTANCE.universe, [0.2, 0.3, 0.4])
DISTANCE["4"] = fuzz.trimf(DISTANCE.universe, [0.3, 0.4, 0.5])
DISTANCE["5"] = fuzz.trimf(DISTANCE.universe, [0.4, 0.5, 0.6])
DISTANCE["6"] = fuzz.trimf(DISTANCE.universe, [0.5, 0.6, 0.7])
DISTANCE["7"] = fuzz.trimf(DISTANCE.universe, [0.6, 0.7, 0.8])
DISTANCE["8"] = fuzz.trimf(DISTANCE.universe, [0.7, 0.8, 0.9])
DISTANCE["9"] = fuzz.trimf(DISTANCE.universe, [0.8, 0.9, 1.0])
DISTANCE["10"] = fuzz.trimf(DISTANCE.universe, [0.9, 1.0, 1.0])

# -- Regenerative Antecedents
REGENERATIVE = ctrl.Antecedent(np.arange(-1.0, 1.0, 0.005), "regenerative_capacity")
REGENERATIVE["NEG"] = fuzz.trimf(REGENERATIVE.universe, [-1.0, -1.0, 0.0])
REGENERATIVE["S"] = fuzz.trimf(REGENERATIVE.universe, [0.0, 0.0, 0.33])
REGENERATIVE["M"] = fuzz.trimf(REGENERATIVE.universe, [0.0, 0.33, 0.66])
REGENERATIVE["L"] = fuzz.trimf(REGENERATIVE.universe, [0.33, 0.66, 1.0])
REGENERATIVE["XL"] = fuzz.trimf(REGENERATIVE.universe, [0.66, 1.0, 1.0])

# -- Score Consequent
SCORE = ctrl.Consequent(np.arange(-0.1, 1.2, 0.01), "score")
SCORE = ctrl.Consequent(np.arange(0.0, 1.0, 0.005), "score")
# SCORE["0"] = fuzz.trimf(SCORE.universe, [-0.1, -0.1, 0.25])
# SCORE["1"] = fuzz.trimf(SCORE.universe, [0, 0.25, 0.5])
# SCORE["2"] = fuzz.trimf(SCORE.universe, [0.25, 0.5, 0.75])
# SCORE["3"] = fuzz.trimf(SCORE.universe, [0.5, 0.75, 1.0])
# SCORE["4"] = fuzz.trimf(SCORE.universe, [0.75, 1.0, 1.2])

SCORE["0"] = fuzz.trimf(SCORE.universe, [0.0, 0.0, 0.125])
SCORE["1"] = fuzz.trimf(SCORE.universe, [0.0, 0.125, 0.25])
SCORE["2"] = fuzz.trimf(SCORE.universe, [0.125, 0.25, 0.375])
SCORE["3"] = fuzz.trimf(SCORE.universe, [0.25, 0.375, 0.5])
SCORE["4"] = fuzz.trimf(SCORE.universe, [0.375, 0.5, 0.625])
SCORE["5"] = fuzz.trimf(SCORE.universe, [0.5, 0.625, 0.75])
SCORE["6"] = fuzz.trimf(SCORE.universe, [0.625, 0.75, 0.875])
SCORE["7"] = fuzz.trimf(SCORE.universe, [0.75, 0.875, 1.0])
SCORE["8"] = fuzz.trimf(SCORE.universe, [0.875, 1.0, 1.0])
