from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB: str = "books"
    API_KEY: str
    RATE_LIMIT: str = "100/hour"
    BASE_URL: str = "https://books.toscrape.com"
    LOG_LEVEL: str = "INFO"
    SCHEDULER_ENABLED: bool = True
    REPORT_BUCKET: str = "./reports"

    class Config:
        env_file = ".env"

settings = Settings()
