# Portfolio Analysis & Optimization (Interim Report)

## 📌 Project Overview
This project analyzes and optimizes a three-asset investment portfolio comprising:
- **Tesla (TSLA)** — High-growth, high-volatility equity in the consumer discretionary sector.
- **Vanguard Total Bond Market ETF (BND)** — Low-risk bond ETF providing stability and income.
- **S&P 500 ETF (SPY)** — Broad U.S. equity market exposure with moderate risk.
## 📈 Key Visualizations

![alt text](image.png)
## 📂 Project Structure
portfolio-analysis/
│
├── data/
│ ├── raw/ # Raw downloaded CSVs from Yahoo Finance
│ └── processed/ # Cleaned data, processed returns, merged portfolio data,portfolio_optimization
│
├── notebooks/
│ ├── 01_eda.ipynb # EDA & Cleaning
│ ├── 02_portfolio_analysis.ipynb
│ └── 03_portfolio_optimization.ipynb
│
├── scripts/
│ ├── fetch_data.py
│ ├── merge_processed_data.py
│ 
│
├── reports/
│ ├── figures/ # Plots saved from analysis & optimization
│ ├── portfolio_metrics.csv
│ ├── portfolio_opt_metrics.csv
│ ├── max_sharpe_portfolio.csv
│ ├── min_vol_portfolio.csv
│ └── portfolio_simulations.csv
│
├── requirements.txt
├── README.md
└── .gitignore


---

## 📊 Data Source & Description
Data was fetched using the **`yfinance`** Python library.

**Period:** `2015-07-01` → `2025-07-31`  
**Assets:**
| Asset | Ticker | Description |
|-------|--------|-------------|
| Tesla Inc. | TSLA | High-growth, high-volatility equity. |
| Vanguard Total Bond Market ETF | BND | Low-risk bond ETF. |
| SPDR S&P 500 ETF Trust | SPY | Broad U.S. market equity ETF. |

**Columns:**
- `Date` — Trading day timestamp
- `Open, High, Low, Close, Adj Close` — Price metrics
- `Volume` — Daily traded volume
- `Daily_Return` — Percentage change in adjusted close price
- `Volatility` — Annualized rolling standard deviation of daily returns

---

## 🔍 Methodology

### **Task 1 — Data Acquisition & Preprocessing**
- Used `yfinance` to download historical price data for TSLA, BND, SPY.
- Computed:
  - **Daily Returns** (`pct_change()` of Adjusted Close prices).
  - **Annualized Volatility** (21-day rolling standard deviation × √252).
- Saved:
  - Raw files → `data/raw/`
  - Processed files (with returns & volatility) → `data/processed/`
- Merged into `portfolio_merged_data.csv` keeping **only common trading dates** to avoid NaNs.

---

### **Task 2 — Exploratory Data Analysis**
- Checked for missing data and ensured alignment across assets.
- Summary statistics for returns & volatility.
- Plots:
  - Adjusted Close price trends.
  - Volatility trends over time.
  - Distribution of daily returns.
- All figures saved in `reports/figures/`.

---

### **Task 3 — Portfolio Analysis**
- Assumed **equal weights** across the three assets.
- Calculated:
  - **Portfolio Daily Return**
  - **Cumulative Return** (growth of $1)
  - **Annualized Return**
  - **Annualized Volatility**
  - **Sharpe Ratio** (risk-adjusted return, RF=2%)
- Correlation matrix of asset returns.
- Outputs saved in:
  - `reports/portfolio_metrics.csv`
  - `reports/returns_correlation_matrix.csv`

---

### **Task 4 — Portfolio Optimization**
- Used **Monte Carlo Simulation** to generate 50,000 random portfolios.
- Computed:
  - Portfolio returns, volatility, Sharpe ratio.
  - Asset weights for each portfolio.
- Identified:
  - **Maximum Sharpe Ratio portfolio**.
  - **Minimum Volatility portfolio**.
- Plotted the **Efficient Frontier** with optimal portfolios highlighted.
- Saved outputs:
  - `reports/portfolio_simulations.csv`
  - `reports/max_sharpe_portfolio.csv`
  - `reports/min_vol_portfolio.csv`
  - `reports/portfolio_opt_metrics.csv`
  - Figures in `reports/figures/`

---

## 📈 Key Outputs
**Example Efficient Frontier (Monte Carlo simulation)**  
![Efficient Frontier](reports/figures/efficient_frontier.png)

**Max Sharpe Portfolio Weights**  
![Max Sharpe Weights](reports/figures/max_sharpe_weights.png)

---

## ⚙️ Requirements
Install dependencies:
```bash
pip install -r requirements.txt
