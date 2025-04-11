def custom_split(string, delimiter=' '):
    result, delim_len = [], len(delimiter)
    idx = 0
    while idx <= len(string):
        next_idx = string.find(delimiter, idx)
        if next_idx == -1:
            result.append(string[idx:])
            break
        result.append(string[idx:next_idx])
        idx = next_idx + delim_len
    return result

test_string = "Some test string to test working ability of the program"
print(f"Working with: {test_string}")
print(f"Result: {custom_split(test_string)}")