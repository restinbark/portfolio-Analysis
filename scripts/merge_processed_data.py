import pandas as pd
from pathlib import Path

# Absolute path to project root
BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

def merge_all_processed():
    # Find all processed CSV files except the merged file itself
    csv_files = [f for f in PROCESSED_DATA_DIR.glob("*_processed_data.csv") 
                 if f.name != "portfolio_merged_data.csv"]

    if not csv_files:
        print("⚠ No processed CSV files found in:", PROCESSED_DATA_DIR)
        return

    merged_df = None

    for file in csv_files:
        df = pd.read_csv(file)

        # Extract ticker from filename (e.g., "TSLA_processed_data.csv" → "TSLA")
        ticker = file.stem.split("_")[0]

        # Rename columns with ticker prefix
        rename_map = {}
        for col in df.columns:
            if col != "Date":
                rename_map[col] = f"{ticker}_{col}"
        df.rename(columns=rename_map, inplace=True)

        # Keep only Date and renamed columns
        df = df[[col for col in df.columns if col == "Date" or col.startswith(ticker)]]

        # Merge into one DataFrame (inner join to keep only common dates)
        if merged_df is None:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on="Date", how="inner")

    # Sort by Date just in case
    merged_df.sort_values("Date", inplace=True)

    # Save merged file
    merged_path = PROCESSED_DATA_DIR / "portfolio_merged_data.csv"
    merged_df.to_csv(merged_path, index=False)
    print(f"✅ Merged dataset saved to {merged_path}")

if __name__ == "__main__":
    merge_all_processed()
