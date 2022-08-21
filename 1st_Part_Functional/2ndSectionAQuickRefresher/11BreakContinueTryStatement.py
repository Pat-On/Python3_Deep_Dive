a = 10
b = 0


try:
    a/b
except ZeroDivisionError:
    print("division by zero")
finally:
    print("this always execute")


c = 0
d = 20
# d = 2

while c < 4:
    print("_" * 40)
    c += 1
    d -= 1
    try:
        c/d
    except ZeroDivisionError:
        print("division by zero {0} and {1}".format(c, d))
        continue
    finally:
        print("this always execute {0} and {1}".format(c, d))

    print("{0}, {1} - main loop".format(c, d))

else:
    print("Code executed without a zero division error")
