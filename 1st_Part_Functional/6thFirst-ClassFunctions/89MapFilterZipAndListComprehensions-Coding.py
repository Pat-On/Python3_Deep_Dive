def fact(n):
    return 1 if n < 2 else n * fact(n-1)


print(fact(3))

print(fact(4))

print(map(fact, [1, 2, 3, 4, 5]))
l = list(map(fact, [1, 2, 3, 4, 5]))
print(l)

print("-" * 40, "1")

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, l)
print(list(result))

print("-" * 40, "2")

l = [1, 2, 3, 4, 5]
result = [fact(i) for i in l]
print(result)


print("-" * 40, "3")

l1 = 1, 2, 3
l2 = [10, 20, 30]
l3 = ('a', 'b', 'c')
# zip is returning generator
print(list(zip(l1, l2, l3)))

print("-" * 40, "4")

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
result = [i + j for i, j in zip(l1, l2)]
print(result)
