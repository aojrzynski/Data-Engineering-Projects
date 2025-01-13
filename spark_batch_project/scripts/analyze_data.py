import os
import shutil
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum, avg

# Initialize SparkSession for distributed data processing
spark = SparkSession.builder.appName("DataAnalysis").getOrCreate()

# Load the cleaned dataset from Parquet format for efficient reading
input_path = "outputs/cleaned_dataset.parquet"
df = spark.read.parquet(input_path)


# -----------------------------------------
# 1. Analysis: Total Transactions and Amount by Merchant Category
# -----------------------------------------
# Group data by merchant category and calculate:
# - Total number of transactions
# - Total transaction amount
# - Average transaction amount
merchant_summary = df.groupBy("merchant_category") \
                     .agg(count("transaction_id").alias("total_transactions"),
                          sum("amount").alias("total_amount"),
                          avg("amount").alias("avg_amount")) \
                     .orderBy(col("total_amount").desc()) # Sort by total amount (descending)

# Display the top 10 merchant categories by total amount
print("Merchant Summary:")
merchant_summary.show(10)

# Save the merchant summary as a single CSV file
output_path = "outputs/merchant_summary"
merchant_summary.coalesce(1).write.csv(output_path, header=True, mode="overwrite")

# Rename the Spark-generated part file to a user-friendly nam
output_csv = "outputs/merchant_summary.csv"
part_file = os.path.join(output_path, "part-00000*.csv")
for file in os.listdir(output_path):
    if file.startswith("part-00000"):
        shutil.move(os.path.join(output_path, file), output_csv)
shutil.rmtree(output_path)  # Remove the temporary folder created by Spark


# -----------------------------------------
# 2. Analysis: High-Value Transactions by Country
# -----------------------------------------
# Filter transactions flagged as high-value and group by country
# Calculate:
# - Count of high-value transactions
# - Total amount of high-value transactions
high_value_summary = df.filter(col("high_value_transaction") == True) \
                       .groupBy("country") \
                       .agg(count("transaction_id").alias("high_value_count"),
                            sum("amount").alias("total_high_value_amount")) \
                       .orderBy(col("total_high_value_amount").desc()) # Sort by total amount (descending)

# Display the top 10 countries with the highest total high-value transaction amounts
print("High-Value Transactions Summary:")
high_value_summary.show(10)

# Save the high-value summary as a single CSV file
output_high_value_path = "outputs/high_value_summary"
high_value_summary.coalesce(1).write.csv(output_high_value_path, header=True, mode="overwrite")

# Rename the Spark-generated part file to a user-friendly name
high_value_csv = "outputs/high_value_summary.csv"
for file in os.listdir(output_high_value_path):
    if file.startswith("part-00000"):
        shutil.move(os.path.join(output_high_value_path, file), high_value_csv)
shutil.rmtree(output_high_value_path)  # Remove the temporary folder created by Spark


# -----------------------------------------
# 3. Final Status Message
# -----------------------------------------
print("Data analysis completed. Results saved in the outputs folder.")
