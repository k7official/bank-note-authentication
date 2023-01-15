# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__) # which point you want to start the application
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)


@app.route('/') # root path
def welcome():
    return "Welcome All"

@app.route('/predict')  # API...get method
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    return f"The predicted value is {prediction}"


@app.route('/predict_file', methods=["POST"])  # API...post method
def predict_note_file():
    df_test = pd.read_csv(request.files.get("file"))
    prediction = list(model.predict(df_test))
    return f"The predicted values for the csv is {prediction}"




if __name__ == '__main__':
    app.run(host ='127.0.0.1')
