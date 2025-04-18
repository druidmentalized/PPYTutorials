def count_frequency(sentence):
    words = sentence.lower().split()
    return {word: words.count(word) for word in words}

test_string = "Test phenomena program python panama java test ananas banana java banana python java"
print(f"Working with: {test_string}")
print(f"Result: {count_frequency(test_string)}")