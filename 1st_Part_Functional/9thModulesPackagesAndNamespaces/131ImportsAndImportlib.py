# Imports and importlib
# https://docs.python.org/3/library/site.html#:~:text=This%20module%20is%20automatically%20imported,%2C%20unless%20%2DS%20was%20used.
# read about path files

import os
import importlib.util
import importlib
import collections
import fractions
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)

print(sys)
print(collections)


print(importlib)

# importing modules using variables
mod_name = "math"
importlib.import_module(mod_name)

print('math' in sys.modules)
print('fractions' in sys.modules)

# import math as math2
# math2 = importlib.import_module(mod_name)
math2 = sys.modules['math']

print(math2.sqrt(2))

print(math2)

# importer is advance concepts but the basic principle is:
# to have:
# - finders - finding the modules that i want to import. (different locations)
# - loaders
# - finder + loader == importer


print(fractions.__spec__)
"""
ModuleSpec(name='fractions', 
loader=<_frozen_importlib_external.SourceFileLoader 
object at 0x1049de0e0>, 
origin='/opt/homebrew/Cellar/python@3.10/3.10.6_1/Frameworks/Python.framework/Versions/3.10/lib/python3.10/fractions.py')

"""

print("*" * 40)

# finders:
pp.pprint(sys.meta_path)

pp.pprint(math2.__spec__)

try:
    import module1
except:
    print("error")

# You can create your own finders and loaders

pp.pprint(importlib.util.find_spec("decimal"))

# crating module
with open('module1.py', 'w') as code_file:
    code_file.write('print("running modul1.py..")\n')
    code_file.write("a=100\n")


print("*" * 40)
print(importlib.util.find_spec("module1"))

print('module1' in globals())

print(module1.a)

print("*" * 40)

# windows
# os.environ
ext_module_path = os.environ["HOME"]

print(ext_module_path)

file_abs_path = os.path.join(ext_module_path, "module2.py")

with open(file_abs_path, "w") as code_file:
    code_file.write('print("running modul2.py..")\n')
    code_file.write("x='python'\n")

print(importlib.util.find_spec('module2'))

# check list - directories
pp.pprint(sys.path)


sys.path.append(ext_module_path)
pp.pprint(sys.path)
print("*" * 40)
print(importlib.util.find_spec('module2'))


try:
    import module2
except:
    print("error")
