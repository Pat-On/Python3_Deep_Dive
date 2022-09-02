# Rounding Floats

a = round(1.9)

print(a, type(a))

a = round(1.9, 0)

print(a, type(a))

round(888.88, 1)
round(888.88, 0)
round(888.88, -1)
round(888.88, -2)
round(888.88, -3)
round(888.88, -4)


print(round(888.88, 1),
      round(888.88, 0),
      round(888.88, -1),
      round(888.88, -2),
      round(888.88, -3),
      round(888.88, -4))  # 0.0 because it is closer value to between 10 000 <---> 0


# banker's rounding
print(round(1.25, 1), round(1.35, 1))
print(round(-1.25, 1), round(-1.35, 1))


def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))


print(round(1.5), _round(1.5))

print(round(2.5), _round(2.5))
