# Sentinel Values for Parameter Defaults

"""
Often we specify the default for a function parameter as `None`. 
This allows to determine if the user specified an argument for that parameter or not. 

There's a potential issue here!

What happens if we need to differentiate between the following:
* a non-`None` value was provided for the argument
* a `None` value *was* provided for the argument
* the argument was not provided at all

"""


"""
The easiest thing to do is to create an instance of the `object` class.
 This is guaranteed to result in an object that the user cannot pass to u
  (they have no way of getting their hands on that object 
  - or at least not without the absolute intention to do so). 
  (remember that Python will always allow us to shoot ourselves 
  in the foot if we try hard enough :-) )


"""
_sentinel = object()


def validate(a=_sentinel):
    if a is not _sentinel:
        print('Argument was provided')
    else:
        print('Argument was not provided')


validate(100)
validate(None)
validate(object())

print("*" * 40)
"""
Now, instead of using a separate variable to hold the sentinel value (`_sentinel`),
 we can introspect the function to find out what the default sentinel value is:

"""


def validate(a=object()):
    default_a = validate.__defaults__[0]
    if a is not default_a:
        print('Argument was provided')
    else:
        print('Argument was not provided')


validate(100)
validate(None)
validate(object())
validate()
print("*" * 40)

# We can expand this to several parameters as well if we need to, using either method:


def validate(a=object(), b=object(), *, kw=object()):
    default_a = validate.__defaults__[0]
    default_b = validate.__defaults__[1]
    default_kw = validate.__kwdefaults__['kw']

    if a is not default_a:
        print('Argument a was provided')
    else:
        print('Argument a was not provided')

    if b is not default_b:
        print('Argument b was provided')
    else:
        print('Argument b was not provided')

    if kw is not default_kw:
        print('Argument kw was provided')
    else:
        print('Argument kw was not provided')


validate(100, 200, kw=None)
validate(100, 200)
validate(b=100)
validate()
