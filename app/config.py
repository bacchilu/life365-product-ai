from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "dev"
    app_name: str = "Life365 Product AI"

    rabbitmq_host: str = "localhost"
    rabbitmq_user: str = "guest"
    rabbitmq_password: str = "guest"
    rabbitmq_port: int = 5672

    llm_provider: Literal["openai", "local"] = "openai"
    openai_api_key: str | None = None
    llm_model: str = "gpt-4o-mini"

    embedding_model: str = "text-embedding-3-small"
    embedding_chunk_size: int = 500

    vector_collection_name: str = "life365_products"

    class ConfigDict:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()
