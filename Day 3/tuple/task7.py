def make_frozenset(items):
    return frozenset(items)

numbers = [1, 2, 3, 2, 1]

result = make_frozenset(numbers)

print(result)


'''A frozenset behaves like a set but cannot be modified,
 which makes it safe to use as a dictionary key or inside another set'''