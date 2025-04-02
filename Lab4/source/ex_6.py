def filter_even_squares(nums):
    return [x ** 2 for x in nums if x % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Base list: {numbers}")
print(f"New list: {filter_even_squares(numbers)}")