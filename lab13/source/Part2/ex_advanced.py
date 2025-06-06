class Temperature:
    temperature_field: float

    def __init__(self, temperature: float):
        self.temperature_field = temperature

    def to_fahrenheit(self, temperature: float) -> float:
        return temperature * 9 / 5 + 32

    @staticmethod
    def from_fahrenheit(temperature: float) -> float:
        return (temperature - 32) * 5 / 9

    @classmethod
    def construct_from_fahrenheit(cls, temperature: float) -> "Temperature":
        return cls(Temperature.from_fahrenheit(temperature))
    
    def __eq__(self, other) -> bool:
        return self.temperature_field == other.temperature_field
    
    def __lt__(self, other) -> bool:
        return self.temperature_field < other.temperature_field
    
temp1 = Temperature(273.15)
temp2 = Temperature(98.7)
print(temp1 == temp2)
print(temp1 < temp2)