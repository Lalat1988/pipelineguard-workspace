from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncio

app = FastAPI(title="PipelineGuard API", version="0.1.0")

class TableCompareRequest(BaseModel):
    source_table: str
    target_table: str
    source_count: int
    target_count: int

class ValidationResult(BaseModel):
    source_table: str
    target_table: str
    mismatch: int
    status: str
    message: str

async def simulate_comparison(source: str, target: str, s_count: int, t_count: int):
    await asyncio.sleep(0.5)
    mismatch = abs(s_count - t_count)
    return mismatch

@app.get("/")
async def root():
    return {"service": "PipelineGuard", "status": "running"}

@app.post("/validate", response_model=ValidationResult)
async def validate_tables(request: TableCompareRequest):
    if request.source_count < 0 or request.target_count < 0:
        raise HTTPException(status_code=400, detail="Row counts cannot be negative")
    
    mismatch = await simulate_comparison(
        request.source_table,
        request.target_table,
        request.source_count,
        request.target_count
    )
    
    status = "PASS" if mismatch == 0 else "FAIL"
    message = "Tables match perfectly" if mismatch == 0 else f"{mismatch} row difference detected"
    
    return ValidationResult(
        source_table=request.source_table,
        target_table=request.target_table,
        mismatch=mismatch,
        status=status,
        message=message
    )

@app.get("/health")
async def health():
    return {"status": "healthy", "version": "0.1.0"}