def number_producer(limit):
    for n in range(limit):
        yield n

def result_doubler(target):
    try:
        while True:
            val = yield
            target.send(val * 2)
    except GeneratorExit:
        print("Doubler exited")

def printer():
    try:
        while True:
            val = yield
            print(val)
    except GeneratorExit:
        print("Printer done")

p = printer(); next(p)
d = result_doubler(p); next(d)
for num in number_producer(15):
    d.send(num)

d.close()