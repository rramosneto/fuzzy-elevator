from enum import Enum
from typing import Dict, List
from uuid import UUID, uuid4

from numpy import select
from pydantic import BaseModel, Field
from pydantic.functional_serializers import PlainSerializer
from typing_extensions import Annotated

from fuzzy_elevator.config import Config
from fuzzy_elevator.fuzzy.model import FuzzyModel

ID = Annotated[UUID, PlainSerializer(lambda x: str(x), return_type=str)]


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    STEADY = "steady"


class Request(BaseModel):
    floor: int
    target_floor: int


class Elevator(BaseModel):
    id: ID = Field(default_factory=uuid4)
    max_load: float
    counterweight: float
    n_floors: int
    current_floor: int
    target_floor: int
    load: float
    average_unitary_load: float

    def is_available(self, request: Request) -> bool:
        is_same_trajectory = (
            request.target_floor in self.trajectory()
            and request.floor in self.trajectory()
        )

        has_free_load = self.load + self.average_unitary_load <= self.max_load

        return is_same_trajectory and has_free_load

    def trajectory(self) -> range:
        if self.current_floor < self.target_floor:
            return range(self.current_floor, self.n_floors + 1)

        elif self.current_floor > self.target_floor:
            return range(self.current_floor, -1, -1)

        else:
            return range(0, self.n_floors + 1)

    @property
    def direction(self) -> Direction:
        if self.current_floor < self.target_floor:
            return Direction.UP
        elif self.current_floor > self.target_floor:
            return Direction.DOWN
        else:
            return Direction.STEADY


class ElevatorManager(BaseModel):
    elevators: List[Elevator]
    model: FuzzyModel

    def send_elevator(self, request: Request) -> UUID:
        available_elevators: List[Elevator] = self.get_available_elevators(request)
        elevator_scores: Dict[Elevator, float] = self.get_elevator_scores(
            available_elevators, request
        )

        # Find the maximum score
        max_score = max(elevator_scores.values())

        # Filter elevators that have the maximum score
        best_elevators = [
            elevator
            for elevator, score in elevator_scores.items()
            if score == max_score
        ]

        # If more than one elevator has the same score, use the lambda function to determine which elevator to send
        if len(best_elevators) > 1:
            selected_elevator = min(
                best_elevators,
                key=lambda elevator: abs(elevator.current_floor - request.floor),
            )
        else:
            selected_elevator = best_elevators[0]

        # Update the selected elevator's target and current floors
        if selected_elevator.direction == Direction.UP:
            selected_elevator.current_floor = request.floor
            selected_elevator.target_floor = max(
                request.target_floor, selected_elevator.target_floor
            )

        elif selected_elevator.direction == Direction.DOWN:
            selected_elevator.current_floor = request.floor
            selected_elevator.target_floor = min(
                request.target_floor, selected_elevator.target_floor
            )

        else:
            selected_elevator.current_floor = request.floor
            selected_elevator.target_floor = request.target_floor

        return selected_elevator.id

    def get_available_elevators(self, request: Request) -> List[Elevator]:
        return [
            elevator for elevator in self.elevators if elevator.is_available(request)
        ]

    def get_elevator_scores(
        self, available_elevators: List[Elevator], request: Request
    ) -> Dict[Elevator, float]:
        scores = {}
        for elevator in available_elevators:
            score = self.model.predict(elevator, request)
            scores[elevator] = score
        return scores

    @classmethod
    def from_config(cls, config: Config):
        return cls(
            elevators=[
                Elevator(
                    max_load=config.max_load,
                    counterweight=config.counterweight,
                    n_floors=config.n_floors,
                    current_floor=0,
                    target_floor=0,
                    load=0,
                    average_unitary_load=config.average_unitary_load,
                )
                for _ in range(config.n_elevators)
            ],
            model=FuzzyModel.from_config(config),
        )
