# import module135

# print(f"loading 135......py: __name__ = {__name__}")

import timing

code = '[x**2 for x in range(1_000)]'

results = timing.timeit(code, 100)
print(results)
