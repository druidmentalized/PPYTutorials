import asyncio

async def delayed_printer(msg, delay):
    await asyncio.sleep(delay)
    print(f"{msg} after {delay}s")

async def main():
    await asyncio.gather(
        delayed_printer("A", 1),
        delayed_printer("B", 2),
        delayed_printer("C", 3),
    )

if __name__ == "__main__":
    print("Starting asyncio-delayed printing:")
    asyncio.run(main())