import os
import sys
from utils import preprocessing
from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

model_path=os.getenv('MODEL')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()

        # TODO: we need preprocess input json. for now we just predict the array of zeros
        # model_input = utils.preprocessing(data)
        model_input=np.zeros(127).reshape(1, -1)

        result = model.predict(model_input)
        output = 'p' if result==1 else 'e'
        return jsonify({"class": output})