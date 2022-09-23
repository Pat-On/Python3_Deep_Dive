# Boolean Operator


# X or Y: if X is truthy , return X, otherwise evaluates Y and returns it


print("a" or [1, 2])
print("" or [1, 2])
print(1 or 1/0)


# getting default values:
s1 = None
s2 = ""
s3 = "abc"

s1 = s1 or "n/a"
s2 = s2 or "n/a"
s3 = s3 or "n/a"

print(s1, s2, s3)


# X and Y: if X is falsy , return X, otherwise evaluates Y and returns it
s1 = None
s2 = ""
s3 = "abc"


print((s1 and s1[0]) or "default value")
print((s2 and s2[0]) or "")
print((s3 and s3[0]) or "")


#  not operator
