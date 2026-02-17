from fastapi import FastAPI
from fastapi import FastAPI
from app.config import Settings

settings = Settings()

app = FastAPI(title="Hourglass API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
