import string
# a)

text = "Exercise 5 to enhance String knowledge in Python"
print(f"Original text: {text}")
print(f"Title Case: {text.title()}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"List of words in the text: {text.split()}")
print(f"After replacing 'String' with 'Integer': {text.replace('String', 'Integer')}")
print(f"Number of occurrences of 'e': {text.count('e')}")
print(f"Trimmed text: {text.strip()}")
print(f"Is the text alphanumeric? {text.replace(' ', '').isalnum()}")
print("\nstring module constants:")
print(f"ASCII Letters: {string.ascii_letters}")
print(f"Digits: {string.digits}")
print(f"Punctuation: {string.punctuation}")
print()

# b)
def is_palindrome(text):
    rev = ""
    for char in text:
        rev = char + rev

    if text == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")


text = input("Enter word: ")
is_palindrome(text)

#c)
text = input("Enter line of text: ")
chars = len(text)
vowels = sum(1 for char in text.lower() if char in "aeiou")
spaces = text.count(' ')
print(f"Chars: {chars}, Vowels: {vowels}, Spaces: {spaces}")