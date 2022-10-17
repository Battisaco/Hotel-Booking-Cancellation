#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:30:19 2022

@author: battisaco
"""
import pickle
import pandas as pd
from flask import Flask, request, jsonify


City_model   = 'model_City.bin'
    
with open(City_model , 'rb') as f_in:
    City = pickle.load(f_in)


app = Flask('City')

@app.route('/predict_city', methods = ['POST'])
def predict_City():
    booking = request.get_json()
    df = pd.read_json(booking)
    
    y_pred = City.predict(df)
    wil_cancel = y_pred >= 0.5
    
    # Saida em json tbm
    result = {
        'cancel_percent':float(wil_cancel),
        'cancel':bool(wil_cancel)
        } 
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 9697)



    
    