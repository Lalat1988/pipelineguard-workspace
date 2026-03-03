import asyncio

async def validate_table(table_name, row_count):
    await asyncio.sleep(0.5)  # simulate DB query time
    status = "PASS" if row_count > 0 else "FAIL"
    return {"table": table_name, "rows": row_count, "status": status}

async def main():
    results = await asyncio.gather(
        validate_table("orders", 1500),
        validate_table("customers", 800),
        validate_table("empty_table", 0)
    )
    for r in results:
        print(r)

asyncio.run(main())