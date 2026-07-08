# deploy_views.py : use it to deploy all the views use : python3 deploy_views.py

from sqlalchemy import create_engine, text
import config

engine = create_engine(
    f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    connect_args={"sslmode": "require"}
)

with open("sql/views.sql") as f:
    sql = f.read()

with engine.begin() as conn:
    conn.execute(text(sql))

print("Views created successfully.")