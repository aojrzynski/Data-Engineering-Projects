import pandas as pd
from faker import Faker
import random
import os

# Initialize Faker for generating synthetic data# Initialize Faker
fake = Faker()

# Define products and their associated categories for transaction simulation    
products = {
    "Laptop": "Electronics",
    "Headphones": "Electronics",
    "Coffee Maker": "Home Appliances",
    "Sneakers": "Footwear",
    "Office Chair": "Furniture",
    "Smartphone": "Electronics",
    "Blender": "Home Appliances"
}

# Generates a single fake transaction record with randomized product, price, and quantity details
def generate_transaction():
    product = random.choice(list(products.keys()))
    category = products[product]
    price = round(random.uniform(20.0, 1500.0), 2)
    quantity = random.randint(1, 5)
    return {
        "transaction_id": fake.uuid4(), # Unique transaction ID
        "customer_id": fake.uuid4(), # Unique customer ID
        "product": product, # Product name
        "category": category, # Product category
        "price": price, # Product price
        "quantity": quantity, # Number of items purchased
        "transaction_date": fake.date_between(start_date="-30d", end_date="today").isoformat() # Random transaction date within the last 30 days 
    }

# Generates a dataset of fake transactions based on the specified number of records
def generate_dataset(num_records=1000):
    data = [generate_transaction() for _ in range(num_records)]
    df = pd.DataFrame(data)
    return df

# Saves the generated dataset to the raw data folder as a CSV file
def save_raw_data(df, filename="sales_data.csv"):
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
    raw_dir = os.path.join(script_dir, "..", "data", "raw")  # Correct path to /data/raw
    os.makedirs(raw_dir, exist_ok=True)
    file_path = os.path.join(raw_dir, filename)
    df.to_csv(file_path, index=False)
    print(f"Raw data saved to {file_path}")

# Main execution block: generates and saves synthetic transaction data if script is run directly
if __name__ == "__main__":
    df = generate_dataset(1000)  # Generate 1000 records
    save_raw_data(df)
