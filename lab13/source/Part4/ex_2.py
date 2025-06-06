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
    
# a)
p1 = Point(1, 2)
p2 = Point(3, 4)

# b)
print(p1 + p2)

# c)
print(f"Are given points equal? {"Yes" if p1 == p2 else "No"}")