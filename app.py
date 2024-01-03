from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd

vector = pickle.load(open("Model/vectorizor.pkl", "rb"))
model = pickle.load(open("Model/finalized_model.pkl", "rb"))
application = Flask(__name__)
app=application

## Route for Single data point prediction
@app.route('/',methods=['GET','POST'])
def prediction():
    if request.method=='POST':
        message =request.form.get("message")
        predict=model.predict(vector.transform([message]))[0]
        if predict == 'ham':
            predict = 'not spam'
        print(predict)
        return render_template('index.html' , prediction_test='SMS is {}'.format(predict))
        
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(host="0.0.0.0" , debug=True)