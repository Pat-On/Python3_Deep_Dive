"""

                Integers - operations


    integers suppport all the standars arithemtic operations

        addition        +
        subtraction     -
        multiplication  *
        division        /
        exponents       **


    But what is the resulting type of each operation?

        int+int = int
        int - int = int
        int * int = int
        int ** int = int

        int / int => float  
                            obviously 3/4 => 0.75 (float)
                            but, also   10/2 => 5 (float)


        Two more operators in integer arithmetic

        first we revisit long integer division

                                                155   numerator
                                                ----
                                                4     denominator


                            155 / 4 = 38 with remainder 3


                            put another way: 
                        
                            4 * 38 + 3 = 155


        155 // 4 = 38
        155 % 4 = 3
                        so 155 = 4 * (155 //4) + (155 % 4)
                            4       * 38        + 3

        // is called floor division (div)
        % is called modulo operator(mod)


        and they always satisfy equation n=d*(n//d)+(n%d)


        What is floor division exactly?
            - First define the floor of a (real) number
                the floor of a real number a is the largest (in the standard number order) integer <= a
            floor(3.14) -> 3
            floor(1.9999) -> 1
            floor(2) ---> 2


        But watch out for negative numbers!
            floor(-3,1) => -4

        So, floor is not quite the same as truncation!


        a // b = floor(a/b)

-------------- Positive numbers


    a = b * (a //b ) + a % b

    a = 135
    b = 4           135 / 4 = 33.75 (33 3/4)

    135 // 4 -> 33
    135 % 4 -> 3

    and in fact: a = b*(a//b)+a%b

    4 * (135 // 4) + (135 % 4) = 135

-------------- Negative numbers


    Be careful, a//b, is not the integer portion of a/b, it is the floor of a/b

    For a > 0 and b > 0 these are indeed the same thing

    but beware when dealing with negative numbers!

    a = -135
                -135 / 4 = -33.75 (-33 3/4)
    b = 4

    -135 // 4 -> -34           Before 135 // 4 -> 33
    -135 % 4 -> 1              Before 135 % 4 -> 3

    and in fact:
        a = b * (a // b) + a % 5

        a * (-135 // 4) + (-135 % 4)
        4 * -34 + 1
        -135 + 1
        = -135

"""
import math

print(type(1+1))
print(type(2 * 3))

print(type(2 / 3))

print(type(3 / 3))


print(math.floor(3.15))
print(type(math.floor(3.15)))

print(math.floor(-3.000001))  # -4

# low precision 1 was dropped so we got -3
print(math.floor(-3.00000000000000000000001))


a = -33
b = 16

print(a/b)
print(a//b)
# -3
print(math.floor(a/b))
# truncation is providing us only with integer dropping remaining float
# it can not be considered the same with floor
# -2
print(math.trunc(a/b))


a = -13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a % b))
print(a == b * (a//b) + a % b)


a = 13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a % b))
print(a == b * (a//b) + a % b)


a = -13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a % b))
print(a == b * (a//b) + a % b)
