"""
                Positional Arguments

    Most common way of assigning arguments to parameters: via the order in which they are passed
    i.e. their position

    def my_func(a, b):
        - some code


    my_func(10, 20) -> a = 10 b = 20

    my_func(20, 10) -> a = 20 b = 10


    Default Values

    A positional arguments can be made optional by specifying a default value for the corresponding parameter
    def my_func(a, b=100):
        - some code


    my_func(10) -> a = 10 b = 100

    my_func(10, 20) -> a = 10 b = 20



    Consider a case where we have three arguments, and we want to make one of them optional:
    Wrong example:
        def my_func(a, b=100, c)

        How would we call this function without specifying a value for the second parameter?
            my_func(5, 15) <-- wrong

    If a positional parameter is defined with a default value
        EVERY positional parameter after it
            MUST also be given a default value


    Correct Example:
        def my_func(a, b = 5, c=10):
            some code

    my_func(1) -> a = 1, b=5, c=10



    But what if we want to specify the 1st and the 3rd arguments but omit the 2nd argument?

    i.e. we want to specify values for a and c, but let b take on its default value?

    -> keyword arguments (named arguments)


    my_func(a=1, c=2) -> a=1, b=5, c=2





    Keyword Arguments


    Positional arguments can, optionally, be specified by using the parameter name
        whether or not the parameters have default values

def my_func(a, b , c):
    - do something


my_func(1,2,3)

my_func(1, 2, c=3)


but one you use a named argument, all arguments thereafter must be named too:

my_func(c=1, 2, 3)  <---- wrong
my_func(1, b=2, 3)  <---- wrong


Keyword Arguments
    All arguments after the first named (keyword) argument, must be named too
    Default arguments may still be omitted

    def my_func(a, b=2, c=3):
        - do something

    my_func(1) -> a=1, b=2, c=3


"""
