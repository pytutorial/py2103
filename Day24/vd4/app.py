#pip install pymongo
from pymongo import MongoClient

db_host = '34.70.69.231'
db_user = 'mongo'
db_pass = 'abc@123'
db_name = 'py2103'
client = MongoClient(db_host, username=db_user, password=db_pass)
db = client.py2103

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    productList = db.product.find()
    return render_template('index.html', productList=productList)

app.run(debug=True)