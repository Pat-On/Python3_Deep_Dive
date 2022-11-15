# Tuples as Data Structures

from math import sqrt
from random import uniform
print((10, 20, 30))
print(10, 20, 30)

a = (10, 20, 30)
b = 10, 20, 30

print(type(a))
print(type(b))

# parentheses are required when passed in functions param


def print_tuple(t):
    for e in t:
        print(e)

# print_tuple(10, 20, 30) <-- error


print_tuple((10, 20, 30))


print(a[0])
print(a[0:2])


a = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

x, *other, z = a  # var [arr] var
print(x, other, z)

# if we have mutable object inside tuple, we can still modify it <-- normal


class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__} (x={self.x}, y={self.y})'


pt = Point2D(10, 20)
pt.x = 100
print(pt)


tupleExample = 1, 2, 3, 4
# tupleExample[0] = 1000

# example of this behavior - why he created new class? ^^
tupleExample2 = [1, 2, 3, 4], 1, 2, 3, 4
print(tupleExample2)
tupleExample2[0][0] = 100000
print(tupleExample2)


#
london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000

cities = london, new_york, beijing

# non pythonic way
total = 0
for city in cities:
    total += city[2]

print(total)

# Pythonic way - list comprehension
print([city[2] for city in cities])
print(sum([city[2] for city in cities]))


# unpacking

record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072

symbol, year, month, day, open_, high, low, close = record

# horrible way:
symbol, year, close = record[0], record[1], record[7]


for element in cities:
    print(element)


for city, country, population in cities:
    print(f'city={city}, population={population}')


for index, value in enumerate(beijing):
    print(f'{index}: {value}')

for city, _, population in cities:
    print(f'city={city}, population={population}')


# Another frequent application of usign tuples as data structures is for returning multiple values from a function.

print("Break - last part")


def random_shot(radius):
    '''Generates a random 2D coordinate within 
    the bounds [-radius, radius] * [-radius, radius]
    (a square of area 4)
    and also determines if it falls within 
    a circle centered at the origin 
    with specified radius'''

    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
    # returned tuple - unpacking
    return random_x, random_y, is_in_circle


num_attempts = 1_000_000
count_inside = 0
for i in range(num_attempts):
    # returned tuple - unpacking
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately: {4 * count_inside / num_attempts}')
