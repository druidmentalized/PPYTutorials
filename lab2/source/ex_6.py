# a)
def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)


print(f"Maximum from the input numbers is {max_of_three(11, 22, 33)}")


# b)
def check_number_for_conditions():
    for i in range(1000, 2001):
        if (i % 7 == 0) and (i % 5 != 0): print(i)


print("Numbers that belong to the conditions mentioned:")
check_number_for_conditions()
