from dataclasses import dataclass, field
from enum import Enum


class Unit(Enum):
    CELSIUS = "celsius"


@dataclass
class Forecast:
    city: str
    temperature: float
    unit: Unit = field(default=Unit.CELSIUS.value)

    def as_json(self):
        return {"city": self.city, "temperature": self.temperature, "unit": self.unit}
