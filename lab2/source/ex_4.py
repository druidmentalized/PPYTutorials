import sys

# a)

nums = [10, 20, 30, 40, 50]
print(f"List: {nums}")
nums_sum = 0
count = 0

for num in nums:
    nums_sum += num
    count += 1

average = nums_sum / count
print(f"Sum of all numbers: {nums_sum}, their average: {average}")

# b)
print(f"Reversed list from above: {list(reversed(nums))}")

# c)
min_value = sys.maxsize
max_value = -sys.maxsize
for num in nums:
    if num > max_value: max_value = num
    if num < min_value: min_value = num

print(f"For the list above min: {min_value} and max: {max_value}")
