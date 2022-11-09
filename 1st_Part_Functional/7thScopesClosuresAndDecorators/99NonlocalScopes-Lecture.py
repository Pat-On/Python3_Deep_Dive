"""

            NONLOCAL SCOPE


Inner Functions
    Functions within other function


    def outer_func():
        # some code
        def inner_function():
            # some code

        inner_func()

    outer_func()

    Both functions have access to the global and built-in scopes as well as their respective local scopes

    But the inner function also has access to its enclosing scopes - the scope of the outer function

    That scope is neither local (to inner_func) nor global - it is called a nonlocal scope


----------------------------------------------------------------------------------------------------------------

Referencing variables from the enclosing scope

    Considering this example we have seen before:

        module1.py

        a = 10

        def outer_func():
            print(a)

        outer_func()

----------------------------------------------------------------------------------------------------------------
Modifying global variables

We saw how to use the global keyword in order to modify a global variable within a nested scope

a = 10

def outer_func1():
    global a            <- we can of course do the same thing from within a nested function
    a = 100

outer_func1()
print(a)

----------------------------------------------------------------------------------------------------------------
Modifying nonlocal variables

    When inner_func is compiled, Python sees an assignment to x
    So it determines that x is a local variable to inner_func
    The variable x in inner_func masks the variable x in outer_func


    Just as with global variables, we have to explicitly tell Python we are modifying a nonlocal variable

    We can do that using the nonlocal keyword

    def outer_func():
        x = "hello"

        def inner_func():
            nonlocal x
            x = "python"

        inner_func()

        print(x)

    outer_func()


----------------------------------------------------------------------------------------------------------------
Nonlocal Variables

    Whenever Python is told that a variable is nonlocal
        It will look for it in the enclosing local scopes chain until it first encounters the specified variable name

        Beware: it will only look in local scopes, it will not look in the global scope
       

"""
