from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
        return {"message": "WPipelineGuard API is running!"}

@app.get("/health")
async def health_check():
        return {"status": "healthy"}

# To run the app, use the command:
# uvicorn e1_simplest_api:app --reload