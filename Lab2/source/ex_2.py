import sys

# a)
a, b = int(sys.argv[1]), int(sys.argv[2])
print(f"Sum of arguments {a} + {b} = {a + b}")

# b)
a, b = 10, 3
print("Arithmetic:", a + b, a - b, a * b, a / b, a % b)
print("Relational:", a > b, a < b, a == b)
print("Logical:", (a > b) and (b > 0), (a < b) or (b > 0))
print("Bitwise:", a & b, a | b, a ^ b)

# c)
personAge = int(input("Input your age please: "))
if personAge >= 18:
    print("You are eligible for voting!")
else:
    print("You are not eligible for voting.")

# d)
year = int(input("Input some year: "))
is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
print("Leap Year" if is_leap else "Not Leap Year")
