import pandas as pd
import numpy as np
import sklearn
from sklearn.svm import SVC
import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    model_prediction = ''
    if request.method == 'POST':
        print(request.form.get('var_1'))
        print(request.form.get('var_2'))
        print(request.form.get('var_3'))
        try:
            var_1 = float(request.form['var_1'])
            var_2 = float(request.form['var_2'])
            var_3 = float(request.form['var_3'])
            pred_args = [var_1, var_2, var_3]
            pred_arr = np.array(pred_args).reshape(1, -1)
            print(pred_arr)
            model = open("svm_model.pkl", "rb")
            lr_model = joblib.load(model)
            model_prediction = lr_model.predict(pred_arr)
            model_prediction = round(float(model_prediction), 2)
            dict1 = {-1: 'Persistent', 1: 'Non persistent'}
            model_prediction = dict1[model_prediction]
        except ValueError:
            return "Please Enter valid values"
    return render_template('predict.html', prediction=model_prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)