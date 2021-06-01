from flask import Flask, render_template

productList = [
    {'code': 'IPX', 'name': 'Iphone X'},
    {'code': 'IP11', 'name': 'Iphone 11'},
    {'code': 'IP12', 'name': 'Iphone 12'},
]

app = Flask(__name__)

#127.0.0.1:5000
@app.route('/')
def index():
    return render_template('index.html',
                productList=[])

app.run(debug=True)
