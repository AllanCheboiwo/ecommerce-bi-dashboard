import sqlite3

#connect to SQLite database (creates retail.db if it doesnt exist)
conn = sqlite3.connect('data/retail.db')
cursor = conn.cursor()

#read and execurte sql script
with open("scripts/sql/create_tables.sql","r") as file:
    sql_script = file.read()
cursor.executescript(sql_script)

#commit and close
conn.commit()
conn.close()

print("Database and tables created: data/retail.db")