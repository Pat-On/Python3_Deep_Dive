""" 
                                             Python Memory Manager
                                    Memory
                        0x1001     [     ]
                        0x1002     [     ]
                        0x1003     [     ]     <--- Heap
                        0x1004     [     ]
                        0x1005     [     ]
                        0x1006     [     ]
                        0x1007     [     ]
                        0x1008     [     ]
                        0x1009     [     ]
                        0x1010     [     ]
                        0x1011     [     ]
                         ...         ...



                       alias /
my_var_1 = 10   ---- reference -->      0x1000 [    10] 
                       0x1000

        so my_var_1 is reference to object in the memory
           

In Python, we can find out the memory address referenced 
by a variable by using id() function.

This will return a base-10 number. We can convert this base 10-number
to hexadecimal, by using the hex() function
"""

a = 10
print(hex(id(a)))
