# DAY 2 — Data Cleaning + SQL Database Design
# Data Dictionary

## fact_nav

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Fund identifier |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | T30/B30 city classification |
| age_group | TEXT | Investor age category |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | UPI, Cheque, Mandate, etc. |
| kyc_status | TEXT | Verified or Pending |

---

## fact_performance

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund identifier |
| scheme_name | TEXT | Fund scheme name |
| fund_house | TEXT | AMC/Fund house |
| category | TEXT | Fund category |
| plan | TEXT | Direct/Regular |
| return_1yr_pct | REAL | 1-year return (%) |
| return_3yr_pct | REAL | 3-year return (%) |
| return_5yr_pct | REAL | 5-year return (%) |
| benchmark_3yr_pct | REAL | Benchmark return (%) |
| alpha | REAL | Alpha measure |
| beta | REAL | Beta measure |
| sharpe_ratio | REAL | Sharpe ratio |
| sortino_ratio | REAL | Sortino ratio |
| std_dev_ann_pct | REAL | Annualized volatility |
| max_drawdown_pct | REAL | Maximum drawdown |
| aum_crore | REAL | Assets under Management (Crores) |
| expense_ratio_pct | REAL | Expense ratio (%) |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk category |