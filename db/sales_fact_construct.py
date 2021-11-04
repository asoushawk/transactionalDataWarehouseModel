import sqlite3

conn = sqlite3.connect('dw.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE Sales_Fact (costumer_key INT,
	product_key INT,
	store_key INT,
	promotion_key INT,
	time_key INT,
	units_sold INT,
	value_sold_brl INT
	);""")
