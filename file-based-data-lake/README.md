# File-Based Data Lake Simulation
This project simulates a **data lake architecture** using a local file system. It demonstrates the end-to-end data engineering process, including data ingestion, transformation, validation, aggregation, and querying. The project is designed to showcase key data engineering concepts without relying on cloud services.

## Tools and Technologies
- **Python:** Core programming language for pipeline development.  
- **pandas:** Data manipulation and processing.  
- **Faker:** Synthetic data generation.  
- **PyArrow:** Efficient storage and handling of Parquet files.  
- **DuckDB:** SQL engine for querying Parquet files.  
- **Jupyter Notebook:** Interactive data exploration.  
- **Matplotlib:** Data visualization.

## Project Workflow
1. **Data Ingestion (Extract):** Generate synthetic sales data and store it in the `raw` zone.  
2. **Data Processing (Transform):** Clean, validate, and convert data to Parquet format in the `processed` zone.  
3. **Data Aggregation (Load):** Aggregate and summarize data in the `curated` zone.  
4. **Metadata Management:** Track dataset versions, schema, and processing history.  
5. **Data Validation:** Perform automated data quality checks.  
6. **Data Querying:** Use DuckDB to run SQL queries on Parquet files for analysis.  
7. **Pipeline Orchestration:** Automate the entire workflow.

## Project Structure
```
file-based-data-lake/
├── data/                  # Data storage (raw, processed, curated zones)
│   ├── raw/              # Raw, unprocessed data
│   ├── processed/        # Cleaned and standardized data
│   └── curated/          # Aggregated and analysis-ready data
├── metadata/              # Metadata and validation logs
├── notebooks/             # Jupyter notebooks for data exploration
│   └── data_exploration.ipynb
├── src/                   # Python scripts for pipeline stages
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   ├── metadata_manager.py
│   └── run_pipeline.py
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## Installation and Running the Project

### 1. Install Prerequisites
- **Python 3.8+**: Install from [python.org](https://www.python.org/)

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Entire Pipeline
```bash
python src/run_pipeline.py
```

### 4. Explore the Data
```bash
jupyter lab
# Open notebooks/data_exploration.ipynb
```

---

## How Output Should Look Like
- **Raw Zone:** `sales_data.csv`  
- **Processed Zone:** `sales_data_cleaned.parquet`  
- **Curated Zone:**  
  - `category_sales.parquet` (sales by category)  
  - `monthly_sales_trend.parquet` (monthly sales trends)  
  - `top_selling_products.parquet` (top-selling products)  

- **Metadata:**  
  - `dataset_catalog.json` → Tracks datasets and schema.  
  - `validation_log.txt` → Logs data quality issues.

- **Analysis Results:**  
  Run SQL queries in **DuckDB** using the Jupyter Notebook to explore:  
  - Total Sales by Category  
  - Monthly Sales Trends  
  - Top 5 Selling Products  

---

## License
This project is licensed under the MIT License.
