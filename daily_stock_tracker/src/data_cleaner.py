import pandas as pd

def clean_stock_data(df):
    """Clean the stock data by handling missing values and converting data types."""
    # Drop any rows with missing values
    df = df.dropna()

    # Ensure data types are consistent (e.g., numeric columns)
    df['open'] = pd.to_numeric(df['open'])
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])
    df['close'] = pd.to_numeric(df['close'])
    df['volume'] = pd.to_numeric(df['volume'])

    # Drop duplicate rows if they exist
    df = df.drop_duplicates()

    return df

if __name__ == '__main__':
    # Sample testing using dummy data or the result from data_extractor.py
    from data_extractor import get_daily_stock_data

    stock_symbol = 'AAPL'
    raw_data = get_daily_stock_data(stock_symbol)
    
    if raw_data is not None:
        cleaned_data = clean_stock_data(raw_data)
        print(cleaned_data.head())
