-- Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Transactions by state
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense ratio below 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Top 5 returns
SELECT scheme_name, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Average 3 year return
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- Total transaction amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- SIP transactions count
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- Distinct fund count
SELECT COUNT(DISTINCT amfi_code)
FROM fact_nav;

-- Average expense ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;