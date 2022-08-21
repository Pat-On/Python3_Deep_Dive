"""
                        Conditionals




"""


a = 10

if a < 5:
    print("a < 5")
elif a < 10:
    print("a < 10")
else:
    print("else")

"""

                Conditional Expression




"""
b = 5

print(a if (b == 5) else b)


""" ternary operator """


b = "a < 5" if a < 5 else "a >= 5"
print(b)
