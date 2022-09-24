"""
            Arguments vs Parameters

Semantics!

    def my_func(a, b):      in this context, a and b are called parameters of my_func
        # code here         Also note that a and b are variables, local to my_func


    When we call the function:
        x = 10
        y = "a"             x and y are called the arguments of my_func
                            aldo note that x and y are passed by reference
        my_func(x, y)       i.e. the memory addresses of x and y are passed

    
    it is ok if you mix up these terms - everyone will understand what you mean! 



    x = 10                                      def my_func(a, b):
    x = "a"                                         # some code 
    my_func(x, y)


    Module Scope                                                Function Scope

                x   --------------> 10 (OxA13F) <-----------------  a
                y   --------------> "a" (OxE345) <----------------  b


    



"""
