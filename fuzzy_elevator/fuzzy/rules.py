from skfuzzy import control as ctrl

from .variables import (
    DISTANCE,
    REGENERATIVE,
    SCORE,
)

# -- Spectrum Fuzzy rules
# fmt: off

RULES: list[ctrl.Rule] = [
    ctrl.Rule(DISTANCE["S"] & REGENERATIVE["NEG"], SCORE["0"]),
    ctrl.Rule(
        DISTANCE["MD"] & (REGENERATIVE["S"] | REGENERATIVE["M"] | REGENERATIVE["L"] | REGENERATIVE["XL"]),
        SCORE["1"]
    ),
    ctrl.Rule(
        DISTANCE["D"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"] | REGENERATIVE["M"]),
        SCORE["1"]
    ),
    ctrl.Rule(
        DISTANCE["D"] & (REGENERATIVE["L"] | REGENERATIVE["XL"]),
        SCORE["2"]
    ),
    ctrl.Rule(
        DISTANCE["P"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"] | REGENERATIVE["M"] | REGENERATIVE["L"]),
        SCORE["2"]
    ),
    ctrl.Rule(DISTANCE["P"] & REGENERATIVE["XL"], SCORE["3"]),
    ctrl.Rule(DISTANCE["MP"] & REGENERATIVE["NEG"], SCORE["2"]),
    ctrl.Rule(
        DISTANCE["MP"] & (REGENERATIVE["S"] | REGENERATIVE["M"] | REGENERATIVE["L"] | REGENERATIVE["XL"]),
        SCORE["3"]
    ),
    ctrl.Rule(DISTANCE["S"], SCORE["4"]),
]
# fmt: on
