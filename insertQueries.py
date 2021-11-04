import sqlite3

conn = sqlite3.connect('db/dw.db')
cursor = conn.cursor()

def insertFactTable(costumer_key, product_key, promotion_key, store_key, time_key,value_sold_brl, units_sold):
	cursor.execute("INSERT INTO Sales_Fact(costumer_key, product_key, store_key, promotion_key, time_key, units_sold, value_sold_brl) VALUES (?,?,?,?,?,?,?)", (costumer_key, product_key, store_key, promotion_key, time_key, units_sold, value_sold_brl))
	conn.commit()

def insertCostumer(costumer_name, purchase_profile, gender, age, city, state, country):
	
	cursor.execute("INSERT INTO costumer_dimension(costumer_name, purchase_profile, gender, age, city, state, country) VALUES (?,?,?,?,?,?,?)", (costumer_name, purchase_profile, gender, age, city, state, country))
	cursor.execute("SELECT last_insert_rowid()")
	
	conn.commit()
	costumer_key = cursor.fetchone()

	return str(costumer_key[0])

def insertProduct(product_title, product_price, product_rating, product_category):
	cursor.execute("INSERT INTO product_dimension(product_title, product_price, product_rating, product_category) VALUES (?,?,?,?)", (product_title, product_price, product_rating, product_category))
	cursor.execute("SELECT last_insert_rowid()")
	conn.commit()
	product_key = cursor.fetchone()

	return str(product_key[0])

def insertPromotion(promotion_name, ad_type):
	cursor.execute("INSERT INTO promotion_dimension(promotion_name, ad_type) VALUES (?,?)", (promotion_name, ad_type))
	cursor.execute("SELECT last_insert_rowid()")
	conn.commit()
	promotion_key = cursor.fetchone()

	return str(promotion_key[0])

def insertStore(store_name, store_city, store_state, store_address):
	cursor.execute("INSERT INTO store_dimension(store_name, store_city, store_state, store_address) VALUES(?,?,?,?)", (store_name, store_city, store_state, store_address))
	cursor.execute("SELECT last_insert_rowid()")
	conn.commit()
	store_key = cursor.fetchone()

	return str(store_key[0])

def insertTime(dayoftheweek, weeknumber, month):
	cursor.execute("INSERT INTO time_dimension(dayoftheweek, weeknumber, SQL_date, month) VALUES (?,?,?,?)", (dayoftheweek, weeknumber, '00-00-0000', month))
	cursor.execute("SELECT last_insert_rowid()")
	conn.commit()
	time_key = cursor.fetchone()

	return str(time_key[0])



