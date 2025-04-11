import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_elapsed = time.time() - time_start
        print(f"Time elapsed: {time_elapsed}")
        return result
    return wrapper

@time_execution
def filter_and_time_execution(numbers, n):
    return list(filter(lambda x : x % n == 0, numbers))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List before filtering: {nums}")
print(f"List after filtering: {filter_and_time_execution(nums, 2)}")