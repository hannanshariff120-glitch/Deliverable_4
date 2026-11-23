import pytest
from Fractions import Fraction


def test_fraction_comparisons():
    fract1 = Fraction(2, 3)
    fract2 = Fraction(4, 6)
    fract3 = Fraction(1, 2)

    assert fract1 == fract2
    assert fract2 == fract1

    assert fract1 != fract3
    assert fract3 != fract1

    assert fract2 > fract3
    assert fract3 < fract2

    assert fract2 >= fract3
    assert fract3 <= fract2

    assert fract2 >= fract1
    assert fract2 <= fract1


def test_formatting_outputs():
    fract = Fraction(1, 2)
    assert str(fract) == "1 / 2"
    assert repr(fract) == "Fraction(1, 2)"


def test_addition_same_denominator():
    fract1 = Fraction(1, 3)
    fract2 = Fraction(2, 3)

    result = fract1 + fract2
    expected_result = Fraction(3, 3)

    assert result == expected_result


def test_addition_different_denominator():
    fract1 = Fraction(1, 3)
    fract2 = Fraction(2, 4)

    result = fract1 + fract2
    expected_result = Fraction(10, 12)

    assert result == expected_result


def test_subtraction_same_denominator():
    fract1 = Fraction(1, 3)
    fract2 = Fraction(2, 3)

    result = fract1 - fract2
    expected_result = Fraction(-1, 3)

    assert result == expected_result


def test_subtraction_different_denominator():
    fract1 = Fraction(1, 3)
    fract2 = Fraction(2, 4)

    result = fract1 - fract2
    expected_result = Fraction(-2, 12)

    assert result == expected_result


def test_negative_denominator():
    with pytest.raises(ValueError):
        Fraction(1, -3)


def test_float_values():
    with pytest.raises(TypeError, match="The numerator should be a integer not a any other type"):
        Fraction(1.4, 3)
    with pytest.raises(TypeError, match="The denominator should be a integer not any other type"):
        Fraction(1, 3.5)
