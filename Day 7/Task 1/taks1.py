import random

numbers = []

for i in range(5):
    number = random.randint(10, 50)
    numbers.append(number)

numbers.sort()

print("Sorted list:", numbers)