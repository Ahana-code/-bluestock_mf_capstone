import pandas as pd
from sqlalchemy import create_engine

# CREATE DATABASE
engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# LOAD CLEANED FILES
nav = pd.read_csv(
    "data/processed/nav_history_cleaned.csv"
)

transactions = pd.read_csv(
    "data/processed/investor_transactions_cleaned.csv"
)

performance = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

# LOAD TABLES INTO SQLITE
nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully.")