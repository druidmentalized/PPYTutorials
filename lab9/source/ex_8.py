def running_average():
    curr_sum = 0
    vals_passed = 0
    try:
        while True:
            new_val = yield curr_sum / vals_passed if vals_passed else 0
            curr_sum += new_val
            vals_passed += 1
    except GeneratorExit:
        print("Generator exited")

gen = running_average()
next(gen)
print(gen.send(5))
print(gen.send(3))
print(gen.send(15))
print(gen.send(6))
print(gen.send(190))
gen.close()