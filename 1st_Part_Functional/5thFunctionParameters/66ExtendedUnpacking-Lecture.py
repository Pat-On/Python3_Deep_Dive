"""
                Extended Unpacking

        Using the * and ** operators

---------------------------------------------   Much of this section applies to Python >= 3.5
The use case for *

We don't always want to unpack every single item in an iterable

we may, for example, want to unpack the first value, and then unpack the remaining values
into another variable

l = [1, 2, 3, 4, 5, 6]

We can achieve this using slicing

        a = l[0]
        b = l[1:]

or, using simple unpacking              a ,b = l[0], l[1:]
                                        (aka parallel assignment)

We can also use the * operator:         a, *b = l


Apart from cleaner syntax, it also works with any iterable, not just sequences types!
Because we do not need concept of indexes that does not exist in sets and dicts



---------------------------------------------
Usage with ordered types


a, *b = [-10, 5, 2, 100] a = -10  b= [5, 2, 100]
a, *b = (-10, 5, 2, 100) a = -10  b= [5, 2, 100]  <-- always list


a, b, *c, d = [-10, 5, 2, 100, 3, 4]


The * operator can only be used once in the lhs an unpacking assignment


Usage with ordered type

We have seen how to use the * operator in the LHS of an assignment to unpack the RGS
a, *b = [-10, 5, 2, 100] 

However we can also use it this way:

l1 = [1,2,3]
l2 = [4,5,6]
l = [*l1, *l2] <-- merging lists


---------------------------------------------
The ** unpacking operator

d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'c': 3, 'h': 10}

d = {**d1, **d2, **d3}    (note that the ** operator cannot be used in the LHS of an assignment)


    IMPORTANT h is overwrites by last merged last dict

"""

d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'c': 3, 'h': 10}

d = {**d1, **d2, **d3}

print(d)
