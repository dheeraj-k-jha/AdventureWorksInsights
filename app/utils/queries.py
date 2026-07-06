from app.utils.database import get_engine


def fetch_sample():
    engine = get_engine()
    with engine.connect() as connection:
        return connection.execute("SELECT 1 as value").fetchall()
