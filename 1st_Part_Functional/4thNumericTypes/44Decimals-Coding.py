# DECIMALS

import decimal
from decimal import Decimal

x = decimal.getcontext()
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1,
# clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
print(x)
print(type(x))

x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.prec = 2
    ctx.rounding = decimal.ROUND_HALF_UP
    print("local", ctx)
    print("local", type(ctx))
    print(round(x, 1))
    print(round(y, 1))

print(round(x, 1))
print(round(y, 1))
