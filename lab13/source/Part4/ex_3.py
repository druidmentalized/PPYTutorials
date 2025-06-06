class Box:
    def __init__(self, volume):
        self.volume = volume

    def __lt__(self, other) -> bool:
        return self.volume < other.volume

    def __gt__(self, other) -> bool:
        return self.volume > other.volume

    def __le__(self, other) -> bool:
        return self.volume <= other.volume

# a)
b1 = Box(10)
b2 = Box(20)
b3 = Box(10)

# b) + c)
print(b1 < b2)
print(b2 > b3)
print(b1 <= b3)