# Decorator Application: Single Dispatch Generic Functions 2

"""

Now, we want a way to add the specialized functions to the `registry` dictionary 
from **outside** the `singledispatch` function - to do so we will create a parametrized
 decorator that will (1) take the type as a parameter,
  and (2) return a closure that will decorate the function associated with the type:
"""

from collections.abc import Sequence
from numbers import Integral
from decimal import Decimal
from html import escape


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
    # generator - pythonic way
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), html_escape(v))
             for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))


def singledispatch(fn):
    registry = {}

    registry[object] = fn
    # hardcoded! <-- not generic!
    registry[int] = lambda a: '{0}(<i>{1}</i)'.format(a, str(hex(a)))
    registry[str] = lambda s: escape(s).replace('\n', '<br/>\n')

    def inner(arg):
        return registry.get(type(arg), registry[object])(arg)

    return inner


@singledispatch
def htmlize(a):
    return escape(str(a))


print(htmlize("1 < 100"))
print(htmlize(100))

# Keep developing correct generic solution
print("*" * 40)


def singledispatch(fn):
    registry = {}

    registry[object] = fn

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)

    # decorator factory <--- how to get to it? WOW As a attribute!
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner

    decorated.register = register
    return decorated


@singledispatch
def htmlize(a):
    return escape(str(a))


print(htmlize("1 < 100"))
print(htmlize(100))

# decorator factory <-- inside the other decorator!


@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


print(htmlize(100))


@htmlize.register(tuple)  # stacking decorators because we returned fn
@htmlize.register(list)
def html_sequence(l):
    # generator - pythonic way
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


# long form of decoration
html_list = htmlize.register(list)(html_list)

print(htmlize([1, 2, 3]))
print(htmlize((1, 2, 3)))
# Keep developing correct generic solution
# This is so nice!
print("*" * 40)

"""
But of course this is not good enough - how do we get a hold of the `register` function 
from outside `singledispatch`? Remember, `singledispatch` is a decorator that returns the
 `decorated` closure, not the `register` closure.


We can do this by adding the `register` function as an **attribute** of the `decorated`
 function before we return it. 

While we're at it we're also going to:

* add the `registry` dictionary as an attribute as so we can look into it to see 
what it contains.

* add another function that given a type will return the function associated 
with that type (or the default function if the type is not found in the dictionary)
"""


def singledispatch(fn):
    registry = dict()

    registry[object] = fn

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn  # we do this so we can stack register decorators!
        return inner

    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    def dispatch(type_):
        return registry.get(type_, registry[object])

    # This idea is super!
    decorator.register = register
    decorator.registry = registry.keys()
    decorator.dispatch = dispatch
    return decorator


@singledispatch
def htmlize(a):
    return escape(str(a))


@htmlize.register(tuple)  # stacking decorators because we returned fn
@htmlize.register(list)
def html_sequence(l):
    # generator - pythonic way
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


print(htmlize.registry)
print(htmlize.register)
print(htmlize.dispatch(int))


# SOLVING OTHER PROBLEMS.
"""
Our single dispatch decorator works quite well - but it has some limitations. 
For example it cannot handle functions that take in more than one argument 
(in which case dispatching would be based on the type of the **first** argument), 
and we also are not allowing for types based on parent classes - for example, 
integers and booleans are both integral numbers - i.e. they both inherit 
from the Integral base class. Similarly lists and tuples are both more 
generic Sequence types. We'll see this in more detail when we get 
to the topic of abstract base classes (ABC's).
"""
# from numbers import Integral


def singledispatch(fn):
    registry = dict()

    registry[object] = fn

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn  # we do this so we can stack register decorators!
        return inner

    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    def dispatch(type_):
        return registry.get(type_, registry[object])

    # This idea is super!
    decorator.register = register
    decorator.registry = registry.keys()
    decorator.dispatch = dispatch
    return decorator


@singledispatch
def htmlize(a):
    return escape(str(a))


@htmlize.register(Integral)
def html_integral_number(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


# it failed because of the type
print(htmlize(10))


# abstract base classes

# from collections.abc import Sequence
@htmlize.register(Sequence)
def html_sequence(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


# because it is instance of Sequence, but the type is not Sequence
print(type([1, 2, 3]) is Sequence)
