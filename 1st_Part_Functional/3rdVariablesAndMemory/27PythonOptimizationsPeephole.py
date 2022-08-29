"""

            Python Optimizations
                Peephole

    
    This is another variety of optimizations that can occur at compile time
    
        Constant expressions
            numeric calculations
                    24 * 60 
                    Python will actually pre-calculate 24 * 60 -> 1440
                    (expression that evaluate to expressions)

        short sequences length < 20
                (1, 2) * 5 -> (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
                'abc' * 3 -> "abcabcabc
                "hello" + "world" -> "helloworld"

        
        but not "the quick brown fox" * 10  (more than 20 characters)


    Membership Tests: Mutables are replaced by Immutables:
        when membership tests such as:
            if e in [1, 2, 3]:   -> 
                are encountered, the [1, 2, 3] constant, is replaced by its immutable counterpart

                (1, 2, 3) tuple
        list -> tuples
        sets -> frozensets

    Set membership is much faster than list or tuple membership (sets are basically like dictionaries)

    So, instead of writing
        if e in [1, 2, 3]:   or if e in (1, 2, 3)

            write if e in {1, 2, 3}   <-- more efficient

"""
import string
import time


def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'quick brown fox' * 5
    f = ["a", "b"] * 3


print(my_func.__code__.co_consts)
# output
"""
(None, 
1440,
(1, 2, 1, 2, 1, 2, 1, 2, 1, 2), 
'abcabcabc', 
'ababababababababababab', 
'quick brown foxquick brown foxquick brown foxquick brown foxquick brown fox',
 'a', 'b', 
 3)
"""

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)


def membership_test(n, container):
    for i in range(n):
        if "z" in container:
            pass


start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list: ', end - start)


start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('tuple: ', end - start)

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('set: ', end - start)
