# a)
N = int(input("Input N: "))
for i in range(1, N + 1):
    print(i)


# b)
def is_palindrome(word):
    i, j = 0, len(word) - 1  # two pointers

    palindrome = True  # assume palindrome
    while i < j:
        if word[i] != word[j]:  # mismatch found
            palindrome = False
            break
        i += 1
        j -= 1
    return palindrome


print("Your word is palindrome" if is_palindrome(input("Input your word: ")) else "Your word is not palindrome")


# c)
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


print(factorial(int(input("Input number for factorial: "))))


# d)
def sum_of_natural(n):
    return_sum = 0
    for i in range(1, N + 1):
        return_sum += i
    return return_sum


print(f"Sum of first natural {N} numbers is {sum_of_natural(N)}")

# e)
num = int(input("Enter a number: "))
sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# f)
def is_prime(num):
    if num <= 1:
        return False
    else:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        return prime


n = int(input("Input a number: "))
for i in range(1, n + 1):
    if is_prime(i): print(i)
