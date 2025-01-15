import pandas as pd
import os

# Loads the processed data from the processed data folder
def load_processed_data(filename="sales_data_cleaned.parquet"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    processed_dir = os.path.join(script_dir, "..", "data", "processed")
    file_path = os.path.join(processed_dir, filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Processed data not found at {file_path}")
    
    df = pd.read_parquet(file_path)
    print(f"Loaded processed data from {file_path}")
    return df

# Validates the data by checking for nulls, duplicates, schema mismatches, and invalid values
def validate_data(df):
    validation_errors = []

    # Null value check
    if df.isnull().any().any():
        null_counts = df.isnull().sum()
        for col, count in null_counts.items():
            if count > 0:
                validation_errors.append(f"Null values found in column '{col}': {count}")

    # Duplicate check
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        validation_errors.append(f"{duplicate_count} duplicate records found.")

    # Schema validation
    expected_schema = {
        "transaction_id": "object",
        "customer_id": "object",
        "product": "object",
        "category": "object",
        "price": "float64",
        "quantity": "int64",
        "transaction_date": "datetime64[ns]"
    }
    for col, expected_type in expected_schema.items():
        if col not in df.columns:
            validation_errors.append(f"Missing column: {col}")
        elif str(df[col].dtypes) != expected_type:
            validation_errors.append(f"Column '{col}' has incorrect type. Expected: {expected_type}, Found: {df[col].dtypes}")

    # Data range checks
    if (df["price"] <= 0).any():
        validation_errors.append("Invalid price values found (price <= 0).")
    if (df["quantity"] <= 0).any():
        validation_errors.append("Invalid quantity values found (quantity <= 0).")

    return validation_errors

# Logs any validation errors to a text file in the metadata folder
def log_validation_errors(errors, log_file="validation_log.txt"):
    # Get the absolute path of the metadata folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    metadata_dir = os.path.join(script_dir, "..", "metadata")
    
    # Ensure the metadata directory exists
    os.makedirs(metadata_dir, exist_ok=True)
    
    # Correct path for the log file
    log_path = os.path.join(metadata_dir, log_file)

    # Write validation results to the log file
    with open(log_path, "w") as f:
        if errors:
            f.write("Data Validation Errors:\n")
            for error in errors:
                f.write(f"- {error}\n")
            print(f"Validation errors logged to {log_path}")
        else:
            f.write("No validation errors found.\n")
            print("No validation errors found.")


# Main execution block: loads, validates, and logs data quality checks
if __name__ == "__main__":
    df = load_processed_data()
    errors = validate_data(df)
    log_validation_errors(errors)
