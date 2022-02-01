#!/usr/bin/env python3
from flask import Flask, jsonify, request
import numpy as np
import json
from joblib import load
import os

app = Flask(__name__)

# load model
mdl = load('XGBoostModelFinalSequential.joblib')

# load type scaler
cat_scaler = load('TypeScalerFinalSequential.joblib')

@app.route("/is-fraud", methods=["POST"])
def analyze():
    data = request.get_json()
    if len(data) < 9:
        return jsonify({"error": "wrong input"}), 400
    if os.path.exists('dumpfile.json'):
        with open('dumpfile.json','r') as fout:
            r = fout.readlines()[-1]
            r = json.loads(r)
        prev_step = r['step']
        prevAmt = r['amount']
        prevType = cat_scaler.transform(np.array(r['type']).reshape(1,-1))[0][0]
        prevNameOrig = r['nameOrig']
        prevNameDest = r['nameDest']
    else:
        prev_step = np.nan
        prevAmt = np.nan
        prevType = np.nan
        prevNameOrig = np.nan
        prevNameDest = np.nan
    with open('dumpfile.json','a') as fout:
        json.dump(data,fout)
        fout.write('\n')
    deltaDest = data['oldbalanceDest'] - data['newbalanceDest']
    type = cat_scaler.transform(np.array(data['type']).reshape(1,-1))[0][0]
    deltaOrig = data['newbalanceOrig'] - data['oldbalanceOrig']
    diffTime = data['step'] - prev_step
    aggAmt = data['amount'] + prevAmt
    nameOrigBool = data['nameOrig'] == prevNameOrig
    nameDestBool = data['nameDest'] == prevNameDest
    diffType = type - prevType
    features = np.array([data['amount'],deltaDest,data['step'],prev_step,type,
                        data['oldbalanceOrig'],data['newbalanceOrig'],data['newbalanceDest'],
                        data['oldbalanceDest'],deltaOrig,prevAmt,diffTime,aggAmt,nameOrigBool,
                        nameDestBool,prevType,diffType],dtype=float)
    pred = mdl.predict(features.reshape(1,-1))
    if pred == 1:
        p = True
    else:
        p = False
    return jsonify({"isFraud": p})


