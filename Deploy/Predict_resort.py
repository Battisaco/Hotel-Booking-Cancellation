#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:30:19 2022

@author: battisaco
"""
import pickle
import pandas as pd
from flask import Flask, request, jsonify


Resort_model   = 'model_Resort.bin'
    
with open(Resort_model , 'rb') as f_in:
    Resort = pickle.load(f_in)


app = Flask('Resort')

@app.route('/Predict_Resort', methods = ['POST'])
def predict_Resort():
    booking = request.get_json()
    df = pd.read_json(booking)
    
    y_pred = Resort.predict(df)
    wil_cancel = y_pred >= 0.5
    
    # Saida em json tbm
    result = {
        'cancel_percent':float(wil_cancel),
        'cancel':bool(wil_cancel)
        } 
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 9697)
