"""
            Floats

        Coercing to integers


Float -> Integer        !Data Loss

Different way to configure this data loss

        10.4
    10?     11?


                        data loss in all cases
                        pick your poison! :>
    truncation  -
            Truncation a float simply returns the integer portion of the number
                ie ignores everything after the decimal point

            The math module provides us the trunc() function:
                import math
                math.trunc(10.4) -> 10
                math.trunc(10.5) -> 10
                math.trunc(10.6) -> 10

                math.trunc(-10.4) -> -10
                math.trunc(-10.5) -> -10
                math.trunc(-10.6) -> -10

            The int constructor
                The Python int constructor will accept a float
                    uses truncation when casting the float to an int
    
    floor       -
            Definition: the floor of a number is the largest integer less than (or equal to)
                        the number
                        floor(x) - max{i E Z| i =< x}

                        x = -10.4 -> floor -11

            For positive numbers, floor and truncation are equivalent

                recall also our discussion on integer division - aka floor division: //
                We defined floor division in combination with the mod operation

                a // b == floor(a/b)

            The math module provides us the floor() function

            import math
            math.floor (10.4) -> 10
            math.floor (10.5) -> 10
            math.floor (10.6) -> 10

            math.floor (-10.4) -> -11
            math.floor (-10.5) -> -11
            math.floor (-10.6) -> -11
             

    ceiling     -
            Definition: the ceiling of a number is the smallest integer
            greater than (or equal to) the number
                ceil(x) = min {i E Z | i => x}

            import math
            math.ceil(10.4) -> 11
            math.ceil(10.5) -> 11
            math.ceil(10.6) -> 11
            
            math.ceil(-10.4) -> -10
            math.ceil(-10.5) -> -10
            math.ceil(-10.6) -> -10


    rounding    -


The int constructor
    The Python int constructor will accept a float
        uses truncation when casting the float to an int


"""
