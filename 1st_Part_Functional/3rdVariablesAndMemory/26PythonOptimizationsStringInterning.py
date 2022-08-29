"""

                Python Optimizations - String Interning

        Some string are also automatically interned - but not all
        As the Python code is compiled, identifiers are interned
            - variable names
            - function names
            - class names
            - etc

            Identifiers:
                - must start with _ or a letter
                - can only contain _, letters and numbers

        Some string literals may also be automatically interned
            - string literals that look like identifiers (e.g. "hello_world")
            - although if it start with a digit, even though that is not a valid identifier, it may still get interned
            

                    But do not count on it!

        Why do this?
            - it is all about (speed and possibly memory) optimization
            - Python both internally, and in the code you write, deals with lots and lots of dictionaries type lookups,
                on string keys, which means a lot of string equality testing
            - let say we want to see if two string are equal

            a = "some_long_string"
            b = "some_long_string"

        using a == b, we need to compare the two string character by character

        But if we know that 'some_long_string" has been interned, then a and b are the same string
        if they both point to the same memory address

        In which case we can use a is b instead - which compares two integers (memory address)

        This is much faster than the character by character

        Not all string are automatically interned by PYthon

        But You can force string to be interned by using the sys.intern() method - singleton

        import sys

        a = sys.intern('the quick brown fox")
        b = sys.intern("the quick brown fox")

        a is b => true

        when should you do this? In general do not do it!
            - dealing with a large number of string that could have high repetition
                eg tokenizing a large corpus of text (NLP - natural language processing)
                    - memory optimization
            - lots of string comparisons
        In general though, you do not need to intern string yourself.
        Only do this if you really need to.

    """
import sys
import time

# looks like identifier
a = "hello"
b = "hello"
print(id(a), id(b))

# interned to lol!
c = "hello world here , there is other thing. crazyhello world here , there is other thing. crazy"
d = "hello world here , there is other thing. crazyhello world here , there is other thing. crazy"


e = "hello world here , there is other thing. crazyhello world here , there is other thing. crazyhello world here , there is other thing. crazyhello world here , there is other thing. crazyhello world here , there is other thing. crazyhello world here , there is other thing. crazy"
f = "hello world here , there is other thing. crazyhello world here , there is other thing. crazyhello world here , there is other thing. crazyhello world here , there is other thing. crazyhello world here , there is other thing. crazyhello world here , there is other thing. crazy"
print(id(c), id(d))

print(a == b)


# forcing string internal - interesting in my case it is interning three at the same address hmm
"""
Explanation:
Here there is something else going on - when Python compiles an entire block at a time, 
it tries to do some optimizations - for example, constants that are equal to each other 
will be re-used (as objects), hence you should always get the same memory address 
(but again, it is an implementation detail, so that can change from one version of Python to another,
 hence why you cannot count on it).

On the other hand, if you use Jupyter, or an interactive Python prompt, then 
(in Python 3.7, but most likely in other versions too), things behave a little differently. 
"""
g = sys.intern("hello other world")
h = sys.intern("hello other world")
i = "hello other world"
print(id(g), id(h), id(i))


def compare_using_equals(n):
    a = "a long string that is not interned" * 200
    b = "a long string that is not interned" * 200
    print("compare equals", id(a), id(b))
    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern("a long string that is not interned" * 200)
    b = sys.intern("a long string that is not interned" * 200)
    print(id(c), id(d))
    for i in range(n):
        if a is b:
            pass


start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()

print("equality", end-start)

start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print("equality interning", end-start)
