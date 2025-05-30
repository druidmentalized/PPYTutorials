import math


class Shape:
    def area(self, *args) -> float:
        raise NotImplementedError("Method is not implemented in base class")

class Circle(Shape):
    def area(self, radius) -> float:
        if radius <= 0:
            raise ValueError("Radius must be positive")
        return math.pi * radius ** 2

class Rectangle(Shape):
    def area(self, length, width=0) -> float:
        if width == 0:
            width = length
        if width <= 0:
            raise ValueError("Side must be positive")
        return length * width

circle = Circle()
print(f"Circle area: {circle.area(15)}")

rectangle = Rectangle()
print(f"Rectangle area: {rectangle.area(10)}")
print(f"Rectangle area: {rectangle.area(10, 5)}")
