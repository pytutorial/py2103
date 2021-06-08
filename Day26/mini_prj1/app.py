from pymongo import MongoClient
from bson.objectid import ObjectId
db_host = '34.70.69.231'
db_user = 'mongo'
db_pass = 'abc@123'
client = MongoClient(db_host, username=db_user, password=db_pass)
db = client.db0001

import time
from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    productList = list(db.product.find())
    return render_template('index.html', productList=productList)

@app.route('/create-product', methods=['GET', 'POST'])
def createProduct():
    if request.method == 'GET':
        return render_template('form.html')
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

app.run(debug=True)