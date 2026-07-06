import os
from sqlalchemy import create_engine


def get_engine():
    database_url = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/adventureworks")
    return create_engine(database_url)
