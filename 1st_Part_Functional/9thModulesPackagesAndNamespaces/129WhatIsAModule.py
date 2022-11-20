# What is a Module? :>

import types
import pprint
import sys
import fractions
import math

pp = pprint.PrettyPrinter(indent=4)


def func():
    a = 10
    return a


print(func)
# name spaces are dictionaries
print(globals())

print(globals()['func'])

print(locals())

# the same scope in that case so true
print(locals() is globals())


print("*" * 40)

# import math
print(math)
# <module 'math' from '/opt/homebrew/Cellar/python@3.10/3.10.6_1/Frameworks/Python.
# framework/Versions/3.10/lib/python3.10/lib-dynload/math.cpython-310-darwin.so'>

# import fractions
print(fractions)
# <module 'fractions' from '/opt/homebrew/Cellar/python@3.10/3.10.6_1/Frameworks/
# Python.framework/Versions/3.10/lib/python3.10/fractions.py'>

# it is going to contain now math fractions etc - reference object
print(globals())
print(type(globals()))

# if you are trying to import module twice in application it is not going to work, because
# global will store reference in the form of the singleton
# it is added to system cache


# import sys
# to check system cache
pp.pprint(sys.modules)
print(type(sys.modules))
print(sys.modules['math'])


print("*" * 40)

# dictionary again so all is reference and look-ups table
pp.pprint(math.__dict__)


# import types
print(isinstance(fractions, types.ModuleType))

# namespaces are basically dictionaries
