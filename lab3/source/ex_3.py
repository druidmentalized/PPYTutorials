# a) Recursive
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# b) Iterative
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


print(f"Recursive fibonacci for 5: {fibonacci_recursive(5)}")
print(f"Recursive fibonacci for 15: {fibonacci_recursive(15)}")
print(f"Recursive fibonacci for 25: {fibonacci_recursive(25)}")
print()
print(f"Recursive fibonacci for 10: {fibonacci_recursive(10)}")
print(f"Recursive fibonacci for 20: {fibonacci_recursive(20)}")
print(f"Recursive fibonacci for 30: {fibonacci_recursive(30)}")
