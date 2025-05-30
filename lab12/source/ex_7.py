class Dog:
    count = 0

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    @classmethod
    def print_count(cls):
        return cls.count

dog1 = Dog("Dog1")
dog2 = Dog("Dog2")
dog3 = Dog("Dog3")

print(f"Dog count {Dog.print_count()}")