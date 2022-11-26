# Do not use *args and **kwargs Names Blindly

# good example:
from operator import mul
from functools import reduce


def audit(func):
    def inner(*args, **kwargs):
        print(f"called {func.__name__}")
        return func(*args, **kwargs)
    return inner


@audit
def say_hello(name):
    return f"Hello {name}"


@audit
def product(*values):
    return reduce(mul, values)


print(say_hello(name="Patryk"))

print(product(1, 2, 3, 4, 5, 6))


# Class example

class Person:
    def __init__(self, name, age, **custom_attributes):
        self.name = name
        self.age = age
        for attr_name, attr_value in custom_attributes.items():
            setattr(self, attr_name, attr_value)


parrot = Person("Polly", 101, status="stiff", is_flying=False)

print(vars(parrot))
