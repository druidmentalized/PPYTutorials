def even_odd_dict(numbers):
    result = {
        "odd": [],
        "even": []
    }
    for num in numbers:
        if num % 2 == 0:
            result["even"].append(num)
        else:
            result["odd"].append(num)
    return result


lst = [1, 2, 3, 4, 5, 6]
print(even_odd_dict(lst))
