import numpy as np
import skfuzzy as fuzz
from pydantic import BaseModel
from skfuzzy import control as ctrl

from .variables import HEALTH_STATUS


class FuzzyInput(BaseModel):
    distance: int
    free_load: float


class FuzzyModel:
    """A model based on Fuzzy Inference that predicts a health score given the features."""

    def __init__(self, rules: list[ctrl.Rule]):
        control_system = ctrl.ControlSystem(rules)
        self.model = ctrl.ControlSystemSimulation(control_system)

    def predict(self, inputs: FuzzyInput) -> float:
        """Diagnoses RMS Inputs object and returns a health score."""
        _features = inputs.model_dump()
        for name, value in _features.items():
            self.model.input[name] = value
        self.model.compute()
        score = self.model.output.get(HEALTH_STATUS.label, 0)
        score = np.clip(score, 0, 1)
        return float(score)

    def get_health_linguistic_label(self, score: float) -> str:
        """Returns the most probable output term related to the value."""
        possible_terms = list(HEALTH_STATUS.terms)
        best_score = 0.0
        best_term = possible_terms[0]

        # 1) Evaluate the health score in the HEALTH Membership Function.
        for term in possible_terms:
            membership_score = fuzz.interp_membership(
                HEALTH_STATUS.universe, HEALTH_STATUS[term].mf, score
            )
            if membership_score > best_score:
                best_score = membership_score
                best_term = term
        return best_term

    @classmethod
    def from_config(cls, config):
        return cls(rules=config.rules)
