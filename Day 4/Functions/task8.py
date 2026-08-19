def require_positive(function):
    def wrapper(*args):
        for number in args:
            if number <= 0:
                print("Error: All numbers must be positive.")
                return

        return function(*args)

    return wrapper


@require_positive
def divide(a, b):
    print("Result:", a / b)


divide(10, 2)
divide(10, -2)
divide(10, 0)