def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

test_string = "Some test string to test working ability of the program"
print(f"Working with: {test_string}")
print(f"Result: {count_vowels(test_string)}")