# A simple function timer

import time


def time_it(fn, *args, rep=1, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)


time_it(print, 1, 2, 3, sep=" - ", end=" ***", rep=10)


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()

    return (end - start) / rep


timeValue = time_it(print, 1, 2, 3, sep=" - ", end=" ***", rep=10)
print(timeValue)


def computer_powers_1(n, *m, start=1, end):
    results = []
    for i in range(start, end):
        results.append(n**i)

    return results


def computer_powers_2(n, *, start=1, end):
    return [n**i for i in range(start, end)]


def computer_powers_3(n, *, start=1, end):
    # generator
    return (n**i for i in range(start, end))


print(time_it(computer_powers_1, 2, start=0, end=20000, rep=5))
print(time_it(computer_powers_2, 2, start=0, end=20000, rep=5))
print(time_it(computer_powers_3, 2, start=0, end=20000, rep=5))
