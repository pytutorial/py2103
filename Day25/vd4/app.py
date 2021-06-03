from flask import Flask, request, jsonify
from pymongo import MongoClient

from bson.objectid import ObjectId
db_host = '34.70.69.231'
db_user = 'mongo'
db_pass = 'abc@123'

client = MongoClient(db_host, username=db_user, password=db_pass)
db = client.nvx

app = Flask(__name__)

app.run(debug=True)