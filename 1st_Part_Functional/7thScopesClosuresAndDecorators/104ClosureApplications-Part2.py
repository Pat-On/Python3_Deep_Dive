# Closures Applications (Part 2)

def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc


counter1 = counter()
print(counter1())


def counterCalls(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print("{0} has been called {1} times".format(fn.__name__, cnt))
        return fn(*args, **kwargs)

    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


counter_add = counterCalls(add)

print(counter_add.__code__.co_freevars)

counter_add(10, 20)

print(counter_add(10, 20))


counters = dict()


def mult(a, b, c):
    return a * b * c


def counter(fn):
    cnt = 0  # initially fn has been run zero times

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is global
        return fn(*args, **kwargs)

    return inner


counted_add = counter(add)


counted_mult = counter(mult)

print(counted_add(1, 2))
print(counted_add(2, 3))
print(counted_mult(1, 2, 'a'))

print(counters)
