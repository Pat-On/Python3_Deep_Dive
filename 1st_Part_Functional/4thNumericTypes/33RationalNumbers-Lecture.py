"""

Rational nmbers are fractions of integers numbers

ex 1/2 -22/7

any real number with a finite number of digit after the decimal point is also a rational number

    0.45 -> 45/100 (rational number)

    0.123456789 

    so 8.3/4 -> 83/40 


The Fraction Class

rational numbers can be represented in python using the Fraction class in the fractions module

from fractions import Fraction


x = Fraction(3,4)
y = Fraction(22,7) 22/7


Fractions are automatically reduced:
    Fraction(6,10) -> Fraction(3,5)


Negative sign if any is always attached to the numerator:
    Fraction(1, -4) -> Fraction(-1, 4)


Constructor
    Fraction(numerator=0, denominator=1)

    Fraction(other_fraction)

    Fraction(float)

    Fraction(decimal)

        Fraction('10') -> Fraction(10, 1)

        Fraction('0.125') -> Fraction(1, 8)

        Fraction('22/7;) -> Fraction(22, 7)
        
    Standard arithmetic operators are supported: + - * /
        and result in Fraction objects as well

    
    Getting the numerator and denominator of Fraction Objects:

    x = Fraction(22, 7)

    x.numerator -> 22
    x.denominator -> 7

Float objects have finite precision => any float object can be written as a fraction

Fraction(0.75) => Fraction(3, 4)


import math

x = Fraction(math.pi) => Fraction(884279........, 281474.........)
        Python found approximation of irrational numbers to present them as a rational - Fraction   
        because they are internally represented as a floats, because number digits in computer is limited

        - Pi and other irrational numbers are internally represented as a floats
            - finite precision real number
            - expressible as a rational number
                but it is an approximation


!!!!!!  Converting a float to a Fraction has an important caveat

    We will examine this in detail in a later video on floats

    1/8 has an exact float representation
        Fraction(0, 125) -> Fraction(1,8)

    3/10 does not have an exact float representation

        Faction(0,3) -> Fraction(540431....., 180143......)

        format(0.3, '.5f) -> 0.30000

        format(0.3, '.25f) -> 0.29999999999988889777698


Constraining the denominator

Given a Fraction object, we can find an approximate equivalent fraction with a constrained denominator

    using the limit_denominator(max_denominator=1000000) instance method

i.e. finds the closest rational (which could be precisely equal) 
    with a denominator that does not exceed max_denominator

x = Fraction(math.pi)   => Fraction(540431....., 180143......)

x.limit_denominator(10) -> Fraction(22, 7)

x.limit_denominator(100) -> Fraction(311, 99)



"""
