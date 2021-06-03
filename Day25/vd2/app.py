from flask import Flask, request, redirect, render_template

app = Flask(__name__)

#127.0.0.1:5000
@app.route('/')
def index():
    return render_template('index.html')

import os
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('img')
    if file is not None and file.filename != '':
        filename = file.filename
        file_path = os.path.join(app.root_path, 'static', filename) #app.root_path + '/static/' + filename
        file.save(file_path)
        return redirect('/static/' + filename)
    else:
        return 'Không có file tải lên'

app.run(debug=True)
