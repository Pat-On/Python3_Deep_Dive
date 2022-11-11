# Decorators Part 2 - Coding

def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print("Run time: {0:.6f}s".format(elapsed))
        return result

    return inner


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n - 2) + calc_fib_recurse(n - 1)


# @timed
def fib(n):
    return calc_fib_recurse(n)


fib = timed(fib)

print(fib(30))

# -------------------------------------------------------------------------------------
print("*" * 40)


def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += end - start

        avg_run_time = total_elapsed/10
        print("Avg run time: {0:.6f}s".format(avg_run_time))
        return result

    return inner


def fib(n):
    return calc_fib_recurse(n)


fib = timed(fib)

print(fib(28))

# -------------------------------------------------------------------------------------
print("*" * 40)


def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += end - start

        avg_run_time = total_elapsed/reps
        print("Avg run time: {0:.6f}s ({1} reps)".format(avg_run_time, reps))
        return result

    return inner


def fib(n):
    return calc_fib_recurse(n)


fib = timed(fib, 5)

print(fib(28))

# -------------------------------------------------------------------------------------
print("*" * 40)


def dec(fn):
    print("Running dec")

    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)
    return inner


@dec
def my_func():
    print("running my func")


def my_func():
    print("running my func")

# the same:


my_func = dec(my_func)


# -------------------------------------------------------------------------------------
print("*" * 40)


def dec_factory():
    print("running dec_factory")

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            return fn(*args, **kwargs)

        return inner

    return dec


dec = dec_factory()


def my_func():
    print("running my func")


my_func = dec(my_func)


@dec_factory()
def my_func():
    print("running my func")


def my_func():
    print("running my func")


# the same
my_func = dec_factory()(my_func)

# -------------------------------------------------------------------------------------
print("*" * 40, "Variables Time")


def dec_factory(a, b):
    print("running dec_factory")

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            print("param", a, b)
            return fn(*args, **kwargs)

        return inner

    return dec


dec = dec_factory(10, 20)


@dec
def my_func():
    print("running my func")


my_func()


@dec_factory(100, 200)
# the same, just shorter syntax
def my_func():
    print("running my func")


my_func()


def my_func():
    print("running my func")


my_func = dec_factory(150, 200)(my_func)
