"""
                Booleans

            integer subclass


    The bool class PEP 285

    Python has a concrete bool class that is used to represent boolean values

    however, the bool class is a subclass of the int
        They posses all the properties and methods of integers and add some specialized
        one such as and or etc

        issubclass(bool, int) -> true

    Two constants are defined: True and False
        isinstance(True, bool) -> True

    They are singleton objects of type bool

        False and True

    is vs ==

        Because True and False are singleton objects, they will always retain their same memory address throughout the lifetime of your application
        
        So, comparison of any boolean expression to True and False can be performed using either the is(identity) operator,
                                                                                or the == (equality) operator

                                        a == True 
                                        a is True
                                        where a is a bool object
        But since bool objects are also int objects, they can be interpreted as the integers 1 and 0

                int(True) -> 1    int(False) -> 0

        But: True and 1 are not the same objects

        id(True) != id(1)
        id(False) != id(0)

            so:
                True is 1 -> false
                True == 1 -> true   <- so it is equal to one but it is not the same like 1


    Booleans as integers

        This can lead to "strange" behavior you may not expect!

            True > False  -> True
            (1 == 2) == False -> True
            (1 == 2) == 0  -> True

        In fact, any integer operation will also work with booleans (//. %, etc)
            True + True + True -> 3   xD

            -True -> -1

    
    The Boolean constructor

        The boolean constructor bool(x) returns True when x is True, and False when x is False
            
        What really happens is that many classes contain a definition of how to cast instances of themselves to a Boolean.

    What really happens is that many classes contain a definition of how to cast instances of
    themselves to a Boolean - this is sometimes called the truth value or truthiness of an object

    Integers have a truth value defined according to this rule:
        bool(0) -> False 
        bool(x) -> True for any int x != 0

"""
