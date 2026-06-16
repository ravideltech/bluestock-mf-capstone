import pandas as pd
import sqlite3
from pathlib import Path

db_path = "data/bluestock_mf.db"

conn = sqlite3.connect(db_path)

processed = Path("data/processed")

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    table_name = file.replace(".csv", "")
    df = pd.read_csv(processed / file)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name}")

conn.close()

print("Database Created Successfully")