def word_freq(strings):
    frequencies = {}
    for item in strings:
        frequencies[item] = frequencies.get(item, 0) + 1
    return frequencies

data = ['a', 'b', 'a', 'a', 'c', 'b']
print(word_freq(data))