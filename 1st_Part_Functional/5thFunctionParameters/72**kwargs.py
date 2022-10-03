"""
        **kwargs

        *args is used to scoop up variable amount of remaining positional arguments         -> tuple
                The parameter name args is arbitrary - * is the real performer here


        **kwargs is used to scoop up a variable amount of remaining keywords arguments      -> dictionary
                  The parameter name args is arbitrary - ** is the real performer here

        **kwargs can be specified even if the positional arguments have not been exhausted
            (unlike keyword-only arguments)

        No parameters can come after **kwargs

        Example:

        def func(*, d, **kwargs):
            # code

        func(d=1, a=2, b=2)  d = 1
                            kwargs = { "a": 2, "b": 3}
        


"""


from timeit import repeat


def func(**others):
    print(others)


func()
func(a=1, b=2)

print("*" * 20)


def func(*args, **others):
    print(args)
    print(others)


func(1, 2, x=100, y=200)


def func(a, b, *, d, **others):
    print(a)
    print(b)
    print(d)
    print(others)


func(1, 2, d=20, x=100, y=200)
