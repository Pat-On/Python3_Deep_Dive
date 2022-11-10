# Decorator Application (Logger, Stacked Decorators)
# Log to file, to db, to console -> target is not important!

def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print("{0}: called {1}".format(run_dt, fn.__name__))
        return result

    return inner


@logged
def func_1():
    pass


@logged
def func_2():
    pass


print(func_1())
print(func_2())

#  ----------------------------------------------------------------------------
print("*" * 40)


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__,
                                                      args_str,
                                                      elapsed))
        return result

    return inner


@timed
@logged
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))


print(fact(5))


def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))


# it is the same like:
fact_manual_decorating = logged(timed(fact))

print("manual: ", fact_manual_decorating(5))


# ------------------------------------------------------------

print("*" * 40)


def dec_1(fn):
    def inner():
        print("running dec_1")
        return fn()
    return inner


def dec_2(fn):
    def inner():
        print("running dec_2")
        return fn()
    return inner


@dec_1
@dec_2
def my_func():
    print("Running my_func")

# my_func = dec_1(dec_2(my_func))


my_func()
# unning dec_1
# running dec_2
# Running my_func


def dec_1B(fn):
    def inner():
        result = fn()
        print("running dec_1")
        return result
    return inner


def dec_2B(fn):
    def inner():
        result = fn()
        print("running dec_2")
        return result
    return inner


@dec_1B
@dec_2B
def my_func_b():
    print("Running my_func")


my_func_b()
# Running my_func
# running dec_2
# running dec_1

# like in pre in and post order in traversing tree

################################################################################################
# AUTHORIZATION WITHIN DECORATOR

"""
@auth
@logged


@auth
@logged
def save_resources():
    pass


save_resource = auth(logged(save_resource))  <-- nice I like it! 

"""
