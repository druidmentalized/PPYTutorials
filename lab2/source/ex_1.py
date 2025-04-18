# a)
def isOdd(number):
    if (number % 2 == 0):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


isOdd(5)
isOdd(12)

# b)
for i in range(1, 11):
    print(f"1/{i} = {1 / i:.2f}")

# c)
num = 1234567890
reverse = 0
temp = num
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
print(f"reverse of {num} is {reverse}")

# d)
num1 = 10
num2 = 20
num3 = 30

if num1 > num2:
    if num1 > num3:
        maximum = num1
    else:
        maximum = num3
else:
    if num2 > num3:
        maximum = num2
    else:
        maximum = num3

print(f"Max from {num1}, {num2}, {num3} is {maximum}")

# e)
userNumber = int(input("Enter a number: "))
while userNumber >= 0:
    print(f"{userNumber}")
    userNumber -= 1
