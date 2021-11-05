# transactionalDataWarehouseModel
This project showcases a Dimensional Data Warehouse model, utilizing random data from Public APIs  to populate the DW. The fact table is transactional based.Data endpoints are available through an API: https://transactionaldw.herokuapp.com/api


## Schema
![alt text](https://github.com/asoushawk/transactionalDataWarehouseModel/blob/main/img/dwSchema.png?raw=true)
## Analytical Queries
Some questions and answers using the Datawarehouse's data:
  - Which is my best day of the week?
  - ![alt text](https://github.com/asoushawk/transactionalDataWarehouseModel/blob/main/img/bestdayoftheweek.png?raw=true)
  - Which country buys the most?
  - ![alt text](https://github.com/asoushawk/transactionalDataWarehouseModel/blob/main/img/country_ranking.png?raw=true)
  - Which purchase_profile buys the most?
  - ![alt text](https://github.com/asoushawk/transactionalDataWarehouseModel/blob/main/img/purchase_profile.png?raw=true)
  - What are my most sold products?
  - ![alt text](https://github.com/asoushawk/transactionalDataWarehouseModel/blob/main/img/most_sold_products.png?raw=true)
  - Which store sells the least?
  - ![alt text](https://github.com/asoushawk/transactionalDataWarehouseModel/blob/main/img/stores_total_sold.png?raw=true)
## Fact Table Example
![alt text](https://github.com/asoushawk/transactionalDataWarehouseModel/blob/main/img/fact_table.png?raw=true)
## Product Dimension
![alt text](https://github.com/asoushawk/transactionalDataWarehouseModel/blob/main/img/product_dimension.png?raw=true)
## Costumer Dimension
![alt text](https://github.com/asoushawk/transactionalDataWarehouseModel/blob/main/img/costumer_dimension.png?raw=true)
