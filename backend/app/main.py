from fastapi import FastAPI
from app.config import Settings
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from sqlalchemy import text

settings = Settings()

app = FastAPI(title="Hourglass API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-test")
async def db_test(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"result": result.scalar()}
