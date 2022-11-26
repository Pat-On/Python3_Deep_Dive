# Timing code using timeit


"""
When we were looking at decorators we wrote a timing decorator.
 It could even take a number of repetitions as a parameter. 
 This can be handy to time functions directly in your code without
  affecting the result of the function. But it wrote the results
   out to the console, and sometimes we just want to access the timing 
   data right inside our Python code.

The `timeit` module in Python is an alternative that works well for 
some things. It is a little more complicated to use because it runs 
'outside' of our local namespace, and you have to pass just small snippets 
of code to it (well you pass multi-line chunks of code, but it gets tedious),
 and you also have to make it aware of you global or local scope 
 if that's needed by the code you want to time. One thing it does 
 that we did not do was *temporarily disable* the garbage collector. 
 Still, there are a lot of pitfalls to benchmarking, and this approach
  like ours, is good enough for most cases. YMMV.

It has the advantage that it can also be run directly from the command line.

Let's take a look at it.

"""

from math import sqrt
import math
from timeit import timeit

"""
We look at the `timeit` function. There are a few others but this is 
the main one and the remaining are slight variations that you may find useful,
 so check out the Python docs for more info.

 Basically the `timeit` function needs to know a few things:

- the Python statement to run (the **stmt** argument)
- how many times to run the same code (the **number** argument 
        - watch out, the default is `1_000_000` times!)
- any setup code (like imports) (the **setup** argument)
- an optional scope that acts like a global scope to the statement 
        (the **globals** argument)

It will then execute the test `number` of times and return 
    the **total** time elapsed (not an average per test).

Let's start with a simple example, where we want to time how long it takes 
to run the `sqrt` function in the `math` module using two different ways of importing it:

"""
print(math.sqrt(2))

print(sqrt(2))


"""
As you can see in the first example we have to specify `name.sqrt` 
every time we want to call the `sqrt` function. 
Is there a time difference between those two approaches?


"""
timeit(stmt='math.sqrt(2)', setup='import math')


result_1 = timeit(stmt='math.sqrt(2)', setup='import math')
result_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')
print(f'Result 1 = {result_1}')
print(f'Result 2 = {result_2}')
