# Closures Applications (Part 1)


from time import perf_counter


class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


a = Averager()

print(a.add(10))
print(a.add(20))
print(a.add(30))


def averager():
    numbers = []

    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add


a = averager()

print(a(10))
print(a(20))
print(a(30))


def averager():
    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1

        return total / count
    return add


b = averager()

print(b(10))
print(b(20))
print(b(30))

print(b.__closure__, b.__code__.co_freevars)


#

print(perf_counter())


class Timer:
    def __init__(self):
        self.start = perf_counter()

    # changing object into callable
    def __call__(self):
        return perf_counter() - self.start


t1 = Timer()

print(t1())


def timer():
    start = perf_counter()

    def poll():
        return perf_counter() - start

    return poll


t2 = timer()


print(t2())
