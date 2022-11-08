"""

                Global And Local Scopes

        When an object is asigned to a variabled 
        that variable points to some object
        and we say that the variable (name) is bound to that object

    
    That object can be accessed using that name in various parts of our code

    But not just anywhere!

    That variable name and it's binding (name and object) only "exist" in specific parts of our code

        the portion of code where that name/binding is defined is called the LEXICAL SCOPE of variable

        these bindings are stored in namespaces <- table with reference

        (each scope has its own namespace)


--------------------------------------------------------------------------------------------------

The Global Scope

    The global scope is essentially the module scope

    It spans a single file only

    There is no concept of a truly global (across all the modules in our entire app) scope in Python

    The only exception to this are some of the built-in globally available objects, such as:
        True    False   None    dict    print

    The built-in and global variables can be used anywhere inside our module
        including any function

--------------------------------------------------------------------------------------------------
Global Scope are nested inside the built-in scope

    Build space-------------------------------------------
    |
    |                   Name Space                                  Name Space
    |   Module scope 1                                              var1 0xA345E
    |   with name space                                             func1 0xFF34A
    |                           Module Scope2   
                                with name space

    If you reference a variable name inside a scope and Python does not find it in that scope's namespace

    It will look for it in an enclosing scope's namespace


-------------------------------------------------------------------------------------------------

The Local Scope

    When we create functions, we can create variables names inside those functions (using assignments)
        eg a = 10

    variables defined inside a function are not created until the function is called

    every time the function is called, a new scope is created
        Variables defined inside the function are assigned to that scope
                -> Function Local scope
                -> Local scope

        The actual object the variable references could be different
        each time the function is called

        (that is why recursion works)


-------------------------------------------------------------------------------------------------
Nested Scopes

    Scopes are often nested

            Built-in Scope
                Module Scope
                    Local Scope <- example function

    Namespace lookups

        When requesting the object bound to a variable name

        Python will try to find the object bound to the variable
            - in current local scope first
            - works up the chain of enclosing scopes


-------------------------------------------------------------------------------------------------
Accessing the global scope from a local scope

    when retrieving the value of a global variable from inside a function, PYthon automatically
    searches the local scope's namespace, and up the chain of all enclosing scope namespaces

        - local -> global -> built-in

    What about modifying a global variables from inside the function?

        a = 0
        def my_func():
            a = 100         <- assignment -> Python interprets this as a local variable (at compile-time)
            print(a)                        -> the local variable a masks the global variable a

        
-------------------------------------------------------------------------------------------------

    The global keyword

        we can tell python that a variable is meant to be scoped in the global scope
        by using the global keyword

        a = 0
        def my_func():
            global a
            a = 100 <- forcing python that it is in global scope so overwriting our a in global scope

-------------------------------------------------------------------------------------------------
    Global and Local Scoping

    When Python encounters a function definition at compile-time
        it will scan for any labels (variables) that have values assigned to them (anywhere in the function)
            If the label has not been specified as global, then it will be local

        variables that are referenced but not assigned a value anywhere in the function will not be local,
        and Python will, at run-time, look for them in enclosing scopes


def func4():
    print(a)
    a = 100 <- assignment at compile time -> a local -> namespace!

        -> when we call func4() print(a) result in a run-time error

        because a is local and we are referencing it before we have assigned a value to it. 

        


"""
