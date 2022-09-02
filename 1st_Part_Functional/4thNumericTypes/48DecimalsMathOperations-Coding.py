import decimal
from decimal import Decimal
import math
x = 10
y = 3
print(x//y, x % y)
print(divmod(x, y))
print(x == y * (x//y) + x % y)

print("-" * 40)
a = Decimal('10')
b = Decimal('3')
print(a//b, a % b)
print(divmod(a, b))
print(a == b * (a//b) + a % b)


a = Decimal('-10')
b = Decimal('3')
print(a//b, a % b)
print(divmod(a, b))
print(a == b * (a//b) + a % b)

print("-" * 40)
a = Decimal('1.5')
print(a.log10())  # base 10 logarithm
print(a.ln())     # natural logarithm (base e)
print(a.exp())    # e**a
print(a.sqrt())   # square root


x = 2
x_dec = Decimal(2)

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)
print("-" * 40)
print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)

x = 0.01
x_dec = Decimal('0.01')

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
print("-" * 40)
print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)
print("-" * 40)
print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)
