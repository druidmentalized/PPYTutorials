class Animal:
    def sound(self):
        raise NotImplementedError("Method is not implemented in base class")

class Lion(Animal):
    def sound(self):
        print("Roar!")

class Elephant(Animal):
    def sound(self):
        print("Sweet!")

lion = Lion()
elephant = Elephant()
lion.sound()
elephant.sound()