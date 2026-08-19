def make_counter(start):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter1 = make_counter(10)
counter2 = make_counter(100)

print(counter1())
print(counter1())
print(counter1())

print(counter2())
print(counter2())