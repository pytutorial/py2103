from pymongo import MongoClient
from bson.objectid import ObjectId
db_host = '34.70.69.231'
db_user = 'mongo'
db_pass = 'abc@123'
client = MongoClient(db_host, username=db_user, password=db_pass)
db = client.db0001

import time
from flask import Flask, request, render_template, redirect, jsonify
app = Flask(__name__)

@app.route('/update-product/<pid>', methods=['GET', 'POST'])
def updateProduct(pid):
    if request.method == 'GET':
        product = db.product.find_one({'_id': ObjectId(pid)})
        return render_template('form.html', product=product)
    else:
        #TODO: Update DB
        return redirect('/')

@app.route('/create-product', methods=['GET', 'POST'])
def createProduct():
    if request.method == 'GET':
        return render_template('form.html', product={})
    else:
        fields = ['code', 'name', 'price', 'qty', 'description']
        product = {f : request.form[f] for f in fields}
        product['price'] = int(product['price'] or 0)
        product['qty'] =  int(product['qty'] or 0)

        file = request.files.get('image')
        
        if file is not None and file.filename != '':
            filepath =  f'/static/images/{str(time.time())}.jpg'
            file.save(app.root_path + filepath)
            product['image'] = filepath

        db.product.insert(product)
        return redirect('/')

@app.route('/delete-product/<pid>', methods=['DELETE'])
def deleteProduct(pid):
    db.product.remove({'_id': ObjectId(pid)})
    return jsonify({'success': True})

@app.route('/')
def index():
    keyword = request.args.get('keyword', '')
    productList = list(db.product.find({
        'name': {'$regex': keyword, '$options': 'i'}
    }))
    return render_template('index.html', productList=productList, keyword=keyword)

app.run(debug=True)