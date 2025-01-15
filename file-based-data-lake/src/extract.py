import pandas as pd
from faker import Faker
import random
import os

# Initialize Faker
fake = Faker()

# Define products and categories
products = {
    "Laptop": "Electronics",
    "Headphones": "Electronics",
    "Coffee Maker": "Home Appliances",
    "Sneakers": "Footwear",
    "Office Chair": "Furniture",
    "Smartphone": "Electronics",
    "Blender": "Home Appliances"
}

def generate_transaction():
    """Generate a single fake transaction record."""
    product = random.choice(list(products.keys()))
    category = products[product]
    price = round(random.uniform(20.0, 1500.0), 2)
    quantity = random.randint(1, 5)
    return {
        "transaction_id": fake.uuid4(),
        "customer_id": fake.uuid4(),
        "product": product,
        "category": category,
        "price": price,
        "quantity": quantity,
        "transaction_date": fake.date_between(start_date="-30d", end_date="today").isoformat()
    }

def generate_dataset(num_records=1000):
    """Generate a dataset of fake transactions."""
    data = [generate_transaction() for _ in range(num_records)]
    df = pd.DataFrame(data)
    return df

def save_raw_data(df, filename="sales_data.csv"):
    """Save the generated data to the raw data folder."""
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
    raw_dir = os.path.join(script_dir, "..", "data", "raw")  # Correct path to /data/raw
    os.makedirs(raw_dir, exist_ok=True)
    file_path = os.path.join(raw_dir, filename)
    df.to_csv(file_path, index=False)
    print(f"Raw data saved to {file_path}")


if __name__ == "__main__":
    df = generate_dataset(1000)  # Generate 1000 records
    save_raw_data(df)
