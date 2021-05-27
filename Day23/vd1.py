from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<b>Hello<b>'

app.run(host="0.0.0.0", port=5000, debug=True) # Hot reload