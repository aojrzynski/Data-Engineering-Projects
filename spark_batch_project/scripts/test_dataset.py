from pyspark.sql import SparkSession

# -----------------------------------------
# Initialize SparkSession
# -----------------------------------------
# SparkSession is the entry point for using Spark SQL and DataFrame APIs
spark = SparkSession.builder.appName("DatasetTest").getOrCreate()

# -----------------------------------------
# Load the Dataset
# -----------------------------------------
# Read the CSV dataset into a Spark DataFrame
# - header=True: Treats the first row as column headers
# - inferSchema=True: Automatically infers data types for each column
dataset_path = "data/synthetic_fraud_data.csv"  # Path to the dataset
df = spark.read.csv(dataset_path, header=True, inferSchema=True)

# -----------------------------------------
# Display the Dataset
# -----------------------------------------
# Show the first 5 rows to verify data loading
df.show(5)

# Print the schema to check the structure and data types
df.printSchema()
