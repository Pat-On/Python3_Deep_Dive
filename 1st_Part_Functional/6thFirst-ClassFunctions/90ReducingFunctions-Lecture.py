"""

            Reducing Functions


    These are functions that recombine an iterable recursively, ending up with a single return value
    
    Also called accumulators, aggregators or folding functions. 

    Example: Finding the maximum value in an iterable

    a0, a1, a2, ..., an-1

    max (a,b) -> maximum of a and b

    result = a0

    result = max(result, a1)
    and so on for every element
    till we find it



    l = [5, 8, 6, 10, 9]

    max_value = lambda a, b: a if a > b else b

    def max_sequence(sequence):
        result = sequence[0]
        for e in sequence[1:]:
            result = max_value(result, e)
        return result

    
    def _reduce(fn, sequence):              <- NICE
    result = sequence[0]
    for e in sequence[1:]:
        result = fn(result, x)
    return result

    _reduce(lambda a, b: a if a > b else b, l) -> maximum


    -----------------------------------------------------------------------------------------------------------------------------------------------------------------

    add = lambda a, b: a+b

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                the functools module

                        You can use any type of iterable

        from functools import reduce

        l = [5, 8, 6, 10, 9]

        reduce(lambda a,b: a if a > b else b, l)

--------------------------------------------------------------------------------------------------------------

Built-in Reducing Functions

    Python provides several common reducing functions:

    min                 min([1, 2, 3, 4, 5])
    max                 max([1,2,3,4,5])
    sum                 sum([1, 2, 3, 4, 5])

    any                 any(l) -> Tru if any element in l is truthy
                            False otherwise

    all                 all(l) -> True if every element in l is truthy
                            False otherwise

Using reduce to reproduce any

    l = [0, "", None, 100]

    result = bool(0) or (bool('') or bool(None) or bool(100) 
                f           f           f           t

    Here we just need to repeatedly apply the or operator to the truth values of each element


--------------------------------------------------------------------------------------------------------------

Calculating the product of all elements in an iterable

    No built-in method to do this

    But very similar to how we added all the elements in an iterable or sequence

    [1, 3, 5, 6] -> 1 * 3 * 5 * 6

    reduce(lambda a, b: a * b, l)


    reduce(lambda a, b: a * b, range(1, 5+1))       -> 5!

--------------------------------------------------------------------------------------------------------------
The reduce initializer

    The reduce function has a third (optional) parameter: initializer (default to None)

    If it is specified, it is essentially like adding it to the front of the iterable.

    It is often used to provide some kind of default case the iterable is empty

    l = []
    reduce(lambda x, y: x+y, l)     -> exception, because array is empty

    reduce(lambda x, y: x+y, l, 1)  -> 1

    l = [1, 2, 3]
    reduce(lambda x, y: x+y, l, 1 ) -> 7

    l = [1, 2, 3]
    reduce(lambda x, y: x+y, l, 100 ) -> 106


BEST option is to use 0

    

"""
