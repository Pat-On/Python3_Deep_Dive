"""
    Named Tuples - Application - Alternative to Dictionaries

"""
from collections import namedtuple
data_dict = dict(key1=100, key2=200, key3=300)

print(data_dict['key1'])

# we can use namedtuples if we do not want to modify values
# that we have the hashable values that can be the valid name of the namedtuple

# 3.6 and bellow order not guaranteed. From 3.7 is guaranteed
Data = namedtuple("Data", data_dict.keys())
print(data_dict.keys())

# it works but it is not very robust way - it is based on the guarantees of the order from dict
d1 = Data(*data_dict.values())
print(d1)


# unpacking the dictionary as a key value
Data = namedtuple("Data", "key3 key2 key1")
d2 = Data(**data_dict)

key_name = "key2"
print(getattr(d2, key_name))

# default support
print(data_dict.get('key10', None))
print(getattr(d2, 'key10', None))
print(d2.key1)


# ---------------------------
print("*" * 40)

data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]


# finding out all unique keys in the list

keys = set()
keys = set()
for d in data_list:
    for key in d.keys():
        keys.add(key)

print(keys)

print("Set Comprehension")

keys = {key for dict_ in data_list for key in dict_.keys()}
print(keys)


print("Union - multiple sets")
"""
In fact, we can also use the fact that we can union multiple sets
 (we'll cover this in detail later) by unpacking all the keys and 
 creating a union of them:
"""

keys = set().union(*(dict_.keys() for dict_ in data_list))
print(keys)


print("named tuple - this is the way :> ")
# Struct = namedtuple('Struct', keys)
Struct = namedtuple('Struct', sorted(keys))

print(Struct._fields)

# setting default values inside dictionary
"""Now, we're also going to provide default values,
 since not all dictionaries have all the keys in them.
  In this case I'm going to set the default to `None`
   if the key is missing:"""

Struct.__new__.__defaults__ = (None,) * len(Struct._fields)

tuple_list = []
for dict_ in data_list:
    tuple_list.append(Struct(**dict_))

# tuple_list = [Struct(**dict_) for dict_ in data_list]

print(tuple_list)

print("******** very generic function - all bundled together ********")
"""
So lastly, let's just package this all up neatly into a single function 
that will take an iterable of dictionaries, or an arbitrary number 
of dictionaries as positional arguments, and return a list of named tuples:
"""


def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', keys)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    # list comprahension
    return [Struct(**dict_) for dict_ in dicts]


print(tuplify_dicts(data_list))


def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', sorted(keys))
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    # list comprahension
    return [Struct(**dict_) for dict_ in dicts]


print(tuplify_dicts(data_list))

# classes that you used only to store data
# and you do not require mutability
# use NAMEDTUPLES! <3
