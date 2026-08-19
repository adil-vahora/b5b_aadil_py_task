temperatures = [0, 10, 20, 30, 40]

fahrenheit = list(
    map(lambda c: (c * 9/5) + 32, temperatures)
)

print(fahrenheit)