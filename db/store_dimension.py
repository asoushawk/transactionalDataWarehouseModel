import sqlite3

conn = sqlite3.connect('dw.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE store_dimension (store_key INTEGER PRIMARY KEY AUTOINCREMENT,
	store_name TEXT,
	store_city TEXT,
	store_state TEXT,
	store_address TEXT);""")
