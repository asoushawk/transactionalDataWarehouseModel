#Gets API Data

import requests
import json
import random


purchase_profiles  = ['moderate', 'high', 'low']
promotions = ['90% OFF CAMPAINGN', 'PAY 5 TAKE 10', 'XMAS PROMOTION']
ad_types = ['tv', 'online', 'street']
weekDays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

months = ['january', 'february', 'march', 'may', 'april', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


stores = [{'store_name': 'store1',
'store_city': 'Rio de Janeiro',
'store_state': 'Rio de Janeiro',
'store_address': 'Rua da Cidade, Bairro da Luz'}, 

{'store_name': 'store2',
'store_city': 'Salvador',
'store_state': 'Bahia',
'store_address': 'Rua do Carro, Centro'},

{'store_name': 'store3',
'store_city': 'Feira de Santana',
'store_state': 'Bahia',
'store_address': 'Rua Padre João, Centro'}]


def generateCostumerDimension():
	
	#Reads API in order to generate a random user
	url = 'https://randomuser.me/api/'
	r = requests.get(url)
	
	jsonResponse = r.json()
	results = jsonResponse['results'][0]

	gender = results['gender']
	
	firstname = results['name']['first']
	lastname = results['name']['last']
	costumer_name = firstname + ' ' + lastname

	#selects a random purchase profile
	purchase_profile = purchase_profiles[random.randint(0,2)]
	
	age = results['dob']['age']
	city = results['location']['city']
	state = results['location']['state']
	country = results['location']['country']

	data = costumer_name, purchase_profile, gender, age, city, state, country
	return data

def generateProductDimension():
	url = 'https://fakestoreapi.com/products/'
	r = requests.get(url)

	jsonResponse = r.json()
	produtoRandom = random.randint(0,19)
	
	#Eversince the api returns 20 products, we will get one of those randomly
	produto = jsonResponse[produtoRandom]
	
	product_title = produto['title']
	product_price = produto['price']
	product_rating = produto['rating']['rate']
	product_category = produto['category']

	data = product_title, product_price, product_rating, product_category
	return data

def generatePromotionDimension():
	promotion_name = promotions[random.randint(0,2)]
	ad_type = ad_types[random.randint(0,2)]

	data = promotion_name, ad_type
	return data



def generateStoreDimension():
	
	#Gets random store
	
	store = stores[random.randint(0,2)]
	store_name = store['store_name']
	store_city = store['store_city']
	store_state = store['store_state']
	store_address = store['store_address']

	data = store_name, store_city, store_state, store_address
	return data

def generateTimeDimension():
	
	dayoftheweek = weekDays[random.randint(0,6)]
	weeknumber = str(random.randint(1,52))
	month = months[random.randint(0,11)]

	data = dayoftheweek, weeknumber, month
	return data


