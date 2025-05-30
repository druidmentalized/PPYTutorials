class Temperature:
    def __init__(self, celsius: int):
        self.celsius = celsius

    def display_temp(self):
        print(self.celsius)

    def to_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self) -> float:
        return self.celsius - 273.15

temp = Temperature(21)
temp.display_temp()
print(f"Temperature in farenheit: {temp.to_fahrenheit()}")
print(f"Temperature in Kelvin: {temp.to_kelvin()}")
