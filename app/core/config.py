from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    GOLD_API_KEY : str
    GOLD_API_BASE_URL: str = "https://www.goldapi.io/api"
    OPENAI_API_KEY : str
    OPENAI_MODEL : str = "gpt-4o-mini"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()