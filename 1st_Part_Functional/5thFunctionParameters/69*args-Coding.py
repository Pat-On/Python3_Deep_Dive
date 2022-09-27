a, b, *c = 10, 20, 'a', 'b'
print(a, b)
print(c)


def func1(a, b, *args):
    print(a)
    print(b)
    print(args)  # tuple


func1(1, 2, 'a', 'b')


# Different approaches to div by 0

def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count


avg()
avg(2, 2, 4, 4)


def avg(*args):
    count = len(args) + 1
    total = a + sum(args)
    return count and total/count


avg()
avg(2, 2, 4, 4)


def avg(a, *args):
    count = len(args) + 1
    total = a + sum(args)
    return total/count


avg(0)
avg(2, 2, 4, 4)
