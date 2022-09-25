"""

            Unpacking Iterable


        A Side Note on Tuples

        (1, 2, 3)

        what defines a tuple in Python is not (), but, 

        1, 2, 3 is also a tuple -> (1, 2, 3)        The () are used to make the tuple clearer


        to create a tuple with a single element:

        (1) <--- wrong, it is just integer
        (1,) <---- correct
        1, <---- correct


        The only exception is when creating an empty tuple: () or tuple()


------------------------------------------------------------------------------------------
                Packed Values

    Packed values refers to values that are bundled together in some way


    Tuples and lists are obvious            t = (1,2,3)
                                            l = [1,2,3]

    Even a string is considered to be a packed value: s = "Python"

    Sets and dictionaries are also packed values:       set1 = {1, 2, 3}

    In fact, any iterable can be considered a packed value


------------------------------------------------------------------------------------------

                Unpacking Packed Values

    Unpacking is the act of splitting packed values into individual variables contained in a list or tuple


        a, b, c, = [1, 2, 3]            -> 3 elements in [1,2,3] -> need 3 variables to unpack

    left side
    this is actually a tuple of 3 variables: a, b and c

    a -> 1 b -> 2 c ->3

    The unpacking into individual variables is based on the relative positions of each elements

    Does this remind you of how positional arguments were assigned to parameters in functions?



            Unpacking other iterables

    a, b, c = 10, 20, "hello"
                    right side - this is actually a tuple containing 3 variables



    in fact, unpacking works with any iterable type


------------------------------------------------------------------------------------------
            Simple Application of Unpacking

    Swapping values of two variables  a = 10        b = 10
                                    b = 20  ->      a = 20


    "Traditional approach"

            tmp = a
            a = b
            b = tmp

    using unpacking

            a, b = b, a

    this works because in Python the entire RHS is evaluated first and completely

    then assignments are made to the lhs


------------------------------------------------------------------------------------------
            Unpacking Sets and Dictionaries

    d = {"K1": 1, "k2":2, "k3":3}

    for e in d  -> e iterated through the keys:K1, K2, K3

    so when unpacking d we are actually unpacking the keys of d

    a, b, c = d     -> a = "key1", b = "key2", c="key3"
                            or
                    -> a = "key2", b = "key1", c="key3"

        Dictionaries and Sets are unordered types
        They can be iterated, but there is no guarantee the order of the results will match


        SETS ARE WORKING IN THE SAME WAY
    
"""


tuples = 1, 2, 3

print(type(tuples))


a, b, c = 10, 20, "hello"

print(a, type(a))
