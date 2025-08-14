import yfinance as yf
import pandas as pd
from pathlib import Path

# Get the absolute path to the project root (parent of 'scripts' folder)
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories (absolute paths)
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

# Ensure directories exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Parameters
TICKERS = ["TSLA", "BND", "SPY"]
START_DATE = "2015-07-01"
END_DATE = "2025-07-31"

def calculate_volatility(df):
    """
    Calculate daily volatility (annualized) using 21-day rolling std dev.
    """
    df["Daily_Return"] = df["Adj Close"].pct_change()
    df["Volatility"] = df["Daily_Return"].rolling(window=21).std() * (252 ** 0.5)
    return df

def fetch_and_save_data():
    for ticker in TICKERS:
        print(f"📥 Fetching data for {ticker}...")
        df = yf.download(ticker, start=START_DATE, end=END_DATE)
        df.reset_index(inplace=True)

        # Save raw data
        raw_path = RAW_DATA_DIR / f"{ticker}_historical_data.csv"
        df.to_csv(raw_path, index=False)
        print(f"   💾 Saved raw data to {raw_path}")

        # Process data
        df = calculate_volatility(df)

        # Save processed data
        processed_path = PROCESSED_DATA_DIR / f"{ticker}_processed_data.csv"
        df.to_csv(processed_path, index=False)
        print(f"   📊 Saved processed data to {processed_path}")

if __name__ == "__main__":
    fetch_and_save_data()
    print("✅ All data fetched, processed, and saved.")
