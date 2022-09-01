"""

                Floats
            Internal Representation

The float class is Python's default implementation for representing real numbers

The python (CPython) float is implemented using the C double type which (usually!)
Implements the IEEE 754 double-precision binary floats, also called binary64

The float uses a fixed number of bytes
            -> 8 bytes (but python objects have some overhead too) because of the object we use 24 bytes
            -> 64 bits  -> 24bytes (CPython 3.6 64-bit)

These 64 bits are used up as follows:

    sign                -> 1 bit
    exponent            -> 1 bits -> range[-1022 - 1023]        1.5E-5 -> 1.5 x 10^-5
    significant digit   -> 52 bits  -> 15-17 significant (base-10) digits

significant digits -> for simplicity, all digits except leading and trailing zeros

1.2345 -> 5 significant digits
1234.5 -> 5 significant digits
1234500000000 -> 5 significant digits
0.0000012345  -> 5 significant digits
12345e-50      -> 5 significant digits


Representation: Decimal

    - number can be represented as base-10 integers and fractions:

        0.75 -> 3/10 + 5/100 -> 7 x 10^-1 + 5 x 10-2        2 significant digits
                                                            2 fractions
        0.256  -> 2/10 + 5/100 + 6/1000 -> 2 x 10^-1 + 5 x 10^-2 + 6 x 10^-3
                                                            3 significant digits
                                                            3 fractions

        11.4     -> 1x10 + 1 + 4/10 -> 1x 10^1 + 1 x 10^0 + 4 x 10^-1 



Some numbers cannot be represented using a finite number of terms

    - Pi  
    - square of 2

but even some rational numbers can not be represented
    - 1/3    0.3333


Representation: binary

    number is a computer are represented using bits, not decimal digits
        -> instead of powers of 10 we need to use powers of 2
        (0.11)      =   (1/2 + 1/4)     = (0.5 + 0.24)
              2     =              10   =             10
                    = (1 x 2^-1 + 1 x 2^-2)
                                            10


The same problem that occurs when trying to represent 1/3 using a decimal expansion
also happens when trying to represent certain numbers using a binary expresion

0.1 = 1/10 using binary fraction, this number does not have a finite representation


so, some numbers that do have a finite decimal representation, 
do not have a finite binary representation,
and some do

(0.75)      =   (0.11)          finite -> exact float representation
     10               2


(0.1)    = (0 0011 0011 0011 ..)        infinite -> approximate float representation (all programing languages)
    10                          2


    


"""
