from functools import reduce

numbers = [15, 42, 8, 67, 23, 91]

largest = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print("Largest:", largest)