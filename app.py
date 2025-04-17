from flask import Flask , render_template , request 

import os 
import numpy as np
import pandas as pd
from src.WineQualityPrediction.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)
@app.route("/", methods = ['GET'])
def homepage():
    return render_template('index.html')


@app.route("/train" , methods = ['GET'])
def training():
    os.system("python main.py")
    return "Training Successful"

@app.route("/predict" , methods = ["POST" , "GET"])
def Predict():
    if request.method == "POST":
        try :
            fixed_acidity = request.form['fixed_acidity']
            volatile_acidity = request.form['volatile_acidity']
            citric_acid = request.form['citric_acid']
            residual_sugar = request.form['residual_sugar']
            chlorides = request.form['chlorides']
            free_sulfur_dioxide = request.form['free_sulfur_dioxide']
            total_sulfur_dioxide = request.form['total_sulfur_dioxide']
            density = request.form['density']
            pH = request.form['pH']
            sulphates = request.form['sulphates']
            alcohol = request.form['alcohol']

            data = [float(fixed_acidity),float(volatile_acidity),float(citric_acid),float(residual_sugar),float(chlorides),float(free_sulfur_dioxide),float(total_sulfur_dioxide),float(density),float(pH),float(sulphates),float(alcohol)]

            data = np.array(data).reshape(1,11)
            obj = PredictionPipeline()
            predict = obj.Predict(data)
            return render_template("results.html" , prediction = str(predict))
        
        except Exception as e:
            return f"Something is wrong : {e}"

    else:
        return render_template('index.html')
    



if __name__ == "__main__":
    app.run(host = "0.0.0.0" , port = 8080 ,debug= True)
    