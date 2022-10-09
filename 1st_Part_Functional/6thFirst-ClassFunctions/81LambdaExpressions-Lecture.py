"""
                Lambda Expressions


        What are Lambda Expressions?

    We already know how to create f unctions using the def statement

    Lambda expressions are s imply another way to create f unctions (annonymous functions)


    lambda [parameter list]: expression

            lambda <- keyword
            [parameter list] <- parameter list (optional)
            the : <- is required even for zero arguments

            expression <- this expression is evaluated and returned when the lambda function is called (this of it as the body of the function)

            THE EXPRESSION RETURNS A FUNCTION OBJECT
                that evaluates and return the expression when it is called

        it can be assigned to a variables
            passed as an argument to another function

        it is a function, just like one created with def

    

    -------


        example:

        lambda x: x**2

        lambda x, y: x + y

        lambda: "hello"

        lambda s: s[::-1].upper()

        type(lambda x: x**2)        -> function

        note that these expression are function objects but are not 'named'
            -> anonymous functions

        Lambdas, or anonymous functions are not equivalent to closures <- basics ^^ 


        -----


        Assign a Lambda to a Variable Name

            my_func = lambda x: x**2
            type(my_func) -> function
            my_func(3) -> 9
            my_func(4) -> 16


            identical to:
                def my_func(x):
                    return x**2

        passing as an argument to another function

        def apply_func(x, fn):
            return fn(x)

        
        apply_func(3, lambda x: x**2)           -> 9

        apply_func(2, lambda x: x + 5)          -> 7


-------------

                LIMITATIONS

        the "body" of a lambda is limited to a single expression

        no assignments      lambda x: x = 5 <-wrong!

        no annotations      lambda x:int : x*2 <- wrong!

        single logical line of code!    -> line-continuation is ok but still just one expression

                    lambda x: x * \
                        math.sin(x)

        





        



"""
