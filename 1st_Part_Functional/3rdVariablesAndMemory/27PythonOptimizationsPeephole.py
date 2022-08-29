"""

            Python Optimizations
                Peephole

    
    This is another variety of optimizations that can occur at compile time
    
        Constant expressions
            numeric calculations
                    24 * 60 
                    Python will actually pre-calculate 24 * 60 -> 1440
                    (expression that evaluate to expressions)

        short sequences length < 20
                (1, 2) * 5 -> (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
                'abc' * 3 -> "abcabcabc
                "hello" + "world" -> "helloworld"

        
        but not "the quick brown fox" * 10  (more than 20 characters)


    Membership Tests: Mutables are replaced by Immutables:
        when membership tests such as:
            if e in [1, 2, 3]:   -> 
                are encountered, the [1, 2, 3] constant, is replaced by its immutable counterpart

                (1, 2, 3) tuple
        list -> tuples
        sets -> frozensets

    Set membership is much faster than list or tuple membership (sets are basically like dictionaries)

    So, instead of writing
        if e in [1, 2, 3]:   or if e in (1, 2, 3)

            write if e in {1, 2, 3}   <-- more efficient

"""
