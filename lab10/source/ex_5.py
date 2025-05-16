def categorize_characters(text):
    counts = {
        'digits': 0,
        'letters': 0,
        'spaces': 0,
        'other': 0
    }
    for char in text:
        if char.isdigit():
            counts['digits'] += 1
        elif char.isalpha():
            counts['letters'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        else:
            counts['other'] += 1

    return counts



print(categorize_characters("Hello, World! 123"))
