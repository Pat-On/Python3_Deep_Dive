# The operator module

# more: https://docs.python.org/3/library/operator.html

from functools import reduce
import operator


print(operator.add(1, 2))
print(operator.mul(2, 3))
print(operator.pow(2, 3))
print(operator.mod(13, 2))
print(operator.floordiv(13, 2))
print(operator.truediv(3, 2))

print("*" * 40)


print(reduce(lambda x, y: x*y, [1, 2, 3, 4]))

print(reduce(operator.mul, [1, 2, 3, 4]))


print("*" * 40)
print(operator.lt(10, 100))
print(operator.le(10, 10))
print(operator.is_('abc', 'def'))

# Element and Attribute Getters and Setters
print("*" * 40)
my_list = [1, 2, 3, 4]
print(my_list[1])
print(operator.getitem(my_list, 1))

print("*" * 40)
my_list = [1, 2, 3, 4]
my_list[1] = 100
del my_list[3]
print(my_list)


print("*" * 40)
my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)
operator.delitem(my_list, 3)
print(my_list)


"""
We can also do the same thing using the **operator** module's **itemgetter** function.

The difference is that this returns a callable:
"""

print("*" * 40)
f = operator.itemgetter(2)
print(f(my_list))

x = 'pytyhon'
print(f(x))

# Similarly, **operator.attrgetter** does the same thing, but with object attributes.
print("*" * 40)


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')


obj = MyClass()

print(obj.a, obj.b, obj.c)

f = operator.attrgetter('a')  # callable

print(f(obj))

my_var = 'b'

print(operator.attrgetter(my_var)(obj))


"""
Of course, attributes can also be methods.

In this case, **attrgetter** will return the object's
 **test** method - a callable that can then be called using **()**:

"""

f = operator.attrgetter('test')
obj_test_method = f(obj)
print(obj_test_method())  # return none so print none


"""
If the callable takes in more than one parameter,
they can be specified as additional arguments in **methodcaller**:

"""


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, c):
        print(self.a, self.b, c)


obj = MyClass()
print(obj.do_something(100))
print(operator.methodcaller('do_something', 100)(obj))


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, *, c):
        print(self.a, self.b, c)


print(obj.do_something(c=100))
print(operator.methodcaller('do_something', c=100)(obj))
