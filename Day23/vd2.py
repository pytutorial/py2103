from flask import Flask, request

app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000?username=Nguyen+Van+A
def index():
    print(request.args)
    username = request.args.get('username', '')
    return f"Hello {username}"

app.run()