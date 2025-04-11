def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

test_string1 = "listen"
test_string2 = "silent"
test_string3 = "silly"

print(f"Working with:\n1) {test_string1}\n2) {test_string2}\n3) {test_string3}\n")
print(f"Result between 1) and 2): {is_anagram(test_string1, test_string2)}")
print(f"Result between 1) and 3): {is_anagram(test_string1, test_string3)}")