# Nonlocal Scopes

"""
In fact, any level of nesting is supported since Python just keeps looking in enclosing scopes until it finds what it needs (or fails to find it by the time it
 finishes looking in the built-in scope, in which case a runtime error occurrs.)

"""


def outer_func():
    x = 'hello'

    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()


outer_func()

print("*" * 40)


def outer():
    x = 'hello'

    def inner1():
        x = 'python'

        def inner2():
            nonlocal x
            x = 'monty'
        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer:', x)


outer()

print("*" * 40)

x = 100


def outer():
    x = 'python'  # masks global x

    def inner1():
        nonlocal x  # refers to x in outer
        x = 'monty'  # changed x in outer scope

        def inner2():
            global x  # refers to x in global scope
            x = 'hello'
            print('inner1 (before):', x)
            inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer', x)


outer()
print(x)
