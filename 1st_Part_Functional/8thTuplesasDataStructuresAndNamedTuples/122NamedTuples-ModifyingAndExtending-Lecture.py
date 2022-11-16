""" 
                Named Tuples

            Modifying and Extending

Named Tuples are Immutable

Sp how can we change one or more values inside tuple?

Just like with strings, we have to create a new tuple, with the modified values

    Point2D = namedtuple("Point2D", 'x y')

    pt = Point2D(0, 0)


Suppose we need to change the value of the x coordinate:

    Simple approach: pt = Point2D(100. pt.y)


------------------------------ Drawback ------------------------------------

The simplest approach can work well, but it has a major drawback

    Stock - namedtuple('Stock', 'symbol year month day open high low close')

    djia = Stock(djia.symbol,
                        djia.year,
                        djia.month,
                        djia.day,       <--paaaaain!
                        djia.open,
                        djia.high,
                        djia.low,
                        26_394)


------------- Maybe slicing or unpacking -------------

    current = djia[:7]  --> tuple back

    *current, _ = djia  --> list back

    djia = Stock(*current, 26_394) <----- all values and modified last one


    We can also use the _make class method - but we need to create an iterable that contains all values first:

        new_values = current + (26_394, )       case of list -> new_values = current.append(26_394)

        new_values -> 'DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_394

        djia = Stock._make(new_values)
                                    <-- it must be iterable

------------- This still had drawbacks -------------

    djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_394)

    What if we wanted to change a value in the middle, say day?

    Cannot use extended unpacking (only one starred value in extending unpacking)

        *pre, day, *post = djia <--- makes no sense...

    Slicing will work
        pre = djia[:3]
        post = djia[4:]

    
    new_values = pre + (26,) + post

    djia = Stock(*new_values)

------------- But even this still has drawbacks! -------------

    djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_394)

    How about modifying both the day and the high values?

    new_values = djia[:3] + (26,) + djia[4:5] + (26_459,) + djia[6:]

    djia = Stock(*new_values)


    This is just unreadable and extremely error prone! 

------------- The _replace instance methods -------------

    named tuples have a very handy instance method _replace

    It will copy the named tuple into a new one, replacing any values from keyword arguments

    The keyword arguments are simple the field names in the tuple and the new value

    the keyword name must match an existing field name

        Stock = namedtuple('Stock', 'symbol year month day open high low close')

        djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_394)

        dji = djia._replace(day=26, high=26_459, close=26_394)  <--- new tuples with a new values

------------- Extending a Named Tuple -------------


    Sometimes we want to create named tuple that extends another named tuple
        appending one or more fields

    Stock = namedtuple('Stock', 'symbol year month day open high low close')

    We want to create a new named tuple class, StockExt that adds a single field, previous_close

    When dealing with classes, this is sometimes done by using subclassing

    But this not easy to do with named tuples


------------- Extending a Named Tuple -------------

    Point2D = namedtuple('Point2D', 'x y')

    Lets say we want to create a Point3D named tuple that has an extra parameter

    The obvious, and simplest approach here is best:
        Point3D = namedtuple('Point3D', ' x y z')

    But what happens if you have a lot of fields in the named tuple? Code is not as clean anymore...

    Stock = namedtuple('Stock', 'symbol year month day open high low close')

    Stock = namedtuple('Stock', 'symbol year month day open high low close previous_close')

    How about re-using the existing field names in Stock?

    Stock._field -> 'symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close'

    We can them create a new named tuple by "extending" the _fields tuple

    new_fields = Stock._fields + ('previous_close', )

    StockExt = namedtuples('StockExt', new_fields)


  -------------

    We can also easily use an existing Stock instance to create a new StockExt instance
    with the same common values, adding in our new previous_close value:

        Stock = namedtuple('Stock', 'symbol year month day open high low close')

         StockExt = namedtuples('StockExt', Stock._fields + ('previous_close', ))

         djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_394)

         djia_ext = StockExt(*djia, 26_00)

                or

        djia_ext = StockExt._make(djia + (26_000, ))







"""
