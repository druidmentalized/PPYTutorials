def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def print_matrix(matrix):
    for row in matrix:
        print(row)


test_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Before transpose:")
print_matrix(test_matrix)
print("After transpose:")
print_matrix(transpose_matrix(test_matrix))