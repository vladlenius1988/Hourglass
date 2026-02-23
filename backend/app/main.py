from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select

from app.config import Settings
from app.db import get_db
from app.db import engine
from app.models import User
from app.db import Base
from app.core.security import hash_password
from app.schemas.user import UserCreate

settings = Settings()

app = FastAPI(title="Hourglass API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-test")
async def db_test(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"result": result.scalar()}

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/register")
async def register(user_data: UserCreate, session: AsyncSession = Depends(get_db)):
    
    # Проверяем, есть ли пользователь
    result = await session.execute(
        select(User).where(User.email == user_data.email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Хэшируем пароль
    hashed_password = hash_password(user_data.password)

    # Создаём пользователя
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_password
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return {"message": "User registered successfully"}