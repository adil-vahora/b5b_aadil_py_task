class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


point1 = Point(10, 20)
point2 = Point(10, 20)
point3 = Point(5, 10)

print(point1)
print(point1 == point2)
print(point1 == point3)