# Rational Numbers

from fractions import Fraction
import math

x = Fraction(1, 1)
print(x)

y = Fraction(numerator=10, denominator=7)

print(y)

w = x + y
print(w)


# automatic reduction

red = Fraction(20/10)
print(red)

neg = Fraction(1, -4)
print(neg)
print(neg.denominator)
print(neg.numerator)

# irrational numbers in python are represented as a rational

x = Fraction(math.pi)
print(x)
x = float(x)
print(x)

# some numbers do not have correct representation

b = 0.3  # it is not what is stored
b = Fraction(b)
print(b)


num = 0.3
print(format(num, '0.5f'))
print(format(num, '0.15f'))
print(format(num, '0.25f'))  # 0.2999999999999999888977698

print(b.limit_denominator(10))
print(b.limit_denominator(1000))
print(b.limit_denominator(10000000000))
