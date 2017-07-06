#!/usr/bin/python
from sklearn.externals import joblib
from flask import (Flask,
                  render_template,
                  request)

import pickle
import numpy as np

clf = joblib.load("../model.pkl")

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html'  )

@app.route('/about')
def about():
   return render_template('about.html'  )

@app.route("/api/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        param1 = float(request.form["param1"])
        param2 = float(request.form["param2"])
        param3 = float(request.form["param3"])
        param4 = float(request.form["param4"])
        param5 = float(request.form["param5"])

        data = np.array([param1, param2, param3, param4, param5], dtype="float32")
        proba = clf.predict_proba(data)

        more_likelyhood = round(proba[0][0]*100, 2) # kemungkinan besar tidak kanker
        less_likelyhood = round(proba[0][1]*100, 2) # kemungkinan kecil kanker

        return render_template("index.html", result=(more_likelyhood, less_likelyhood))

if __name__ == '__main__':
   app.run()
