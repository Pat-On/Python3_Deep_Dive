#  Decorating Classes

# Monkey Patching - adding attributes at run time :>

from functools import total_ordering
from math import sqrt
from datetime import datetime, timezone
from fractions import Fraction


f = Fraction(2, 3)

print(f.denominator, f.numerator)

# at run time we are creating speak attribute
Fraction.speak = 100

print(f.speak)

# creating instance method
Fraction.speak = lambda self, message: "Fractions says: {0}".format(message)

print(f.speak("This is a late parrot!"))


# Part2
print("*" * 40, "More useful example")


Fraction.is_integral = lambda self: self.denominator == 1

f1 = Fraction(2, 3)
f2 = Fraction(64, 8)

print(f1.is_integral())
print(f2.is_integral())


# Part 3
print("*" * 40, "Using function that is going to decorate Fractions")


def dec_speak(cls):
    cls.speak = lambda self, message: "{0} says: {1}".format(
        self.__class__.__name__, message)
    return cls


# class decorator
Fraction = dec_speak(Fraction)


f1 = Fraction(2, 3)
print(f1.speak("Hello"))


# Part 4
print("*" * 40, "Debugging info added to our standard class")


def info(obj):
    results = []
    results.append("time: {0}".format(datetime.now(timezone.utc)))
    results.append("Class {0}".format(obj.__class__.__name__))
    results.append("id: {0}".format(hex(id(obj))))
    for k, v in vars(obj).items():
        results.append("{0}: {1}".format(k, v))
    return results


def debug_info(cls):
    # obj is self basically if it would be written inside the class
    cls.debug = info
    # if you are mutating the class you do not need to return it but it is preferable because both solutions work - shot and long "syntax"
    return cls


@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi():
        return "Hello there!"


# decorating
# Person = debug_info(Person)

p = Person("John", 1939)
print(p.debug())

# Part 5
print("*" * 40, "built in decorators")


@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed_mph):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed_mph = top_speed_mph
        self.current_speed = 0

    @property
    def speed(self):
        return self.current_speed

    @speed.setter
    def speed(self, new_speed):
        self.current_speed = new_speed


s = Automobile('Ford', 'Model T', 1908, 45)

print(s.debug())
# Part 5
print("*" * 40, "modification built in method of objects")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__.__name__, self.x, self.y)


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)
p4 = Point(1, 2)

print(p1, p2, p1 == p2)

print(abs(p1), abs(p4), p1 < p4)


def complete_ordering(cls):
    # brutal solution not useful in production <- created based on assumption we have
    # implemented already == and >
    # lack of type checking etc
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not (
            self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)
        # we need to return for the sake of decorator syntax - short one
    return cls


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__, self.x, self.y)


Point = complete_ordering(Point)
p1, p2, p3 = Point(1, 1), Point(3, 4), Point(3, 4)
print(abs(p1), abs(p2), abs(p3))

print(p1 < p2, p1 <= p2, p1 > p2, p1 >= p2, p2 > p2, p2 >= p3)

# Part 6
print("*" * 40, "functools -> total_ordering :>")


# from functools import total_ordering
@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)

    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)

    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented


g1, g2 = Grade(80, 100), Grade(60, 100)
print(g1 >= g2, g1 > g2)
