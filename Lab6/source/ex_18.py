def longest_unique_substring(s):
    seen = {}
    start = max_len = 0
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len

test1 = "abcdefg"
test2 = "aaaaaaa"
test3 = "abcabcbb"
print(f"Working with:\n1) {test1}\n2) {test2}\n3) {test3}\n")
print(f"Results: \n1) {longest_unique_substring(test1)}\n2) {longest_unique_substring(test2)}\n3) {longest_unique_substring(test3)}\n")