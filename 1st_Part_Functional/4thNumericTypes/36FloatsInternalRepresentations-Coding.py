from fractions import Fraction

# print(help(float))


print(float(10))

a = Fraction("22/7")
print(float(a))

# infinite representation

infinite = 0.1

print(infinite)

print(format(infinite, '0.15f'))
print(format(infinite, '0.35f'))
print(format(infinite, '0.55f'))

sum = 0.1 + 0.1 + 0.1
other_num = 0.3

print(sum == other_num)
