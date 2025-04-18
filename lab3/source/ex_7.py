def numbers_average(numbers, round_digits=None):
    if len(numbers) == 0:
        return None
    avg = sum(numbers) / len(numbers)
    if round_digits is not None:
        return round(avg, round_digits)
    return avg


print(numbers_average([1, 2, 3, 4, 5, 5], 2))
print(numbers_average([1, 2, 3, 4, 5, 4, 2, 1, 5]))
