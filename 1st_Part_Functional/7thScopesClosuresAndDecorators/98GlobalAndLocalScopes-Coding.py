# Global and Local Scopes
# Interesting Details
a = 10


def my_func(n):
    c = n ** 2
    return c


def my_func(n):
    print('global:', a)
    c = a ** n
    return c


print(my_func(2))


def my_func(n):
    a = 2
    c = a ** 2
    return c


print(a)
print(my_func(3))
print(a)


def my_func(n):
    global a
    a = 2
    c = a ** 2
    return c


print(a)
print(my_func(3))
print(a)

"""
If you have experience in some other programming languages you may be wondering
 if loops and other code "blocks" have their own local scope too. 
 For example in Java, the following would not work:

``for (int i=0; i<10; i++) {
    int x = 2 * i;
}
system.out.println(x);
``

But in Python it works perfectly fine:
"""

for i in range(10):
    x = 2 * i
print("x", x)
