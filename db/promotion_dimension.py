import sqlite3

conn = sqlite3.connect('dw.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE promotion_dimension (promotion_key INTEGER PRIMARY KEY AUTOINCREMENT,
	promotion_name TEXT,
	ad_type TEXT);""")
