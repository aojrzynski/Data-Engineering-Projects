import pandas as pd
import os

# Loads raw CSV data from the raw data folder
def load_raw_data(filename="sales_data.csv"):
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
    raw_dir = os.path.join(script_dir, "..", "data", "raw")
    file_path = os.path.join(raw_dir, filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Raw data file not found at {file_path}")
    
    df = pd.read_csv(file_path)
    print(f"Loaded raw data from {file_path}")
    return df

# Cleans the raw data by removing duplicates, handling missing values, and validating data types
def clean_data(df):
    print("Starting data cleaning...")

    # Remove duplicate rows
    before_duplicates = len(df)
    df = df.drop_duplicates()
    after_duplicates = len(df)
    print(f"Removed {before_duplicates - after_duplicates} duplicate rows.")

    # Drop rows with any missing values
    before_missing = len(df)
    df = df.dropna()
    after_missing = len(df)
    print(f"Removed {before_missing - after_missing} rows with missing values.")

    # Validate and correct data types
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

    # Drop rows with invalid data types after conversion
    df = df.dropna(subset=['price', 'quantity', 'transaction_date'])
    print("Data types validated and corrected.")

    return df

# Saves the cleaned DataFrame to the processed folder in Parquet format
def save_processed_data(df, filename="sales_data_cleaned.parquet"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    processed_dir = os.path.join(script_dir, "..", "data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    file_path = os.path.join(processed_dir, filename)

    df.to_parquet(file_path, index=False)
    print(f"Processed data saved to {file_path}")

# Main execution block: loads raw data, cleans it, and saves the processed data
if __name__ == "__main__":
    raw_df = load_raw_data()
    cleaned_df = clean_data(raw_df)
    save_processed_data(cleaned_df)
