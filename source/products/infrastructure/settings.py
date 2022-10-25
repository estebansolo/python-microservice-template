from pydantic import BaseSettings


class Settings(BaseSettings):
    environment: str


settings = Settings()
