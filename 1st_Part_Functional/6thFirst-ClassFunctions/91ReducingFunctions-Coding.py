# Reducing Functions in Python


from functools import reduce
l = [5, 8, 6, 10, 9]


def _max(a, b): return a if a > b else b


def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result


print(max_sequence(l))

print("*" * 80)


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


print(_reduce(_max, l))


def _min(a, b): return a if a < b else b


print(_reduce(_min, l))
print("*" * 80)

# ----------------------------------------------------------------

print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))
print(reduce(lambda a, b: a + b, l))
print("*" * 80)
# ----------------------------------------------------------------

l = []
print(reduce(lambda x, y: x*y, l, 0))


# ----------------------------------------------------------------

def _reduce(fn, sequence, initial=0):
    result = initial
    for x in sequence:
        result = fn(result, x)
    return result


l = [5, 8, 6, 10, 9]

print(_reduce(lambda a, b: a+b, l, 100))
print(_reduce(lambda a, b: a*b, l, 1))

print(_reduce(lambda a, b: a*b, {1, 2, 3, 4}, 1))
