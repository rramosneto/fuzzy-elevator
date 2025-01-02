from skfuzzy import control as ctrl

from .variables import (
    DISTANCE,
    REGENERATIVE,
    SCORE,
)

# -- Spectrum Fuzzy rules
# fmt: off

RULES: list[ctrl.Rule] = [
    ctrl.Rule(DISTANCE["10"] & REGENERATIVE["NEG"], SCORE["0"]),
    ctrl.Rule(
        (DISTANCE["10"] & (REGENERATIVE["S"] | REGENERATIVE["M"])) |
        (DISTANCE["9"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"])) |
        (DISTANCE["8"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"])), SCORE["1"]),

    ctrl.Rule(
        (DISTANCE["10"] & (REGENERATIVE["L"] | REGENERATIVE["XL"])) |
        (DISTANCE["9"] & (REGENERATIVE["M"] | REGENERATIVE["L"])) |
        (DISTANCE["7"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"])) |
        (DISTANCE["6"] & REGENERATIVE["NEG"]), SCORE["2"]),
    ctrl.Rule(
        (DISTANCE["9"] & REGENERATIVE["XL"]) |
        (DISTANCE["8"] & (REGENERATIVE["M"] | REGENERATIVE["L"])) |
        (DISTANCE["7"] & REGENERATIVE["M"]) |
        (DISTANCE["6"] & (REGENERATIVE["S"] | REGENERATIVE["M"])) |
        (DISTANCE["5"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"])), SCORE["3"]),
    ctrl.Rule(
        (DISTANCE["8"] & REGENERATIVE["XL"]) |
        (DISTANCE["7"] & (REGENERATIVE["L"] | REGENERATIVE["XL"])) |
        (DISTANCE["6"] & REGENERATIVE["L"]) |
        (DISTANCE["5"] & (REGENERATIVE["M"] | REGENERATIVE["L"])) |
        (DISTANCE["4"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"])) |
        (DISTANCE["3"] & REGENERATIVE["NEG"]), SCORE["4"]),
    ctrl.Rule(
        (DISTANCE["6"] & (REGENERATIVE["XL"])) |
        (DISTANCE["5"] & (REGENERATIVE["XL"])) |
        (DISTANCE["4"] & (REGENERATIVE["M"] | REGENERATIVE["L"])) |
        (DISTANCE["3"] & (REGENERATIVE["S"] | REGENERATIVE["M"])) |
        (DISTANCE["2"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"])) |
        (DISTANCE["1"] & (REGENERATIVE["NEG"])), SCORE["5"]),
    ctrl.Rule(
        (DISTANCE["4"] & (REGENERATIVE["XL"])) |
        (DISTANCE["3"] & (REGENERATIVE["L"] | REGENERATIVE["XL"])) |
        (DISTANCE["2"] & (REGENERATIVE["M"])) |
        (DISTANCE["1"] & (REGENERATIVE["S"] | REGENERATIVE["M"])) |
        (DISTANCE["0"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"])), SCORE["6"]),
    ctrl.Rule(
        (DISTANCE["2"] & (REGENERATIVE["L"] | REGENERATIVE["XL"])) |
        (DISTANCE["1"] & (REGENERATIVE["L"])) |
        (DISTANCE["0"] & (REGENERATIVE["M"] | REGENERATIVE["L"])), SCORE["7"]),
    ctrl.Rule(
        (DISTANCE["1"] & (REGENERATIVE["XL"])) |
        (DISTANCE["0"] & (REGENERATIVE["XL"])), SCORE["8"]),
]

# -- Spectrum Fuzzy rules
# fmt: off

# RULES: list[ctrl.Rule] = [
#     ctrl.Rule(DISTANCE["S"] & REGENERATIVE["NEG"], SCORE["0"]), # FIXME: The distance should be "MD" instead of "S"
#     ctrl.Rule(
#         DISTANCE["MD"] & (REGENERATIVE["S"] | REGENERATIVE["M"] | REGENERATIVE["L"] | REGENERATIVE["XL"]),
#         SCORE["1"]
#     ),
#     ctrl.Rule(
#         DISTANCE["D"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"] | REGENERATIVE["M"]),
#         SCORE["1"]
#     ),
#     ctrl.Rule(
#         DISTANCE["D"] & (REGENERATIVE["L"] | REGENERATIVE["XL"]),
#         SCORE["2"]
#     ),
#     ctrl.Rule(
#         DISTANCE["P"] & (REGENERATIVE["NEG"] | REGENERATIVE["S"] | REGENERATIVE["M"] | REGENERATIVE["L"]),
#         SCORE["2"]
#     ),
#     ctrl.Rule(DISTANCE["P"] & REGENERATIVE["XL"], SCORE["3"]),
#     ctrl.Rule(DISTANCE["MP"] & REGENERATIVE["NEG"], SCORE["2"]),
#     ctrl.Rule(
#         DISTANCE["MP"] & (REGENERATIVE["S"] | REGENERATIVE["M"] | REGENERATIVE["L"] | REGENERATIVE["XL"]),
#         SCORE["3"]
#     ),
#     ctrl.Rule(DISTANCE["S"], SCORE["4"]),
# ]
# fmt: on
