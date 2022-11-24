# Random Samples

from collections import Counter
import random

print(random.choices(list("abc"), k=10))


l = list(range(10))
print(l)

# repetition
print(random.choices(l, k=5))


suits = 'C', "D", "H", "S"

ranks = tuple(range(2, 11)) + tuple("JQKA")

print(suits, ranks)


deck = []
for suit in suits:
    for rank in ranks:
        deck.append(str(rank) + suit)

print(deck)


deck = [str(rank) + suit for suit in suits for rank in ranks]
print(deck)


print(Counter(random.choices(deck, k=20)))


# no repetition
print(Counter(random.sample(deck, k=20)))

# no repetition
print(Counter(random.sample(deck, k=52)))
