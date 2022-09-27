"""

            *args


Recall from iterable unpacking

a, b, c = (10, 20, 30)


def func1(a, b, c):
    do something


func1(19, 20, 30)


*args

    recall also: a, b, *c = 10, 20, "a", "b"  -> c = ["a", "b" ]


    def func1(a, b, *c):  -> c would take everything else
        do something

    func1(10, 20, "a", "b") -> c = ("a", "b") <- this is a tuple, not a list


    the * parameter name is arbitrary - you can make it whatever you want

    it is customary (but not required) to name it *args

        def func1(a, b, *args): 
            do something


*args - EXHAUSTS POSITIONAL ARGUMENTS

    You can not add more positional arguments after *args


Unpacking arguments

    def func1(a, b, c):
        do something

    l = [10, 20, 30]


    But we can unpack the list first and then pass it to the function
    
        func1(*l)

"""
