def keyword_filter(keyword):
    try:
        while True:
            line = yield
            if keyword in line:
                print(line)
    except GeneratorExit:
        print("Generator exited")


if __name__ == '__main__':
    fltr = keyword_filter("test")
    next(fltr)
    fltr.send("This is test message")
    fltr.send("And this is not")
    fltr.send("This is also possibly a test message")