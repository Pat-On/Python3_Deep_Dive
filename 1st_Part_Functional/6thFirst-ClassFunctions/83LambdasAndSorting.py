"""
            Lambda and Sorting


"""


# print(help(sorted))

l = [1, 5, 10, 4, 9, 6]
print(sorted(l))


l = ["c", "B", 'a', "D"]

print(sorted(l))  # by character code

print(sorted(l, key=lambda s: s.upper()))


d = {"def": 300, "abc": 200, "ghi": 100}

print(sorted(d))
print(sorted(d, key=lambda e: d[e]))

print(sorted(d, key=lambda e: d[e], reverse=True))


# imaginary number - sorting objects that does not have implemented sorting

def dist_sq(x):
    return (x.real) ** 2 + (x.imag) ** 2


l = [3+3j, 1-1j, 0, 3+0j]

print(sorted(l, key=dist_sq))
print(sorted(l, key=lambda x: (x.real) ** 2 + (x.imag)**2))


l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']

print(sorted(l, key=lambda s: s[-1]))
# python has stable sort - so it mean that if you have the same values
# python will retain the original order
