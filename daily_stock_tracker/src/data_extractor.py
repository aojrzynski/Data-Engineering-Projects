import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the .env file
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# Define the base URL for Alpha Vantage API
BASE_URL = 'https://www.alphavantage.co/query'

def get_daily_stock_data(symbol):
    """Fetch daily stock data for a given symbol."""
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY,
        'outputsize': 'compact'  # Use 'full' for complete historical data
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if 'Time Series (Daily)' not in data:
        print("Error fetching data:", data)
        return None

    # Parse the time series data into a DataFrame
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    })

    # Convert index to datetime and sort
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    return df

if __name__ == '__main__':
    # Example usage
    stock_symbol = 'AAPL'  # Replace with the symbol of your choice
    stock_data = get_daily_stock_data(stock_symbol)

    if stock_data is not None:
        print(stock_data.head())
