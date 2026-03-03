import asyncio
import time

async def compare_table(table_name, source_count, target_count):
    print(f"Comparing {table_name}...")
    await asyncio.sleep(1)  # simulate real DB comparison time
    mismatch = abs(source_count - target_count)
    return {
        "table": table_name,
        "source": source_count,
        "target": target_count,
        "mismatch": mismatch,
        "status": "PASS" if mismatch == 0 else "FAIL"
    }

async def run_all_comparisons():
    start = time.time()
    results = await asyncio.gather(
        compare_table("orders", 1000, 995),
        compare_table("customers", 500, 500),
        compare_table("products", 250, 260),
        compare_table("inventory", 3000, 3000)
    )
    elapsed = time.time() - start
    print(f"\nAll comparisons done in {elapsed:.2f}s\n")
    for r in results:
        print(r)

asyncio.run(run_all_comparisons())