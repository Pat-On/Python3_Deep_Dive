"""

                    Functions



function are like variables

def is key words with is assigning function without execution, 
    just storing it as a object and metadata for example about parameters
    it is not executing these functions at all at the moment of creations

    so we can call not existing function yet within the function definition,
    that function has to exist when function is called

    assiging the variable name to function

"""
import math

# Built in
s = [1, 2, 3]

print(len(s))

print(math.pi)


# define function

def func_1():
    print("Running func_1")


func_1()

# it is just for documentation purposes


def func_2(a: int, b: int):
    return a * b

# lambda functions
# it allows you to create function ,but it does not require the name for the function
# You can not have big code block, just simple code in one line


print(type(func_1))

print(lambda x: x**2)


def fn1(x): return x**2


print(fn1(2))
