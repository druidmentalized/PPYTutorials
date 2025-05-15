import time

def rate_limiter(n_per_sec):
    interval = 1 / n_per_sec
    try:
        while True:
            task = yield
            print(f"Processing {task} at {time.time()}")
            time.sleep(interval)
    except GeneratorExit:
        print("Rate limiter closed")

print("Starting rate-limited processing (2 per second):")
limiter = rate_limiter(2)
next(limiter)

for i in range(5):
    limiter.send(f"Task {i+1}")

limiter.close()