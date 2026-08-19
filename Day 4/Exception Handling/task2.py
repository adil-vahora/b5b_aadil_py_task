def get_value(items, index):
    try:
        return items[index]

    except IndexError:
        return None


numbers = [10, 20, 30]

print(get_value(numbers, 1))
print(get_value(numbers, 5))