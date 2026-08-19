def marks(m):
    return (min(m), max(m), sum(m) / len(m))

m = [70, 85, 20, 40, 95,77]

low, high, ave = marks(m)

print(low)
print(high)
print(ave)