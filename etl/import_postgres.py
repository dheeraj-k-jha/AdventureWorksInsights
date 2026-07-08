import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import config
from .clean_data import clean_product, clean_sales, clean_targets

# Credentials:
engine = create_engine(
    f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    connect_args={"sslmode": "require"}
)

data_folder = Path("data/raw")
    
files = {
    "product": "Product.csv",
    "sales": "Sales.csv",
    "region": "Region.csv",
    "reseller": "Reseller.csv",
    "salesperson": "Salesperson.csv",
    "salespersonregion": "SalespersonRegion.csv",
    "targets": "Targets.csv"
}

for table, file in files.items():
    print(f"Importing {table}...")

    df = pd.read_csv(data_folder / file, sep="\t")


    if table == "product":
        df = clean_product(df)

    elif table == "sales":
        df = clean_sales(df)

    elif table == "targets":
        df = clean_targets(df)

    df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
      .str.replace("-", "_")
    )

    df.to_sql(table, engine, if_exists="replace", index=False)



print("Done!")