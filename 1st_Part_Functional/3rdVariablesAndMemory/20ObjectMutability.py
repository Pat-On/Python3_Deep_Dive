"""

        Object Mutability


    Consider an object in memory:
                                    type    Ox1000          Changing the data inside the object
                                    state                       is called modifying the internal state of the object
                                    (data)

    my_account ---->Bank Account   0x1000   Bank Account   0x1000
                    Acct #: 12345           Acct #: 12345        
                    Balance: 150            Balance: 500         


                        Memory address han not changed
                        internal state (data) has changed
                        -> Object was mutated -> fancy way of saying the internal data has changed


    An object whose internal state can be changed is called:
                Mutable

    An object whose internal state cannot be changed, is called:
                Immutable

    

------------------ Examples in Python ------------------


Immutable:
    - Numbers (int, floats, Booleans, complexNumbers etc.)
    - Strings
    - Tuples (container type of object)
    - Frozen Sets
    - User-Defined Classes - if you are going to set it up

Mutable:
    - Lists (container type)
    - Sets
    - Dictionaries
    - User-defined Classes


t = (1, 2, 3) Tuples are immutable: elements cannot be deleted, inserted, or replaced
                In this case, both the container (tuple) and all its elements (ints) are immutable

But consider this: 
a = [1, 2]
b = [3, 4]              List are mutable: elements can be deleted, inserted or replaced
t = (a, b)         t = ([1, 2], [3, 4])


a.append(3)         t = ([1, 2, 3 ], [3, 4, 5])
b.append(5)         We can change the state of the mutable object within the immutable object


In this case, although the tuple is immutable, its elements are not.
The object references in the tuple did not change.
    but the referenced objects did mutate.



t = (1, 2, 3)           tuple is immutable
                        tuple contains references to immutable objects (int)

t = ([1, 2], [3, 4])    tuple is immutable
                        tuple contains references to mutable objects (arrays/lists)


"""

my_list = [1, 2, 3]
print(type(my_list))
print(id(my_list))

my_list.append(4)
print(type(my_list))
print(id(my_list))

my_list_1 = [1, 2, 3]
print(id(my_list_1))

# new object - new object in memory
my_list_1 = my_list_1 + [4]
print(id(my_list_1))

my_dict = dict(key1=1, key2="a")
print(id(my_dict))

my_dict["key3"] = 10.5
print(id(my_dict))
