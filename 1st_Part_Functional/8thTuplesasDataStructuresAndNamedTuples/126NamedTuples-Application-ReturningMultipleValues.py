"""
            Named Tuples - Application - Returning Multiple Values


"""

from random import randint, random

from collections import namedtuple


def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return red, blue, green, alpha


color = random_color()

print(color)

Color = namedtuple("Color", 'red green blue alpha')


def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, blue, green, alpha)


# nice
color = random_color()
print(color)
