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









if __name__ == '__main__':
    app.run(host ='127.0.0.1')
