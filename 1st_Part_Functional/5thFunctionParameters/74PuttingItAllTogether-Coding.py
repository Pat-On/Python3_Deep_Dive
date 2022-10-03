def func(a, b):
    print(a, b)


func('hello', 'world')


func(b='world', a='hello')


def func(a, b, *args):
    print(a, b, args)


# can not use in this way - positonal argument after keyword arguments
# func(b=2, a=1, 'x', 'y', 'z')
print("break " * 20)

# Keywords and Positionals: some positionals (no defaults), keywords (no defaults)


def func(a, b, *, c, d):
    print(a, b, c, d)


func(1, 2, c=3, d=4)


# Keywords and Positionals: extra positionals, extra keywords
print("break " * 20)


def func(a, b, *args, c, d=4, **kwargs):
    print(a, b, args, c, d, kwargs)


func(1, 2, 'x', 'y', 'z', c=3, d=5, x=100, y=200, z=300)


# help(print)
