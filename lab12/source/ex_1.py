class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self) -> None:
        print(f"Car: {self.make}, {self.model}, {self.year}")

car = Car("Ford", "Mustang", 1999)
car.display_info()