def custom_range(start, stop, step):
    while start < stop:
        yield round(start, 10)
        start += step

for num in custom_range(0.5, 3.0, 0.5):
    print(num)