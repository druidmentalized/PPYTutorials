def capitalize(string):
    return ' '.join(word.capitalize() for word in string.split())

test_string = "Some test string to test working ability of the program"
print(f"Working with: {test_string}")
print(f"Result: {capitalize(test_string)}")