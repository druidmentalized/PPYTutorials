def is_palindrome(string):
    return string == string[::-1]

test_string = "madam"
print(f"Working with: {test_string}")
print(f"Result: {is_palindrome(test_string)}")

test_string = "something"
print(f"\nWorking with: {test_string}")
print(f"Result: {is_palindrome(test_string)}")