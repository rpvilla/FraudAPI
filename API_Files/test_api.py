#!/usr/bin/env python3

import requests

json = {
"step":1,
"type":"TRANSFER",
"amount":9839.64,
"nameOrig":"C1231006815",
"oldbalanceOrig":170136.0,
"newbalanceOrig":160296.36,
"nameDest":"M1979787155",
"oldbalanceDest":0.0,
"newbalanceDest":0.0
}

r = requests.post('https://onlinefraudapi.herokuapp.com/is-fraud',json=json)
print(r.json())


for k in range(0,1000):
    json['oldbalanceOrig'] = json['newbalanceOrig']
    json['newbalanceOrig'] = json['newbalanceOrig'] - json['amount']
    #json['newbalanceDest'] = json['oldbalanceDest'] + json['amount']
    #json['oldbalanceDest'] = json['newbalanceDest']
    #json['newbalanceDest'] = 0.0
    r = requests.post('https://onlinefraudapi.herokuapp.com/is-fraud',json=json)
    print(r.json())
    if r.json()['isFraud']:
        break
print(json)
