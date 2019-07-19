import grammar as gm
import json
import os
from flask import Flask, redirect, url_for, request, jsonify, flash
from pyknow import *
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = {'py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def initialize():
   return 'Use /Match'

@app.route('/Match', methods = ['POST'])
def Match():
    # Getting the POST Request Body Data
    Data = request.data
    # Converting Text/Plain to JSON Structure
    JsonData = json.loads(Data)
    # Extracting product titles and product classes
    titles = JsonData["products"]
    engine = gm.Knowledge()
    predictions = []
    for title in titles:
        engine.reset()
        engine.declare(Fact(title=title))
        engine.run()  # Run it!
        prediction = engine.category
        predictions.append(prediction)

    response = {
    "predictions":predictions,
    }
    return jsonify(response)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/Upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    print(request.files['grammar'])
    if 'grammar' not in request.files:
        flash('No file part')
        return "False"
    file = request.files['grammar']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "True"

if __name__ == '__main__':
    app.secret_key = '110'
    app.debug = True
    app.run(host='0.0.0.0', port=5020)
