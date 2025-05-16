def even_squares(numbers):
    return [n ** 2 for n in numbers if n % 2 == 0]


print(even_squares([1, 2, 3, 4, 5, 6]))
