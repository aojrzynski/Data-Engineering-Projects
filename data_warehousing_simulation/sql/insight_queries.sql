-- Query 1: Total Number of Customers
-- This query provides the total number of customers in the database.
SELECT COUNT(*) AS total_customers
FROM customers;

-- --------------------------------------------------------

-- Query 2: Total Sales Revenue by Product
-- This query calculates the total revenue generated by each product and orders the results from highest to lowest.
SELECT 
    p.product_name,
    SUM(s.quantity * p.price) AS total_revenue
FROM 
    sales s
JOIN 
    products p ON s.product_id = p.product_id
GROUP BY 
    p.product_name
ORDER BY 
    total_revenue DESC;

-- --------------------------------------------------------

-- Query 3: Top 5 Customers by Number of Purchases
-- This query identifies the top 5 customers based on the number of purchases they made.
SELECT 
    c.name,
    COUNT(s.sale_id) AS total_purchases
FROM 
    sales s
JOIN 
    customers c ON s.customer_id = c.customer_id
GROUP BY 
    c.name
ORDER BY 
    total_purchases DESC
LIMIT 5;

-- --------------------------------------------------------

-- Query 4: Monthly Sales Trends
-- This query shows the total revenue per month, helping to identify seasonal trends.
SELECT 
    d.month,
    SUM(s.quantity * p.price) AS monthly_revenue
FROM 
    sales s
JOIN 
    dates d ON s.sale_date = d.full_date
JOIN 
    products p ON s.product_id = p.product_id
GROUP BY 
    d.month
ORDER BY 
    d.month;

-- --------------------------------------------------------

-- Query 5: Most Popular Product Categories
-- This query displays the most popular product categories based on the number of sales.
SELECT 
    p.category,
    COUNT(s.sale_id) AS total_sales
FROM 
    sales s
JOIN 
    products p ON s.product_id = p.product_id
GROUP BY 
    p.category
ORDER BY 
    total_sales DESC;
