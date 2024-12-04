import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from fuzzy_elevator.fuzzy.variables import DISTANCE, REGENERATIVE, SCORE
from fuzzy_elevator.objects import FuzzyInput


class FuzzyModel:
    def __init__(self, rules: list[ctrl.Rule]):
        control_system = ctrl.ControlSystem(rules)
        self.model = ctrl.ControlSystemSimulation(control_system)

    def predict(self, inputs: FuzzyInput) -> float:
        """Diagnoses RMS Inputs object and returns a health score."""
        _features = inputs.model_dump()
        for name, value in _features.items():
            self.model.input[name] = value
        self.model.compute()
        score = self.model.output.get(SCORE.label, 0)
        score = np.clip(score, 0, 1)
        return float(score)

    def get_health_linguistic_label(self, score: float) -> str:
        """Returns the most probable output term related to the value."""
        possible_terms = list(SCORE.terms)
        best_score = 0.0
        best_term = possible_terms[0]

        # 1) Evaluate the health score in the HEALTH Membership Function.
        for term in possible_terms:
            membership_score = fuzz.interp_membership(
                SCORE.universe, SCORE[term].mf, score
            )
            if membership_score > best_score:
                best_score = membership_score
                best_term = term
        return best_term

    @classmethod
    def from_config(cls, config):
        return cls(rules=config.rules)

    def visualize_membership_functions(self):
        """
        Visualize the membership functions for inputs and output.
        """
        fig, axes = plt.subplots(nrows=3, figsize=(8, 12))

        for label, mf in DISTANCE.terms.items():
            axes[0].plot(DISTANCE.universe, mf.mf, label=label)
        axes[0].set_title("Input Membership Functions (DISTANCE)")
        axes[0].legend()

        for label, mf in REGENERATIVE.terms.items():
            axes[1].plot(REGENERATIVE.universe, mf.mf, label=label)
        axes[1].set_title("Input Membership Functions (REGENERATIVE)")
        axes[1].legend()

        for label, mf in SCORE.terms.items():
            axes[2].plot(SCORE.universe, mf.mf, label=label)
        axes[2].set_title("Output Membership Functions (SCORE)")
        axes[2].legend()

        plt.tight_layout()
        plt.show()
