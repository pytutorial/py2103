from flask import Flask, request

app = Flask(__name__)

#127.0.0.1:5000/hello
@app.route('/hello', methods=['POST'])
def hello():
    username = request.form['username']
    return "Xin chào " + username

app.run(debug=True)