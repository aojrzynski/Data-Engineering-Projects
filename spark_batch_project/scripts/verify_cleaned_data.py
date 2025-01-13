from pyspark.sql import SparkSession

# -----------------------------------------
# Initialize SparkSession
# -----------------------------------------
# SparkSession is required to interact with Spark DataFrames
spark = SparkSession.builder.appName("VerifyCleanedData").getOrCreate()

# -----------------------------------------
# Load the Cleaned Dataset
# -----------------------------------------
# Load the cleaned dataset saved in Parquet format for efficient processing
df = spark.read.parquet("outputs/cleaned_dataset.parquet")

# -----------------------------------------
# Verify the Data
# -----------------------------------------
# Display the first 5 rows to confirm that the cleaned dataset was loaded correctly
df.show(5)
