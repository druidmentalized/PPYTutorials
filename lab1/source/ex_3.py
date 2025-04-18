a, b, c = "a", 3, 5.5

try:
    a + b
except:
    print("string + int is not allowed!")

try:
    a + c
except:
    print("string + float is not allowed!")

print("b + c:", b + c)