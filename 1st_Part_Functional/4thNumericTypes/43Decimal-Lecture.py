"""

                Decimals

The decimal module -> PEP 327

float 0.1 (binary float) -> infinite binary expansion


                        -> final decimal expansion  1/10

alternative to using the (binary) float type -> avoids the approximation issues with floats

    finite number of significant digits -> rational number

So why not just use the Fraction class?

    to add two fractions -> common denominator

                         -> complex, requires extra memory


-------------------------------- Why do we even care? --------------------------------

finance, banking, and any other field where exact finite representations are highly desirable

let's say we are adding up all the financial transactions that took place over a certain time period

amount = 100.1
transactions 1 000 000 000
    NYSE 2-6 billion shares traded daily! wow

    sum => 100010000000.00
           100009998761.14639282226562
           1238.85... off!!


-------------------------------- --------------------------------
Decimal have a context that control certain aspect of working with decimals

    precision during arithmetic operations
    rounding algorithm

This context can be global -> the default context
    or temporary (local)    -> sets temporary settings without affecting the global settings

import decimal

default context -> decimal.getcontext()

local context -> decimal.localcontext(cts=None)

                creates a new context, copied from cts
                or from default if cts not specified

                returns a context manager (use a with statement)


Precision and Rounding

ctx = decimal.getcontext() -> context(global in this case)

ctx.prec    -> get or set the precision (value is an int)
ctx.rounding -> get or set the rounding mechanism (value is a string)

                ROUND_UP        - rounds away from zero
                ROUND_DOWN      - rounds towards zero
                ROUND_CEILING   - rounds to ceiling (towards +Infinity)
                ROUND_FLOOR     - rounds to floor (towards -Infinity)
                ROUND_HALF_UP   - rounds to nearest, ties away from zero        <----- 
                ROUND_HALF_DOWN - rounds to nearest, ties towards zero
                ROUND_HALF_EVEN - rounds to nearest, ties to even (least significant digit)   <----- (float rounding algorithm)


-------------------------------- Working with Global and Local Context --------------------------------



Global
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

Local 
with decimal.localcontext() as ctx:
    ctx.prec = 2
    ctx.rounding = decimal.ROUND_HALF_UP

    // decimal operations performed here
    // will use the ctx context



"""
