
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.config import Settings

settings = Settings()


engine = create_async_engine(
    settings.DATABASE_URL, echo=True, future=True
)



AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
