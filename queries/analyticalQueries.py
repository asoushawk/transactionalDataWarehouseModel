import sqlite3


conn = sqlite3.connect('db/dw.db', check_same_thread=False)
cursor = conn.cursor()



#Total bought by country
def getTotalByCountry():
	cursor.execute("""SELECT c.country, SUM(t.value_sold_brl) AS total_purchased FROM Sales_Fact as t
	LEFT OUTER JOIN costumer_dimension AS c ON t.costumer_key = c.costumer_key
	GROUP BY c.country ORDER BY SUM(t.value_sold_brl) DESC""")
	
	result = cursor.fetchall()
	return result


#Total sold by store
def getTotalByStore():
	cursor.execute("""SELECT s.store_name, SUM(t.value_sold_brl) AS total_purchased
		FROM Sales_Fact as t
		LEFT OUTER JOIN store_dimension AS s ON t.store_key = s.store_key
		GROUP BY s.store_name""")


	result = cursor.fetchall()
	return result



#Product with the most units sold
def getProductWithMostUnitsSold():
	cursor.execute("""SELECT p.product_title, SUM(t.units_sold) as total_sold FROM Sales_Fact as t
		LEFT OUTER JOIN product_dimension AS p ON p.product_key = t.product_key
		GROUP BY p.product_title ORDER BY SUM(t.units_sold) DESC""")

	result = cursor.fetchall()
	return result
	


#Day of the week with the most units sold
def getBestDayOfTheWeek():
	cursor.execute("""SELECT tm.dayoftheweek, SUM(t.units_sold), SUM(t.value_sold_brl) as best_day
		FROM Sales_Fact as t
		LEFT OUTER JOIN time_dimension AS tm ON tm.time_key = t.time_key
		GROUP BY tm.dayoftheweek ORDER BY SUM(t.value_sold_brl) DESC""")

	result = cursor.fetchall()
	return result

#Best month based on total sold in brl
def getBestMonth():
	cursor.execute("""SELECT tm.month, SUM(t.units_sold), SUM(t.value_sold_brl) as best_day
		FROM Sales_Fact as t
		LEFT OUTER JOIN time_dimension AS tm ON tm.time_key = t.time_key
		GROUP BY tm.month ORDER BY SUM(t.value_sold_brl) DESC""")

	result = cursor.fetchall()
	return result




def getClientProfile():
	cursor.execute("""SELECT c.purchase_profile, SUM(t.value_sold_brl) AS pf
		FROM Sales_Fact as t
		LEFT OUTER JOIN costumer_dimension AS c ON c.costumer_key = t.costumer_key
		GROUP BY c.purchase_profile ORDER BY SUM(t.value_sold_brl) DESC""")

	result = cursor.fetchall()
	return result
