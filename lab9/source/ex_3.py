def even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            yield num

test_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Test list: {test_lst}")

for num in even_numbers(test_lst):
    print(num)