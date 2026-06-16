import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(exist_ok=True)

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
    try:
        df = pd.read_csv(raw_path / file)

        df.columns = df.columns.str.strip()

        df = df.drop_duplicates()

        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].astype(str).str.strip()

        output_file = processed_path / file
        df.to_csv(output_file, index=False)

        print(f"Cleaned: {file}")

    except Exception as e:
        print(f"Error in {file}: {e}")

print("Day 2 Cleaning Complete")