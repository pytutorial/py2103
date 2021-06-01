#pip install pymongo
import re
from pymongo import MongoClient

db_host = '34.70.69.231'
db_user = 'mongo'
db_pass = 'abc@123'
#db_name = 'py2103'
client = MongoClient(db_host, username=db_user, password=db_pass)
db = client.nvx

from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    productList = db.product.find()
    return render_template('index.html', productList=productList)

@app.route('/add-product')
def addProduct():
    return render_template('product_form.html')

@app.route('/save-product', methods=['POST'])
def saveProduct():
    code = request.form['code']
    name = request.form['name']
    price = int(request.form['price'] or 0)
    db.product.insert({
        'code': code,
        'name': name,
        'price': price
    })
    return redirect('/')

from bson.objectid import ObjectId
@app.route('/delete-product',methods=['POST'])
def deleteProduct():
    pid = request.form['pid']
    db.product.remove({'_id': ObjectId(pid)})
    #return 'Pid:' + pid
    return redirect('/')

app.run(debug=True)