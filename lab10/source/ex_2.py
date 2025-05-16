import string


def word_frequency(text):
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    words_freq = {}
    for word in words:
        words_freq[word] = words_freq.get(word, 0) + 1

    return words_freq


test_text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency(test_text))
