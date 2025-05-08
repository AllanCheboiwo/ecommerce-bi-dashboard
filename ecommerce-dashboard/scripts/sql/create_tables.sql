 -- Drop tables if they exit
 -- Create customer table
 CREATE TABLE customers(
    customer_id INTEGER PRIMARY KEY,
    country TEXT NOT NULL
 );

 --create product table
 CREATE TABLE products(
    stock_code TEXT PRIMARY KEY,
    description TEXT,
    unit_price REAL
 );

---create transaction table
CREATE TABLE transactions(
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_no TEXT NOT NULL,
    stock_code TEXT NOT NULL,
    customer_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    invoice_date TEXT NOT NULL,
    total_price REAL NOT NULL,
    FOREIGN KEY (stock_code) REFERENCES products(stock_code),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

--Create indexes for faster queries
CREATE INDEX idx_transactions_invoice_no ON transactions(invoice_no);
CREATE INDEX idx_transactions_customer_id ON transactions(customer_id);