import os
import traceback
import sys
import pandas as pd
import numpy as np

from flask import request
from flask import Flask
from flask import jsonify
import joblib


app = Flask(__name__)
lr = joblib.load('model.pkl')
model_columns = joblib.load('model_columns.pkl')

@app.route('/')
def Main():
    if lr:
        try:
            info = []
            info.append(request.args.get("sex"))
            info.append(request.args.get("age"))
            info.append(request.args.get("currentSmoker"))
            a = np.array(info)
            result = str(round(float(lr.predict_proba(a)[:, 1] * 100), 2)) + '%'
            return result
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        return 'No model here to use'
