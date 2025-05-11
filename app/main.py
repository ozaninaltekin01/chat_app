from fastapi import FastAPI

app = FastAPI(title="Chat App")

@app.get("/health")
async def health_check():
    return {"status":"ok"}