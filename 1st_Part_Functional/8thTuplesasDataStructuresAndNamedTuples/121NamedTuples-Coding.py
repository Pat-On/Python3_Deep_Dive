# Named Tuples - Coding

from collections import namedtuple


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


Point2D = namedtuple("Point2D", ["x", "y"])

pt1 = Point2D(10, 20)
print(pt1)

# you should keep it consistent:
# Pt2D = namedtuple("Point2D", ("x", "y"))
Point2D = namedtuple("Point2D", ("x", "y"))

pt2 = Point2D(10, 20)

print(pt2)


# with the namedtuples, because they are extension of the tuple class we are getting for fre tuple1 is tuple2 and tuple1 == tuple2
# example


pt3 = Point2D(10, 20)
pt4 = Point2D(10, 20)

print(pt3 == pt4, pt3 is pt4)


# methods of tuple:
print(max(pt4))


# ANOTHER EXAMPLE:

a = (1, 2)
b = (1, 1)

print(list(zip(a, b)))

1  # using generator
print(sum(e[0] * e[1] for e in zip(a, b)))

# xD
Circle = namedtuple("Circle", "center_x center_y        radius")

c = Circle(0, 10, 20)
print(c)


# We can unpack them in the same way <- end of course extended unpacking by using:  *_
p = Point2D(10, 20)
x, y = p
print(x, y)


# renaming note:

# Person = namedtuple("Person", 'name age _ssn', rename=True)
Person = namedtuple(
    'Person', ['firstname', 'lastname', '_age', 'ssn'], rename=True)

print(Person._fields)
# print(Person._source) works only for version 3.5
