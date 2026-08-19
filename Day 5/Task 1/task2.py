class Counter:
    total_count = 0

    def __init__(self):
        Counter.total_count += 1

    @classmethod
    def get_count(cls):
        return cls.total_count


c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()

print("Total objects:", Counter.get_count())