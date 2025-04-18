import string
from collections import Counter


def top_n_frequent_words(text, n):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    words_filter = (word for word in words if len(word) > 2)

    words_frequency = Counter(words_filter)
    unique_count = len(words_frequency)
    if n > unique_count:
        print(f"Too many words queried, returning only first {unique_count} words")
        n = unique_count

    top_words = [word for word, count in words_frequency.most_common(n)]
    return top_words

sample_text = ("Python is great and Python is fun. Students love Python because Python is simple. Programming in Python"
               " is better than many other languages. Learning Python helps students understand logic. Some students "
               "love Python more than others, but most find Python easy. Python, Python, and more Python! When students"
               " practice Python, they improve. Code in Python, debug in Python, and repeat. Projects in Python"
               " are common. Python’s syntax is readable. Python grows with your skill. Python is power. Learn Python,"
               " teach Python, master Python. Python solves problems. Python reads data. Python writes data. Python"
               " loves files. Python builds apps. Python builds minds.")

print(f"Normal execution: {top_n_frequent_words(sample_text, n=5)}")

print(f"Edge case execution: {top_n_frequent_words(sample_text, n=1000)}")
