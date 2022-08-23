"""
-------------------------------------------------------------------------------------------
        Immutable objects are safe from unintended side-effect


                                my_var's reference is passed to process()
        def process(s):                                                                         
            s = s + ' world'                  Scopes                                                          
            return s                                                                            
                                                module scope
        my_var = 'hello'                            my_var   ->     hello at 0x1000                                        

                                                                                ^
        process(my_var)                                          process()scope  |
            ---> hello
                            Because strings are immutable scope changed
                                inside the process() s is pointing to new memory location
                                but
                                my_var in module scope is still pointing to the the memory location hello at 0x1000


        !WATCH OUT": for immutable collection objects that contain mutable objects


-------------------------------------------------------------------------------------------
        Mutable objects are not safe from unintended side-effect:

        def process(list)                       Scopes                                                                     
            list.append(100)                                                                                             
                                                module scope
                                                    my_list ----> 1, 2, 3 at 0x1000
        my_list = [1, 2, 3]

        process(my_list)                                     process() scope ^
                                                                        lst  |                          

        print(my_list)
                -------> [1, 2, 3, 100]                                                                           
 
-------------------------------------------------------------------------------------------
        Immutable collection object that contain mutable object

        def process(t):                           Scopes                                      
            t[0].append(3)                                                                  
                                                    Module Scopes       [1,2,3] 'a' at 0x100
                                                        my_tuple   ---->         ^
        my_tuple = ([1, 2], 'a')                                                 |                  
                                                    process()scopes           ---|                              
        process(my_tuple)                                    t                                                 
               ----> ([1,2,3], 'a')                                                                              


"""


def process(s):
    print('initial s # = {0}'.format(hex(id(s))))
    s = s + ' world'
    print('s after change # = {0}'.format(hex(id(s))))


my_var = 'hello'
print('my_var # = {0}'.format(hex(id(my_var))))

process(my_var)


def modify_list(items):
    print('initial items # = {0}'.format(hex(id(items))))
    if len(items) > 0:
        items[0] = items[0] ** 2
    items.pop()
    items.append(5)
    print('final items # = {0}'.format(hex(id(items))))


my_list = [2, 3, 4]
print('my_list # = {0}'.format(hex(id(my_list))))


modify_list(my_list)

print(my_list)
print('my_list # = {0}'.format(hex(id(my_list))))


def modify_tuple(t):
    print('initial t # = {0}'.format(hex(id(t))))
    t[0].append(100)
    print('final t # = {0}'.format(hex(id(t))))


my_tuple = ([1, 2], 'a')

hex(id(my_tuple))

modify_tuple(my_tuple)


my_tuple
