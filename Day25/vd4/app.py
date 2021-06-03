from flask import Flask, request, jsonify, render_template

from pymongo import MongoClient
from bson.objectid import ObjectId
db_host = '34.70.69.231'
db_user = 'mongo'
db_pass = 'abc@123'

client = MongoClient(db_host, username=db_user, password=db_pass)
db = client.py2103

app = Flask(__name__)

@app.route('/get-product-list') #127.0.0.1:5000/get-product-list
def getProductList():
    productList = list(db.product.find())
    for p in productList: p['_id'] = str(p['_id'])
    return jsonify(productList)

@app.route('/get-product-detail/<pid>')
def getProductDetail(pid):
    product = db.product.find_one({'_id': ObjectId(pid)})
    product['_id'] = str(product['_id'])
    return jsonify(product)

@app.route('/create-product', methods=['POST'])
def createProduct():
    code = request.form['code']
    name = request.form['name']
    price = request.form['price']
    print(f'code={code}, name={name}, price={price}')
    product = {'code': code, 'name': name, 'price': int(price)}
    productId = db.product.insert(product)
    product['_id'] = str(productId)
    return jsonify(product)

@app.route('/update-product/<pid>', methods=['PUT'])
def updateProduct(pid):
    code = request.form['code']
    name = request.form['name']
    price = request.form['price']
    product = {'code': code, 'name': name, 'price': price}
    db.product.update({'_id': ObjectId(pid)}, product)
    product['_id'] = pid
    return jsonify(product)

@app.route('/delete-product/<pid>', methods=['DELETE'])
def deleteProduct(pid):
    db.product.remove({'_id': ObjectId(pid)})
    return jsonify({'sucess': True})

@app.route('/search-product')
def searchProduct():
    keyword = request.args.get('keyword', '')
    priceMin = int(request.args.get('priceMin') or 0)
    priceMax = int(request.args.get('priceMax') or 100e6)
    productList = list(db.product.find({
        'name':{'$regex': keyword, '$options': 'i'},
        'price':{'$gte': priceMin, '$lte': priceMax}
    }))
    for p in productList: p['_id'] = str(p['_id'])
    return jsonify(productList)

@app.route('/') #127.0.0.1:5000
def index():
    return render_template('index.html')

app.run(debug=True)