a = 1, 2, 3
print(type(a))

b = 1,
print(type(b))

c = tuple()
print(type(c))


l = [1, 2, 3, 4]
a, b, c, d = l
print(a, b, c, d)


a = 10
b = 20
print("a={0}, b={1}".format(a, b))

tmp = a
a = b
b = tmp
print("a={0}, b={1}".format(a, b))

a = 10
b = 20
print("a={0}, b={1}".format(a, b))

# called sometimes parallel assignment
a, b = b, a
print("a={0}, b={1}".format(a, b))

(a, b) = (b, a)
print("a={0}, b={1}".format(a, b))

dict1 = {'p': 1, 'y': 2, 't': 3, 'h': 4, 'o': 5, 'n': 6}
print(dict1)
print(dict1)

a, b, c, d, e, f, = dict1.values()

print(a, b, c, d, e, f,)
a, b, c, d, e, f, = dict1.items()

print(a, b, c, d, e, f,)
print(type(a))
