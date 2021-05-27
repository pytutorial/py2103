from flask import Flask, request

productList = [
    {'id' : 1, 'name': 'IPhone X','price':10.5},
    {'id' : 2, 'name': 'IPhone 11','price':11.5},
    {'id' : 3, 'name': 'IPhone 12','price':12.5},
]

app = Flask(__name__)

#127.0.0.1:5000/calc-order
@app.route('/calc-order', methods=['POST'])
def calcOrder():
    productId = request.form['productId']
    qty = request.form['qty']
    print('productId=', productId)
    print('qty=', qty)
    return 'Tổng số tiền : ....'

app.run(debug=True)