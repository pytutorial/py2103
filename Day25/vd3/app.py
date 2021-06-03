from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

#127.0.0.1:5000
@app.route('/')
def index():
    return render_template('index.html') #return jsonify({'message': 'Hello'})

#127.0.0.1:5000/get-product-list
@app.route('/get-product-list')
def getProductList():
    productList = [
        {'code': 'IPX', 'name': 'IPhone X'},
        {'code': 'IP11', 'name': 'IPhone 11'},
    ]
    return jsonify(productList)

app.run(debug=True)