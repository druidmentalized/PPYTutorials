def generate_even_squares(limit):
    for i in range(0, limit + 1):
        if i % 2 == 0:
            yield i ** 2

first_nums = 50
sum_even_squares = (lambda gen: sum(gen))(generate_even_squares(first_nums))
print(f"Sum of the first {first_nums} even squares: {sum_even_squares}")