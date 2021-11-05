from generateDimensionsData import *
from insertQueries import *
import sqlite3

import random

conn = sqlite3.connect('db/dw.db', check_same_thread=False)
cursor = conn.cursor()


#Simulates a Transaction
def newTransaction():
	#Costumer
	costumer_name, purchase_profile, gender, age, city, state, country = generateCostumerDimension()

	#Product
	product_title, product_price, product_rating, product_category = generateProductDimension()

	#Promotion
	promotion_name, ad_type = generatePromotionDimension()

	#Store
	store_name, store_city, store_state, store_address = generateStoreDimension()

	#Time
	dayoftheweek, weeknumber, month = generateTimeDimension()

	#Simulates number of units sold and generates price
	units_sold = str(random.randint(1,10))
	value_sold_brl = str(round(float(product_price * float(units_sold)),2))

	#Inserts data in the dimension tables and then in the fact table and
	#returns the primary keys
	costumer_key = insertCostumer(costumer_name, purchase_profile, gender, age, city, state, country)
	product_key = insertProduct(product_title, product_price, product_rating, product_category)
	promotion_key = insertPromotion(promotion_name, ad_type)
	store_key = insertStore(store_name, store_city, store_state, store_address)
	time_key = insertTime(dayoftheweek, weeknumber, month)

	#Inserts data in the fact table
	insertFactTable(costumer_key, product_key, promotion_key, store_key, time_key,value_sold_brl, units_sold)

	response = {'status': "Transaction Complete",
	'client': costumer_name,
	'value': value_sold_brl,
	'store': store_name}

	return response










