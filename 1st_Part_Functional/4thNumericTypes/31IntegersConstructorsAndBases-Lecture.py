"""
            An integer number is an object - an instance of the int class

            the int class provides multiple constructors

                a = int (10)
                a = int(-10)

            Other (numerical) data type are also supported in  the argument of the int constructor:

                a = int(10.9)    // we will lose some information -> 10 (truncations)
                a = int(-10.9)  --> -10

                a = int(True)   a --> 1
                b = int(False)  b --> 0

                a int(Decimal("10.9)) -> truncation a -> 10


            as well as strings (that can be parsed to a number):
                a = int("10")       a -> 10

            

            number base
                int("123")  -> (123) base 10

            When used with a string, constructor has an optional second parameter: base
                2<= base <= 36

            If base is not specified the default is base 10 - as in the example above

                int('1010', 2) ---> 10 base 10
                int(1010", base=2)

                int('a12f' base=16) -> (41263)10

                int('B", base=11)  -> ValueError: invalid literal for int() with base 11: 'B'


            
---------------------------------------------------------------------------------------------
    Reverse Process: changing an integer from base 10 to another base:


        built-in functions          bin()  bin(10) -> '0b1010'      ob -> documentation
                                    oct()  oct(10) -> '0o12         0o -> doc
                                    hex()  hex(10) -> '0xa'         0x -> doc

        The prefixes in the strings help document the base of the number: int('0xA', 16) -> 10 base 10

        These prefixes are consistent with literal integers using a base prefix (no strings attached!)

            a = 0b1010      <-- python will got it
                                (a -> 10)
            a = 0o12        a -> 10

            a = 0oA         a -> 10


    What about other bases?
            We need custom code!

    
    Base Change Algorithm

        n = base-10 number (>=10) b = base (>=2)

        if b < 2 or n < 0: raise exception

        if n === 0: return [0]

        digits = []                                                 n = 232
        while n > 0:                                                b = 5           return digits [1,4,1,2]
            m = n % b                                           
            n = n // b                                              n = 1485
            digits.insert(0, m)                                     b = 16              returns digits [5, 12, 13]


    This algorithm returns a list of the digits in the specified base eb ( a representation of n base 10 in base b)

    usually we want to return an encoded number where digits higher than 9 use such as A-Z

    We simply need to decide what character to use for the various digits in the base


    Encoding 
        Typically, we use 0-9 and A-Z for digits required in bases higher than 10

        But we do not have to use letters or even standard 0-9 digits to encode our number
            We just need to map between the digits in our number, to a character of our choice

            0 -> 0
            9 -> 9
            10 -> a
            36 -> Z

        or
            0 -> 0
            10-> A
            37 -> a
            62 -> z

        Python uses 0-9 and a-z (case insensitive) and is therefore limited to base <= 36


        The simplest way to do this given a list of digits to encode, is to create a string with as many characters as needed,
        and use their index (ordinal position) for our encoding map

            base b (>-2)
            map = " ... " (of length b)
            digits = [ ... ]

            encoding = map[digits[o]] + map[digits[1]] + ...


            example base 12:

            map = '0123456789abc'
            digits  = [4, 11, 3, 12]
            encoding='4b3c'



            encoding = ''
            for d in digits:                        (not very efficient - because all the time it is creating new string)
                encoding += map[d]


            more efficient solution - list comprehension

                ending = "".join([map[d] dor d in digits])

            





"""
