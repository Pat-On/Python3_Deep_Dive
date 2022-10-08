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

            help(fact)          -> is doing the same!

            
        -------

        Function Annotations

            Function annotations give us an additional way to document our functions:
                (4:16)


"""
