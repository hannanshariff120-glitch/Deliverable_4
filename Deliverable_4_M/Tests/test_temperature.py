import pytest
from Temperature import Temperature


def test_case_insensitive_unit() -> None:
    """Tests if upper-case and lower-case letters/units are treated the same"""
    temp = Temperature(25, "c")
    assert temp.value == 25
    assert temp.unit == "C"


@pytest.mark.parametrize("unit, expected_unit", [("c", "C"),
                                                 ("k", "K"),
                                                 ("f", "F"),
                                                 ("C", "C"),
                                                 ("K", "K"),
                                                 ("F", "F")])
def test_case_all_units(unit: str, expected_unit: str) -> None:
    """Tests if all lower- and upper-case letters/units are treated the same"""
    temp = Temperature(25, unit)
    assert temp.value == 25
    assert temp.unit == expected_unit


def test_invalid_unit_raises_exception() -> None:
    """Tests that the the right error-code and message are given when an invalid unit is given"""
    with pytest.raises(ValueError, match="The temperature must be in C, K or F"):
        Temperature(25, "p")


def test_read_only_behavior_for_value() -> None:
    """Tests if the read-only behavior for the value works"""
    with pytest.raises(AttributeError):
        temp = Temperature(25, "c")
        temp.value = 30


def test_read_only_behavior_for_unit() -> None:
    """Tests if the read-only behavior for the unit works"""
    with pytest.raises(AttributeError):
        temp = Temperature(25, "c")
        temp.unit = "F"


@pytest.mark.parametrize("value, unit", [(-300, "C"),
                                         (-500, "F"),
                                         (-1, "K")])
def test_temperatures_below_absolute_zero(value: float, unit: str) -> None:
    """Tests if degrees bellow absolute zero for all units gives an error-code"""
    with pytest.raises(ValueError):
        Temperature(value, unit)


@pytest.mark.parametrize("celsius, fahrenheit, kelvin", [(-273.15, -459.67, 0),
                                                         (-40, -40, 233.15),
                                                         (0, 32, 273.15),
                                                         (37, 98.6, 310.15),
                                                         (100, 212, 373.15)])
def test_convertion_accuracy(celsius: float, fahrenheit: float, kelvin: float) -> None:
    """Tests if the convertion from one unit to another works"""
    d_C = Temperature(celsius, "C")
    d_F = Temperature(fahrenheit, "F")
    d_K = Temperature(kelvin, "K")
    delta = 10**(-9)

    assert abs(d_C.to_kelvin() - d_K.value) <= delta
    assert abs(d_C.to_fahrenheit() - d_F.value) <= delta

    assert abs(d_F.to_celsius() - d_C.value) <= delta
    assert abs(d_F.to_kelvin() - d_K.value) <= delta

    assert abs(d_K.to_celsius() - d_C.value) <= delta
    assert abs(d_K.to_fahrenheit() - d_F.value) <= delta


def test_round_trip_convertion() -> None:
    """Tests if a value sent through the convertions ends up with the same value (+/- delta)"""
    celsius = Temperature(25, "C")
    fahrenheit = celsius.convert_to("F")
    kelvin = fahrenheit.convert_to("K")
    new_celsius = kelvin.convert_to("C")
    delta = 10**(-9)
    assert abs(celsius.value - new_celsius.value) <= delta

def test_cross_unit_comparisons() -> None:
    """Tests if the comparison-methods work as intended"""
    kelvin = Temperature(25, "K")
    celsius = Temperature(25, "C")

    fahrenheit = Temperature(-40, "F")
    celsius_cross = Temperature(-40, "C")

    assert kelvin < celsius
    assert celsius > kelvin
    assert celsius != kelvin
    assert fahrenheit == celsius_cross
    assert fahrenheit <= celsius_cross
    assert fahrenheit >= celsius_cross
    assert celsius_cross >= fahrenheit
    assert celsius_cross <= fahrenheit


def test_formatting_outputs() -> None:
    """Tests if the __str__()- and __repr__()-method gives the expected strings"""
    celsius = Temperature(25, "C")
    assert str(celsius) == "25.00°C"
    assert repr(celsius) == "Temperature(25.0, 'C')"
