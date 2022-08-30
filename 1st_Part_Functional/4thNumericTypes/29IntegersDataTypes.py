"""



                Integers 


    the int data type = object
        ex: 0, 10 - 100, 100000000...
        How large can a Python int become (positive or negative)?

        Integers are represented internally using base-2 binary) digits, not decimals


        2^7     2^6     2^5     2^4     2^3     2^2     2^1     2^0   

        128     64      32      16      8       4       2       1


        (10011)2 == (19)10

        Representing the decimal numbers 19 requires 5 bits

        What is the largest (base) integer number that can be represented using 8 bits?
            Lets assume first that we only care about non-negative integers

                answer 255   2^8 - 1

            If we care about handling negative integers as well, then 1 bit is reserved to represent the sing of the numbers
            leaving us with only 7 bits for the number itself out of the original 8 bits

            the largest number we can represent using 7 bits is 2^7 -1 = 127

            so using 8 bis we are able to represent all the integers in the range [-127, 127]

            Since 0 does not require a sign, we can squeze out and extra number,
            and we end up with the range [-128, 127]
                                        [-2^7, 2^7 - 1]

        if we want to use 16 bits to store (signed) integers, our range would be:
            2^(16-1) = 2^15 = 32, 768       Range:[-32,768... 32 767]

        If we had an unsigned integer type, using 32 bits our range would be:
            [0, 2^32] = [0.... 4,294,967,296]


    In a 32-bit OS: 
        memory spaces (bytes) are limited by their address number -> 32 bits
            4,294,967,296 bytes of addressable memory
                4,294,967,296 / 1024 = 4, 194, 304 KB
                4,194,304 / 1024 = 4,096 MB


    So how large an integers can be depends on how many bits are used to store the numbers:

    Some languages (such as Java, C...) provide multiple distinc integer data types that use a fixed number of bits:

        JAVA (consistent across platform)
            byte        signed 8-bit numbers
            short       signed 16-bit number
            int         signed 32-bit numbers
            large       signed 64 bit numbers

                and more...

            You can have many implementation signed and unsigned numbers


    Python does not work this way
        The int object uses a variable numb  er of bits

        Can use 4 bytes, (32 bites) 8 bytes(64 bites) 12 bytes(96 bits) etc         Seamless to us - we do not need to think about it

        [since ints are actually objects, there is a further fixed overhead per integer]

        Theoretically limited only by the amount of memory available

        Of course larger numbers will use more memory
            and standard operators such as +, *, etc will run slower as numbers get larger

            if the integers are larger that 32 bits (os) You will have to process them in few operation

"""
import sys


print(type(100))


print(sys.getsizeof(0), "bytes")

print(sys.getsizeof(1))

print(sys.getsizeof(2**1000))
