from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Spam Detector"
    DATABASE_URL: str = "sqlite:///./spam_detector.db"

    class Config:
        env_file = ".env"


settings = Settings()