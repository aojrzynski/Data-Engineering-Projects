import pandas as pd

# -----------------------------------------
# Define File Paths
# -----------------------------------------
# Path to the large dataset and where to save the sampled dataset   
large_file_path = "data/synthetic_fraud_data.csv" # Path to the full dataset
sample_file_path = "data/sample_fraud_data.csv" # Path to save the sampled dataset

# -----------------------------------------
# Load the Large Dataset
# -----------------------------------------
# Read the large CSV file into a Pandas DataFrame
df = pd.read_csv(large_file_path)

# -----------------------------------------
# Sample the Dataset
# -----------------------------------------
# Randomly select 10,000 rows for a smaller, quicker-to-process dataset
df_sample = df.sample(n=10000)

# -----------------------------------------
# Save the Sampled Dataset
# -----------------------------------------
# Write the sampled DataFrame to a new CSV file without the index
df_sample.to_csv(sample_file_path, index=False)

print(f"Sample dataset created at {sample_file_path}")
