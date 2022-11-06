"""
            MAP, FILTER< ZIP

        HOF def
        a function that takes a function as a parameter and or returns a function as its return value

        example: sorted

        map and filter -> modern alternative -> list comprehensions and generator expressions


----------------------------------------------------------------------------------------------------------------

        The map function

map(func, *iterable)

*iterables -> a variable number of iterable objects

func -> some function that takes as many arguments as there are iterable objects passed to iterables


map -  will the return an iterator that calculates the  function applied to each element of the iterables

    The iterator stops as sons as one of the iterables has been exhausted so unequal length iterables can be used

------------------------------------------------------------------------------------------------------------
examples:


l = [1, 2, 3]

def sq(x):
    return x**2

list(map(sq, l)) -> [4, 9, 16]


l1 = [1,2,3]
l2 = [10, 20, 30]

list(map(add, l1, l2)) -> [11, 22, 33]

list(map(lambda x, y: x+y), l1, l2)

------------------------------------------------------------------------------------------------------------

            The filter function

filter(func, iterable)

    iterable -> a single iterable
    func    -> some function that takes a  single argument

filter(func, iterable) will then return an iterator that contains all the elements of the iterable for which the function called on it is 
                    Truthy

if the function is None, is simply return the elements of iterable that are Truthy


examples:

    l = [0, 1, 2, 3, 4]

    list(filter(None, l)) -> [ 1, 2, 3, 4]

    def is_even(n):
        return n % 2 == 0

    list(filter(is_even, l)) -> [0, 2, 4]
    list(filter(lambda n: n % 2 == 0, l))



------------------------------------------------------------------------------------------------------------

The zip function - is not higher order function

zip(*iterables)

[1, 2, 3, 4]            -> (1,10), (2, 20), (3, 30), (4, 40)
[10, 20, 30, 40]

[1, 2, 3, 4, 5]         -> (1,10), (2, 20), (3, 30)
[10, 20, 30]

l1 = range(100)
l2 = 'abcd'

list(zip(l1, l2))       -> [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]


------------------------------------------------------------------------------------------------------------

List Comprehension Alternative to map

l = [2, 3, 4]

def sq(x):
    return x**2         list(map(lambda x: x**2, l)) -> [4, 9, 16]
list(map(sq, l))

results = []
for x in l:
    result.append(x**2)


[x**2 for x in l] -> [4, 9, 16]

[<expressions> for <varname> in <iterable>]

l1 = [1,2,3]
l2 = [10, 20, 30]

list(map(lambda x, y: x+y, l1, l2))

Remember zip(l1, l2) -> [(1, 10), (2, 20), (3, 30)]

[x + y for x, y in zip(l1, l2)]

------------------------------------------------------------------------------------------------------------

l = [1, 2, 3, 4]

list(filter(lambda n: n % 2 == 0, l)) -> [2,4]

[x for x in l if x % 2 == 0]        -> [2,4]

    [<expression1> for <varname> in <iterable> if <expression2>]

------------------------------------------------------------------------------------------------------------

                Combining map and filter

l - range(10)

list(filter(lambda y:y < 25, map(lambda x: x**2, l))) -> [0, 1, 4, 9, 16]

using a list comprehension is much clearer:

    [x**2 for x in range(10) if x**2 < 25]  -> [0, 1, 4, 9, 16]

"""
