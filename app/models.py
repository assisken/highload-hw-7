from dataclasses import dataclass, field, asdict
from enum import Enum


class Unit(Enum):
    CELSIUS = "celsius"


@dataclass
class Forecast:
    city: str
    temperature: float
    timestamp: str
    unit: Unit = Unit.CELSIUS.value

    def as_json(self):
        return asdict(self)
