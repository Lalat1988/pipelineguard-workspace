from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ComparisonRequest(BaseModel):
    source_table: str
    target_table: str
    threshold: float =  0.0

class ComparisonResult(BaseModel):
    source_table: str
    target_table: str
    mismatch_count: int
    status: str

@app.post("/compare", response_model=ComparisonResult)
async def compare_tables(request: ComparisonRequest):
    # Simulate comparison logic
    mismatch_count = 5  # Placeholder for actual mismatch count
    status = "PASS" if mismatch_count <= request.threshold else "FAIL"
    
    return ComparisonResult(
        source_table=request.source_table,
        target_table=request.target_table,
        mismatch_count=mismatch_count,
        status=status
    )