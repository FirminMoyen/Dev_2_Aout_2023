class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : den != 0
        POST : A Fraction object with the given numerator and denominator.
        RAISES : ZeroDivisionError if den == 0
        """

        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        self._numerator = num
        self._denominator = den

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

# ------------------ Textual representations ------------------

    def __str__(self):
        """
        Return a textual representation of the reduced form of the fraction

        PRE : /
        POST : Returns a string representing the fraction.
        """

        return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : ?
        POST : Returns a string representing the fraction as a mixed number.
        """

        whole_part = self.numerator // self.denominator
        numerator_part = self.numerator % self.denominator
        if whole_part == 0:
            return str(self)
        return f"{whole_part} {numerator_part}/{self.denominator}"


# ------------------ Operators overloading ------------------


    def __add__(self, other):
        """
        Overloading of the + operator for fractions

        PRE : other is a Fraction
        POST : Returns a new Fraction representing the sum of self and other.
         """
        new_numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other is a Fraction
        POST : Returns a new Fraction representing the difference of self and other.
        """
        new_numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other is a Fraction
        POST : Returns a new Fraction representing the product of self and other.
        """
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other is a Fraction and other != 0
        POST : Returns a new Fraction representing the division of self by other.
        RAISES : ZeroDivisionError if other == 0
        """
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : exponent is an integer
        POST : Returns a new Fraction representing self raised to the power of exponent.
        """
        return Fraction(self.numerator ** other, self.denominator ** other)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other is a Fraction
        POST : Returns True if self and other represent the same fraction, False otherwise.
        """
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : /
        POST : Returns a float representing the decimal value of the fraction.
        """
        return self.numerator / self.denominator


# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)


# ------------------ Properties checking ------------------


    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : /
        POST : Returns True if the fraction is 0, False otherwise.
        """

        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : /
        POST : Returns True if the fraction represents an integer, False otherwise.
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : /
        POST : Returns True if the absolute value of the fraction is < 1, False otherwise.
        """
        return abs(self.numerator) < abs(self.denominator)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : /
        POST : Returns True if the numerator is 1 in reduced form, False otherwise.
        """
        return abs(self.numerator) == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : other is a Fraction
        POST : Returns True if the fractions are adjacent, False otherwise.
        """
        difference = abs(float(self) - float(other))
        return abs(difference - round(difference)) < 1e-9
