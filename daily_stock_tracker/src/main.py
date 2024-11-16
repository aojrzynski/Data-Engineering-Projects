from data_extractor import get_daily_stock_data
from data_cleaner import clean_stock_data
from data_storage import save_to_sqlite

def run_pipeline(stock_symbol='AAPL'):
    # Extract the data
    raw_data = get_daily_stock_data(stock_symbol)
    
    if raw_data is not None:
        # Clean the data
        cleaned_data = clean_stock_data(raw_data)
        
        # Save the data to SQLite
        save_to_sqlite(cleaned_data)
        print("Pipeline run completed successfully.")
    else:
        print("Failed to fetch data. Pipeline run aborted.")

if __name__ == '__main__':
    run_pipeline()
