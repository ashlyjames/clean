import os
import string
# import requests
import numpy as np
# import tensorflow as tf
import pickle
from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
# from keras.models import load_model
from string import printable
from keras.preprocessing import sequence
# from flask_ngrok import run_with_ngrok
app = Flask(__name__)
# run_with_ngrok(app)
Bootstrap(app)
"""
Loading Saved Files
"""
model = keras.models.load_model(new_model)
# with open('printable.pickle', 'rb') as f:
    # model=pkl.load(f)
"""
Constants
"""
CLASSES = ['Malicious', 'Benign']
MAX_SEQUENCE_LENGTH = 75



"""
Routes
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_val = request.form.values()
        if text_val != '':
                X_t = [[printable.index(x) + 1 for x in url if x in printable]]
                data_t = keras.preprocessing.sequence.pad_sequences(X_t, maxlen=MAX_SEQUENCE_LENGTH)
                result = model.predict(data_t)
                prediction = result[0][0]
                class_name = CLASSES[int(prediction > 0.5)]
                dic = {
                    'score': prediction,
                    'class_name':class_name
                }
                return render_template('show.html', result=dic)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)