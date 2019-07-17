import grammar as gm
import json
import os
from flask import Flask, redirect, url_for, request, jsonify
from pyknow import *


app = Flask(__name__)

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

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5010)
