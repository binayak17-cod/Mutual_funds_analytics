# Mutual Fund Analytics Dashboard

## Project Overview

This project analyzes Mutual Fund data using Python, SQL, and Streamlit. The objective is to study fund performance, investor behavior, NAV trends, and portfolio characteristics through exploratory data analysis and interactive visualizations.

---

## Project Progress

### Day 1 – Data Collection & Validation

* Collected and organized mutual fund datasets
* Performed data quality checks
* Validated relationships between datasets

#### Data Quality Summary

* Unique Fund Houses: 10
* Total Master Relationship Keys: 40
* Total History Tracking Keys: 40
* Data Discrepancies / Missing Records: 0

---

### Day 2 – Data Cleaning & SQL Database Design

#### Data Cleaning

* Cleaned and standardized mutual fund datasets
* Handled missing values and datatype conversions
* Prepared processed datasets for analysis

#### Database Tables

##### fact_nav

Stores daily NAV history.

| Column    | Description            |
| --------- | ---------------------- |
| amfi_code | Unique fund identifier |
| date      | NAV date               |
| nav       | Net Asset Value        |

##### fact_transactions

Stores investor transaction data and demographics.

| Column           | Description                |
| ---------------- | -------------------------- |
| investor_id      | Investor identifier        |
| transaction_date | Transaction date           |
| amfi_code        | Fund identifier            |
| transaction_type | SIP / Lumpsum / Redemption |
| amount_inr       | Investment amount          |
| state            | Investor state             |
| city             | Investor city              |
| city_tier        | T30 / B30 classification   |
| age_group        | Investor age group         |
| gender           | Investor gender            |

##### fact_performance

Stores mutual fund performance metrics.

| Column         | Description         |
| -------------- | ------------------- |
| scheme_name    | Scheme name         |
| fund_house     | Fund house          |
| category       | Fund category       |
| return_1yr_pct | 1-Year return       |
| return_3yr_pct | 3-Year return       |
| return_5yr_pct | 5-Year return       |
| alpha          | Alpha               |
| beta           | Beta                |
| sharpe_ratio   | Sharpe Ratio        |
| risk_grade     | Risk classification |

---

### Day 3 – Exploratory Data Analysis

Created and exported visualizations for:

* NAV Trend Analysis
* AUM Growth Analysis
* Category Inflow Heatmap
* Investor Age Distribution
* Investment Amount by Age Group
* Gender Distribution
* State-wise Investment Analysis
* Folio Growth Analysis
* NAV Correlation Matrix
* Sector Allocation Analysis
* Top 10 Fund Houses by AUM
* Top 10 Funds by Alpha
* Top 10 Funds by Sharpe Ratio
* Category Return Analysis
* Risk Grade Distribution

Total Charts Generated: 15

---

### Day 4 – Fund Performance Analytics

Performed advanced performance evaluation and risk analysis across all mutual fund schemes.

#### Metrics Computed

* Daily Return Analysis
* CAGR (Compound Annual Growth Rate)
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta Analysis
* Maximum Drawdown Analysis
* Fund Scorecard Ranking
* Benchmark Comparison (NIFTY 50 & NIFTY 100)
* Tracking Error Analysis

#### Deliverables Generated

##### Performance Analytics Notebook

* Performance_Analytics.ipynb

##### Processed Outputs

* alpha_beta.csv
* fund_scorecard.csv
* max_drawdown.csv
* tracking_error.csv

##### Visualizations

* Daily Return Distribution
* Top 10 Funds by CAGR
* Top 10 Funds by Sharpe Ratio
* Sharpe Ratio Distribution
* Top 10 Funds by Alpha
* Maximum Drawdown Analysis
* Fund Scorecard Ranking
* Benchmark Comparison Chart
* Tracking Error Analysis

Total Additional Charts Generated: 9

#### Key Performance Measures

| Metric           | Purpose                                  |
| ---------------- | ---------------------------------------- |
| CAGR             | Measures annualized growth rate          |
| Sharpe Ratio     | Measures risk-adjusted return            |
| Sortino Ratio    | Measures downside risk-adjusted return   |
| Alpha            | Measures excess return over benchmark    |
| Beta             | Measures market sensitivity              |
| Maximum Drawdown | Measures worst historical decline        |
| Tracking Error   | Measures deviation from benchmark        |
| Fund Score       | Composite ranking of overall performance |

---

## Dashboard

A Streamlit dashboard was developed to display analytical insights and visualizations generated throughout the project.

### Features

* Automated Chart Loading
* EDA Visualizations
* Performance Analytics Visualizations
* Fund Ranking Charts
* Benchmark Comparison Charts
* Interactive Dashboard Interface

---

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* PostgreSQL
* SQLAlchemy
* Streamlit
* Git & GitHub

---

## Project Structure

```text
Mutual_funds_analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── mutual_funds_exploration.ipynb
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── sql/
│
├── charts/
│
├── dashboard/
│   └── app.py
│
└── README.md
```

---

## Project Status

### Completed

* Day 1 – Data Collection & Validation
* Day 2 – Data Cleaning & SQL Database Design
* Day 3 – Exploratory Data Analysis
* Day 4 – Fund Performance Analytics

---

## Author

**Binayak Naudia**
