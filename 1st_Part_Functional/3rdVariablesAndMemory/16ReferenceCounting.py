"""

my_var = 10     my_var  ----> 0x1000 [  10]

    reference       count
      0x1000    |  1           
                |           
                |           
                |           
                |   

other_var = my_var
    reference       count
      0x1000    |  2           
                |           
                |           
                |           
                |   

because we are sharing reference

my_var = None

    reference       count
      0x1000    |  1           
                |           
                |           
                |           
                |   


other_var = None

    reference       count
      0x1000    |   0

Object removed from memory by Python Memory Manager  


"""


# Finding reference count in python

import ctypes
import sys


my_var = [1, 2]

# passing my_var to getrefcount() creates and extra reference! :> by 1
print(sys.getrefcount(my_var))

my_var_2 = my_var


print(sys.getrefcount(my_var))

my_var_3 = my_var
my_var_4 = my_var
# Here we just pass the memory address (an integer), not a reference - does not affect reference count
print(ctypes.c_long.from_address(id(my_var)).value)


# interesting part:
a = [1, 2, 3]
a_id = id(a)
a = None
print(a_id)

# segmentation fault python3 <-- research it!
print(ctypes.c_long.from_address(4311995712).value)
