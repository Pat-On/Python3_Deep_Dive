# Relevant Python 3.9 Changes

# Additional info - notebook

from collections import ChainMap
import math
import zoneinfo
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import dateutil
import pytz

now_utc_naive = datetime.utcnow()
print(now_utc_naive)

now_utc_aware = now_utc_naive.replace(tzinfo=timezone.utc)
print(now_utc_aware)

print(pytz.utc.localize(datetime.utcnow()))

tz_melbourne = pytz.timezone('Australia/Melbourne')
print(tz_melbourne)

tz_zi_dublin = ZoneInfo("Europe/Dublin")
print(tz_zi_dublin)


# The `math` module already had the `gcd` function to calculate the great common divisor of two numbers:

print(math.gcd(27, 45))
print(math.gcd(27, 45, 18, 15))

print(math.lcm(2, 3, 4))


# Dictionary Unions

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 30, 'd': 40}

print({**d1, **d2})

# We could also use the `ChainMap` function in the `collections` module:
# from collections import ChainMap
merged = ChainMap(d1, d2)

print(merged['a'], merged['c'], merged['d'])


# As you can see, in the `ChainMap`, the firest occurrence of the key is used - so in this case `c` comes from `d1`, not `d2`.


s1 = {'a', 'b', 'c'}
s2 = {'c', 'd'}

print(s1 | s2)
