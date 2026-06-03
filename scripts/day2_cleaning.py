import pandas as pd
from sqlalchemy import create_engine

# =========================
# LOAD DATA
# =========================

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

transactions = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# =========================
# CLEAN NAV HISTORY
# =========================

nav_history.columns = (
    nav_history.columns.str.lower()
)

nav_history["date"] = pd.to_datetime(
    nav_history["date"]
)

nav_history = nav_history.sort_values(
    by=["amfi_code", "date"]
)

nav_history = nav_history.drop_duplicates()

nav_history["nav"] = (
    nav_history.groupby("amfi_code")["nav"]
    .ffill()
)

nav_history = nav_history[
    nav_history["nav"] > 0
]

# =========================
# CLEAN TRANSACTIONS
# =========================

transactions.columns = (
    transactions.columns.str.lower()
)

transactions["transaction_date"] = (
    pd.to_datetime(
        transactions["transaction_date"]
    )
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.upper()
    .str.strip()
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .replace({
        "LUMP SUM": "LUMPSUM",
        "REDEEM": "REDEMPTION"
    })
)

transactions = transactions[
    transactions["amount_inr"] > 0
]

# =========================
# CLEAN PERFORMANCE
# =========================

performance.columns = (
    performance.columns.str.lower()
)

performance["return_1yr_pct"] = pd.to_numeric(
    performance["return_1yr_pct"],
    errors="coerce"
)

performance["return_3yr_pct"] = pd.to_numeric(
    performance["return_3yr_pct"],
    errors="coerce"
)

performance["return_5yr_pct"] = pd.to_numeric(
    performance["return_5yr_pct"],
    errors="coerce"
)

performance = performance[
    (performance["expense_ratio_pct"] >= 0.1)
    &
    (performance["expense_ratio_pct"] <= 2.5)
]

# =========================
# SAVE CLEANED FILES
# =========================

nav_history.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

transactions.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

performance.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Cleaning complete.")