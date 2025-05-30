class Divider:

    @classmethod
    def divide(cls, a: int | float, b: int | float) -> float:
        try:
            return a / b
        except ZeroDivisionError:
            return 0.0

print(f"Good division: {Divider.divide(5, 2)}")
print(f"Zero division: {Divider.divide(7, 0)}")