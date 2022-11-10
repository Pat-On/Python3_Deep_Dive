# Decorator Application - Timer

from functools import reduce


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


def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)


print(calc_recursive_fib(3))

# ----------
print("*" * 40)
"""
Since we are calling the function recursively,
we are actually calling the **decorated** function recursively.
 In this case I wanted the total time to calculate the n-th number,
  not the time for each recursion.

You will notice from the above how inefficient the recursive method is:
 the same fibonacci numbers are calculated repeatedly!
 This is why as the value of `n` start increasing beyond 30
 we start seeing considerable slow downs.

"""


@timed
def fib_recursed_2(n):
    if n <= 2:
        return 1
    else:
        return fib_recursed_2(n-1) + fib_recursed_2(n-2)


fib_recursed_2(10)

# ----------
print("*" * 40)


@timed
def fib_recursed(n):
    return calc_recursive_fib(n)


print(fib_recursed(3))
print(fib_recursed(35))


# ----------
print("*" * 40, "loop")


@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


print(fib_loop(3))
print(fib_loop(35))


# ----------
print("*" * 40, "reduce")
"""
We first need to understand how we are going to calculate the Fibonnaci sequence using reduce:

<pre>
n=1:
(1, 0) --> (1, 1)

n=2:
(1, 0) --> (1, 1) --> (1 + 1, 1) = (2, 1)  : result = 2

n=3
(1, 0) --> (1, 1) --> (2, 1) --> (2+1, 2) = (3, 2)  : result = 3

n=4
(1, 0) --> (1, 1) --> (2, 1) --> (3, 2) --> (5, 3)  : result = 5
</pre>

In general each step in the reduction is as follows:

<pre>
    previous value = (a, b)
    new value = (a+b, a)
</pre>

If we start our reduction with an initial value of `(1, 0)`, we need to run our "loop" n times.

We therefore use a "dummy" sequence of length `n` to create `n` steps in our reduce.

"""

# example of reducer


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


l = [5, 8, 6, 10, 9]


def _reduce(fn, sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = fn(result, e)
    return result


print(_reduce(lambda a, b: a if a > b else b, l))


@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    # functools.reduce(function, iterable[, initializer])
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                   dummy,
                   initial)
    return fib_n[0]


print(fib_reduce(3))
print(fib_reduce(6))


"""
So yes, it's cool that you can write this using a single line of code, 
but consider two things here:
1. Is it as efficient as another method?
2. Is the code **readable**?

Code readability is something I cannot emphasize enough. 
Given similar efficiencies (cpu / memory), 
give preference to code that is more easily understandable!

Sometimes, if the efficiency is not greatly impacted 
(or does not matter in absolute terms), 
I might even give preference to less efficient, 
but more readable (i.e. understandable), code.

But enough of the soapbox already :-)

"""


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)  # parametrized decorator
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count = 0

        for i in range(10):
            print("Running iteration {0}...".format(i))
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            elapsed_total += elapsed
            elapsed_count += 1

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        elapsed_avg = elapsed_total / elapsed_count
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__,
                                                      args_str,
                                                      elapsed_avg))
        return result

    return inner


@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    # functools.reduce(function, iterable[, initializer])
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                   dummy,
                   initial)
    return fib_n[0]


print(fib_reduce(100))
