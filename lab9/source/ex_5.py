def chunker(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]

test_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Test list: {test_lst}")

for chunk in chunker(test_lst, 3):
    print(chunk)