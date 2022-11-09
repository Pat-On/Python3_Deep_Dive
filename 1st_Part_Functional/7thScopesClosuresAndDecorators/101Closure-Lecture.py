"""
            Closures


        Free Variables and Closures

    Remember: Function defined inside another function can access the outer (nonlocal) variables

    def outer():
        x = "python"

        def inner():
            print("{0} rocks!".format(x))       <- this x refers to the one in outer's space
                                                      this nonlocal variable x is called a free variable
        inner()                                  When we consider inner, we really are looking at:
    outer()                                             the function inner
                                                        the free variable x (with current value python)


----------------------------------------------------------------------------------------------------------------------------------

Returning the inner function 

    what happens if, instead of calling (running) inner from inside outer we return it?

    def outer():                                                                        
        x = "python"                                x is a free variable in inner                                        
                                                    it is bound to the variable x in outer
        def inner():                                this happens when outer runs                                          
            print("{0} rock".format(x))                         (i.e. when inner is created)                            
                                                            this the closure
        return inner                                                                        

                                            when we return inner, we are actually returning the closure

    We can assign that return value to a variable: fn = outer()

    fn() -> python rocks!

    When we called fn
    at that time Python determined the value of x in the extended scope

    But notice that outer had finished running before we called fn - it is scope was gone

----------------------------------------------------------------------------------------------------------------------------------

                                        Python Cells and Multi-Scoped Variables


    def outer():
        x = "python"
        def inner():
            print(x)
        return inner

    here the value of x is shared between two scopes:
        outer 
        closure
    the label x is in two different scopes but always reference the same value

    Python does this by creating a cell as an intermediary object


            outer.x         ->      cell 0xA500              ->      str 0xFF100        (indirect reference)
                            /           0xFF100                             Python
            inner.x      ---

                            cell is intermediary


    in effect, both variables x (in outer and inner), point to the same cell

    When requesting the value of the variable, Python will "double-hop" to get the final value


----------------------------------------------------------------------------------------------------------------------------------
                            Closures

    You can think of the closure as a function plus an extended scope that contains the free variables

    The free variable's value is the object the cell points to - so that could chan ce over time!

    Every time the function in the closure is called and the free variable is referenced:
        Python looks up the cell object, and then whatever the cell is pointing to:

    def outer():
        a = 100 #local variable

        x = "python" # free variable

        def inner():
            a = 10 #local variable
            print("{0} rocks!".format(x))
        
        return inner

    fn = outer()        -> fn -> inner      + extended scope x

----------------------------------------------------------------------------------------------------------------------------------
                                Inspection

    def outer():                           outer.x         ->      cell 0xA500              ->      str 0xFF100        (indirect reference)         
        a = 100                                            /           0xFF100                             Python     
        x = "python"                       inner.x      ---             

        def inner():
            a = 10
            print("{0} rocks!".format(x))
        return inner

    fn = outer()

    fn.__code__.co_freevars -> ('x', )  (a is not a free variables) 

    fn.__closure__          -> (<cell at 0xA500: str object at 0xFF100>, )

-------------------------

        def outer():                            
        a = 100                          
        x = "python"                        (it is abstracted)
        print(hex(id(x)))           -> 0xFF100 indirect reference            

        def inner():
            a = 10
            print(hex(id(x)))        -> 0xFF100 indirect reference   
            print("{0} rocks!".format(x))
        return inner

----------------------------------------------------------------------------------------------------------------------------------
                                Modifying free variables


def counter():
    count = 0       <- count is a free variables. it is bound to the cell count

    def inc():
        nonlocal count
        count += 1
        return count
    
    return inc

fn = counter()

fn()    -> 1 count's(indirect) reference changed from the object 0 to the object 1


----------------------------------------------------------------------------------------------------------------------------------
                Multiple instances of Closures

    Every time we run a function, a new scope is created

    if that function generates a closure, a new closure is created every time as well


def counter():
    count = 0       

    def inc():
        nonlocal count
        count += 1
        return count
    
    return inc

f1 = counter()      (two different separated closures) -> the cells are different
f2 = counter()

----------------------------------------------------------------------------------------------------------------------------------
    Shared Extended Scope

def counter():
    count = 0       

    def inc1():
        nonlocal count
        count += 1
        return count
    
    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2

f1, f2 = outer()

f1() -> 1
f2() -> 2


----------------------------------------------------------------------------------------------------------------------------------
    Shared Extended Scope

You may this this shared extended scope is highly unusual.. but it is not


def adder(n):
    def inner(x):
        return x + n
    
    return inner

add_1 = adder(1)
add_2 = adder(2)        Three different closures - no shared scopes
add_3 = adder(3)

add_1(10)   -> 11
add_2(10)   -> 12
add_3(10)   -> 13


But suppose we tried doing it this way:

    adders = []
    for n in range(1,4):            <--- shared cell
        adders.append(lambda x: x + n)

n = 1 : the free variable in the lambda is n, and it is bound to the n we created in the loop
n = 2 : it is bound to the same n
n = 3 : it is bound to the same n

Now we could call the adders in the following

adders[0](10)   -> 13
adders[1](10)   -> 13
adders[2](10)   -> 13


Remember, Python does not evaluate the free variable n until the address[i] function is called

Since all three functions in adders are bound to the same n
    by the time we call adders[0], the value of n is 3
        (the last iteration of the loop set n to 3)

----------------------------------------------------------------------------------------------------------------------------------

    Nested Closures

def incrementer(n):

    # inner + n is a closure
    def inner(start):
        current = start

        # inc + current + n is a closure
        def inc():
            nonlocal current
            current += n
            return current
        
        return inc
    return inner

(inner)
fn = incrementer(2) -> fn.__code__.co_freevars -> 'n' n=2

(inc)
inc_2 = fn(100) -> inc2.__code__.co_freevars -> 'current', 'n' | current=100 n=2

(callls inc)
inc_2() -> 102
inc_2() -> 104



"""
