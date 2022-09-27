"""
        Keyword Argument


    def func(a, b, c):
        do something

    
    func(1,2,3)

    func(a=1, c=2, b=3)



            Mandatory Keywords Arguments

        We can make keywords arguments mandatory
        to do so, we create parameters after the positional parameters have been exhausted


        def func(a, b, *args, d):
            do something

        In this case, *args effectively exhausts all positional arguments
            and d must be passed as a keyword (named) argument

        func(1, 2, "x", "y", d = 100)


    We can even omit an y mandatory positional arguments:
    
    def func(*args, d):
        do something

    
    func(1,2,3, d=100) 
    func(d=100)

    In fact we can force no positional arguments at all:

    def func(*, d):         * indicates the "end" of positional arguments
        do something


    func(1, 2, 3, d=100)

                                        Putting it together

    def func(a, b=1, *args, d, e=True):                      def func(a, b=1, *, d, e=True):
        do something                                             do something

    a: mandatory positional argument(may be specified using a named argument)
    b: optional positional argument (may be specified positionally, as  a named argument, or not at all), default to 1


    args: catch-all for any optional                         *: no additional positional arguments allowed
    additional positional arguments          

    d: mandatory keyword argument
    e: optional keyword argument, defaults to True

"""
