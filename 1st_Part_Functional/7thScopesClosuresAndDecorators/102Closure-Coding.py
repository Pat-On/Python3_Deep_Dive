def outer():
    x = 'python'

    def inner():
        print(x)
    return inner


fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)

print("*" * 40)


def outer():
    x = [1, 2, 3]
    print('outer:', hex(id(x)))

    def inner():
        print('inner:', hex(id(x)))
        print(x)
    return inner


fn = outer()
fn()


print("*" * 40)


def outer():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2


fn1, fn2 = outer()
print(fn1.__closure__, fn2.__closure__)


# Beware!
"""

Remember when I said the captured variable is a 
reference established when the closure is created, but the value is looked up only once the function is called?

This can create very subtle bugs in your program.

Consider the following example where we want to create some functions that can
 add 1, 2, 3, 4 and to whatever is passed to them.
"""

print("*" * 40)


def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x: x + n)
    return adders


adders = create_adders()

print(adders)

print(adders[3](10))
print(adders[0](10))

"""When the lambdas are **created** their `n` is the `n` used in the loop - the **same** `n`!!"""

print(adders[0].__code__.co_freevars)
print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[2].__closure__)
print(adders[3].__closure__)
# As we can see the memory address of the singleton integer 4, is what that cell is pointing to.
print(hex(id(4)))


# Solution
print("*" * 40)
"""
If you want to use a loop to do this and not end up using the same cell 
for each of the free variables, we can use a simple trick that forces 
the evaluation of `n` at the time the closure is **created**, 
instead of when the closure function is evaluated.

We can do this by creating a parameter for `n` in our lambda whose default 
value is the current value of `n` - remember from an earlier video
 that parameter defaults are evaluated when the function is created, not called.
"""


def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x, step=n: x + step)
    return adders


adders = create_adders()

print(adders[0].__closure__)
print(adders[0].__code__.co_freevars)

print(adders[0](10))
print(adders[1](10))
print(adders[2](10))
print(adders[3](10))

"""
You just need to understand that since the default values 
are evaluated when the function (lambda in this case)
 is **created**, the then-current `n` value is assigned
  to the local variable `step`. So `step` will not change every
   time the lambda is called, and since n is not referenced inside 
   the function (and therefore evaluated when the lambda is called),
    `n` is not a free variable.

"""
