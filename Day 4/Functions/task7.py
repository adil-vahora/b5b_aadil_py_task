import time

def timer(function):
    def wrapper():
        start = time.time()

        function()

        end = time.time()
        print("Time taken:", end - start, "seconds")

    return wrapper


@timer
def calculate_sum():
    total = 0

    for i in range(1, 1000001):
        total += i

    print("Sum:", total)


calculate_sum()