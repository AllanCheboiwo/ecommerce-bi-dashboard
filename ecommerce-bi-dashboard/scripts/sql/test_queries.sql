-- Test Customers
SELECT * FROM customers LIMIT 5;

-- Test Products
SELECT * FROM products LIMIT 5;

-- Test Transactions
SELECT * FROM transactions LIMIT 5;

-- Verify foreign keys
SELECT COUNT(*) AS invalid_transactions
FROM transactions t
LEFT JOIN customers c ON t.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- Total sales by country
SELECT c.country, SUM(t.total_price) AS total_sales
FROM transactions t
JOIN customers c ON t.customer_id = c.customer_id
GROUP BY c.country
ORDER BY total_sales DESC
LIMIT 5;