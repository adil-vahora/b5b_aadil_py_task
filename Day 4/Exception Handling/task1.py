def safe_division(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except TypeError:
        print("Error: Please use numbers only.")


print(safe_division(10, 2))
print(safe_division(10, 0))
print(safe_division(10, "2"))