#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:27:46 2023

@author: musa.official
"""

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger


app = Flask(__name__) # which point you want to start the application
Swagger(app) # indication to the app to generate the UI part of the app

pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)


@app.route('/') # root path
def welcome():
    return "Welcome All"

@app.route('/predict', methods=["Get"])  # API...get method
def predict_note_authentication():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    
    
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    return f"The predicted value is {prediction}"


@app.route('/predict_file', methods=["POST"])  # API...post method
def predict_note_file():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    
    df_test = pd.read_csv(request.files.get("file"))
    prediction = list(model.predict(df_test))
    return f"The predicted values for the csv is {prediction}"




if __name__ == '__main__':
    app.run(host ='127.0.0.1')
