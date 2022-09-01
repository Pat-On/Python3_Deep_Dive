from math import isclose

x = 0.1


print(format(x, '.25f'))

x = 0.1 + 0.1 + 0.1
y = 0.3

print(x == y)


print(isclose(x, y))

x = 123456789.1
y = 123456789.2

print("isclose", isclose(x, y, rel_tol=0.01))


x = 0.1
y = 0.2

print("isclose", isclose(x, y, rel_tol=0.01))


x = 0.0000000001
y = 0.0000000002
# relative tolerance does not work on small numbers! You need to use absolute tolerance
# we need to check delta x - y
print("isclose", isclose(x, y, rel_tol=0.01))

print("isclose", isclose(x, y, rel_tol=0.01, abs_tol=0.01))
# so:
# small numbers - absolute tolerance
# large numbers - relative tolerance

# use both to cover all edge cases
