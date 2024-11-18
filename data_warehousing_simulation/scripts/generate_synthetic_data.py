from faker import Faker # For generating fake data
import pandas as pd # For handling data in DataFrame format
import random # For generating random numbers

# Initialize Faker for data generation and set seed for reproducibility
faker = Faker()
Faker.seed(0)  # Ensures reproducibility

# Function to generate customer data
def generate_customers(num_customers=100):
    customer_data = []
    for _ in range(num_customers):
        customer_data.append({
            'customer_id': faker.unique.random_int(min=1000, max=9999),
            'name': faker.name(),
            'email': faker.email(),
            'phone_number': faker.phone_number(),
            'address': faker.address()
        })
    return pd.DataFrame(customer_data)

# Generate and preview customer data
customers_df = generate_customers(100)
print(customers_df.head())  # View the first few rows

# Function to generate product data
def generate_products(num_products=50):
    product_data = []
    for _ in range(num_products):
        product_data.append({
            'product_id': faker.unique.random_int(min=100, max=999),
            'product_name': faker.word().capitalize(),
            'category': faker.random_element(elements=['Electronics', 'Clothing', 'Home', 'Books']),
            'price': round(random.uniform(5.0, 500.0), 2) # Random price between 5 and 500
        })
    return pd.DataFrame(product_data)

# Generate and preview product data
products_df = generate_products(50)
print(products_df.head())  # View the first few rows

# Function to generate sales data with customer and product references
def generate_sales(num_sales=500, customers_df=customers_df, products_df=products_df):
    sales_data = []
    for _ in range(num_sales):
        sales_data.append({
            'sale_id': faker.unique.random_int(min=10000, max=99999),
            'customer_id': customers_df.sample(1)['customer_id'].values[0], # Randomly select a customer ID
            'product_id': products_df.sample(1)['product_id'].values[0], # Randomly select a product ID
            'quantity': random.randint(1, 5),
            'sale_date': faker.date_this_year() # Random date within the current year
        })
    return pd.DataFrame(sales_data)

# Generate and preview sales data
sales_df = generate_sales(500)
print(sales_df.head())  # View the first few rows

# Export generated data to CSV files
customers_df.to_csv('data/customers.csv', index=False)
products_df.to_csv('data/products.csv', index=False)
sales_df.to_csv('data/sales.csv', index=False)