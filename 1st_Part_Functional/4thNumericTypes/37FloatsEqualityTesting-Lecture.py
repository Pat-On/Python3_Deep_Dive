"""

            Floats
        Equality Testing


was showed that some decimal numbers (with a finite representation) 
cannot be represented with a finite binary representation

this can lead to some "weirdness" and bugs in our core (but nt a python bug

it exists in other languages too

    x = 0.1 + 0.1 + 0.1
    y = 0.3

    x == y  -> false

Using rounding will not necessarily solve the problem either

it is no more possible to exactly represent round(0.1, 1) than 0.1 itself

    round(0.1, 1) + round(0.1, 1) + round(0.1, 1) === round(0.3, 1) -> False

but it can be used to round the entirety of both sides of the equality comparison

    round(0.1 + 0.1 + 0.1, 5) == round(0.3, 5) -> True  

------------

    To test for equality of two different floats, you could do the following methods:
        - round both sides of the equality expression to the number of significant digits
            round(a, 5) == round(b, 5)
        - or more generally use an appropriate range(E) within which two numbers are deemed equal
            for some e > 0          (e - epsilon :> not correct symbol)

            a = b if and only if |a - b| < e  (approximately equal)

            example

            def is_equal(x, y, eps):
                return math.fabs(x - y) < eps           fabs(floating point absolute value)

    this can be tweaked by specifying that the difference between the two numbers
    be a percentage of their size -> the smaller the number, the smaller the tolerance
        i.e. are two numbers within x% of each other?

    but there are not-trivial issues with using these seemingly simple tests
        - numbers very close to zero vs away from zero

    
    Using absolute tolerances...

    x = 0.1 + 0.1 + 0.1
    y = 0.3

    there is difference between them only after 17th digit after decimal so:
                                                    0.000000000000000005551

    a - 10000.1 + 10000.1 + 10000.1
    b = 30000.3

    difference between them is 12th digit after decimal pt
                                                    0.000000000000363797881


    using an absolute tolerance: abs_tol = 10^-15 = 0.0000000000000001

    then:
        math.fabs(x - y) < abs_tol   <--- true

        math.fabs(a - b) < abs_tol   <--- false


Maybe We should use relative tolerances....

    x = 0.1 + 0.1 + 0.1
    y = 0.3                                 tol = 0.00000300000000

    a - 10000.1 + 10000.1 + 10000.1
    b = 30000.3                             tol = 0.30000300000000

    Using a relative tolerance: rel_tol = 0.001% = 0.00001 = 1e-5
    i.e. maximum allowed difference between the two numbers
        relative to the larger magnitude of the two numbers


    tol = rel_tol * max(|x|, |y|)

    math.fabs(x - y) < tol -> True

    math.fabs(a - b) < tol -> True

        Success, but it is really?



    x = 0.0000000001 (1e-10)
    y = 0

    using a relative tolerance: rel_tol = 0.1%= 0.0001 = 1e-3

    tol = rel_tol * max(|x|,|y|) -> tol = rel_tol * |x| => 1e-3 * 1e-10 = 1e-13

    math.fabs(x - y) < abc_tool -> False

            it happens because this number are close to zero 
            so tolerance is always going to be greater than actual difference between these two numbers


    Using a relative tolerance technique does not work well for numbers close to zero!

    So using absolute and relative tolerances, in isolation, makes it
    difficult to get a one-size-fits-all solution

    We can combine both methods
        - calculating the absolute and relative tolerances
        - and using the lager of the two tolerances

        tol = max(rel_tol * max(|x|,|y|, abs_tool))    

                relative                absolute


    read more 
    ->PEP 485

    -------------------------------------------------------------------------------------------
    The math module has that solution for us!

    math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

    ! If you do not specify abs_tol, then it defaults to 0 and you will face the problem we 
    encountered in the last slide when comparing numbers close to zero



    x = 0.0000001
    y = 0.0000002                                 
            math.isclose(x, y) -> false    
                        Because abs_tol is equal to zero - always specify it, 

    a = 10000.0000001 
    b = 30000.0000002            
            math.isclose(a, b) -> true                


        but

    math.isclose(x, y, abs_tol=1e-5) -> True
    math.isclose(a, b, abs_tol=1e-5) -> True


        also work in situation like this:

    x = 1000.01
    y = 1000.02
    math.isclose(x, y, abs_tol=1e-5) -> True

    a = 0.01
    b = 0.02
    math.isclose(a, b, abs_tol=1e-5) -> False
    
    X, Y are relatively close to each other where
    a and b are relatively not close to each other <- work nicely! 

"""
