#!/usr/bin/env python3
from flask import Flask, jsonify, request
import numpy as np
import json
from joblib import load
import os

app = Flask(__name__)

# load model
#mdl = load('XGBoostModelFinal.joblib')

# load type scaler
#cat_scaler = load('TypeScalerFinal.joblib')

@app.route("/is-fraud", methods=["POST"])
def analyze():
    data = request.get_json()
    #if os.path.exists('dumpfile.json'):
    #    with open('dumpfile.json','r') as fout:
    #        r = fout.readlines()[-1]
    #        r = json.loads(r)
    #    prev_step = r['step']
    #    prevAmt = r['amount']
    #    prevType = cat_scaler.transform(np.array(r['type']).reshape(1,-1))[0][0]
    #else:
    #    prev_step = np.nan
    #    prevAmt = np.nan
    #    prevType = np.nan
    #with open('dumpfile.json','a') as fout:
    #    json.dump(data,fout)
    #    fout.write('\n')
    #deltaDest = data['oldbalanceDest'] - data['newbalanceDest']
    #type = cat_scaler.transform(np.array(data['type']).reshape(1,-1))[0][0]
    #deltaOrig = data['newbalanceOrig'] - data['oldbalanceOrig']
    #features = np.array([data['amount'],deltaDest,data['step'],prev_step,
    #                    type,data['oldbalanceOrig'],data['newbalanceOrig'],data['newbalanceDest'],
    #                    data['oldbalanceDest'],deltaOrig,prevAmt,prevType],dtype=float)
    #pred = mdl.predict(features.reshape(1,-1))
    #if pred == 1:
    #    p = True
    #else:
    #    p = False
    #return jsonify({"isFraud": p})
    return jsonify(data)


