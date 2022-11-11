# Decorator Application - Decorator Class

def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print("decorated function called: a={0} b={1}".format(a, b))
            return fn(*args, **kwargs)

        return inner
    return dec


@my_dec(10, 20)
def my_func(s):
    print("Hello {0}".format(s))


my_func("World")

# callable classes in Python
print("*" * 40, " Callable Classes")


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c):
        print("called a={0}, b={1} c={2}".format(self.a, self.b, c))


obj = MyClass(10, 20)

obj(111)

obj.__call__(1200)


# callable classes in Python
print("*" * 40, " Callable Classes p2")


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # decorator
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print("called a={0}, b={1}".format(self.a, self.b))
            return fn(*args, **kwargs)

        return inner


@MyClass(10, 20)
def my_func(s):
    print("Hello {0}".format(s))


my_func("hello world")


# callable classes in Python
print("*" * 40, " Callable Classes p - longer way - the same results")


def my_func(s):
    print("Hello {0}".format(s))


obj = MyClass(10, 20)

my_func = obj(my_func)

my_func("World")
