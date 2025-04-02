import time

def time_execution(func):
    print("Decorator start")

    def wrapper():
        timeStart = time.time()
        func()
        timeElapsed = time.time() - timeStart
        print(f"Time elapsed: {timeElapsed:.2f} seconds")

    return wrapper


@time_execution
def slow_function():
    print("Slow function start")
    time.sleep(2)


slow_function()