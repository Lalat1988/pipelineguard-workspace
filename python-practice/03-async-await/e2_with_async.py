'''

'''

import asyncio
import time

async def fetch_data(name):
    print(f"Fetching {name}...")
    await asyncio.sleep(2)  # simulates slow DB or API call
    print(f"Done fetching {name}")
    return f"data from {name}"

async def main():
    start = time.time()
    results = await asyncio.gather(
        fetch_data("table_A"),
        fetch_data("table_B"),
        fetch_data("table_C")
    )
    print(f"Total time: {time.time() - start:.2f}s")
    print(results)

asyncio.run(main())
# Takes ~2 seconds — runs concurrently