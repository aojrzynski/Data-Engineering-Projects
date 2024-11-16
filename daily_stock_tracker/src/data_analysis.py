import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
db_path = 'daily_stock_tracker/data/stock_data.db'
conn = sqlite3.connect(db_path)

# Read data from the database
query = "SELECT * FROM daily_stock_prices"
df = pd.read_sql_query(query, conn)
conn.close()

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Plot daily closing prices
plt.figure(figsize=(14, 7))
plt.plot(df['date'], df['close'], marker='o', linestyle='-', label='Closing Price')
plt.title('Daily Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)

# Save the plot as an image
plt.savefig('daily_stock_tracker/data/stock_prices_plot.png')

# Show the plot
plt.show()
