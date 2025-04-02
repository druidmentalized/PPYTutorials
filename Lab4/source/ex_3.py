def filter_multiples_of_n(numbers, n):
    return list(filter(lambda x: x % n == 0, numbers))


nums = [1, 2, 3, 4, 5, 3, 4, 1, 9, 12]
print(f"Before filtering: {nums}")
print(f"After filtering: {filter_multiples_of_n(nums, 3)}")