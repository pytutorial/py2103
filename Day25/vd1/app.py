from flask import Flask

app = Flask(__name__)

#127.0.0.1:5000/static/test.txt
#127.0.0.1:5000/static/images/img1.jpg
app.run(debug=True)