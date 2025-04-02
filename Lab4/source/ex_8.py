def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(f"Printing nums, using generator: {fibonacci()}")
fib = fibonacci()
for _ in range(15):
    print(next(fib))