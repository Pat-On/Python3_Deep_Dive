
# iterable - In python, an iterable is an object capable of returning values one at a time
# iterators and generators as well! :>

"""
    while loop is the closes in python to implementation of for loop in C like languages

    so many of code rewriten to python is done with while


"""


i = 0
while i < 5:
    print(i)
    i += 1
# i = None this is done automatically

print("-" * 40)

# // iterate through iterable
# it work more like for (const item of items) {} for (const item in items) {} in JS
for i in range(5):
    print(i)


print("-" * 40)

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

# continue, break is working in the same way like in if statements


print("-" * 40)
s = "hello"
for c in s:
    print(c)

# how to get index back?

print("-" * 40)


# naive approach:
i = 0
for c in s:
    print(i, c)
    i += 1


print("-" * 40)
# better solution
for i in range(len(s)):
    print(s[i], i)

print("-" * 40)
# better ++ solution <-- built in
for i, c in enumerate(s):
    print(i, c)
