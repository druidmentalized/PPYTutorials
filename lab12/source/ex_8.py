class NegativeNumberError(Exception):
    pass

def raise_if_negative(number) -> None:
    if number < 0:
        raise NegativeNumberError("Number should be positive!")
    else:
        print("Passed")

# Test calls
raise_if_negative(100)    # Output: Passed
raise_if_negative(-100)   # Raises NegativeNumberError