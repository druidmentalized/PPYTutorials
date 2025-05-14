def count_up_to(n):
    for i in range(n):
        yield i

for num in count_up_to(15):
    print(num)