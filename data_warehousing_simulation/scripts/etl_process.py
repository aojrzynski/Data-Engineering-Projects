import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine('postgresql+psycopg2://username:password@localhost:5432/data_warehouse')

# Generate date range for the year and create the 'dates' table data
date_range = pd.date_range(start='2024-01-01', end='2024-12-31')
dates_df = pd.DataFrame({
    'full_date': date_range,
    'day': date_range.day,
    'month': date_range.month,
    'year': date_range.year
})

# Load the data into the 'dates' table
dates_df.to_sql('dates', con=engine, if_exists='append', index=False)
print("Date data loaded successfully.")

# Load the customers data
customers_df = pd.read_csv('data/customers.csv')
customers_df.to_sql('customers', con=engine, if_exists='append', index=False)
print("Customers data loaded successfully.")

# Load the products data
products_df = pd.read_csv('data/products.csv')
products_df.to_sql('products', con=engine, if_exists='append', index=False)
print("Products data loaded successfully.")

# Load the sales data
sales_df = pd.read_csv('data/sales.csv')
sales_df.to_sql('sales', con=engine, if_exists='append', index=False)
print("Sales data loaded successfully.")
