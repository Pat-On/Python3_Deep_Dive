# Named Tuples - Modifying and Extending

from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')
origin = Point2D(10, 0)

print(origin)


# "changing" value

origin = Point2D(0, origin.y)
print(origin)


# Of course this could become quite unwieldy when
# we have a larger number of properties and we only need to change a single item:

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

# update 1 way - painful
djia = Stock(djia.symbol, djia.year, djia.month, djia.day,
             djia.open, djia.high, djia.low, 26_394)


# update 2 way
*values, _ = djia
print(values)
djia = Stock(*values, 26_393)
print(djia)


# Slicing way

print(djia[:3] + (26,) + djia[4:])

djia2 = Stock(*(djia[:3] + (26,) + djia[4:]))

print(djia2)


# slicing is not best solution - readability

values = djia[0:1] + (2019,) + djia[2:3] + (26,) + djia[4:]
djia3 = Stock(*values)
print(djia3)


# Stock._make(values) <--- instance method
djia4 = Stock._make(values)
print(djia4)


# better way
# This is really getting too complex.

# Fortunately there's a better way!

# The namedtuple implementation also provides another instance method called `_replace`
#  which takes keyword-only arguments. That method will make a copy of the current tuple
#  and substitute property values based on the keyword-only arguments passed in.

print(id(djia))
djia5 = djia._replace(year=2019, day=26)

print(djia5)
print(id(djia5))


# Extending Named Tuples
print("**** Second Part ****")

# easiest way
Point2D = namedtuple('Point2D', 'x y')
Point3D = namedtuple('Point3D', 'x y z')

pt = Point2D(10, 20)

pt3d = Point3D(*pt, 100)
print(pt3d, "<---------")

# the way of using existing fields and appending additional one

StockExt = namedtuple('StockExt',
                      '''symbol year month day open high low 
                      close previous_close''')

print(Stock._fields)


new_fields = Stock._fields + ('previous_close',)
print(new_fields)


StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))
print(StockExt._fields)


# extending
djia_ext = StockExt(*djia, 25_000)
print(djia_ext)


# _make method
djia_ext = StockExt._make(djia + (25_000, ))
print(djia_ext)
