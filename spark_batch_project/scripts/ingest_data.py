from pyspark.sql import SparkSession

# -----------------------------------------
# Initialize SparkSession
# -----------------------------------------
# SparkSession is the entry point to using Spark's functionality
spark = SparkSession.builder.appName("DataIngestion").getOrCreate()

# -----------------------------------------
# Load Raw CSV Data
# -----------------------------------------
# Read the raw transactional dataset in CSV format
# - header=True: uses the first row as column names
# - inferSchema=True: automatically detects data types
dataset_path = "data/synthetic_fraud_data.csv"  # Replace with your dataset file name
df = spark.read.csv(dataset_path, header=True, inferSchema=True)

# -----------------------------------------
# Inspect the Dataset
# -----------------------------------------
# Print the schema to understand the structure and data types
print("Dataset Schema:")
df.printSchema()

# -----------------------------------------
# Save as Parquet for Efficient Processing
# -----------------------------------------
# Save the ingested data in Parquet format for optimized storage and faster processing
output_path = "outputs/raw_dataset.parquet"
df.write.parquet(output_path, mode="overwrite") # Overwrites if the file already exists

print(f"Raw dataset saved to {output_path}")
