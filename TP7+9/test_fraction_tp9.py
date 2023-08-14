import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):

    # Tests for initialization and basic properties
    def test_init(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)
        f = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

    # Tests for textual representations
    def test_str_representation(self):
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

    def test_as_mixed_number(self):
        f1 = Fraction(5, 2)
        self.assertEqual(f1.as_mixed_number(), "2 1/2")
        f2 = Fraction(3, 4)
        self.assertEqual(f2.as_mixed_number(), "3/4")

    # Tests for operator overloading
    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

    def test_subtraction(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

    def test_multiplication(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        result = f1 * f2
        expected_result = Fraction(1, 3)
        self.assertTrue(result == expected_result)

    def test_division(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        result = f1 / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 4)

    def test_equality(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertTrue(f1 == f2)

    def test_float_conversion(self):
        f = Fraction(1, 2)
        self.assertEqual(float(f), 0.5)

    # Tests for properties checking
    def test_is_zero(self):
        f = Fraction(0, 1)
        self.assertTrue(f.is_zero())

    def test_is_integer(self):
        f1 = Fraction(4, 2)
        self.assertTrue(f1.is_integer())
        f2 = Fraction(3, 4)
        self.assertFalse(f2.is_integer())

    def test_is_proper(self):
        f1 = Fraction(1, 2)
        self.assertTrue(f1.is_proper())
        f2 = Fraction(5, 2)
        self.assertFalse(f2.is_proper())

    def test_is_unit(self):
        f1 = Fraction(1, 2)
        self.assertTrue(f1.is_unit())
        f2 = Fraction(3, 4)
        self.assertFalse(f2.is_unit())

    def test_is_adjacent_to(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        self.assertFalse(f1.is_adjacent_to(f2))
        f3 = Fraction(2, 3)
        self.assertTrue(f1.is_adjacent_to(f3))


if __name__ == '__main__':
    unittest.main()
