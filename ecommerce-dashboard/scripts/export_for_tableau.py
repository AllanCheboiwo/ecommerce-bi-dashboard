import sqlite3
import pandas as pd

conn = sqlite3.connect('data/retail.db')

# Export customers
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
customers_df.to_csv('data/customers.csv', index=False)

# Export products
products_df = pd.read_sql_query("SELECT * FROM products", conn)
products_df.to_csv('data/products.csv', index=False)

# Export transactions
transactions_df = pd.read_sql_query("SELECT * FROM transactions", conn)
transactions_df.to_csv('data/transactions.csv', index=False)

conn.close()
print("Exported tables to CSV: data/customers.csv, data/products.csv, data/transactions.csv")