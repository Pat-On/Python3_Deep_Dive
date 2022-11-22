# Import Variants and Misconceptions

import sys

for key in sorted(sys.modules.keys()):
    print(key)

print('cmath' in sys.modules, 'cmath' in globals())

try:
    from cmath import exp
except:
    print("Ups error")

print('cmath' in sys.modules, 'cmath' in globals())
print('exp' in sys.modules, 'exp' in globals())

print(id(exp))

print("*" * 40)
# it is importing entire module

cmath = sys.modules['cmath']

print('cmath' in globals())

print(cmath.sin(2+2j))

# horrible idea - everything is in globals(), so everything might be overwritten example math.sin and cmath.sin etc
# from cmath import *


# very bad idea - you need to have one source of truth about dependencies - readability
def my_func(a):
    # efficiency - it is going to be loaded only once, and then it would just go and find reference
    import math
    return math.sqrt(a)


try:
    from time import perf_counter
    from collections import namedtuple
except:
    print("Ups error")

Timings = namedtuple("Timings", 'timing_1m, timing_2, abs_diff, red_diff_perc')


def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1) / timing1 * 100

    timings = Timings(round(timing1, 1),
                      round(timing2, 1),
                      round(timing2 - timing1, 1),
                      round(rel_diff, 2))

    return timings


print(compare_timings(1, 2))


test_repeats = 10_000_000

# Timing using fully qualified module.symbol
try:
    import math
except:
    print("Ups error")

start = perf_counter()

for _ in range(test_repeats):
    math.sqrt(2)

end = perf_counter()

elapsed_fully_qualified = end - start

print(f'Elapsed: {elapsed_fully_qualified}')


# Timing using a directly import symbol name
try:
    from math import sqrt
except:
    print("Ups error")

start = perf_counter()

for _ in range(test_repeats):
    sqrt(2)

end = perf_counter()

elapsed_direct_symbol = end - start

print(f'Elapsed: {elapsed_direct_symbol}')


print("Comparing timing")

print(compare_timings(elapsed_fully_qualified, elapsed_direct_symbol))

# the same is for wrapping sqrt and very similar for import inside the function 10 000 000 loop and the solution was faster around 1.8 second
# this time difference coming from additional lookup


def func():
    import math
    math.sqrt(2)


start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_fully_qualified = end - start
print(f'Elapsed: {elapsed_nested_fully_qualified}')


def func():
    # slower because of finding reference again - extra step
    from math import sqrt
    sqrt(2)


start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_direct_symbol = end - start
print(f'Elapsed: {elapsed_nested_direct_symbol}')

print(compare_timings(elapsed_nested_fully_qualified, elapsed_nested_direct_symbol))

"""

So does this mean you should put imports inside functions?

No, of course not - follow the convention, it makes code far more readable, 
and of course optimize your code only once you have identified the bottlenecks. 

Does this mean you shouldn't care at all about the performance of your code 
based on the import variants?

Again, of course not - you absolutely should.

But, there is absolutely no reason to re-write your code from 

`import math
math.sqrt(2)`

to 

`from math import sqrt
sqrt(2)
`

for **speed** reasons if during the entire lifetime of your application 
you only call that function `100` times... or `10,000,000` times.

Really depends on your circumstance - be aware of it, but don't try to 
optimize code until you know **where** you **need** to optimize!

*[I've seen people refactor parts of their code for sub-second improvements,
 when, in fact, the largest bottleneck was that they were opening and closing 
 database connections at every read and write instead of pooling connections or 
 something like that]*

"""
