from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')  # 127.0.0.1:5000
def index():
    return render_template('index.html') 

@app.route('/hello')
def hello():
    name = request.args.get('name', '') 
    return render_template('hello.html', name=name)

app.run(debug=True)