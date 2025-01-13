import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------
# Load Merchant Summary Data
# -----------------------------------------
# Load the merchant transaction summary (total transactions by category)
merchant_summary_path = "outputs/merchant_summary.csv"
merchant_df = pd.read_csv(merchant_summary_path)

# -----------------------------------------
# Visualization 1: Total Transaction Amount by Merchant Category
# -----------------------------------------
# Set the figure size
plt.figure(figsize=(10, 6))

# Create a horizontal bar plot for transaction amounts by merchant category
sns.barplot(
    x="total_amount", 
    y="merchant_category", 
    data=merchant_df.sort_values(by="total_amount", ascending=False),
    palette="viridis"
)

# Add plot titles and axis labels for clarity
plt.title("Total Transaction Amount by Merchant Category", fontsize=14)
plt.xlabel("Total Amount (in billions)", fontsize=12)
plt.ylabel("Merchant Category", fontsize=12)

# Adjust layout and save the plot as a PNG file
plt.tight_layout()
plt.savefig("outputs/total_amount_by_category.png")  # Save the plot
plt.show()

# -----------------------------------------
# Load High-Value Transaction Summary Data
# -----------------------------------------
# Load the summary of high-value transactions by country
high_value_summary_path = "outputs/high_value_summary.csv"
high_value_df = pd.read_csv(high_value_summary_path)

# -----------------------------------------
# Visualization 2: High-Value Transaction Amounts by Country
# -----------------------------------------
# Set the figure size
plt.figure(figsize=(12, 6))

# Create a bar plot for high-value transactions by country
sns.barplot(
    x="country",
    y="total_high_value_amount",
    data=high_value_df.sort_values(by="total_high_value_amount", ascending=False),
    palette="magma"
)

# Add plot titles and axis labels for clarity
plt.title("High-Value Transaction Amounts by Country", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Total High-Value Amount", fontsize=12)
plt.xticks(rotation=45)

# Adjust layout and save the plot as a PNG file
plt.tight_layout()
plt.savefig("outputs/high_value_amount_by_country.png")  # Save the plot
plt.show()
