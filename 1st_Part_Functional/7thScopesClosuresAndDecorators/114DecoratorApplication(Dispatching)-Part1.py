# Decorator Application: Single Dispatch Generic Functions

# overloading function - we do not have it in python, no function signature etc
"""
If you have a background in some other OO languages such as Java or C#, 
you'll know that we can easily do something like this by basically **overloading** 
functions: using a different data type for the function parameter, 
hence changing the function signature. Then although the name of the function is the same, 
calling `do_something(100)` and `do_something('java')` would call a different function,
 the first one would call the `do_something(int)` function, and the second would call the 
 `do_something(String)` function.

Of course, Python is not statically typed, so even if Python had function overloading built-in,
 we would not be able to make such a distinction in our function signatures since 
 there is nothing that says that a parameter must be of a specific type, 
 so in a best case scenario we would have to "distinguish" functions with the same name only
  by the number of parameters they take. And then we'd have to somehow deal
   with variable numbers of positional and keyword arguments too... Uuugh!
In any event, single dispatch could never work.

Instead we have to come up with a different solution.



Let's say we want to display various data types in html format, 
with different presentations for integers (we want both base 10 and hex values), 
floats (we always want it rounded to 2 decimal points), strings (we want the string html-escaped,
 and all newline characters replaced by `<br/>`), 
 lists and tuples should be implemented using bulleted lists, and the same with dictionaries
  except we want the name/value pair to be displayed in the bulleted list.

For starters, let's just implement individual functions to do each of those things.

I am going to keep the functions very simple, but in practice you should handle situations
 like None objects, empty lists and dictionaries, possibly the wrong type being passed 
 to the function, etc.

"""

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


print(html_str("""this is 
a multi line string
with special characters: 10 < 100"""))

print(html_int(255))

print(html_escape(3+10j))


# from decimal import Decimal
print("*" * 40, "dispatcher")


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


print(htmlize([1, 2, 3]))

print(htmlize(dict(key1=1, key2=2)))

print(htmlize(255))

print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))


print("*" * 40, "dispatcher 2")


def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))


def html_real(a):
    return '{0:.2f}'.format(round(a, 2))


def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v))
             for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


# now this is working
print(htmlize(["""first element is   
a multi-line string""", (1, 2, 3)]))


print("*" * 40, "dispatcher 3")
"""
As you can see this works just fine.

But we still have something undesirable. You'll notice that the dispatch function `htmlize`
 needs to have this big `if...elif...else` statement that will just keep growing as we need to
  handle more and more types (including potentially custom types).

This will just get unwieldy, and not very flexible (every time someone creates a new type 
that has to have a special html representation they will need to go into the `htmlize` 
function and modify it.

So instead, we are going to try a more flexible approach using decorators.


The way we are going to approach this is to create a dispatcher function, 
and then separately "register" each type-specific function with the dispatcher.

First, we are going to create a decorator that will do something that may seem kind 
of silly - it is going to take the decorated function and store it in a dictionary,
 using a key consisting of the **type** `object`.

Then when the returned closure is called, the closure will call the function stored 
in that dictionary.
"""


def singledispatch(fn):
    registry = dict()
    registry[object] = fn

    def inner(arg):
        return registry[object](arg)

    return inner


@singledispatch
def htmlizer(arg):
    return escape(str(arg))


print(htmlizer('a < 10'))


print("*" * 40, "dispatcher 4")


def singledispatch(fn):
    registry = dict()

    registry[object] = fn
    registry[int] = lambda arg: '{0}(<i>{1}</i)'.format(arg, str(hex(arg)))
    registry[float] = lambda arg: '{0:.2f}'.format(round(arg, 2))

    def inner(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)
    return inner


@singledispatch
def htmlize(a):
    return escape(str(a))


print(htmlize(10))
print(htmlize(3.1415))


"""
Now, we want a way to add the specialized functions to the `registry` dictionary
 from **outside** the `singledispatch` function - to do so we will create
  a parametrized decorator that will (1) take the type as a parameter, 
  and (2) return a closure that will decorate the function associated with the type:

"""


def singledispatch(fn):
    registry = dict()

    registry[object] = fn

    def register(type_):
        def inner(fn):
            registry[type_] = fn
        return inner

    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    return decorator
