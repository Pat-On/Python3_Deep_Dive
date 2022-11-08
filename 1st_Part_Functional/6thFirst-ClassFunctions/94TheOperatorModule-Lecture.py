"""
            THE operator MODULE

        Functional Equivalents to Operators
    
    in the last lecture we wrote code such as:

    l = [2, 3, 4]
    
    reduce(lambda a, b: a * b, l)

    We used a lambda expression to create a functional version of the * operator

    This is something that happens quite often, so the operator module was created

    This module is a convenience module

    You can always use your own functions and lambda expressions instead

------------------------------------------------------------------------------------------


The operator module

Arithmetic Functions

    add(a, b)
    mul(a, b)
    pow(a, b)
    mod(a, b)
    floordiv(a, b)
    neg(a)
        --and many more

        
Comparison and Boolean Operators

    lt(a, b)
    le(a, b)
    gt(a, b)
    ge(a, b)
    eq(a, b)
    ne(a, b)
    is_(a, b)
    is_not(a, b)

    and_(a, b)

Sequence/Mapping Operators
    concat(a1, s2)
    contains(s, val)
    countOf(s, val)
    getitem(s, i)

    mutable objects:
    setitem(s, i, val)
    delitem(s, i)

Item Getters

    the itemgetter function returns a callable


    getitem(s, i)   <- takes two parameters and returns a value: s[i]


        s = [1, 2, 3]
        getitem(s, 1)   -> 2

    itemgetter(i)           <-- this about it as a partial function
                                returns a callable which takes one parameter: a sequence object

            f = itemgetter(1)

            s = [1, 2, 3]
            f(s) -> 2

            s = "python"
            f(s) -> y

----------------------------------------------------------------------------------------------------

Item Getters

    We can pass more than one index to itemgetter:


    l = [1, 2, 3, 4, 5, 6]

    s = "python"

    f = itemgetter(1, 2, 3)

    f(l) -> (2, 4, 5)
    f(s) -> ("y", "h", "o")


----------------------------------------------------------------------------------------------------
Attributes Getters

    The attrgetter function is similar to itemgetter but is used to retrieve object attributes

    it also return a callable, that takes the object as an argument

    suppose my_obj is an object with three properties:

        my_obj.a -> 10
        my_obj.b -> 20
        my_obj.c -> 30

        f = attrgetter('a') <-callable that it is going to look for attribute a

        f(my_obj)   -> 10

        f = attrgetter('a', 'c')    f(my_obj) -> (10, 30)
    
    Can also call directly:
        attrgetter('a', 'b', 'c')(my_obj) -> (10, 20, 30)

----------------------------------------------------------------------------------------------------

    Calling another Callable

        consider the str class that provides the upper() method:

            s = "python"        s.upper()   -> Python

            f = attrgetter('upper')

            f(s) -> return the upper method of s
                    it is callable, and can be called using ()

            f(s)() -> PYTHON

            attrgetter('upper')(s)()    -> PYTHON

        Or, we can use the slightly simpler methodcaller function

            methodcaller('upper')('python') -> PYTHON

        Basically, methodcaller retrieves the named attribute and calls it as well

        It can also handle more arguments











"""
