# Bluestock Mutual Fund Analytics Capstone Project

## Overview

This project was developed as part of the Bluestock Fintech Capstone Program. The objective was to build a complete Mutual Fund Analytics platform covering data ingestion, cleaning, database design, exploratory data analysis, performance analytics, risk analytics, dashboard development, and reporting.

The project processes mutual fund datasets, computes advanced performance metrics, analyzes investor behavior, and presents insights through interactive dashboards and professional reports.

---

## Project Objectives

* Build an end-to-end ETL pipeline for mutual fund data
* Design and implement a SQLite database
* Perform exploratory data analysis (EDA)
* Compute fund performance metrics
* Analyze portfolio risk and investor behavior
* Develop an interactive Power BI dashboard
* Produce a professional report and presentation

---

## Technology Stack

### Programming

* Python 3.x
* Pandas
* NumPy
* SciPy
* SQLAlchemy
* Requests

### Database

* SQLite

### Visualization

* Matplotlib
* Seaborn
* Plotly
* Power BI

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── multi_nav_fetch.py
│   ├── create_database.py
│   ├── day2_cleaning.py
│   └── analyze_nav.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboards/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Bluestock_MF_Analytics_Report.pdf
│   ├── Bluestock_MF_Analytics_Presentation.pptx
│   ├── rolling_sharpe_chart.png
│   ├── var_cvar_comparison.png
│   └── benchmark_comparison.png
│
├── README.md
└── requirements.txt
```

---

## Data Sources

The project uses the following mutual fund datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

Live NAV data was fetched using MFAPI.

---

## ETL Pipeline

### Data Ingestion

* Loaded all CSV datasets
* Validated schema consistency
* Identified missing values and anomalies

### Data Cleaning

* Standardized date formats
* Removed duplicate records
* Validated NAV values
* Corrected transaction categories
* Performed data quality checks

### Database Loading

* Designed SQLite schema
* Created fact and dimension tables
* Loaded cleaned datasets
* Validated row counts

---

## Exploratory Data Analysis

Key analyses performed:

* NAV trend analysis
* Fund house AUM comparison
* SIP inflow trends
* Category inflow heatmaps
* Investor demographics
* Geographic transaction analysis
* Portfolio sector allocation
* NAV correlation matrix

---

## Performance Analytics

Computed metrics include:

### Return Metrics

* 1-Year Return
* 3-Year Return
* 5-Year Return
* CAGR

### Risk Metrics

* Standard Deviation
* Sharpe Ratio
* Sortino Ratio
* Beta
* Alpha
* Maximum Drawdown

### Benchmark Analysis

* Fund vs Nifty Comparison
* Tracking Error
* Relative Performance

---

## Advanced Analytics

### Value at Risk (VaR)

Historical 95% Value at Risk calculated for all schemes.

### Conditional Value at Risk (CVaR)

Expected loss beyond the VaR threshold.

### Investor Cohort Analysis

Analyzed investor retention and transaction behavior by cohort.

### SIP Continuity Analysis

Identified investors with irregular SIP contributions.

### Fund Recommendation Engine

Generated fund recommendations based on:

* Risk Appetite
* Sharpe Ratio
* Risk Grade
* Historical Performance

### Portfolio Concentration Analysis

Computed Herfindahl-Hirschman Index (HHI) for portfolio diversification assessment.

---

## Dashboard Features

### Page 1 – Industry Overview

* Total AUM
* SIP Inflows
* Folio Counts
* AUM by AMC

### Page 2 – Fund Performance

* Risk vs Return Scatter Plot
* Fund Scorecards
* Benchmark Comparison

### Page 3 – Investor Analytics

* Transaction Analysis
* Demographic Insights
* Geographic Distribution

### Page 4 – SIP & Market Trends

* SIP Inflows
* Category Trends
* Market Comparison

---

## Key Findings

* SIP inflows showed strong growth during the study period.
* Large-cap equity funds attracted the highest investor participation.
* Risk-adjusted returns varied significantly across schemes.
* Certain investor cohorts demonstrated stronger long-term retention.
* Portfolio concentration differed substantially among equity funds.

---

## Deliverables

### Code

* ETL Scripts
* Data Cleaning Scripts
* Database Scripts
* Analytics Scripts

### Notebooks

* EDA Analysis
* Performance Analytics
* Advanced Analytics

### Dashboard

* Power BI Dashboard

### Reports

* Final PDF Report
* Presentation Deck

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ravideltech/bluestock-mf-capstone.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Author

Ravi Kumar

Bluestock Fintech Capstone Project

2026
