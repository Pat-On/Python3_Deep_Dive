# print(help(print))


def my_func(a, b):
    return a*b


# print(help(my_func))


def my_func(a, b):
    'Returns the product of a and b'
    return a*b


# print(help(my_func))


def fact(n):
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n-1)


# print(help(fact))


def my_func(a: 'annotation for a', b: 'annotations for b') -> 'annotation for return':  # type: ignore

    return a*b


# print(help(my_func))

print(my_func.__annotations__)


def fact(n: 'int >= 0') -> int:
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n-1)


print("*" * 10)

print(fact.__annotations__)
print(fact.__doc__)
