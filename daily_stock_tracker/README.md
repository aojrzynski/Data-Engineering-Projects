# Daily Stock Tracker

## Project Overview
The **Daily Stock Tracker** automates the process of fetching, cleaning, storing, and visualizing daily stock price data. This project uses Python and the Alpha Vantage API to retrieve stock data, clean it, store it in an SQLite database, and generate visual insights. The pipeline can run daily using Windows Task Scheduler for automation.

## Features
- **Data Extraction**: Retrieves daily stock prices using the Alpha Vantage API.
- **Data Cleaning**: Cleans and formats data, handling missing values and duplicates.
- **Data Storage**: Saves cleaned data into an SQLite database.
- **Data Visualization**: Generates a plot of daily closing prices.
- **Automation**: Runs the pipeline daily using Windows Task Scheduler.

## Installation

### Prerequisites
- Python 3.8 or higher
- An Alpha Vantage API key (get a free API key [here](https://www.alphavantage.co/support/#api-key))

### Installation Steps
1. **Install dependencies (found in the requirements.txt file)**<br>
Can also use the command: `pip install -r requirements.txt`
2. **Create a .env file in the root directory and add your API key**<br>
`ALPHA_VANTAGE_API_KEY=your_api_key_here`

## Usage
***IMPORTANT NOTE: The default stock ticker symbol used in this project is AAPL (Apple Inc.). If you want to track a different stock, modify the run_pipeline() function in src/main.py:***
```
# src/main.py
def run_pipeline(stock_symbol='AAPL'):
    # Change 'AAPL' to your preferred stock ticker symbol
```

### Running the Pipeline Manually
Run the entire pipeline manually with: `python src/main.py`

### Generating Data Visualization
Create and save a plot of daily closing prices by running: `python src/data_analysis.py`

### Automating with Windows Task Scheduler
**Create or edit a Batch File (run_pipeline.bat)**

   This file should be in the root directory with the following content:
   ```
   @echo off
   python C:\path\to\your\project\src\main.py
   pause
   ```
   Replace C:\path\to\your\project with the full path to your project directory.

**Set Up Task Scheduler**
  - Open Task Scheduler and click Create Basic Task.
  - Name the task (e.g., "Daily Stock Tracker Pipeline") and set the trigger to Daily at a specific time.
  - For the Action, select Start a Program and browse to run_pipeline.bat.
  - Finish the setup and save the task.

## Example Output
### Database View
![image](https://github.com/user-attachments/assets/ca8e064d-5788-4079-bd75-fb616de7f925)

### Visualization
![stock_prices_plot](https://github.com/user-attachments/assets/9090611b-491f-41f3-8aec-f0a131e07994)

## License
This project is licensed under the MIT License.

## Acknowledgments
Data sourced from Alpha Vantage.

