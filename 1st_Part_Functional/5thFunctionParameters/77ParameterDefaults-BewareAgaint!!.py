"""


"""


def add_item(name, quantity, unit, grocery_list=[]):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    #  when you are mutating, sometimes is better to not return mutable object
    return grocery_list


store_1 = add_item('bananas', 2, 'units')
add_item('grapes', 1, 'bunch', store_1)
print(store_1)

print("**" * 10)


def add_item(name, quantity, unit, grocery_list=[]):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list


del store_1


store_1 = add_item('bananas', 2, 'units')
add_item('grapes', 1, 'bunch', store_1)

store_2 = add_item('milk', 1, 'gallon')
# because of the way how function is validated:
# def -> then all default values
print(store_1)
print(store_2)


# Solution
def add_item(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list


store_1 = add_item('bananas', 2, 'units')
add_item('grapes', 1, 'bunch', store_1)
store_2 = add_item('milk', 1, 'gallon')
store_2

print(store_1, "|", store_2)

print("*" * 10)


def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorial(n-1)


factorial(30)


def factorial(n, cache={}):
    # caching results
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n-1, cache=cache)
        cache[n] = result
        return result


factorial(3)
cache = {}
print("*" * 10)
factorial(30, cache=cache)
print(cache)
print("*" * 10)
factorial(30, cache=cache)
print(cache)
