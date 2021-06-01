from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')  # 127.0.0.1:5000?name=Nguyen+Van+A
def index():
    name = request.args.get('name', '') 
    return render_template('index.html', username=name) 

app.run(debug=True)