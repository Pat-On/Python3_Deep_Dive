"""
                BOOLEANS
        Booleans Operators in Python


Booleans Operator and Truth Values

    Boolean Algebra

Normally, Boolean operators are defined in operate on and return Boolean values

    True or False -> True

    But every object in PYthon has a truth value (truthiness)
        so, for any object X and Y, we could also write: bool(X) and bool(Y)
                                                            We do not have to write bool just:
                                                                X and Y
        So what is returned when evaluating these expressions?
            A Boolean? No!


********************************************************************************************************

                                            Definition of or in Python

    x or y              If X is truthy, returns X, otherwise returns Y

    Does this work as expected when X and Y are Boolean values?

    x   y               Rule                        result
    0   0           X is False, so return Y             0
    0   1           X is False, so return Y             1
    1   0           X is True, so return X              1
    1   1           X is True, so return X              1

    If X is truthy, returns X, otherwise evaluates Y and returns it <== short circuiting


********************************************************************************************************

                                            Definition of and in Python

x and y          If X is falsy, return X, otherwise return Y

Does this work as expected when X and Y are Boolean values?

    x   y               Rule                        result
    0   0           X is False, so return x             0
    0   1           X is False, so return x             0
    1   0           X is True, so return Y              0
    1   1           X is True, so return Y              1

if X is falsy, returns X, otherwise evaluates Y and returns it


********************************************************************************************************

Consequence: or

    x or y              If X is truthy, returns X, otherwise returns Y


    x               Y                   x or y
    None            "N/A"               "N/A"
    ""              "N/A"               "N/A"
    "hello"         "N/A"               "N/A"

a = s or "N/A"  if s is None  a -> N/A
                if s is ""    a -> N/A
                if s is a string
                with characters     a -> s

i.e. a will either be s or "N/A" if s is None or an empty string


example:
We can expand this further:

a = s1 or s2 or s3 or "N/A"

in this case, a wil be equal to the first truthy value (left to right evaluation)
and is guaranteed to have a value, since "N/A" is truthy

Example:
We have an integer variable a that cannot be zero - if it is zero, we want to set it to 1

a = a or 1


x and y          If X is falsy, return X, otherwise return Y
Consequence of and

x and y          If X is falsy, return X, otherwise return Y


x       y           x and y
10      20/x            2
0       20/x            0


Seems like we are able to avoid a division by zero error using the and operator

x = a and total/a


********************************************************************************************************

example

Computing an average

sum, n  Sometimes n is non-zero, sometimes it is

    in either case:     avg = n and sum/n

Example

    You want to return the first character of a string s, or an empty string if the string is None or empty

Option 1                      Option 2                      
    if s:                                           
        return s[0]            return s and s[0]   -> does not handle None case                          
    else:                                           
        return ""              return (s and s[0]) or ""



********************************************************************************************************

The Boolean not

not is a built-in function that returns a Boolean value

    not x -> True if x is falsy
          -> False if x is truthy

    [] -> falsy
        not [] -> True


    [1, 2] -> True
        not [1, 2] -> False

    





"""
