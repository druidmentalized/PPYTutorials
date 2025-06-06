class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height
    
# a)
rect = Rectangle(5, 10)

# b)
print("Area:", rect.area)

# c)
try:
    rect.area = 100
except AttributeError as e:
    print("Error:", e)

# d)
rect._width = 20
rect._height = 4
print("Updated area:", rect.area)