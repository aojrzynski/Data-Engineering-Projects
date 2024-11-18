# Data Warehousing Simulation
## Overview
This project is a data engineering simulation that demonstrates how to build and manage a data warehouse using PostgreSQL. It includes generating synthetic data, creating database schemas, loading data into PostgreSQL, and building an interactive dashboard with Streamlit to visualize and analyze the data. The project is designed to be an example of how data engineering principles can be applied in practice.

## Prerequisites
Before running this project, ensure the following tools and technologies are installed:
-  Python 3.8+: Required to run the Python scripts.
-  PostgreSQL (version 12 or higher): The database management system used for storing and querying data.
-  pgAdmin (optional): A GUI tool for managing PostgreSQL databases.
-  Streamlit: For running the interactive dashboard.

## Installation and Setup
### 1. Install Python Dependencies
Ensure all required Python libraries are installed by checking the requirement.txt file or running:
`pip install -r requirements.txt`

### 2. Set Up PostgreSQL
**Create the data_warehouse Database:**
-  Open your PostgreSQL client (e.g., psql, pgAdmin).
-  Create a new database: `CREATE DATABASE data_warehouse;`

**Update Connection Strings:**

Modify the database connection strings in etl_process.py and dashboard.py to match your PostgreSQL username and password:
```
engine = create_engine('postgresql+psycopg2://username:password@localhost:5432/data_warehouse')
```
Replace username and password with your actual PostgreSQL credentials.

### 3. Run the Schema Creation Script
Create the tables in your data_warehouse database: 
```
psql -U postgres -d data_warehouse -f sql/create_schema.sql
```
Note: Replace postgres with your PostgreSQL username if different.

### 4. Load Data into PostgreSQL
The pre-generated customers.csv, products.csv, and sales.csv files in the data/ directory will be used for data loading.
-  Run the ETL script to load the data: `python scripts/etl_process.py`
-  Verify that the data has been loaded successfully by checking the customers, products, and sales tables in your PostgreSQL database.

### 5. Run the Streamlit Dashboard
The dashboard provides an interactive interface for visualizing and analyzing the data.
-  Run the Streamlit app: `streamlit run dashboard/dashboard.py`
-  Open the URL displayed in your terminal (e.g., http://localhost:8501) to access the dashboard in your web browser.

## Optional: Generate New Synthetic Data
If you want to generate new synthetic data using the Faker library, use the generate_data.py script:
```
python scripts/generate_data.py
```
This will create new versions of customers.csv, products.csv, and sales.csv in the data/ directory.

***Note: After generating new data, you will need to rerun etl_process.py to load it into the database.***

## Optional: Running Analysis Queries
You can run pre-written analysis queries to gain insights from the data:
```
psql -U postgres -d data_warehouse -f sql/insight_queries.sql
```

## Important Notes
-  **Database Credentials:** Ensure you update the username and password in the connection strings within etl_process.py and dashboard.py.
-  **Port and Address:** Ensure that PostgreSQL is running on localhost and the default port 5432. If not, modify the connection strings accordingly.
-  **pgAdmin:** If you prefer a GUI to manage your database, pgAdmin can be used to view and verify table data.

## Tools and Technologies Used
-  **PostgreSQL:** Database management and storage.
-  **SQLAlchemy:** ORM for connecting to and interacting with the database.
-  **pandas:** Data manipulation and loading.
-  **Faker:** Generating synthetic data for testing.
-  **Streamlit:** Building an interactive dashboard for data visualization.

## License
This project is licensed under the MIT License.
