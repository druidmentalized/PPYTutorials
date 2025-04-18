def spaces_to_dashes(string):
    return string.replace(" ", "-")

test_string = "Some test string to test working ability of the program"
print(f"Working with: {test_string}")
print(f"Result: {spaces_to_dashes(test_string)}")