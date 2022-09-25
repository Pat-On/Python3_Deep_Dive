s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
print(s1.union(s2).union(s3).union(s4))
print(s1.union(s2, s3, s4))


print({*s1, *s2, *s3, *s4})


*l, = (1, 2, 3)
print(type(l), l)
