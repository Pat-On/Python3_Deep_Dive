import cmath

a = complex(1, 2)
b = 1 + 2j

print(a == b)
print("BREAK")

print(a.real, type(a.real))
print(a.imag, type(a.imag))

print(a.conjugate())

# Polar / Rectangular Conversions

a = 1 + 1j
r = abs(a)
phi = cmath.phase(a)
print('{0} = ({1},{2})'.format(a, r, phi))
