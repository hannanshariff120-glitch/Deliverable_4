from temperature import Temperature  # Imports my previously made class Temperature from the temperature.py file.
import pytest  # Imports the pytest module for testing.

# Create test functions for each conversion method and the convert_to method.
def test_celsius_to_fahrenheit():
    t = Temperature(0, "C")
    assert t.to_fahrenheit() == 32


def test_celsius_to_kelvin():
    t = Temperature(0, "C")
    assert t.to_kelvin() == 273.15


def test_fahrenheit_to_celsius():
    t = Temperature(32, "F")
    assert t.to_celsius() == 0


# Testing invalid units
import pytest


def test_invalid_unit():

    with pytest.raises(ValueError):
        Temperature(100, "X")  # Invalid unit


# Testing absolute zero
def test_absolute_zero():

    with pytest.raises(ValueError):
        Temperature(-1, "K")  # Below absolute zero


# Testing comparisons
def test_temperature_equality():

    t1 = Temperature(0, "C")
    t2 = Temperature(32, "F")

    assert t1 == t2  # They should be equal


def test_temperature_ordering():

    cold = Temperature(0, "C")
    hot = Temperature(100, "C")

    assert cold < hot