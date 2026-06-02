import pandas as pd

# Load fund master
df = pd.read_csv("data/raw/01_fund_master.csv")

print("UNIQUE FUND HOUSES:")
print(df["fund_house"].unique())

print("\nUNIQUE CATEGORIES:")
print(df["category"].unique())

print("\nUNIQUE RISK GRADES:")
print(df["risk_category"].unique())

# Validate AMFI codes
nav = pd.read_csv("data/raw/02_nav_history.csv")
missing = set(df["amfi_code"]) - set(nav["amfi_code"])
print(f"\nMISSING CODES: {missing if missing else 'None! All codes match ✅'}")