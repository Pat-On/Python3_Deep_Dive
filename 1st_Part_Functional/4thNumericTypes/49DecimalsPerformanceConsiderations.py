"""
                Decimals
    Ease and Performance Considerations

There are some drawbacks to the Decimal class vs the float class

    - not as easy to code: construction via strings or tuples
    - not all mathematical functions that exist in the math module have a Decimal counterpart
    - more memory overhead
    - performance: much slower than floats (relatively)

"""
from decimal import Decimal
import sys

import time

# memory footprint

a = 3.1415
b = Decimal('3.1415')
# 24
print(sys.getsizeof(a))
# 104
print(sys.getsizeof(b))

# pseudo timing


def run_float(n=1):
    for i in range(n):
        a = 3.1415


def run_decimal(n=1):
    for i in range(n):
        a = Decimal("3.1415")


n = 10_000_000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()

print(end - start)

n = 10_000_000
start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()

print(end - start)

# adding
print("Adding")


def run_float_add(n=1):
    a = 3.1415
    for i in range(n):
        a + a


def run_decimal_add(n=1):
    a = Decimal("3.1415")
    for i in range(n):
        a + a


n = 10_000_000
start = time.perf_counter()
run_float_add(n)
end = time.perf_counter()

print(end - start)

n = 10_000_000
start = time.perf_counter()
run_decimal_add(n)
end = time.perf_counter()

print(end - start)
