import flask
import json
from flask import render_template
from flask import request, redirect, url_for, send_file, jsonify

from transactions import *
from queries.analyticalQueries import *
import json

app = flask.Flask(__name__)

#****END POINTS
@app.route('/api')
def api():

	return """<h1>API Transactional Data API</h1>
    <p>This API simulates transactions, stores data in a dimensional model and returns analytical data</p>
    <h3>Docs:</h3>
    <p>End Points:</p>
    <ul>
  	<li><a href="api/simulateTransaction">"/api/simulateTransaction":</a> Makes a transaction</li>
   	<li><a href="api/getTotalByCountry">"/api/getTotalByCountry"</a>: Returns most sold by country</li>
   	<li><a href="api/getProductWithMostUnitsSold">"/api/getProductWithMostUnitsSold"</a>: Returns products with most units sold</li>
  	<li><a href="api/getBestDayOfTheWeek">"/api/getBestDayOfTheWeek"</a>: Sales by weekday</li>
  	<li><a href="api/getBestMonth">"/api/getBestMonth"</a>: Sales by month</li>
 	<li><a href="api/getClientProfile">"/api/getClientProfile"</a>: Sales by client profile</li>	
    </ul>
    """


@app.route('/api/simulateTransaction', methods=['GET'])
def simulateTransaction():
	response = newTransaction()
	return jsonify(response)


@app.route('/api/getTotalByCountry', methods=['GET'])
def returnTotalByCountry():
	
	response = getTotalByCountry()
	data = list()
	id = 0
	
	for item in response:
		id = id+1
		country = item[0]
		total_sold_brl = round(float(item[1]), 2)

		dataDict = {'id': id,
		'country': country,
		'total_sold_brl': total_sold_brl}
		data.append(dataDict)

	return json.dumps({'data': data})

@app.route('/api/getTotalByStore', methods=['GET'])
def returnTotalByStore():

	response = getTotalByCountry()
	data = list()
	id = 0


	for item in response:
		store = item[0]
		total_sold_brl[1]
		id = id+1
		dataDict = {'id': id,
		'store': store,
		'total_sold_brl': total_sold_brl}
		data.append(dataDict)

	return json.dumps({'data': data})


@app.route('/api/getProductWithMostUnitsSold', methods=['GET'])
def returnProductWithMostUnitsSold():

	response = getProductWithMostUnitsSold()
	data = list()
	id = 0


	for item in response:
		product = item[0] 
		units_sold = item[1]

		id = id+1
		dataDict = {'id': id,
		'product': product,
		'units_sold': units_sold}
		data.append(dataDict)

	return json.dumps({'data': data})

@app.route('/api/getBestDayOfTheWeek', methods=['GET'])
def returnBestDayOfTheWeek():

	response = getBestDayOfTheWeek()
	data = list()
	id = 0


	for item in response:
		day_of_the_week = item[0]
		units_sold = item[1]
		total_sold_brl = item[2]

		id = id+1
		dataDict = {'id': id,
		'day_of_the_week': day_of_the_week,
		'units_sold': units_sold,
		'total_sold_brl': total_sold_brl}
		data.append(dataDict)

	return json.dumps({'data': data})

@app.route('/api/getBestMonth', methods=['GET'])
def returnBestMonth():

	response = getBestMonth()
	data = list()
	id = 0


	for item in response:
		month = item[0]
		units_sold = item[1]
		total_sold_brl = item[2]

		id = id+1
		dataDict = {'id': id,
		'month': month,
		'units_sold': units_sold,
		'total_sold_brl': total_sold_brl}
		data.append(dataDict)

	return json.dumps({'data': data})

@app.route('/api/getClientProfile', methods=['GET'])
def returnClientProfile():

	response = getClientProfile()
	data = list()
	id = 0


	for item in response:
		purchase_profile = item[0]
		total_sold_brl = item[1]

		id = id+1
		dataDict = {'id': id,
		'purchase_profile': purchase_profile,
		'total_sold_brl': total_sold_brl}
		data.append(dataDict)

	return json.dumps({'data': data})
