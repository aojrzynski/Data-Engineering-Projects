import sqlite3
import pandas as pd

def save_to_sqlite(df, db_path='daily_stock_tracker/data/stock_data.db', table_name='daily_stock_prices'):
    """Save the cleaned DataFrame to an SQLite database."""
    # Connect to SQLite database (creates db if not exists)
    conn = sqlite3.connect(db_path)
    try:
        # Save DataFrame to SQL table
        df.to_sql(table_name, conn, if_exists='append', index_label='date')
        print(f"Data successfully saved to {db_path} in table '{table_name}'.")
    except Exception as e:
        print("Error saving data to database:", e)
    finally:
        conn.close()

if __name__ == '__main__':
    # Sample testing using dummy cleaned data
    from data_extractor import get_daily_stock_data
    from data_cleaner import clean_stock_data

    stock_symbol = 'AAPL'
    raw_data = get_daily_stock_data(stock_symbol)
    
    if raw_data is not None:
        cleaned_data = clean_stock_data(raw_data)
        save_to_sqlite(cleaned_data)
