def count_substrings(string, substring):
    return string.count(substring)

test_string = "Test phenomena program python panama java test ananas banana"
print(f"Working with: {test_string}")
print(f"Result: {count_substrings(test_string, "na")}")