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

## Dashboard

A Streamlit dashboard was developed to display all generated visualizations from the EDA phase.

Features:

* Chart Gallery View
* Automatic Chart Loading
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
├── notebooks/
├── sql/
├── charts/
├── dashboard/
└── README.md
```

---

## Author

Binayak Naudia

