def double_even_indices(numbers):
    for index, num in enumerate(numbers):
        if index % 2 == 0:
            numbers[index] *= 2
    return numbers

nums = ["Zach", 0, "King", "Dio", 15345]
print(f"Before call: {nums}")
double_even_indices(nums)
print(f"After call: {nums}")