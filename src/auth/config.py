import os
import dotenv
dotenv.load_dotenv()
from pydantic_settings import BaseSettings



class AuthConfig(BaseSettings):

    JWT_ALG: str = os.getenv("JWT_ALG")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_EXP: int = os.getenv("JWT_EXP")

auth_config = AuthConfig()