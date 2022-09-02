"""

    some arithmetic operators do not work the same as floats or integers

    // and % -> also divmod()

    the // and % operators still satisfy the usual equation: 
        n = d * (n // d) + (n % d)

    but for integers, the // operators performs floor division

    for decimals however it performs truncated division

    10 // 3 -> 3 
    Decimal(10) // Decimal(3) -> Decimal(3)

    -10 // 3 -> -4
    Decimal(-10) // Decimal(3) -> Decimal(-3)



Boils down to the algorithm used to actually perform integer division

    a   dividend
    -   --------
    b   divisor


    - figure out the sign of the result
    - use absolute values for divisor and dividend
    - keep subtracting b from a as long as a >= b
    - return the signed number of times this was performed

    10            10 - 3    7 - 3   4 - 3
    --  res is +  = 7       = 4     = 1     1 < 3 STOP      return 3    
     3                  

    -10            10 - 3    7 - 3   4 - 3
    --  res is +  = 7       = 4     = 1     1 < 3 STOP      return -3    
     3     
    
    this is basically the same as truncating the real division

    trunc(10/3) -> 3
    trunc(-10/3) -> -3

    this is still satisfied:  n = d * (n // d) + (n % d)


    n = -135    d = 4




                                Integer                         Decimal
                - 135 // 4      -34                             -33
                -135 % 4        1                               -3
 n = d * (n // d) + (n % d)     -135 = 4 * (-34) + (1)          -135 = 33 * (-33) + (-3)


Other mathematical operations
    - The Decimal class defines a bunch of various mathematical operations,
        such as sqrt, logs, etc
    - But not all functions defined in the math module are defined in the Decimal class

    E.g. trig functions


We can use math module
    but decimal objects will first be cast to floats <-- interesting
    - so we lose the whole precision mechanism that made us use Decimal objects in the first place
    


"""
