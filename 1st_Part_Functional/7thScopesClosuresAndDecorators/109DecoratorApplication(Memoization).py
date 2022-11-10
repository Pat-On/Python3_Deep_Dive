# Decorator Application (Memoization)

from functools import lru_cache


def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


fib(10)
print("*" * 40)


class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print("Calculating fib({0})".format(n))
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]


f = Fib()

print(f.fib(10))

# Simple class can be written as a closure
print("*" * 40, "Closure")


def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print("Calculating fib({0})".format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n - 2)
        return cache[n]

    return calc_fib


f = fib()
print(f(10))
print(f(10))


print("*" * 40, "Decorator")


def memoize_fib(fib):
    cache = {1: 1, 2: 1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]

    return inner


@memoize_fib
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(10))
print(fib(10))


print("*" * 40, "Decorator - general")


def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@memoize
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(10))
print(fib(10))
print(fib(12))


print("*" * 40, "Decorator - general - limiting the cache size")
# from functools import lru_cache


@lru_cache()
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(10))
print(fib(10))
print(fib(12))

print(fib(500))


@lru_cache(maxsize=8)
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(10))
print(fib(10))
print(fib(12))
print(fib(500))
