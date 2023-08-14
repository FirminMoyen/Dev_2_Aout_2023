from fraction import Fraction


def main():

    f1 = Fraction(3, 4)
    f2 = Fraction(5, 6)
    f3 = Fraction(0, 1)
    f4 = Fraction(-2, 3)
    f5 = Fraction(4, 4)
    f6 = Fraction(7, 2)

    # Displaying fractions
    print("f1:", f1)
    print("f2:", f2)
    print("f3 (zero fraction):", f3)
    print("f4 (negative fraction):", f4)
    print("f5 (equal numerator and denominator):", f5)
    print("f6 (improper fraction):", f6)

    # Adding fractions
    print("f1 + f2:", f1 + f2)
    print("f1 + f3 (adding zero):", f1 + f3)

    # Subtracting fractions
    print("f1 - f4 (subtracting negative):", f1 - f4)

    # Multiplying fractions
    print("f1 * f3 (multiplying by zero):", f1 * f3)

    # Dividing fractions
    print("f1 / f4 (dividing by negative):", f1 / f4)

    # Division by zero exception
    try:
        print("f1 / f3 (dividing by zero, should raise exception):", f1 / f3)
    except ZeroDivisionError as e:
        print("Caught exception:", e)

    # Power
    print("f4 ** 2 (negative to even power):", f4 ** 2)
    print("f4 ** 3 (negative to odd power):", f4 ** 3)

    # Comparing fractions
    print("f1 == f5 (equal fractions):", f1 == Fraction(3, 4))
    print("f1 == f6 (unequal fractions):", f1 == f6)

    # Converting to mixed number
    print("f6 as mixed number:", f6.as_mixed_number())

    # Checking if zero
    print("f3.is_zero() (zero fraction):", f3.is_zero())

    # Checking if integer
    print("f5.is_integer() (integer fraction):", f5.is_integer())

    # Checking if proper
    print("f6.is_proper() (improper fraction):", f6.is_proper())

    # Checking if unit
    print("f5.is_unit() (unit fraction):", f5.is_unit())

    # Checking if adjacent
    print("f1.is_adjacent_to(f2) (non-adjacent fractions):", f1.is_adjacent_to(f2))


if __name__ == "__main__":
    main()
