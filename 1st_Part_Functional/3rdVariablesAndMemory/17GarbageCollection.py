"""
                    Garbage Collection

Circular References

    example:
        my_var -> [object a]
                    var_1   ---->   Object B
                            <----   var_2

                Reference counting is not going to destroy it!
                Circular Reference
                Result in Memory leak

    Garbage Collector
        - can be controlled programmatically using the gc module
        - by default it is turned on
        - you may turn it off if you are sure your code does not create circular references - but beware!!
                (it is very easy to create circular references)
            Why to turn it off? Because of performance
        - runs periodically on its own (if turned on)
        - you can call it manually, and even do our own cleanup

    
    In general GC works just fine
        but, not always...

        for Python < 3.4

            if even one of the objects in the circular reference has a destructor [e.g. __del__()]
            Destructor is the code which you run when you are destroying object:
                action in that - cleaning files, closing connections etc.

                the destruction order of the objects may be important

                    but the GC does not know what that order should be
                    so the object is marked as uncollectable

                        and the objects in the circular references are not cleaned up  ----> memory leak! 

"""

from audioop import add
import ctypes
import gc


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"


# classes with circular references


class A:
    def __init__(self):
        self.b = B(self)
        print("A: self {0}, b{1}".format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print("B: self {0}, a{1}".format(hex(id(self)), hex(id(self.a))))


# disabling gc
gc.disable()

my_var = A()
