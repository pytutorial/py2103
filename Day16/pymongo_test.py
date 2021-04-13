from pymongo import MongoClient

db_host = '34.122.175.106'
username = 'admin'
password = 'abc@123'

client = MongoClient(
    db_host, 
    username=username,
    password=password)

db = client.py2103   #db name
product = db.product.find_one({'code': 'IPX'})
print('IPX:', product['name'])

phone = input('Số điện thoại KH:')
lst = db.pos_order.find({'customer.phone' : phone})
for item in lst:
    print(item['product']['name'])