class Fraction:
    """Represents a fraction (numerator / denominator)"""

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Initialise the Fraction
        Args:
        numerator (int): the numerator in the fraction
        denominator (int): the denominator in the fraction
        """
        if type(numerator) is not int:
            raise TypeError("The numerator should be a integer not a any other type")
        self._numerator = numerator
        if type(denominator) is not int:
            raise TypeError("The denominator should be a integer not any other type")
        elif denominator <= 0:
            raise ValueError("The denominator has to be larger than zero")
        self._denominator = denominator

    @property
    def value(self) -> float:
        """Public read-only property to inspect the value without allowing unsafe, direct edits"""
        return self._numerator / self._denominator

    def __lt__(self, other):
        """Checks if one fraction is smaller than another"""
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value < other.value

    def __gt__(self, other):
        """Checks if one fraction is larger than another"""
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value > other.value

    def __eq__(self, other):
        """Checks if one fraction is equal to another"""
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value == other.value

    def __le__(self, other):
        """Checks if one fraction is smaller or equal to another"""
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value <= other.value

    def __ge__(self, other):
        """Checks if one fraction is larger or equal to another"""
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value >= other.value

    def __str__(self):
        """String representation of fraction object"""
        return f"{self._numerator} / {self._denominator}"

    def __repr__(self):
        """Representation of fraction object"""
        return f"Fraction({self._numerator}, {self._denominator})"

    def __add__(self, other):
        """Adds to fractions together"""
        if self._denominator == other._denominator:
            new_numerator = self._numerator + other._numerator
            return Fraction(new_numerator, self._denominator)
        new_denominator = other._denominator * self._denominator
        new_other_nom = other._numerator * self._denominator
        new_self_nom = self._numerator * other._denominator
        new_numerator = new_other_nom + new_self_nom
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Subtracts on fraction from another"""
        if self._denominator == other._denominator:
            new_numerator = self._numerator - other._numerator
            return Fraction(new_numerator, self._denominator)
        new_denominator = other._denominator * self._denominator
        new_other_nom = other._numerator * self._denominator
        new_self_nom = self._numerator * other._denominator
        new_numerator = new_self_nom - new_other_nom
        return Fraction(new_numerator, new_denominator)
