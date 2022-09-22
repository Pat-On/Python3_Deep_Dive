"""

Objects have Truth Values

All objects in PYthon have an associated truth value

Every object has a True truth value, except:
- None
- False
- 0 
- empty sequences: list, tuples, string
- empty mapping types: dicitonary set etc
- custom classes that implement a __bool__ or __len__ 
    method that return False or 0

Under the hood
    - Classes define their truth values by defining a special instance method:
        __bool__(self)  or __len__

    - then when we call bool(x) -> Python will actually executes x.__bool__()
                                        or __len__ if __bool__ is not defined
                                        if neither is defined then True

    example: Integers

    def __bool__(self):
        return self != 0
    
    When we call bool(100) Python actually executes 100.__bool__()
    and therefore returns the result of 100 != 0  -> True
    
    


"""
