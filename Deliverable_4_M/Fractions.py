class Fraction:

    def __init__(self, numerator: int, denominator: int):
        if type(numerator) is not int:
            raise TypeError("The numerator should be a integer not a any other type")
        self.numerator = numerator
        if type(denominator) is not int:
            raise TypeError("The denominator should be a integer not any other type")
        elif denominator <= 0:
            raise ValueError("The denominator has to be larger than zero")
        self.denominator = denominator

    @property
    def value(self):
        return self.numerator / self.denominator

    def __lt__(self, other):
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value < other.value

    def __gt__(self, other):
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value > other.value

    def __eq__(self, other):
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value == other.value

    def __le__(self, other):
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value <= other.value

    def __ge__(self, other):
        if type(other) is not type(self):
            raise TypeError("You must compare to fractions")
        return self.value >= other.value

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        if self.denominator == other.denominator:
            new_numerator = self.numerator + other.numerator
            return Fraction(new_numerator, self.denominator)
        # lik nevner
        new_denominator = other.denominator * self.denominator
        new_other_nom = other.numerator * self.denominator
        new_self_nom = self.numerator * other.denominator
        new_numerator = new_other_nom + new_self_nom
        # summere teller
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            new_numerator = self.numerator - other.numerator
            return Fraction(new_numerator, self.denominator)
        # lik nevner
        new_denominator = other.denominator * self.denominator
        new_other_nom = other.numerator * self.denominator
        new_self_nom = self.numerator * other.denominator
        new_numerator = new_self_nom - new_other_nom
        # summere teller
        return Fraction(new_numerator, new_denominator)
