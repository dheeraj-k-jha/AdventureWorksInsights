import pandas as pd
from sqlalchemy import create_engine
import config

engine = create_engine(
    f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASSWORD}@localhost:5432/adventureworks"
)

def run_query(query):
    return pd.read_sql(query, engine)