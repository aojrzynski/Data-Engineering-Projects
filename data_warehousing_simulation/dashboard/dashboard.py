import streamlit as st # For building the web app interface
import pandas as pd # For data manipulation
from sqlalchemy import create_engine # For connecting to the PostgreSQL database

# Connect to PostgreSQL database
engine = create_engine('postgresql+psycopg2://username:password@localhost:5432/data_warehouse')

# Set the title of the Streamlit dashboard
st.title("Data Warehouse Dashboard")

# Sidebar options for report selection
st.sidebar.header("Select Report")
option = st.sidebar.selectbox("Choose a report", ["Total Customers", "Top 5 Products", "Monthly Revenue"])

# Generate report based on selected option
if option == "Total Customers":
    # Query for total number of customers
    query = "SELECT COUNT(*) AS total_customers FROM customers;"
    result = pd.read_sql(query, con=engine)
    st.write("Total Number of Customers:", result['total_customers'][0])

elif option == "Top 5 Products":
    # Query for top 5 products by total quantity sold
    query = """
    SELECT p.product_name, SUM(s.quantity) AS total_quantity
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_quantity DESC
    LIMIT 5;
    """
    result = pd.read_sql(query, con=engine)
    st.write("Top 5 Products by Sales:")
    st.dataframe(result)

elif option == "Monthly Revenue":
    # Query for monthly revenue calculation
    query = """
    SELECT d.month, SUM(s.quantity * p.price) AS monthly_revenue
    FROM sales s
    JOIN dates d ON s.sale_date = d.full_date
    JOIN products p ON s.product_id = p.product_id
    GROUP BY d.month
    ORDER BY d.month;
    """
    result = pd.read_sql(query, con=engine)
    st.line_chart(result.set_index('month')['monthly_revenue'])
