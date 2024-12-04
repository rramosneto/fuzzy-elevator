from enum import Enum
from typing import Dict, List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from pydantic.functional_serializers import PlainSerializer
from typing_extensions import Annotated

from fuzzy_elevator.fuzzy.model import FuzzyModel
from fuzzy_elevator.objects import Config, Direction, Elevator, FuzzyInput, Request

# ID = Annotated[UUID, PlainSerializer(lambda x: str(x), return_type=str)]


class ElevatorManager(BaseModel):
    elevators: List[Elevator]
    model: FuzzyModel

    def send_elevator(self, request: Request) -> int:
        available_elevators: List[Elevator] = self.get_available_elevators(request)
        elevator_scores: Dict[int, float] = self.get_elevator_scores(
            available_elevators, request
        )

        # Find the maximum score
        max_score = max(elevator_scores.values())

        # Filter elevators that have the maximum score
        best_elevators = [
            elevator_id
            for elevator_id, score in elevator_scores.items()
            if score == max_score
        ]

        # If more than one elevator has the same score, use the lambda function to determine which elevator to send
        if len(best_elevators) > 1:
            selected_elevator_id = min(
                best_elevators,
                key=lambda elevator: abs(
                    self.get_elevator_by_id(elevator).current_floor - request.floor
                ),
            )
        else:
            selected_elevator_id = best_elevators[0]

        selected_elevator = self.get_elevator_by_id(selected_elevator_id)
        # Update the selected elevator's target and current floors
        selected_elevator.current_floor = request.floor

        if selected_elevator.direction == Direction.UP:
            selected_elevator.target_floor = max(
                request.target_floor, selected_elevator.target_floor
            )

        elif selected_elevator.direction == Direction.DOWN:
            selected_elevator.target_floor = min(
                request.target_floor, selected_elevator.target_floor
            )

        else:
            selected_elevator.target_floor = request.target_floor

        return selected_elevator.id

    def get_elevator_by_id(self, elevator_id: int) -> Elevator:
        return next(
            elevator for elevator in self.elevators if elevator.id == elevator_id
        )

    def get_available_elevators(self, request: Request) -> List[Elevator]:
        return [
            elevator for elevator in self.elevators if elevator.is_available(request)
        ]

    def get_elevator_scores(
        self, available_elevators: List[Elevator], request: Request
    ) -> Dict[int, float]:
        scores = {}
        for elevator in available_elevators:
            fuzzy_input = FuzzyInput.from_request(elevator, request)
            score = self.model.predict(fuzzy_input)
            scores[elevator.id] = score
        return scores

    def get_state(self):
        return {
            f"elevator {elevator.id}": elevator.current_floor
            for elevator in self.elevators
        }

    @classmethod
    def from_config(cls, config: Config):
        return cls(
            elevators=[
                Elevator(
                    id=i,
                    weight=config.elevator_weight,
                    max_load=config.max_load,
                    counterweight=config.counterweight,
                    n_floors=config.n_floors,
                    current_floor=0,
                    target_floor=0,
                    load=0,
                    average_unitary_load=config.average_unitary_load,
                )
                for i in range(config.n_elevators)
            ],
            model=FuzzyModel.from_config(config),
        )

    class Config:
        arbitrary_types_allowed = True
