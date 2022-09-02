"""

        Constructing Decimal Objects

The Decimal class is in the decimal module

import decimal
from decimal import Decimal

Decimal(x)  x can be a variety of types

integers 
other Decimal objects
strings                 a = Decimal("0.1")
tuples                  a = Decimal((1, (3,1,4,1, 5), -4))


floats?         Yes but not usually done
        We are not doing that usual because Decimal is going to store approximation
    Decimal(0.1) 

-> use strings or tuples instead

----------------------------------------------

Using the tuple constructor

1.23            -> +123 x 10^-2

-1.23           -> -123 x 10^-2

                sign digits exponent
                so:

                (s, (d1, d2, d3, ...), exp)

                s -> 0 if x >= 0 
                     1 if x < 0

example:
    -3.1415 -> (1, (3,1,4,1,5), -4)

    a = Decimal((1, (3,1,4,1,5), -4))


Context Precision and the Constructor

    Context precision affects mathematical operations
    Context precision does not affect the constructor

        import decimal
        from decimal import Decimal
        decimal.getcontext().prec = 2           <- global (default)  context now has precision set to 2

        a = Decimal('0.12345)   -> a = 0.12345
        b = Decimal('0.12345)   -> a = 0.12345
        c = a + b               -> a + b = 0.2469  
                                -> c would be rounded c-> 0.25

        so precision does not impact the storage but impact calculations


Local vs Global Context

import decimal
from decimal import Decimal

Local vs Global Context
decimal.getcontext().prec = 6
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)

with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print(c)
print(c)
"""
