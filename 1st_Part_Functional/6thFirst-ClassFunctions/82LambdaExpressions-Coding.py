func_2 = lambda x, *args, y, **kwargs: print(x, args, y, kwargs)
func_2(1, 'a', 'b', 'c', y=100, a=10, b=20)


def apply_func(x, fn):
    return print(fn(x))


apply_func(3, lambda x: x**2)
apply_func(3, lambda x: x**3)


print("*" * 10)


def apply_func(fn, *args, **kwargs):
    return print(fn(*args, **kwargs))


apply_func(lambda x, y: x+y, 1, 2)
apply_func(lambda x, *, y: x+y, 1, y=2)
apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5)
