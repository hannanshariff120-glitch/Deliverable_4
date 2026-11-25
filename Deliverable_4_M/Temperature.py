class Temperature:

    def __init__(self, value: float, unit: str) -> None:
        """
        Initialise the Temperature
        Args:
        unit (str): the temperature unit, can be Celsius, Kelvin or Fahrenheit
        value (float): the temperature (amount of degrees)
        """
        unit = unit.upper()
        if unit != "C" and unit != "K" and unit != "F":
            raise ValueError("The temperature must be in C, K or F")
        self._unit = unit
        if unit == "K" and value < 0:
            raise ValueError("The temperature can't be bellow absolute zero")
        if unit == "C" and value < -273.15:
            raise ValueError("The temperature can't be bellow absolute zero")
        if unit == "F" and value < -459.67:
            raise ValueError("The temperature can't be bellow absolute zero")
        self._value = value

    @property
    def value(self) -> float:
        """Public read-only property to inspect the value of the temperature without allowing unsafe, direct edits"""
        return self._value

    @property
    def unit(self) -> str:
        """Public read-only property to inspect the temperature unit without allowing unsafe, direct edits"""
        return self._unit

    def to_celsius(self) -> float:
        """Converts Kelvin and Fahrenheit to Celsius"""
        if self._unit == "C":
            return self._value
        elif self._unit == "K":
            return self._value - 273.15
        return (self._value - 32) * 5 / 9

    def to_kelvin(self) -> float:
        """Converts Celsius and Fahrenheit to Kelvin"""
        if self._unit == "K":
            return self._value
        elif self._unit == "C":
            return self._value + 273.15
        return (self._value - 32) * 5 / 9 + 273.15

    def to_fahrenheit(self) -> float:
        """Converts Celsius and Kelvin to Fahrenheit"""
        if self._unit == "F":
            return self._value
        elif self._unit == "C":
            return self._value * 9 / 5 + 32
        return (self._value - 273.15) * 9 / 5 + 32

    def convert_to(self, target_unit: str):
        """Converts any implemented unit a given wanted value"""
        if target_unit.upper() == "C":
            c_value = self.to_celsius()
            return Temperature(c_value, target_unit)

        elif target_unit.upper() == "K":
            k_value = self.to_kelvin()
            return Temperature(k_value, target_unit)

        elif target_unit.upper() == "F":
            f_value = self.to_fahrenheit()
            return Temperature(f_value, target_unit)

        raise ValueError("The temperature must be in C, K or F")

    def __repr__(self) -> str:
        """Representation of temperature object"""
        return f"Temperature({self._value:.1f}, '{self._unit}')"

    def __str__(self) -> str:
        """String representation of temperature object"""
        return f"{self._value:.2f}°{self._unit}"

    def __lt__(self, other) -> bool:
        """Checks if one temperature is colder than another"""
        if type(other) is not type(self):
            raise NotImplementedError("You must compare two temperatures")
        new_other = other.convert_to(self.unit)
        return new_other.value > self.value

    def __gt__(self, other) -> bool:
        """Checks if one temperature is warmer than another"""
        if type(other) is not type(self):
            raise NotImplementedError("You must compare two temperatures")
        new_other = other.convert_to(self.unit)
        return new_other.value < self.value

    def __le__(self, other) -> bool:
        """Checks if one temperature is colder or the same as another"""
        if type(other) is not type(self):
            raise NotImplementedError("You must compare two temperatures")
        new_other = other.convert_to(self.unit)
        return new_other.value >= self.value

    def __ge__(self, other) -> bool:
        """Checks if one temperature is warmer or the same as another"""
        if type(other) is not type(self):
            raise NotImplementedError("You must compare two temperatures")
        new_other = other.convert_to(self.unit)
        return new_other.value <= self.value

    def __eq__(self, other) -> bool:
        """Checks if two temperatures are the same"""
        if type(other) is not type(self):
            raise NotImplementedError("You must compare two temperatures")
        new_other = other.convert_to(self.unit)
        if abs(new_other.value - self.value) <= 10**(-9):
            return True
        return False
