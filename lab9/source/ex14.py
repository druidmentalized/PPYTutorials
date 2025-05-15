def num_gen(n):
    for i in range(n):
        val = yield i
        print("sent:", val)

def middleware (target):
    try:
        while True:
            val = yield
            target.send(val * 5)
    except GeneratorExit:
        target.close()

def stats():
    count = total = 0
    try:
        while True:
            val = yield
            count += 1
            total += val
            print(f"Received: {val}, avg: {total / count}")
    except GeneratorExit:
        print("Stats complete")

s = stats(); next(s)
m = middleware(s); next(m)
for num in num_gen(15):
    m.send(num)

m.close()