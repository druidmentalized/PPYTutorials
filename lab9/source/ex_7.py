def printer():
    try:
        while True:
            val = yield
            print(val)
    except GeneratorExit:
        print("Printer closed")

p = printer()
next(p)
p.send("Some test message")
p.close()