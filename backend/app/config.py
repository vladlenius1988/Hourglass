from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Hourglass API"
   
    DEBUG: str = "DEBUG"
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/hourglass"

  
    SECRET_KEY: str | None = None
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
