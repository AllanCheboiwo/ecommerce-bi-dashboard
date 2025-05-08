import sqlite3
import pandas as pd

#load cleaned CSV
df = pd.read_csv("data/onlineRetailCleaned.csv")

#Connect to database 
conn = sqlite3.connect("data/retail.db")
cursor = conn.cursor()

#prepare and load customers
customers_df = df[["CustomerID","Country"]].drop_duplicates(subset=['CustomerID']).rename(columns={'CustomerID':'customer_id',"Country":"country"})
customers_df.to_sql("customers",conn,if_exists='append',index=False)
print(f"Loaded {len(customers_df)} customers")

#prepare and load products
products_df = df[['StockCode','Description','UnitPrice']].drop_duplicates(subset=['StockCode']).rename(
    columns={'StockCode': 'stock_code', 'Description': 'description', 'UnitPrice': 'unit_price'}
)
products_df.to_sql('products', conn, if_exists='append', index=False)
print(f"Loaded {len(products_df)} products")

# Prepare and load Transactions
transactions_df = df[['InvoiceNo', 'StockCode', 'CustomerID', 'Quantity', 'InvoiceDate', 'TotalPrice']].rename(
    columns={
        'InvoiceNo': 'invoice_no',
        'StockCode': 'stock_code',
        'CustomerID': 'customer_id',
        'Quantity': 'quantity',
        'InvoiceDate': 'invoice_date',
        'TotalPrice': 'total_price'
    }
)

print("Unique invoice_no values:", transactions_df['invoice_no'].nunique())
print("Total transactions:", len(transactions_df))
transactions_df.to_sql('transactions', conn, if_exists='append', index=False)
print(f"Loaded {len(transactions_df)} transactions")

# Commit and close
conn.commit()
conn.close()

print("Data loaded into data/retail.db")
