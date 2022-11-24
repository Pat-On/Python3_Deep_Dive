# Random choices
# How would you pick a random element from a list?

# style from java - it is not pythonic
from time import perf_counter
from collections import namedtuple
import random
l = [10, 20, 30, 40, 50]

random_index = random.randrange(len(l))
print(l[random_index])


l = list(range(1000))

random.seed(0)
for i in range(10):
    print(l[random.randrange(len(l))])


# pythonic way

print(random.choice(l))

random.seed(0)
for _ in range(10):
    print(random.choice(l))


print("*" * 40)

randoms = [random.choice(l) for _ in range(5)]
print(randoms)


list_1 = list(range(1000))

print(random.choices(list_1, k=5))

for _ in range(5):
    print(random.choices(list_1, k=3))

print("*" * 40)


Freq = namedtuple('Freq', 'count freq')


def freq_counts(list_):
    total = len(list_)
    return {k: Freq(list_.count(k), 100 * list_.count(k)/total) for k in set(list_)}


list_2 = ['a', 'b', 'c']

print(freq_counts(random.choices(list_2, k=1000)))

print(freq_counts(random.choices(list_2, k=1_000, weights=(8, 1, 1))))


print("*" * 40)


"""
Only caution here is if you are generating random things on multiple threads 
- in which case you don't know when what thread is going to run and in that 
case you very well may end up with different random results from the various 
threads from run to run - even if you use a specific seed.

Here's one practical application of being able to skew random selections.

Let's say you want to know what's more efficient - guarding a divide by zero exception 
using a LBYL (look before you leap) approach, or EAFP (easier to ask for forgiveness
 than permission):
"""

denominators = random.choices([0, 1], k=1_000_000)

start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')


start = perf_counter()
for denominator in denominators:
    try:
        10 / denominator
    except ZeroDivisionError:
        continue

end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')

"""
As we can see it looks like the `try... except...` appeoach is slower.

But in reality, we expect that a zero will only occur 10% of the time.

So now we can test this using a skewed set of random denominators:

"""

denominators = random.choices([0, 1], k=1_000_000, weights=[1, 9])

start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')

start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator

end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')
