# a) Recursion

def factorial_recursion(n):
    if n == 0:
        return 1
    return n * factorial_recursion(n - 1)


# b) Iterative
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Recursive 1 factorial: {factorial_recursion(1)}")
print(f"Recursive 5 factorial: {factorial_recursion(5)}")
print(f"Recursive 10 factorial: {factorial_recursion(10)}")
print()
print(f"Iterative 3 factorial: {factorial_recursion(3)}")
print(f"Iterative 7 factorial: {factorial_recursion(7)}")
print(f"Iterative 12 factorial: {factorial_recursion(12)}")