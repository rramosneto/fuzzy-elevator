from pydantic import BaseModel


class Config(BaseModel):
    n_floors: int
    n_elevators: int
    counterweight: float
    max_load: float
    average_unitary_load: float
