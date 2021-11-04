import sqlite3

conn = sqlite3.connect('dw.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE costumer_dimension (costumer_key INTEGER PRIMARY KEY AUTOINCREMENT,
	costumer_name TEXT,
	purchase_profile TEXT,
	gender TEXT,
	age INT,
	city TEXT,
	state TEXT,
	country TEXT);""")
