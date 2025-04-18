def every_second(string):
    return string[1::2]

test_string = "Some test string to test working ability of the program"
print(f"Working with: {test_string}")
print(f"Result: {every_second(test_string)}")