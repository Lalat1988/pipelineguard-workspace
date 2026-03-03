from fastapi import FastAPI

app = FastAPI()

@app.get("/tables/{table_name}")
async def get_table_info(table_name: str, include_stats: bool = False):
    response = {"table": table_name}
    if include_stats:
        response["stats"] = {"row_count": 1000, "last_updated": "2026-03-01"}
    return response