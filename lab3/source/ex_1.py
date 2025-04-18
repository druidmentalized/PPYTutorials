import cmath


def solve_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinite solutions possible"
            else:
                return "No solution possible"
        return [-c / b]
    else:
        discriminant = b ** 2 - 4 * a * c
        sqrt_discriminant = cmath.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        if discriminant > 0:
            return [x1.real, x2.real]
        elif sqrt_discriminant == 0:
            return [x1.real]
        else:
            return [x1, x2]


print(f"Answers for x^2 + 16x + 4 are {solve_quadratic_equation(1, 16, 4)}")
print(f"Answers for x^2 + 4x - 1 are {solve_quadratic_equation(1, 4, -1)}")
print(f"Answers for 10x - 10 are {solve_quadratic_equation(0, 10, 10)}")
print(f"Answers for 20x^2 + x + 5 are {solve_quadratic_equation(20, 1, 5)}")