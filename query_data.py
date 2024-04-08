import sqlite3

conn = sqlite3.connect('company_data.db')
c = conn.cursor()

c.execute('SELECT * FROM Customer_Data')
rows = c.fetchmany(50)  # Fetch the first 50 rows to check

for row in rows:
    print(row)

conn.close()
