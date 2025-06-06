class Car:
    wheels_num = 4

    def __init__(self, color: str) -> None:
        self.color = color

# a)
car1 = Car("red")
car2 = Car("blue")

# b)
car1.wheels_num = 6

# c)
def print_cars_info(car_1: Car, car_2: Car):
    print(f"Color: {car_1.color}")
    print(f"Wheel count: {car_1.wheels_num}")
    print(f"Color: {car_2.color}")
    print(f"Wheel count: {car_2.wheels_num}")
print_cars_info(car1, car2)

# d)
Car.wheels_num = 8
print_cars_info(car1, car2)