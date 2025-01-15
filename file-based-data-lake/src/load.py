import pandas as pd
import os

# Loads the cleaned data from the processed data folder
def load_processed_data(filename="sales_data_cleaned.parquet"):
    """Load the cleaned data from the processed folder."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    processed_dir = os.path.join(script_dir, "..", "data", "processed")
    file_path = os.path.join(processed_dir, filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Processed data not found at {file_path}")
    
    df = pd.read_parquet(file_path)
    print(f"Loaded processed data from {file_path}")
    return df

# Aggregates total sales by product category
def aggregate_sales_by_category(df):
    """Aggregate total sales by product category."""
    df['total_sales'] = df['price'] * df['quantity']
    category_sales = df.groupby('category')['total_sales'].sum().reset_index()
    category_sales = category_sales.sort_values(by='total_sales', ascending=False)
    return category_sales

# Analyzes monthly sales trends by aggregating sales over months
def monthly_sales_trend(df):
    df['transaction_month'] = df['transaction_date'].dt.to_period('M')
    monthly_trend = df.groupby('transaction_month')['total_sales'].sum().reset_index()
    monthly_trend['transaction_month'] = monthly_trend['transaction_month'].astype(str)
    return monthly_trend

# Identifies the top N selling products based on total sales
def top_selling_products(df, top_n=5):
    product_sales = df.groupby('product')['total_sales'].sum().reset_index()
    top_products = product_sales.sort_values(by='total_sales', ascending=False).head(top_n)
    return top_products

# Saves the aggregated and curated data to the curated data folder
def save_curated_data(df, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    curated_dir = os.path.join(script_dir, "..", "data", "curated")
    os.makedirs(curated_dir, exist_ok=True)
    file_path = os.path.join(curated_dir, filename)
    
    df.to_parquet(file_path, index=False)
    print(f"Curated data saved to {file_path}")

# Main execution block to run data aggregation and save results if script is run directly
if __name__ == "__main__":
    # Load processed data
    processed_df = load_processed_data()

    # Aggregate sales by category
    category_sales_df = aggregate_sales_by_category(processed_df)
    save_curated_data(category_sales_df, "category_sales.parquet")

    # Monthly sales trend
    monthly_trend_df = monthly_sales_trend(processed_df)
    save_curated_data(monthly_trend_df, "monthly_sales_trend.parquet")

    # Top-selling products
    top_products_df = top_selling_products(processed_df)
    save_curated_data(top_products_df, "top_selling_products.parquet")
