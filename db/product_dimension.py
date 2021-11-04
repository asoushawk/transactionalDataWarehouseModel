import sqlite3

conn = sqlite3.connect('dw.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE product_dimension (product_key INTEGER PRIMARY KEY AUTOINCREMENT,
	product_title TEXT,
	product_price INT,
	product_rating INT,
	product_category TEXT);""")
