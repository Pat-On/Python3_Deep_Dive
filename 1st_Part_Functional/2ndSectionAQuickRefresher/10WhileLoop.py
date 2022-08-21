i = 0

while i < 5:
    print(i)
    i += 1


min_length = 2
# name = input("Please write your name: ")

# while not (len(name) >= min_length and name.isprintable() and name.isalpha()):
#     name = input("Please enter your name: ")

# print("Hello, {0}".format(name))

# better way
# while True:
#     name = input("Please enter your name: ")
#     if len(name) >= min_length and name.isprintable() and name.isalpha():
#         break

# print("Hello, {0}".format(name))


# else statement in while

l = [1, 2, 3]
val = 10


found = False
idx = 0

while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)

print(l)


# other way:
val2 = 100
while idx < len(l):
    if l[idx] == val2:
        break
    idx += 1

else:
    # it will run only if we are not going to go out of while by break
    l.append(val2)

print(l)
