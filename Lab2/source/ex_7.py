# a)
def fibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2

    return fibonacci(num - 1) + fibonacci(num - 2)


a, b = 5, 15
print(f"Fibonacci for {a} is {fibonacci(a)}")
print(f"Fibonacci for {b} is {fibonacci(b)}")


# b)
def armstrong(number):
    power = len(str(number))

    def sum_of_digits(num):
        if num == 0:
            return 0

        return (num % 10) ** power + sum_of_digits(num // 10)

    return number == sum_of_digits(number)


a, b = 153, 201
print(f"Is {a} and armstrong number? {armstrong(a)}")
print(f"Is {b} and armstrong number? {armstrong(b)}")


# c)
def modify_list(list_var):
    list_var.append(100)


nums_list = [1, 2, 3]
print(f"Nums before function call: {nums_list}")
modify_list(nums_list)
print(f"Nums after function call: {nums_list}")


# d)
def factorial(num):
    if num == 1: return 1
    return num * factorial(num - 1)


a, b = 5, 13
print(f"Factorial for {a} is {factorial(a)}")
print(f"Factorial for {b} is {factorial(b)}")
