"""
        Docstring and Annotations

    Docstring

        we have seen the help(x) function before    ->  returns some documentation (if available) for x

        we can document our functions (and modules, classes etc) to achieve the same result using docstring -> pep 257

        If the first line in the function body is a string (not an assignment, not a comment, just a string by itself), it will be interpreted as a docstring

        example:

            def my_func(a):
                "documentation for my_func"
                return a
        
        Multi-line docstring are achieved using....
                            multi-line strings

        

        ------

        Where are docstrings stored?

            in the function's __doc__ property

            def fact(n):
                '''Calculates n! (factorial function)

                Inputs:
                    n: non-negative integer

                returns
                    the factorial of n
                '''

            fact.__doc__        -> is going to contain entire docstring from the function

            help(fact)          -> is doing the same! + fact(n)

            
        -------

        Function Annotations (this is just meta data)

            Function annotations give us an additional way to document our functions:   -> pep 3107

            def my_func(a: <expression>, b: <expression) -> <expression>:
                pass

            def my_func(a: 'a string', b: 'a positive integer') -> 'a string':
                return a * b

            help(my_func) -> my_func(a: 'a string', b: 'a positive integer') -> 'a string':


            my_func.__doc__ -> empty string

-----------

        Annotations can be any expression
            annotation is evaluated when the compiler executing def. So everything provided there is not going to change during the run program


            def my_func(a: str, b: 'int > 0') -> str:
                return a*b

            def my_func(a: str, b: [1,2,3]) -> str:
                return a*b
        
-----------


            Default values, *args, **kwargs

                can still be used as before

            def my_func(a: str = "xyz', b: int = 1) -> str:
                pass

            def my_func(a: str = 'xyz',
                        *args: 'additional parameters',
                        b: int = 1,
                        **kwargs: 'additional keyword only params') -> str:
                pass

-----------

            Where are annotations stored?

                in the __annotations__ property of the function

                -> dictionary       keys are the parameter names
                                        for a return annotation, the key is return
                
                                    values are the annotations

            def my_func(a: 'info on a', b: int) -> float:
                pass

            my__func.__annotations__
                -> {'a': 'info on a', 'b': int, 'return': float}

-----------
            Where does Python use docstrings and annotations

                it does not really
                mainly used by external tools and modules

                    examples: apps that generate documentation from your code (Sphinx)


                Docstrings and annotations are entirely optional, and do not "force" anything in out PYTHON code

                we will look at an enhanced version of annotations in an upcoming section on TYPE HINTS            
"""
