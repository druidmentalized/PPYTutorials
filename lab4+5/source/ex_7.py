def count_word_frequencies(words):
    return {word: words.count(word) for word in set(words)}

wrds = ["Some", "some", "words", "that", "are", "are", "just", "some"]
print(f"Test list: {wrds}")
print(f"Dictionary: {count_word_frequencies(wrds)}")