import sqlite3
conn = sqlite3.connect('data/retail.db')
cursor = conn.cursor()
with open('scripts/sql/test_queries.sql', 'r') as file:
    queries = file.read().split(';')
for query in queries:
    if query.strip():
        cursor.execute(query)
        print("\nQuery:", query.strip())
        print("Result:", cursor.fetchall())
conn.close()