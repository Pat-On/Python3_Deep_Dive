import decimal
from decimal import Decimal


a = Decimal((1, (3, 1, 4, 1, 5), -4))
c = Decimal((0, (3, 1, 4, 1, 5), -4))
b = Decimal('0.12345')

print(a, c, b)
# 0.1000000000000000055511151231257827021181583404541015625
print(Decimal(0.1))

# 0.1
print(Decimal('0.1'))

print(Decimal('0.1') == print(Decimal(0.1)))

decimal.getcontext().prec = 6
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)

with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print(c)
print(c)
