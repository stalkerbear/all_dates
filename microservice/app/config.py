import logging
import os

from cachetools import TTLCache, cached
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


@cached(cache=TTLCache(maxsize=5, ttl=86_400))
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    print("WENT IN")
    return Settings()
