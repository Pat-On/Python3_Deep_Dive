"""
            Tuples as Data Structure



    Tuples                              Lists                                   String
    -------------------------------------------------------------------------------------------
    Containers                          containers                              containers
    order matters                       order matters                           order matters
    *Heterogeneous*/homogeneous         Heterogeneous/*homogeneous*             Homogeneous
    indexable                           indexable                               indexable
    iterable                            iterable                                iterable

    immutable                           mutable                                 immutable
        fixed length                        length can change                       fixed length                        <-----
        fixed order                         order of elements can change            fixed order                         <-----
            cannot do in-place sorts            can do in-place sorts                   cannot do in-place sorts    
            cannot do in-place reversals        can do in-place reversals               cannot do in-place reversals    



                                ----Immutability of Tuples----

    elements cannot be added or removed
    the order of elements cannot be changed
    works well for representing data structures:
        Point: (10, 20)             1st element is the x-coordinate
                                    2nd element is the y-coordinate

        Circle: (0, 0, 10)          1st element is the x-coordinate of the center
                                    2nd element is the y-coordinate of the center
                                    3rd element is radius

        City("London", "UK", 8_780_000)


    The position of the data has meaning

                                ----Tuples as a data record----

    This of a tuple as a data record where the position of the data has meaning

        new_york = ("New York", "USA", 8_500_000)
        etc

    Because tuples, strings and integers are immutable, we are guaranteed
    that the data and data structure for london will never change! 

    new_york = ("New York", "USA", 8_500_000)   <- string immutable
                                                <- integer immutable   <- total lock down :>

    We can have a list of these tuples

    cities_list = [(tuple1),
                    (tuple2)]

                                ----Extracting data from Tuples----

    Since tuples are sequences just like strings and lists, we can retrieve items by index

    london = ("London", "UK", 8_780_000)
    city = london[0]            <--- index

    cities_list = [("London", "UK", 8_780_000),
                  ("London", "UK", 8_780_000)]

    total_population = 0
    for city in cities:
        total_population += city[2]


    You will notice how the list of cities is homogeneous (contains cities only) <-- normal concept!
    But a city (the tuple) is heterogeneous

                                ----extracting data from Tuples----

    We can also use tuple unpacking
    We actually already know how to do this - we covered this in the section on function arguments

    london = ("London", "UK", 8_780_000)        <-- coma is creating tuple
                packed three values into a tuple


    city, country, population = new_york        <--- unpacked tuples

    city, country, population = ("London", "UK", 8_780_000)
    city, country, population = "London", "UK", 8_780_000


                                ----Dummy Variables----

    This is something you are likely to run across when you look at python code that uses tuple unpacking

    sometimes we are only interested in a subset of the data fields in a tuple, not all of them

    Suppose we are interested only in the city name and the population:

    city, _, population = ("Beijing", "China", 21_000_000)

    _ is actual a legal variable name - so there is nothing special about it

    bu by convention, we use the underscore to indicate this is a variable we do not care about

    in fact, we could just have used:

    city, ignored, population = ("London", "UK", 8_780_000)


                                    ----Extended Unpacking----

    It is also used in extended unpacking too

    record = ("DJIA", 2018, 1, 19, 25987.35, 26071.72, 25942.83, 26071.72)
    symbol, year, month, day, open, high, low, close = record

    Let's say we are only interested in the symbol, year, month, day and close fields,

    We could do it this way: 
                    symbol = record[0]
                    year = record[1]                <--- looks really bad!
                    month = record[2]
                    day = record[3]
                    close = record[7]

        symbol, year, close = record[0], record[1], record[7]           <---- awful!


    
    symbol, year, month, day, *_, close = record
    1st,    2nd,    3rd, 4th, all other, last element

"""
