import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print("Time taken:", end - self.start, "seconds")


with Timer():
    for i in range(1000000):
        pass