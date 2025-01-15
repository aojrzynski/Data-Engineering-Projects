import pandas as pd
import os

def load_raw_data(filename="sales_data.csv"):
    """Load raw CSV data from the raw data folder."""
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
    raw_dir = os.path.join(script_dir, "..", "data", "raw")
    file_path = os.path.join(raw_dir, filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Raw data file not found at {file_path}")
    
    df = pd.read_csv(file_path)
    print(f"Loaded raw data from {file_path}")
    return df

def clean_data(df):
    """Clean the raw data."""
    print("Starting data cleaning...")

    # Remove duplicates
    before_duplicates = len(df)
    df = df.drop_duplicates()
    after_duplicates = len(df)
    print(f"Removed {before_duplicates - after_duplicates} duplicate rows.")

    # Handle missing values (drop rows with any missing values)
    before_missing = len(df)
    df = df.dropna()
    after_missing = len(df)
    print(f"Removed {before_missing - after_missing} rows with missing values.")

    # Validate data types
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

    # Drop any rows with invalid data types
    df = df.dropna(subset=['price', 'quantity', 'transaction_date'])
    print("Data types validated and corrected.")

    return df

def save_processed_data(df, filename="sales_data_cleaned.parquet"):
    """Save the cleaned data to the processed data folder in Parquet format."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    processed_dir = os.path.join(script_dir, "..", "data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    file_path = os.path.join(processed_dir, filename)

    df.to_parquet(file_path, index=False)
    print(f"Processed data saved to {file_path}")

if __name__ == "__main__":
    # Load, clean, and save the data
    raw_df = load_raw_data()
    cleaned_df = clean_data(raw_df)
    save_processed_data(cleaned_df)
