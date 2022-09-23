"""
                Categories of Comparison Operators


            - binary operators
            - evaluate to a bool value


            Identity operation: is   is not         - compares memory address - any type

            Value Comparisons: == !=                - Compares values - different types ok,
                                                        but must be compatible

            Ordering Comparisons   <   <=  >  > =   = does not work for all types

            Membership operations   in  not in      - used with iterable types



    Numeric Types

        Value comparisons will work with all numeric types

        Mixed types (except complex) in value and ordering comparisons is supported

        Note: Value equality operators work between floats and Decimals, but as we have seen
            before, using value equality with floats has some issues! 
                (because of floats decimal representation)

                10.0 == Decimal("10.0") -> True
                0.1 == Decimal("0.1") -> False
                Decimal("0.125") == Fraction(1, 8) -> True
                True == 1 -> True
                True == Fraction(3,3)

    Ordering Comparisons
        
        Again, these work across all numeric types, except for complex numbers

        1 < 3.14  -> True
        Fraction(22, 7) > math.pi -> True
        Decimal("0.5") <= Fraction(2,3) -> True
        True < Decimal("3,14") -> True
        Fraction(2,3) > False -> False


    Chained Comparisons

        a == b == c         ->      a == b and b == c (this on the left is only syntax)

        a < b < c           ->      a < b and b < c 

        1 == Decimal("1.0") == Fraction(1,1)  ->        1 == Decimal("1.0") and Decimal("1.0") == Fraction(1,1)  ===> True


        1 < 2 < 3  ===> True

        a < b > c           ->      a < b and b > c
        5 < 6 > 2           ->      5 < 6 and 6 > 2     => True


        a < b < c < d       ->      a < b and b < c and c < d
"""

# identity operations
print(3 is 3)
print([1, 2] is [1, 2])


# membership operations
print(3 not in [1, 2, 3])
