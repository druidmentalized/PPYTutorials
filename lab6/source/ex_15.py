import string
from collections import Counter

def most_frequent_char(s):
    s_clean = s.replace(' ', '').translate(str.maketrans('', '', string.punctuation))
    freq = Counter(s_clean)
    return freq.most_common(1)[0][0] if freq else None

test_string = "Some test string to test working ability of the program. Sadly, but this task took to long to actually do :("
print(f"Working with: {test_string}")
print(f"Result: {most_frequent_char(test_string)}")