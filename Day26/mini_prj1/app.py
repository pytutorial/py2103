from pymongo import MongoClient
from bson.objectid import ObjectId
db_host = '34.70.69.231'
db_user = 'mongo'
db_pass = 'abc@123'
client = MongoClient(db_host, username=db_user, password=db_pass)
db = client.db0001

from flask import Flask, request, render_template, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)