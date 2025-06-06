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
    
# a)
temperature_test = Temperature.construct_from_fahrenheit(98.6)

# b)
print(f"In Celsius: {temperature_test.temperature_field}")
print(f"In Fahrenheit: {temperature_test.to_fahrenheit(temperature_test.temperature_field)}")

# c)
print(f"300K converted to Celsius: {Temperature.from_fahrenheit(300000)}")