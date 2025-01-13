from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# -----------------------------------------
# Initialize SparkSession
# -----------------------------------------
# SparkSession allows interaction with Spark for data processing
spark = SparkSession.builder.appName("DataCleaning").getOrCreate()

# -----------------------------------------
# Load the Ingested Dataset
# -----------------------------------------
# Load the raw dataset stored in Parquet format for efficient processing
input_path = "outputs/raw_dataset.parquet"  #  Path to the raw dataset
df = spark.read.parquet(input_path)

# Inspect the schema of the loaded dataset
print("Original Dataset Schema:")
df.printSchema()

# -----------------------------------------
# 1. Drop Unnecessary Columns
# -----------------------------------------
# Remove columns that are not relevant for analysis
columns_to_drop = ["device_fingerprint", "ip_address", "velocity_last_hour"]
df = df.drop(*columns_to_drop)

# -----------------------------------------
# 2. Handle Missing Values
# -----------------------------------------
# Replace missing numeric values with 0 (neutral/default)
df = df.fillna({"amount": 0, "distance_from_home": 0})

# Replace missing categorical values with "Unknown"
df = df.fillna({"merchant_category": "Unknown", "city": "Unknown", "currency": "Unknown"})

# -----------------------------------------
# 3. Create a Derived Column
# -----------------------------------------
# Add a new column 'high_value_transaction' to flag transactions > 1000
df = df.withColumn("high_value_transaction", when(col("amount") > 1000, True).otherwise(False))

# -----------------------------------------
# 4. Filter Invalid Transactions
# -----------------------------------------
# Keep only transactions with:
# - a positive amount
# - a non-null timestamp
df = df.filter((col("amount") > 0) & (col("timestamp").isNotNull()))

# -----------------------------------------
# Save the Cleaned Dataset
# -----------------------------------------
# Write the cleaned dataset back to Parquet for further processing
output_path = "outputs/cleaned_dataset.parquet"
df.write.parquet(output_path, mode="overwrite")

print(f"Cleaned dataset saved to {output_path}")
