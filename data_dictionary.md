# Data Dictionary

## fact_nav

| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER | Mutual fund code |
| date | DATE | NAV date |
| nav | REAL | Net asset value |

## fact_transactions

| Column | Type | Description |
|---|---|---|
| investor_id | INTEGER | Investor identifier |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |

## fact_performance

| Column | Type | Description |
|---|---|---|
| return_1yr_pct | REAL | 1 year return percentage |
| return_3yr_pct | REAL | 3 year return percentage |
| return_5yr_pct | REAL | 5 year return percentage |
| expense_ratio_pct | REAL | Expense ratio |