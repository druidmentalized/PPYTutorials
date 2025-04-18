def validate_inputs(func):
    def wrapper(nums, n):
        if not nums:
            print("You can't pass empty list!")
            return
        elif n == 0:
            print("You can't divide by zero!")
            return
        else:
            return func(nums, n)
    return wrapper

@validate_inputs
def find_multiples_and_square(nums, n):
    return [x ** 2 for x in nums if x % n == 0]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(f"List: {input_list}")
print(f"Normal execution: {find_multiples_and_square(input_list, 2)}")
print(f"When zero passed as n: {find_multiples_and_square(input_list, 0)}")
print(f"Passing empty list: {find_multiples_and_square([], 2)}")