"""

                Variable Equality

We can think of variable equality in two fundamental ways


    Memory Address                  Object State (data)

        is                                  ==

    identity operator               equality operator

    var_1 is var_2                  var_1 == var_2



Negation:

        is not                              !=

    var_1 is not var_2                  var_1 != var_2
    not(var_1 is var_2)                 not(var_1 is var_2) 



a = 10          a is b ---> True
b = a           a == b ---> true

a = "hello"
b = "hello"

a is b --> True (but as we will see later do not count on it)
a == b --> True


a = [1, 2, 3]
b = [1, 2, 3]
a is b ---> false
a == b ---> true


a = 10          a is b ---> False
b = 10.0        a == b ---> True (even if it is not the same data type)





The None object

    The None object can be assigned to variables to indicate that they are not set
    (in the way we would expect them to be), i.e. an 'empty' value (or null pointer)


    But the None object is a real object that is managed by the Python memory manager

    Furthermore, the memory manager will always use a shared reference when assigning a variable to None

    a = None
    b = None            The same memory address 0x1000
    c = None    

So we can test if a variable is "not set" or "empty" by comparing it's memory 
address to the memory address of None using the is operator

    a is None   ----> True  

    x is None   ----> False
    X is not None ----> True
"""
