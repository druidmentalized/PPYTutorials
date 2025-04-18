# a)
input = input("Enter comma-separated sequence of numbers: ")
list_var = list(map(str.strip, input.split(',')))
tuple_var = tuple(list_var)

print(f"List: {list_var}")
print(f"Tuple: {tuple_var}")

# b)
tuple_var = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
half = len(tuple_var) // 2

print(tuple_var[:half])
print(tuple_var[half:])
