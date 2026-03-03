import asyncio

async def task(name, seconds):
    print(f"{name} starting")
    await asyncio.sleep(seconds)
    print(f"{name} done")

async def main():
    await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 1)
    )

asyncio.run(main())