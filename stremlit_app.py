#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:06:38 2023

@author: musa.official
"""

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import streamlit as st

from PIL import Image


app = Flask(__name__) # which point you want to start the application
#Swagger(app) # indication to the app to generate the UI part of the app

pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)


# @app.route('/') # root path
def welcome():
    return "Welcome All"

# @app.route('/predict', methods=["Get"])  # API...get method
def predict_note_authentication(variance, skewness, curtosis, entropy):
    
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")



if __name__ == '__main__':
    app.run(host ='127.0.0.1', port=8000)
