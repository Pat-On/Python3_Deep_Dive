from collections.abc import Sequence
from numbers import Integral
from decimal import Decimal
from html import escape
from functools import singledispatch

"""
You'll note that a string is also a sequence type, hence our dispatcher will call
 the `html_sequence` function on a string.

In fact, at this point things would not even run properly.

If we were to call

`htmlize('abc')`

we'd get an infinite recursion!

The call to `htmlize` the string `abc` would treat it as a sequence,
which would call `htmlize` character by character.
But each character is itself just a string of length 1, so it will `htmlize` 
for that single character, which would treat it as a sequence, 
which would call `htmlize` for that single character again, and so on, in an infinite loop. 
"""


"""
The way we have implement our decorator, 
if we register an Integral generic function, it won't pick up either integers or Booleans.

We can certainly fix this shortcoming ourselves, but of course...

We can can use Python's built-in single dispatch support, in ...

you guessed it!

the `functools` module.

from functools import singledispatch
"""


@singledispatch
def htmlize(a):
    return escape(str(a))


"""
The `singledispatch` returned closure has a few attributes we can use:
1. A `register` decorator (just like ours did)
2. A `registry` property that is the registry dictionary
3. A `dispatch` function that can be used 
    to determine which registry key (registered type) it will use for the specified type.
"""


@htmlize.register(Sequence)
def html_sequence(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(Integral)
def htmlize_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


print(htmlize.dispatch(list))
print(htmlize.dispatch(tuple))

# print(htmlize('abc')) # error


@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')


print(htmlize('abc'))
