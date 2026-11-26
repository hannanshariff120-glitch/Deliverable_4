class Fraction:

    def __init__(self, numerator, denominator):

        if not isinstance(numerator, int):
            raise TypeError(
                "Numerator must be an integer"
            )
        
        if not isinstance(denominator, int):
            raise TypeError(
                "Denominator must be an integer"
            )

        if denominator <= 0:
            raise ValueError(
                "Denominator must be greater than zero"
            )

        self.numerator = numerator
        self.denominator = denominator
        
    @property
    def value(self):
        return self.numerator / self.denominator
    
    def __eq__(self, other):

        if not isinstance(other, Fraction):
            return NotImplemented

        return self.value == other.value
     
    def __lt__(self, other):

        if not isinstance(other, Fraction):
            return NotImplemented

        return self.value < other.value

    def __gt__(self, other):

        if not isinstance(other, Fraction):
            return NotImplemented

        return self.value > other.value

    def __le__(self, other):

        if not isinstance(other, Fraction):
            return NotImplemented

        return self.value <= other.value

    def __ge__(self, other):

        if not isinstance(other, Fraction):
            return NotImplemented

        return self.value >= other.value

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):

        if not isinstance(other, Fraction):
            return NotImplemented

        new_numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )
        
        new_denominator = (
            self.denominator * other.denominator
        )

        return Fraction(
            new_numerator,
            new_denominator
        )

    def __sub__(self, other):

        if not isinstance(other,Fraction):
            return NotImplemented

        new_numerator = (
            self.numerator * other.denominator
            - other.numerator * self.denominator
        )

        new_denominator = (
            self.denominator * other.denominator
        )

        return Fraction(
            new_numerator,
            new_denominator
        )
    


    
    