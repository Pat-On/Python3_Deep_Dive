"""

                Everything is an Object

Throughout this course, we will encounter many data types.
    - Integers (int)
    - Booleans (bool)
    - Floats (float)
    - Strings (str)
    - Lists (list)
    - Tuples (tuple)
    - Sets (set)
    - Dictionaries (dict)
    - None (NoneType)

We will also see other constructs:
    - Operators ( +, - ==, is, ...)
    - Functions
    - Classes
    - Types

But the one thing in common with all these things, is that they are all OBJECTS (instances of classes)

    Functions -> function instance
    Classes -> class instance
    Types -> type


This means they all have a memory address


AS a consequence:
    - Any object can be assigned to a variable
                                    - including functions...
    - Any object can be passed to a function
                                    - including functions...

    - any object can be retuned from a function
                                    - including function

    1st class citizens :-D

    Important note:
        my_func is the name of the function
        my_func() invokes the function

"""

a = 10
b = int(10)

print(help(int))

c = int('101', base=2)
