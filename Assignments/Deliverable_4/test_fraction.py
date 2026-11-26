from fraction import Fraction
import pytest

def test_invalid_denominator():

    with pytest.raises(ValueError):
        Fraction(1, 0)

def test_invalid_numerator_type():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)

def test_invalid_denominator_type():

    with pytest.raises(TypeError):
        Fraction(1, 2.5)

def test_fraction_ordering():

    small = Fraction(1, 3)
    large = Fraction(1, 2)

    assert small < large

def test_fraction_addition():

    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)

    result = f1 + f2

    assert result == Fraction(5, 6)

def test_fraction_subtraction():
    
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)

    result = f1 - f2

    assert result == Fraction(1, 6)

def test_fraction_string_output():

    f = Fraction(1, 2)

    assert repr(f) == "Fraction(1, 2)"