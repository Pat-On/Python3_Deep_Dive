# Named Tuples - Docstring and Default Values

from collections import namedtuple

Point2D = namedtuple("Point2D", 'x y')
print(Point2D.__doc__)

print(Point2D.x.__doc__)

Point2D.__doc__ = "2D Cartesian Coordinate"
Point2D.x.__doc__ = "x coordinate"
Point2D.y.__doc__ = "y coordinate"

print(Point2D.__doc__)
print(Point2D.x.__doc__, "\n", Point2D.y.__doc__)


# The way of setting defaults
# Prototype

Vector2D = namedtuple("Vector2D", "x1 y1 x2 y2 origin_x origin_y")
print(Vector2D._fields)

vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
print(vector_zero)

# proto! proto!
v2 = vector_zero._replace(x1=10, y1=10, y2=20, x2=20)
print(v2)


# another way of def defaults

def func(a, b=10, c=20):
    print(a, b, c)


func(1)
# this tuple is aligned from the right to the left
print(func.__defaults__)
func.__defaults__ = (100, 200, 300)

func()

func.__defaults__ = (300,)
# func() # TypeError: func() missing 2 required positional arguments: 'a' and 'b'
func(10000, 20000)

print(type(Vector2D.__new__.__defaults__))

Vector2D.__new__.__defaults__ = (0, 0)

v1 = Vector2D(10, 10, 20, 20)  # nice!
print(v1)


Vector2D.__new__.__defaults__ = (101, 101, 202, 202, 0, 0, )
v10 = Vector2D()

print(v10)
