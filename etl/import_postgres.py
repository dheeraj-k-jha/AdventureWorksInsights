import os


def import_to_postgres(csv_path: str) -> None:
    print(f"Import placeholder for {csv_path}")
    os.makedirs("data/processed", exist_ok=True)
