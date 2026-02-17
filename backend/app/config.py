from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Hourglass API"
    DEBUG: bool = True
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/hourglass"

    class Config:
        env_file = ".env" 


settings = Settings()
