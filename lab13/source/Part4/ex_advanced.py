class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other: "Point") -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __mul__(self, multiplier: int | float) -> "Point":
        return Point(self.x * multiplier, self.y * multiplier)

    def __rmul__(self, multiplier: int | float) -> "Point":
        return self.__mul__(multiplier)

p = Point(1, 2)
print(p * 3)
print(3 * p)