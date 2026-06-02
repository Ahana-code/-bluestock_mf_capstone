import pandas as pd
import os

# Path to our raw data folder
raw_path = "data/raw/"

# All 10 CSV file names
csv_files = [
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

# Load and explore each file
for file in csv_files:
    print(f"\n{'='*50}")
    print(f"FILE: {file}")
    print(f"{'='*50}")
    df = pd.read_csv(raw_path + file)
    print(f"Shape: {df.shape}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nFirst 3 rows:\n{df.head(3)}")