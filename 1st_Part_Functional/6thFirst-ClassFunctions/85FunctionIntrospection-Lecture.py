"""

                Function Introspection

            Analyzing function by using code.


Functions are first-class objects
    they have attributes
        methods properties
        __doc__  __annotations__

    We can attach our own attributes:


    def my_func(a, b):
        return a + b

    my_func.category = "math"
    my_func.sub_category = 'arithmetic'


The dir() function

    dir() is a built-in function that, given an object as an argument, will return a list of valid attributes for the object

    dir(my_func)


Function Attributes: __name__, __defaults__, __kwdefaults__

__name__ -> name of function

__defaults__ -> tuple containing positional parameter defaults

__kwdefaults__ -> dictionary containing kewyord-only parameter defaults

def my_func(a, b=2, c=3, *, kw1, kw2=2):
    pass

my_func.__name__ -> my_func
my_func.__defaults__ -> (2,3)
my_func.__kwdefaults__ -> {'kw2': 2}





function attribute: __code__

def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b



This __code__object itself has various properties, which include:


co_varnames parameter and local variables

            my_func.__code__.co_varnames    -> ("a", "b", "args", "kwargs", "i")

            parameter names first, followed by local variable name

co_argcount number of parameters 

            my_func.__code__.co_argcount    -> 2
            does not count *args and **kwargs!!

------------------------------------------------------------------------------------------------

The inspect Module

import inspect

ismethod(obj)   isfunction(obj) isroutine(obj)  and many others..

- isroutine() -> returns true for both

- what is the difference between a function and a method

    Classes and objects have attributes - an object that is bound (to the class or the object)
    an attribute that is callable is called a method


------------------------------------------------------------------------------------------------

Code Introspection

We can recover the source code of our functions/methods

inspect.getsource(my_func) ->   A string containing our entire def statement, including annotations, docstrings etc

We can find out in which module our function was created

inspect.getmodule(my_func) -> <module '__main__'>

inspect.getmodule(print) -> <module 'builtins' (built-ins)>

inspect.getmodule(math.sin) -> <module 'math' (built-ins) >


------------------------------------------------------------------------------------------------

Function Comments

# setting up variable
i = 10
# TODO: Implement function
# some additional notes
def my_func(a, b=1):
    # comment inside my_func
    pass

inspect.getcomments(my_func)

        ->  '# TODO: Implement function \n # some additional notes'

------------------------------------------------------------------------------------------------

Callable Signatures

inspect.signature(my_func) -> Signature instance

Contains an attribute called parameters

Essentially a dictionary of parameters names (keys), and metadata about the parameters (values)
    keys -> parameter name
    values -> object with attributes such as name, default, annotation, kind

kind POSITIONAL_OR_KEYWORD
        VAR_POSITIONAL
        KEYWORD_ONLY
        VAR_KEYWORD
        POSITIONAL_ONLY         <- WE DO NOT HAVE WAY TO MAKE THEM IN PYTHON BY OURSELF INTERESTING!
                                        INTERNALLY DONE BY PYTHON MORE IN NEXT LECTURE

------------------------------------------------------------------------------------------------
Callable Signatures:"

def my_func(a: 'a string',
            b: int = 1,
            *args: 'additional positional args',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg',
            **kwargs: 'additional keyword-only args') -> str:
    ''' does something
        or other'''
    pass


    for param in inspect.signature(my_func).parameters.values():
        print("name:", param.name)
        print("Default", param.default)
        print("Annotation", param.annotation)
        print("Kind", param.kind)






    




"""
