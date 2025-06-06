class Dog:
    dog_count = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Dog.dog_count += 1

    @staticmethod
    def show_created_count():
        print(f"{Dog.dog_count} were created so far.")
        

# a)
dog1 = Dog("Dog1")
dog2 = Dog("Dog2")
dog3 = Dog("Dog3")

# b)
Dog.show_created_count()

# c)
print(f"First dog name: {dog1.name}")
print(f"First dog name: {dog2.name}")
print(f"First dog name: {dog3.name}")

