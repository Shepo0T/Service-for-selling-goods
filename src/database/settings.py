from databases import Database
from sqlalchemy import MetaData, create_engine

from src.database.config import  settings

DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

metadata = MetaData()
engine = create_engine(
    DATABASE_URL, echo=True
)


database = Database(DATABASE_URL)
