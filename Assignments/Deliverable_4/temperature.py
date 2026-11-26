from functools import total_ordering
import math


@total_ordering
class Temperature:
    TOLERANCE = 1e-9

    def __init__(self, value, unit="C"):
        unit = unit.upper()

        if unit not in ("C", "F", "K"):
            raise ValueError("Unit must be C, F, or K")
        
        self._value = float(value)
        self._unit = unit

        if self.to_kelvin() < 0:
            raise ValueError(
                "Temperature cannot be below absolute zero"
                )
    @property
    def value(self):
        return self._value
    
    @property
    def unit(self):
        return self._unit

    def to_celsius(self):

        if self.unit == "C":
            return self.value

        elif self.unit == "F":
            return (self.value - 32) * 5 / 9

        else:  # Kelvin
            return self.value - 273.15

    def to_fahrenheit(self):

        if self.unit == "F":
            return self.value

        elif self.unit == "C":
            return (self.value * 9 / 5) + 32

        else:  # Kelvin
            return (self.value - 273.15) * 9 / 5 + 32

    def to_kelvin(self):
        if self.unit == "K":
            return self.value

        elif self.unit == "C":
            return self.value + 273.15

        else:  # Fahrenheit
            return (self.value - 32) * 5 / 9 + 273.15
        
    def convert_to(self, target_unit):

        target_unit = target_unit.upper()

        if target_unit not in ("C", "F", "K"):
            raise ValueError("Target unit must be C, F, or K")

        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")

        elif target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")

        else:
            return Temperature(self.to_kelvin(), "K"
                               )

    def __repr__(self):
        return f"Temperature({self.value}, '{self.unit}')"

    def __str__(self):
        return f"{self.value:.2f} °{self.unit}"

    def __eq__(self, other):

        if not isinstance(other, Temperature):
            return NotImplemented

        return math.isclose(
            self.to_kelvin(), 
            other.to_kelvin(), 
            rel_tol=self.TOLERANCE
        )

    def __lt__(self, other):

        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() < other.to_kelvin()