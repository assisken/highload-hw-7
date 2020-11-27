from dataclasses import dataclass, asdict
from enum import Enum


class Unit(str, Enum):
    celsius = "celsius"


@dataclass
class Forecast:
    city: str
    temperature: float
    unit: Unit = Unit.celsius.value

    def as_json(self):
        return asdict(self)
