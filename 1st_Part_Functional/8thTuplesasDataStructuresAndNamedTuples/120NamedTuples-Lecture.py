"""
            Named Tuples
        
Tuples as Data Structure

    we have seen how we interpreted tuples as data structures

    the position of the object contained in the tuple gave it meaning

    For example, we can represent a 2D coordinates as: (10, 20)
                                                        x,  y


    if pt is a position tuple we can retrieve the x and y coordinates using: 
            x, y = pt

    So, for example, to calculate the distance of pt from the origin we could write:
        dist = math.sqrt(pt[0] ** 2 + pt[1] ** 2)

    Now this is not very readable, and if someone sees this code they will have to know that pt[0] means the x-coordinate
    and pt[1] means y-coordinate

    This is not very transparent


-------------------------- Using a class Instead -----------------------

    At this point, in order to make things clearer for the reader (not the compiler, the reader), we 
    might want to approach this using a class instead

class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    pt = Point2D(10, 20)

    distance = sqrt(pt.x ** 2 + pt.y ** 2)


# You do not have to define classes in Python! 
# you can use named tuples! 


-------------------------- Extra Stuff --------------------------

At the very least we should implement the __repr__ method

    -> Point(x=10, y=20)

We probably should implement the __eq__method too
    
    -> Point(10, 20) == Point(10, 20) -> True


class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2d(x={self.x}, y={self.y})'

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        else:
            return False



------------------ Named Tuples to the Rescue ------------------

There are other reasons to seek another approach. I cover some of this in the coding video

Amongst other things, Point2Do objects are MUTABLE - something we may not want! 

There is a lot to like using tuples to represent simple data structures

The real drawback is that we have to know what the position mean, and remember this in our code

If we ever need to change the structure of our tuple in our code (like inserting a value that we forgot)

most likely our code will break!

eric = ("Idle", 42)
last_name, age = eric


eric = ("Eric", "idle", 42)
last_name, age = eric <--- error! Broken!



So what if we could somehow combine these two approaches, essentially creating tuples where we can, in addition, give meaningful names to the positions?

That is what namedtuples essentially do

    They subclass tuple, and add a layer to assign property names to the positional elements

    Located in the collections standard library module

    from collections import namedtuple

    namedtuple is a function which generates a new class <--- class factory

        that new class inherits from tuple

        but also provides names properties to access elements of the tuple

        but an instance of that class is still a tuple



------------ Generating Named Tuple Classes ------------

    We have to understand that namedtuple is a class factory

    When we use it, we are essentially creating a new class, just as if we had used class ourselves

    namedtuples needs a few things to genereate this class:

        - the class name we want to use
        - a sequence of field names (strings) we want to assign, in the order of the elements in the tuple
            field names can be any valid variable name
            except that they cannot start with an underscore
             
    The return value of the call to namedtuple will be a class

    We need to assign that class to a variable name in our code so we can use it to construct instances

    Point2D = namedtuple("Point2D", ["x", "y"])
                                        list of fields


    We can create instances of Point2D just as we would with any class (since it is a class)

    pt = Point2D(10, 20)

    The variable name that we use to assign to the class generated and returned by namedtuple is arbitrary

    Pt2D = namedtuple("Point2D", ['x', 'y'])
    pt = Pt2D(10, 20)


    ------------------

    Pt2DAlias = namedtuple("Point2D", ['x', 'y'])


    variable: Pt2DAlias -> class: Point2D 0xFF900

    This is the same concept as aliasing a function, or assigning a lambda function to a variable name! <-- yeah, right


------------------ Generating Named Tuples Classes ------------------

    There are many ways we can provide the list of field names to the namedtuple function

    - a list of string
    - a tuple of strings            <- in fact any sequence, just remember that order matters!
    - a single string with the field names separated by whitespace or commas

    namedtuple("Point2D", ['x', 'y'])
    namedtuple("Point2D", ('x', 'y'))

    namedtuple("Point2D", 'x, y')
    namedtuple("Point2D", 'x y')

------------------ Instantiating named tuples ------------------

    After we have created a named tuples class, we can instantiate them just like an ordinary class

    In fact, the __new__ method of the generated class uses the field names we provided as param names

    Point2D = namedtuple('Point2D', 'x y')
    
    ----- Positional Arguments
    pt1 = Point2D(10, 20)

    ----- Keyword arguments
    pt2 = Point2D( x=10, y=20)


------------------ Accessing Data in a Named Tuple ------------------

    Since named tuples are also regular tuples, we can still handle them just like any other tuples
    - by index
    - slice
    - iterate

    Point2D = namedtuple("Point2D", "x y")

    pt1 = Point2D(10, 20)                   isinstance(pt1, tuple) -> True

            x, y = pt1
            x = pt1[0]

            for e in pt1:
                print(e)
            
    But now in addition we can also access the data using the field names:


        Point2D = namedtuple("Point2D", "x y")

        pt1 = Point2D(10, 20) 

        pt1.x -> 10
        pt2.y -> 20

    Since namedtuple generated classes inherit from tuple   class Point2D(tuple):


    pt1 is a tuple, and is therefore immutable! <----- hoah! 

    pt1.x = 100 will not work! 


------------------ The rename keyword-only argument for namedtuple ------------------

    Remember that field names for named tuples must be valid identifiers, but cannot start with an underscore

    That would not work: Person = namedtuple("Person", 'name age _ssn")
                                                                    _ssn - you can not use "_"

    namedtuple has a keyword-only argument, rename          (default to False)
    that will automatically rename any invalid field name

    uses convention: _{position in list of field names}

    This will now work:

    Person = namedtuple("Person", 'name age _ssn', rename=True)

    And the actual field names would be

    name age _2


------------------ Introspection ------------------

    We can easily find out the field names in a named tuple generated class

    class property -> _fields

    Person = namedtuple('Person', 'name age _ssn', rename=True)

    Person._fields  -> ('name', 'age', '_2')


    Remember that namedtuple is a class factory, i.e. it generators a class

    We can actually see what the code for that is, using the class property _source

    Point2D = namedtuple('Point2D', 'x y')
    Point2D._source     <--- print it - next section


------------------ Extracting Named Tuple Values to a Dictionary ------------------

    Instance method: _asdict()

    that creates a dictionary of all the named values in the tuple


    Point2D = namedtuple("Point2D", "x y")
    pt1 = Point2D(10, 20)    

    pt1._asdict()   ->  {'x': 10, 'y': 20}





"""
