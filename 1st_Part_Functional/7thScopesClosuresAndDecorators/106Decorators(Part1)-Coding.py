# Decorators - Wrappers - Function Composition

from functools import wraps
import inspect


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner


def add(a, b=0):
    """
    returns the sum of a and b
    """
    return a + b


# print(help(add))

print(id(add))
add = counter(add)
print(id(add))

add(1, 2)
add(2, 2)

# using @Decorator Syntax
print("*" * 40)


@counter
def mult(a: float, b: float = 1, c: float = 1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c


mult(1, 2, 3)

print(add.__name__)
print(mult.__name__)

# ---------------------------
print("*" * 40)


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner


@counter
def add(a: int, b: int = 10) -> int:
    """
    returns sum of two integers
    """
    return a + b


# print(help(add))  # does not work :>

print(add.__name__)


# functools.wraps
print("*" * 40)


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))

    return inner


@counter
def add(a: int, b: int = 10) -> int:
    """
    returns sum of two integers
    """
    return a + b

# print(help(add)) # works :>


print(inspect.getsource(add))
print(inspect.signature(add))
print(inspect.signature(add).parameters)
