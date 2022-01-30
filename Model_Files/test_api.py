#!/usr/bin/env python3

import requests

json = {
"step":1,
"type":"TRANSFER",
"amount":50000,
"nameOrig":"C1231006815",
"oldbalanceOrig":1701360.0,
"newbalanceOrig":1651360.0,
"nameDest":"M1979787155",
"oldbalanceDest":0.0,
"newbalanceDest":0.0
}


r = requests.post('http://127.0.0.1:5000/is-fraud',json=json)
print(r.json())

for k in range(0,34):
    json['oldbalanceOrig'] = json['newbalanceOrig']
    json['newbalanceOrig'] = json['newbalanceOrig'] - json['amount']
    #json['newbalanceDest'] = json['oldbalanceDest'] + json['amount']
    #json['oldbalanceDest'] = json['newbalanceDest']
    r = requests.post('http://127.0.0.1:5000/is-fraud',json=json)
    print(r.json())
print(json)
