import os

import dotenv
dotenv.load_dotenv()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")



settings = Settings()