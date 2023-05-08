from flask import Flask,render_template, session, url_for, request
import pickle
import pandas as pd
import numpy as np
from tensorflow import keras
from keras.models import load_model, model_from_json
import re
import sys
import os


sys.path.append(os.path.abspath("./model"))

app = Flask(__name__)
app.config['SECRET_KEY']='jeypeedee'
model_intro = load_model('intro_dnn_model.h5')
model_oop = load_model('OopDnnModel.h5')
model_comprog = load_model('ComprogDnnModel.h5')
smote_model_intro = load_model('2nd_smote_Intro_Dnn_model.h5')
smote_model_oop = load_model('smote_Oop_Dnn_model.h5')

from keras.models import model_from_json
import tensorflow as tf


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/oop_analytics')
def oop_analytics():
    return render_template('oop_analytics.html')

@app.route('/intro_analytics')
def intro_analytics():
    return render_template('intro_analytics.html')

@app.route('/comprog_prediction')
def comprog_prediction():
    return render_template('comprog_prediction.html')

@app.route('/oop_prediction')
def oop_prediction():
    return render_template('oop_prediction.html')

@app.route('/intro_prediction')
def intro_prediction():
    return render_template('intro_prediction.html')

@app.route('/predict',methods=["GET","POST"])
def predict():
    socioeconomic_status = 0
    sex_data = {'Male':0,'Female':0}
    ws_data = {'Yes': 0, 'No': 0}
    scholar_data = {'Yes': 0, 'No': 0}
    hl_data = {'Yes': 0, 'No': 0}

    for key in sex_data:
        if request.form['sex'] == key:
            sex_data[key] = 1
        else:
            sex_data[key] = 0

    for key in ws_data:
        if request.form['working'] == key:
            ws_data[key] = 1
        else:
            ws_data[key] = 0

    for key in scholar_data:
        if request.form['scholar'] == key:
            scholar_data[key] = 1
        else:
            scholar_data[key] = 0

    for key in hl_data:
        if request.form['laptop/pc'] == key:
            hl_data[key] = 1
        else:
            hl_data[key] = 0


        if request.form['se_status'] == "Upper Middle":
            socioeconomic_status = 3
        elif request.form['se_status'] == "Lower middle":
            socioeconomic_status = 2
        elif request.form['se_status'] == "Middle":
            socioeconomic_status = 1
        elif request.form['se_status'] == "Low":
            socioeconomic_status = 0


        newdata=dict()
        prediction=-1
        newdata['age'] = request.form['age']
        newdata['socioeconomic_status'] = socioeconomic_status
        newdata['lecture_quizzes(30%)'] = float(request.form['Lec_Quiz']) * 0.30
        newdata['lecture_seatwork(30%)'] = float(request.form['Lec_Seat']) * 0.30
        newdata['lecture_exam(40%)'] = float(request.form['Lec_Exam']) * 0.40
        newdata['laboratory_activities(40%)'] = float(request.form['Lab_Act']) * 0.40
        newdata['laboratory_exam(60%)'] = float(request.form['Lab_Exam']) * 0.60
        newdata['sex_female'] = sex_data['Female']
        newdata['sex_male'] = sex_data['Male']
        newdata['working_student_no'] = ws_data['No']
        newdata['working_student_yes'] = ws_data['Yes']
        newdata['scholar_no'] = scholar_data['No']
        newdata['scholar_yes'] = scholar_data['Yes']
        newdata['Has a Laptop/PC_no']  = hl_data['No']
        newdata['Has a Laptop/PC_yes'] = hl_data['Yes']

        df=pd.DataFrame([newdata.values()],columns=list(newdata.keys()))
        tf_arr = tf.convert_to_tensor(df,dtype=tf.float32)

        
        
        prediction=model_comprog.predict(tf_arr)
        print('\n\nPrediction: ',prediction,'\n\n')
        prediction = round(float(prediction), 2)

    return render_template('comprog_prediction.html', prediction=prediction )

@app.route('/predict1',methods=["GET","POST"])
def predict1():
    socioeconomic_status = 0
    sex_data = {'Male':0,'Female':0}
    ws_data = {'Yes': 0, 'No': 0}
    scholar_data = {'Yes': 0, 'No': 0}
    hl_data = {'Yes': 0, 'No': 0}

    for key in sex_data:
        if request.form['sex'] == key:
            sex_data[key] = 1
        else:
            sex_data[key] = 0

    for key in ws_data:
        if request.form['working'] == key:
            ws_data[key] = 1
        else:
            ws_data[key] = 0

    for key in scholar_data:
        if request.form['scholar'] == key:
            scholar_data[key] = 1
        else:
            scholar_data[key] = 0

    for key in hl_data:
        if request.form['laptop/pc'] == key:
            hl_data[key] = 1
        else:
            hl_data[key] = 0


        if request.form['se_status'] == "Upper Middle":
            socioeconomic_status = 3
        elif request.form['se_status'] == "Lower middle":
            socioeconomic_status = 2
        elif request.form['se_status'] == "Middle":
            socioeconomic_status = 1
        elif request.form['se_status'] == "Low":
            socioeconomic_status = 0


        newdata=dict()
        prediction=-1
        newdata['age'] = request.form['age']
        newdata['socioeconomic_status'] = socioeconomic_status
        newdata['lecture_quizzes(30%)'] = float(request.form['Lec_Quiz']) * 0.30
        newdata['lecture_seatwork(30%)'] = float(request.form['Lec_Seat']) * 0.30
        newdata['lecture_exam(40%)'] = float(request.form['Lec_Exam']) * 0.40
        newdata['laboratory_activities(40%)'] = float(request.form['Lab_Act']) * 0.40
        newdata['laboratory_exam(60%)'] = float(request.form['Lab_Exam']) * 0.60
        newdata['sex_female'] = sex_data['Female']
        newdata['sex_male'] = sex_data['Male']
        newdata['working_student_no'] = ws_data['No']
        newdata['working_student_yes'] = ws_data['Yes']
        newdata['scholar_no'] = scholar_data['No']
        newdata['scholar_yes'] = scholar_data['Yes']
        newdata['Has a Laptop/PC_no']  = hl_data['No']
        newdata['Has a Laptop/PC_yes'] = hl_data['Yes']

        df=pd.DataFrame([newdata.values()],columns=list(newdata.keys()))
        tf_arr = tf.convert_to_tensor(df,dtype=tf.float32)

        prediction=model_oop.predict(tf_arr)
        print('\n\nPrediction: ',prediction,'\n\n')
        prediction = round(float(prediction), 2)
        
    return render_template('oop_prediction.html', prediction=prediction)

@app.route('/predict2',methods=["GET","POST"])
def predict2():
    socioeconomic_status = 0
    sex_data = {'Male':0,'Female':0}
    ws_data = {'Yes': 0, 'No': 0}
    scholar_data = {'Yes': 0, 'No': 0}
    hl_data = {'Yes': 0, 'No': 0}

    for key in sex_data:
        if request.form['sex'] == key:
            sex_data[key] = 1
        else:
            sex_data[key] = 0

    for key in ws_data:
        if request.form['working'] == key:
            ws_data[key] = 1
        else:
            ws_data[key] = 0

    for key in scholar_data:
        if request.form['scholar'] == key:
            scholar_data[key] = 1
        else:
            scholar_data[key] = 0

    for key in hl_data:
        if request.form['laptop/pc'] == key:
            hl_data[key] = 1
        else:
            hl_data[key] = 0


        if request.form['se_status'] == "Upper Middle":
            socioeconomic_status = 3
        elif request.form['se_status'] == "Lower middle":
            socioeconomic_status = 2
        elif request.form['se_status'] == "Middle":
            socioeconomic_status = 1
        elif request.form['se_status'] == "Low":
            socioeconomic_status = 0


        newdata=dict()
        prediction=-1
        newdata['age'] = request.form['age']
        newdata['socioeconomic_status'] = socioeconomic_status
        newdata['lecture_quizzes(30%)'] = float(request.form['Lec_Quiz']) * 0.30
        newdata['lecture_seatwork(30%)'] = float(request.form['Lec_Seat']) * 0.30
        newdata['lecture_exam(40%)'] = float(request.form['Lec_Exam']) * 0.40
        newdata['laboratory_activities(40%)'] = float(request.form['Lab_Act']) * 0.40
        newdata['laboratory_exam(60%)'] = float(request.form['Lab_Exam']) * 0.60
        newdata['sex_female'] = sex_data['Female']
        newdata['sex_male'] = sex_data['Male']
        newdata['working_student_no'] = ws_data['No']
        newdata['working_student_yes'] = ws_data['Yes']
        newdata['scholar_no'] = scholar_data['No']
        newdata['scholar_yes'] = scholar_data['Yes']
        newdata['Has a Laptop/PC_no']  = hl_data['No']
        newdata['Has a Laptop/PC_yes'] = hl_data['Yes']

        df=pd.DataFrame([newdata.values()],columns=list(newdata.keys()))
        tf_arr = tf.convert_to_tensor(df,dtype=tf.float32)

       
        prediction=model_intro.predict(tf_arr)
        print('\n\nPrediction: ',prediction,'\n\n')
        prediction = round(float(prediction), 2)

    return render_template('intro_prediction.html', prediction=prediction)


if __name__=="__main__":
    app.run(debug=True)