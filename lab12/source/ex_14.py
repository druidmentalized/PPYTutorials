
class InvalidOperationError(Exception):
    pass

class Calculator:
    @staticmethod
    def calculate(a: int | float, b: int | float, operation: str) -> int | float:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            raise InvalidOperationError

print("Operations with number 5 and 2:")
print(f"Sum: {Calculator.calculate(5, 2, "+")}")
print(f"Subtraction: {Calculator.calculate(5, 2, "-")}")
print(f"Multiplying: {Calculator.calculate(5, 2, "*")}")
print(f"Division: {Calculator.calculate(5, 2, "/")}")
print(f"Unsupported: {Calculator.calculate(5, 2, "max")}")