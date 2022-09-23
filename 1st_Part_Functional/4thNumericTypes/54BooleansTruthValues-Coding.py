print(1, bool(1))
print(0, bool(0))
print(-1, bool(-1))

# so basically it is calling x.__bool__ or x.__len__

print((100).__bool__())
print(([1, 2, 3]).__len__())

print(bool(None))  # always false


a = [1, 2, 3]
if a is not None and len(a) > 0:
    print(a[0])
else:
    print("Nothing to see here")

a = []
if a:  # what is python doing: bool(a)
    print(a[0])
else:
    print("Nothing to see here...")


# be careful with:
a = [1, 2, 3]
if len(a) > 0 and a is not None:
    print(a[0])
else:
    print("Nothing to see here")

a = []
if len(a) > 0 and a is not None:
    print(a[0])
else:
    print("Nothing to see here")

# ERROR: TypeError: object of type 'NoneType' has no len()
# a = None
# if len(a) > 0 and a is not None:
#     print(a[0])
# else:
#     print("Nothing to see here")

# short circuiting:
a = None
if a is not None and len(a) > 0:
    print(a[0])
else:
    print("Nothing to see here")
