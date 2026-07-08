import pandas as pd
from sqlalchemy import create_engine
import config

# Credentials:
engine = create_engine(
    f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    connect_args={"sslmode": "require"}
)

def run_query(query):
    return pd.read_sql(query, engine)