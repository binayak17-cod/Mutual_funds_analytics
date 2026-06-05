-- Top 5 funds by AUM
-- Average NAV per month
-- SIP Year-over-Year growth
-- Transactions by state
-- Funds with expense_ratio_pct < 1
-- Top 5 Sharpe Ratio funds
-- Top 5 Alpha funds
-- Average transaction amount by state
-- Category-wise average return
-- Fund count by risk grade

-- 1. Top 5 Funds by AUM
SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT
    AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Monthly Average NAV
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 4. Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Top 5 Funds by Sharpe Ratio
SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 7. Top 5 Funds by Alpha
SELECT
    scheme_name,
    alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

-- 8. Average Transaction Amount by State
SELECT
    state,
    ROUND(AVG(amount_inr), 2) AS avg_amount
FROM fact_transactions
GROUP BY state
ORDER BY avg_amount DESC;

-- 9. Transaction Type Distribution
SELECT
    transaction_type,
    COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total DESC;

-- 10. Fund Count by Risk Grade
SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade
ORDER BY total_funds DESC;