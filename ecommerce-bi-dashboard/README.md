# E-Commerce BI Dashboard

A Business Intelligence project analyzing online retail sales data using Python, SQL, and Tableau.

## Project Overview
This project creates a comprehensive BI dashboard for an online retail company, focusing on sales performance, customer insights, and product trends. The dashboard is built using Tableau, with data cleaned and modeled using Python and SQL. It serves as a portfolio piece for the Data and Analytics (BI) Specialist role at the Canadian Cancer Society (CCS), demonstrating skills in data preparation, modeling, and visualization.

## Dataset Description
The dataset used in this analysis is the **Online Retail Dataset**, sourced from the UCI Machine Learning Repository and mirrored on Kaggle. It contains transactions from a UK-based online retailer specializing in unique all-occasion gifts, with many customers being wholesalers. The data spans transactions between 01/12/2010 and 09/12/2011.

### Source Details
- **Original Source**: UCI Machine Learning Repository ([Online Retail Data Set](http://archive.ics.uci.edu/ml/datasets/online+retail)).
- **Kaggle Availability**: Often mirrored as "Online Retail Dataset" (e.g., [Online Retail Dataset on Kaggle](https://www.kaggle.com/datasets/vijayuv/onlineretail)).
- **Contributor**: Dr. Daqing Chen, Director of Public Analytics group, Brunel University, London.
- **Format**: Provided as a CSV or Excel file (e.g., `Online_Retail.csv` or `Online_Retail.xlsx`).

### Dataset Structure
The original dataset includes 541,909 transactions with the following attributes:
- `InvoiceNo`: A 6-digit number uniquely assigned to each transaction (starts with 'C' for cancellations).
- `StockCode`: A 5-digit number uniquely assigned to each product.
- `Description`: Product name or description.
- `Quantity`: Quantities of each product per transaction.
- `InvoiceDate`: Date and time of the transaction.
- `UnitPrice`: Product price per unit in sterling (£).
- `CustomerID`: A 5-digit number uniquely assigned to each customer.
- `Country`: Country where the customer resides.

### Preprocessing
- **Data Cleaning** (Phase 1):
  - Resolved encoding issues (converted from UTF-8 to ISO-8859-1).
  - Removed rows with missing `CustomerID`, duplicates, and invalid entries (e.g., negative `Quantity` or `UnitPrice` ≤ 0).
  - Added `TotalPrice` column (`Quantity` × `UnitPrice`), rounded to 2 decimal places.
  - Final row count: ~401,604 transactions.
- **Data Modeling** (Phase 2):
  - Created a normalized schema with three tables: `customers` (~4,372 rows), `products` (~3,684 rows), and `transactions` (~401,604 rows).
  - Stored in SQLite database (`data/retail.db`), exported to CSVs for Tableau.

## Phase 1: Data Collection and Preparation
- Downloaded Online Retail Dataset from Kaggle.
- Resolved encoding issue (UTF-8 to ISO-8859-1).
- Cleaned data: removed missing CustomerID, duplicates, invalid quantities/prices.
- Added and rounded TotalPrice column to 2 decimal places.
- Added .gitignore to ignore venv/, large datasets, and system files.

## Phase 2: Data Modeling with SQL
- Designed a normalized schema with customers, products, and transactions tables.
- Created separate scripts for database creation and data loading.
- Loaded cleaned data into SQLite database (retail.db).
- Tested data integrity and ran BI queries.

## Phase 3: Data Visualization with Tableau
- Built a Tableau dashboard with visuals for sales by country, top products, sales trends, and top customers.
- Created an insights report summarizing key findings and recommendations.
- Stored dashboard, screenshots, and report in reports/ directory.
- Published dashboard on Tableau Public: [E-Commerce Sales Dashboard](https://public.tableau.com/views/ecommerce-dashboard/E-CommerceSalesDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
- Insights Report: [Dashboard Insights](reports/dashboard_insights.md)
