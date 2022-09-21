"""
        Complex numbers

    
The complex class                                                   Literals
                                                                        x + yJ              or          x + yj
    Constructor: complex(x, y) x -> real part                                   J -> mean that it is imaginary part
                                y -> imaginary part
            (rectangular coordinates)


    
    example a = complex(1, 2)
            b = 1 + 2j
            a == b -> True

    x and y (the real and imaginary parts) are stored as floats


Some instance properties and methods

    .real               -> return the real part
    .imag               -> returns the imaginary part
    .conjugate()        -> returns the complex conjugate

    d = 2 - 3j
    d.real -> 2
    d.imag -> -3
    d.conjugate()   -> 2 + 3j



Arithmetic Operators
    The standard arithmetic operators (+, -, /, *, **) work as expected with complex numbers

        (1 + 2j) + (3 + 4j) -> 4 + 6j
        (1 + 2j) * (3 + 4j) -> 5 + 10j

    Real and Complex numbers can be mixed:
        (1 + 2j) + 3 -> 4 + 2j
        (1 + 2j) * 3 -> 3 + 6j

    // and % operators are not supported

Other operations
    the == and != operators are supported

    comparison operators such a <, >, <= and >= are not supported

    Functions in the math module will not work

    Use the cmath module <=== complex equivalent of math module
        - exponential
        - logs
        - trigs and inverse trigs
        - hyperbolics and inverse hyperbolics
        - polar / rectangular conversions
        - isclose



Rectangular to Polar

    import cmath

    cmath.phase(x)


"""
