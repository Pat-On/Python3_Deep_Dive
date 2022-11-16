# Relevant Python changes 3.10

# 1 Error messaging for errors
# Structural pattern matching

from itertools import zip_longest


def respond(language):
    match language:
        case "Java":
            return "Hmm, coffee!"
        case "Python":
            return "I'm not scared of snakes!"
        case "Rust":
            return "Don't drink too much water!"
        case "Go":
            return "Collect $200"
        case _:
            return "I'm sorry..."


print(respond("Python"))
print(respond("Go"))

# For example, you can have multiple pattern matching:


def respond(language):
    match language:
        case "Java" | "Javascript":
            return "Love those braces!"
        case "Python":
            return "I'm a lumberjack and I don't need no braces"
        case _:
            return "I have no clue!"


print(respond("Java"))


symbols = {
    "F": "\u2192",
    "B": "\u2190",
    "L": "\u2191",
    "R": "\u2193",
    "pick": "\u2923",
    "drop": "\u2925"
}


def op(command):
    match command:
        case "move F":
            return symbols["F"]
        case "move B":
            return symbols["B"]
        case "move L":
            return symbols["L"]
        case "move R":
            return symbols["R"]
        case "pick":
            return symbols["pick"]
        case "drop":
            return symbols["drop"]
        case _:
            raise ValueError(f"{command} does not compute!")


print(op("move L"))

# We could use something called **capturing**
# matched sub-patterns to simply our code somewhat:


def op(command):
    match command:
        # capturing matched sub-patterns
        case ["move", ("F" | "B" | "L" | "R") as direction]:
            return symbols[direction]
        case "pick":
            return symbols["pick"]
        case "drop":
            return symbols["drop"]
        case _:
            raise ValueError(f"{command} does not compute!")


print(op(["move", "B"]))


try:
    op("fly")
except ValueError as ex:
    print(ex)

# There are many ways we could solve this,
#  but pattern matching on multiple values can be really useful here.


def op(command):
    match command:
        case ['move', *directions]:
            # nice!
            return tuple(symbols[direction] for direction in directions)
        case "pick":
            return symbols["pick"]
        case "drop":
            return symbols["drop"]
        case _:
            raise ValueError(f"{command} does not compute!")


print(op(["move", "F", "F", "L"]))

print([
    op(["move", "F", "F", "L"]),
    op("pick"),
    op(["move", "R", "L", "F"]),
    op("drop"),
])


"""

We would rather just get our custom `ValueError`. 
To do this we can place a **guard** on our `case` for the `move` command,
 that will not only do the match but also test an additional condition:"""


def op(command):
    match command:
        case ['move', *directions] if set(directions) < symbols.keys():
            return tuple(symbols[direction] for direction in directions)
        case "pick":
            return symbols["pick"]
        case "drop":
            return symbols["drop"]
        case _:
            raise ValueError(f"{command} does not compute!")


try:
    op(["move", "up"])
except Exception as ex:
    print(type(ex), ex)


# The `zip` Function

l1 = ['a', 'b', 'c']
l2 = [10, 20, 30, 40]

print(list(zip(l1, l2)))

# from itertools import zip_longest

print(list(zip_longest(l1, l2, fillvalue='???')))


l1 = (i ** 2 for i in range(4))
l2 = (i ** 3 for i in range(3))


# It will use generator
# len(list(l1)) == len(list(l2))

# exception when one of the arguments is longer
try:
    # side node - zip is of course generator
    list(zip(l1, l2, strict=True))
except ValueError as ex:
    print(ex)

# So why is this useful?

# In **many** cases, our code zips iterables that we expect to be of the same length.
#  To avoid bugs in our program, we should check that this condition is true,
# otherwise zip will silently just zip based on the shortest one.
# But as we saw with iterators, that can be difficult to do without exhausting
#  the very iterators we are trying to zip. (it can be done, it's just more code).

# So, if you are one of the lucky devs that gets to write Python 3.10 (or higher :-) )
#  code, you can just use `strict` whenever you zip things together and expect that
#  they are all of the same length. Much easier to do it this way
#  (and, as we discuss in Exception handling, falls into the category of
# "ask forgiveness later" which we saw was the preferred way (in general)
# to handle exceptions in our apps, as opposed to the "look before you leap"
# approach we would have to use to test the argument lengths.
