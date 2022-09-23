"""

not --> and --> or



"""
import string
# logic from uni
print(True or True and False)
print(True or (True and False))
print((True or True) and False)


# Short-Circuiting
# True or Y -> True (always, Y is not evaluated)
# False and Y --> False (always, Y is not evaluated)
a = 10
b = 0
if b > 0 and a/b > 2:
    print("division by zero can not take place")

if b > 0:
    if a/b > 2:
        print("division by zero can not take place")

# Pythonic way
if b and a/b > 2:
    print("division by zero can not take place")


# separator
print("separator")

a = 'c'
print(a in string.ascii_uppercase)
print(string.ascii_uppercase)


name = ''

# name = None


if name and name[0] in string.digits:
    print("Name cannot start with a digit")
