from flask import Flask
from flask.globals import request

app = Flask(__name__)

productList = [
    {'id': 1, 'name': 'IPhone X', 'price': 10500000},
    {'id': 2, 'name': 'IPhone 11', 'price': 11500000},
    {'id': 3, 'name': 'IPhone 12', 'price': 12500000},
]

@app.route('/')
def index():
    html = '<ul>'
    for p in productList:
        pid = p['id']
        html += f'<li><a href="/view-product-detail?id={pid}"> {p["name"]} </a></li>'
    html += '</ul>'
    return html

#http://127.0.0.1:5000/view-product-detail?id=1
@app.route('/view-product-detail')
def viewProduct():
    productId = int(request.args.get('id', -1))
    if productId < 1 or productId > len(productList):
        return 'Not found'
    
    p = productList[productId-1]
    return f'''
        <div>
            <p>Sản phẩm: <b> {p['name']} </b>    </p>
            <p>Đơn giá : <b> {p['price']} đ </b> </p>
        </div>
    '''

app.run(debug=True)  # hot reload