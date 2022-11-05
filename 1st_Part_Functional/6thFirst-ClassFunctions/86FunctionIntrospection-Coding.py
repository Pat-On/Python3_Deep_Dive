# Function Inspection
import inspect
from inspect import isfunction, ismethod, isroutine


def my_func(a: "mandatory positional",
            b: "optional" = 1,
            c=2,
            *args: "add extra positional here",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs) -> "does nothing":
    """does something or other"""
    i = 10
    j = 20


print(my_func.__doc__)


my_func.short_description = "factorial function"
print(my_func.short_description)

print(id(my_func))


def func_call(f):
    print(id(f))
    print(f.__name__)


func_call(my_func)

# ------------------------------------------------------------------------
print("-" * 80)

print(my_func.__defaults__)
print(my_func.__kwdefaults__)


# ------------------------------------------------------------------------
print("-" * 80)

a = 10

print(isfunction(a))

print(isfunction(my_func))


# ------------------------------------------------------------------------
print("-" * 80)

print(my_func.__annotations__)


class MyClass:
    def f_instance(self):
        pass

    @classmethod
    def f_class(cls):
        pass

    @staticmethod
    def f_static():
        pass


print(inspect.isfunction(MyClass.f_instance))

print(inspect.ismethod(MyClass.f_instance))

print(inspect.isfunction(MyClass.f_static), inspect.ismethod(MyClass.f_static))


my_obj = MyClass()
print(inspect.isfunction(my_obj.f_instance),
      inspect.ismethod(my_obj.f_instance))


# print(help(divmod))

print(divmod(4, 3))

for param in inspect.signature(divmod).parameters.values():
    # we can not create positional_only parameters
    # it is thing that python use internaly
    print(param.kind, param)
