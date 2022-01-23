from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):

    class Config:
        case_sensitive: bool = True
        env_file: str = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
