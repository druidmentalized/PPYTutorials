class Calculator:

    def __init__(self, a: int) -> None:
        self.a = a

    def get_square(self) -> int:
        return self.a ** 2

    @classmethod
    def class_method(cls, a: int) -> int:
        return a * 15
    
    @staticmethod
    def static_method(a: int, b: int) -> int:
        return a + b
    
# a)
calculator = Calculator(5)

# b)
print(calculator.get_square())

# c)
print(Calculator.class_method(5))

# d)
print(Calculator.static_method(5, 13))