class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width * self.height == other.width * other.height


rectangle1 = rectangle(4, 6)
rectangle2 = rectangle(3, 8)

print(rectangle1 == rectangle2)