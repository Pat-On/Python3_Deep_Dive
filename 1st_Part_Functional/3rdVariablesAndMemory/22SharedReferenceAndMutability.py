"""

        Shared References and Mutability

The term shared reference is the concept of two variable referencing
the same object in memory (i.e. having the same memory address)


a = 10              ----> 10 at 0x1000
b = 10              ----> 10 
            so it is coping not a value but the references



def my_func(v):
    '''
t = 20
my_func(t)



In fact, the following may surprise you

a = 10              ----> 10 at 0x1000
b = 10              ----> 10 


a = 'hello'              ----> 'hello' at 0x1000
b = 'hello'              ----> 'hello' 

In both these cases, Python's memory manager decides to automatically re-use the memory references!!


Is this even safe?
    Yes, because these object are immutable
        The integer object 10, and the string object "hello" are immutable
        - so it is safe to set up a shared reference


----------------------------------------------------------------------------------------
When working with mutable object we have to be more careful!

a = [1, 2, 3]
b = a
b.append(100)


With mutable objects, the python memory manager will never create shared references

a = [1, 2, 3]       a ---> 0x1000
b = [1, 2, 3]       b ---> 2x2124

"""
my_var_1 = 'hello'
my_var_2 = my_var_1
print(my_var_1)
print(my_var_2)

print(hex(id(my_var_1)))
print(hex(id(my_var_2)))

my_var_2 = my_var_2 + ' world!'


print(hex(id(my_var_1)))
print(hex(id(my_var_2)))


my_list_1 = [1, 2, 3]
my_list_2 = my_list_1
print(my_list_1)
print(my_list_2)

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

my_list_2.append(4)

print(my_list_2)

print(my_list_1)

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

a = 10
b = 10

print(hex(id(a)))
print(hex(id(b)))

my_list_1 = [1, 2, 3]
my_list_2 = [1, 2, 3]

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))
