from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AI Spam Detector"

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/spam_detector"
    MODEL_NAME: str = "RUSpam/spam_deberta_v4"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()