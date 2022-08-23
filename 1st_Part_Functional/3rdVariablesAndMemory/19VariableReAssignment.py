"""

        Variable Re-Assignment

    
my_var = 10

                my_var ---> int     0x1000
                            10          

            We are not changing value in memory but we are changing the pointer and assign new space in ram
                so new memory address with a new int object

my_var = 15

                my_var ---> int     0x1234
                            15      

            The same happen during the operations

my_var = 15 + 5

                my_var ---> int     0x2345
                            20      



    !Important:
                In fact, the value inside the int object, can never be changed

"""

# example

a = 10
print(hex(id(a)))

a = 15
print(hex(id(a)))

a += 15
print(hex(id(a)))

# memory addresses are the same because they are pointing to the same int object
a = 10
b = 10
print("a: ", hex(id(a)))
print("b: ", hex(id(b)))
