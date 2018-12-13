import os
import sys
from flask import Flask, request, jsonify
import numpy as np
import pickleW
import utils.utils as utils

app = Flask(__name__)

model = pickle.load(open(os.getenv('MODEL'), 'rb'))
features=pickle.load(open(os.getenv('FEATURES'), 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        valid = utils.is_valid(data, features)
        if valid is not True:
            return jsonify({
                "error": valid,
                })
        model_input = utils.preprocessing(data, features)
        result = model.predict(model_input)
        output = 'p' if result==1 else 'e'
        return jsonify({
            "class": output,
            "debug": {"model_used": os.getenv('MODEL')}
            })