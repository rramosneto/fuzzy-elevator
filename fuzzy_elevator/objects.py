from enum import Enum
from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field
from pydantic.functional_serializers import PlainSerializer
from skfuzzy.control.rule import Rule
from typing_extensions import Annotated

# ID = Annotated[UUID, PlainSerializer(lambda x: str(x), return_type=str)]


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    STEADY = "steady"


class Request(BaseModel):
    floor: int
    target_floor: int
    load: float


class Elevator(BaseModel):
    # id: ID = Field(default_factory=uuid4)
    id: int
    weight: float
    max_load: float
    counterweight: float
    n_floors: int
    current_floor: int
    target_floor: int
    load: float
    average_unitary_load: float
    score: float

    def is_available(self, request: Request) -> bool:
        is_same_trajectory = (
            request.target_floor in self.trajectory()
            and request.floor in self.trajectory()
        )

        is_same_floor = request.floor == self.current_floor

        has_free_load = self.load + self.average_unitary_load <= self.max_load

        return is_same_trajectory and has_free_load and not is_same_floor

    def trajectory(self) -> range:
        if self.current_floor < self.target_floor:
            return range(self.current_floor, self.n_floors + 1)

        elif self.current_floor > self.target_floor:
            return range(self.current_floor, -1, -1)

        else:
            return range(0, self.n_floors + 1)

    def update(self) -> None:
        self.current_floor = self.target_floor
        self.load = 0.0

    @property
    def direction(self) -> Direction:
        if self.current_floor < self.target_floor:
            return Direction.UP
        elif self.current_floor > self.target_floor:
            return Direction.DOWN
        else:
            return Direction.STEADY

    @property
    def ideal_load(self) -> float:
        return self.counterweight - self.weight


class Config(BaseModel):
    n_floors: int
    n_elevators: int
    elevator_weight: float
    counterweight: float
    max_load: float
    average_unitary_load: float
    rules: List[Rule]

    class Config:
        arbitrary_types_allowed = True


class FuzzyInput(BaseModel):
    distance: float
    regenerative_capacity: float

    @classmethod
    def from_request(cls, elevator: Elevator, request: Request) -> "FuzzyInput":
        # distance = min(abs(elevator.current_floor - request.floor), 15)
        distance = abs(elevator.current_floor - request.floor)/elevator.n_floors

        if elevator.direction == Direction.UP:
            regenerative_capacity = (
                elevator.counterweight - (elevator.load + elevator.weight)
            ) / elevator.ideal_load

        elif elevator.direction == Direction.DOWN:
            regenerative_capacity = (
                (elevator.load + elevator.weight) - elevator.counterweight
            ) / elevator.ideal_load

        else:
            regenerative_capacity = 0.0

        return cls(distance=distance, regenerative_capacity=regenerative_capacity)
