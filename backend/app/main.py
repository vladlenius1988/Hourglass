from fastapi import FastAPI

app = FastAPI(title="Hourglass API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
